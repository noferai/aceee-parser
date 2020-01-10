import scrapy
import json


class ArticleItem(scrapy.Item):
    id = scrapy.Field(serializer=int)
    title = scrapy.Field(serializer=str)
    pubdate = scrapy.Field(serializer=str)
    categories = scrapy.Field(serializer=json.dumps)
    article_body = scrapy.Field(serializer=str)
    tags = scrapy.Field(serializer=json.dumps)
    external_links = scrapy.Field(serializer=json.dumps)
