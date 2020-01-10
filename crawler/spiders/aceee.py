from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ArticleItem
from datetime import datetime
import re


class AceeeSpider(CrawlSpider):
    name = 'aceee'
    start_urls = ('https://aceee.org/news-blog',)
    datestring = '%Y-%m-%d'  # Date formatting pattern
    categories = []
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a[contains(text(), "NEXT")]')),  # crawl pages
        Rule(LinkExtractor(allow=r'(blog|press)/[\d]{4}/[\d]{2}/.*'), callback='parse_article')  # crawl articles
    )

    def parse_start_url(self, response):
        """
        Parses and saves all categories listed on aceee.org
        """
        self.categories = set(
            response.xpath('//h2[@class="pane-title" and contains(., "Blog Categories")]/..//a/text()').extract())
        return []

    def parse_article(self, response):
        extractor = LinkExtractor(restrict_xpaths='//article', deny_domains='aceee.org')
        raw_tags = set(response.xpath('//span[contains(., "Tags:")]/..//a/text()').extract())

        yield ArticleItem(
            id=re.search(r'[\d]+', response.xpath('//head//link[@rel="shortlink"]/@href').extract_first()).group(0),
            title=response.xpath('//head//meta[@property="og:title"]/@content').extract_first(),
            pubdate=datetime.fromisoformat(
                response.xpath('//head//meta[@property="article:published_time"]/@content').extract_first()
            ).strftime(self.datestring),
            categories=list(raw_tags & self.categories),
            article_body=re.sub(r'\s{2,}', ' ', re.sub(r'[^\x00-\x7F]+|[\t\n\r\f]+', ' ', ''.join(
                response.xpath('//div[contains(@class, "left_common_cust")]//article//text()').extract()))).strip(),
            tags=list(raw_tags - self.categories),
            external_links=list(map(lambda link: link.url, extractor.extract_links(response)))
        )
