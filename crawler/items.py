import scrapy


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    pubdate = scrapy.Field()
    categories = scrapy.Field()
    article_body = scrapy.Field()
    tags = scrapy.Field()
    external_links = scrapy.Field()
