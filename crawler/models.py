from sqlalchemy import create_engine, Column, String, Text, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from crawler import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Article(DeclarativeBase):
    __tablename__ = 'article'
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    pubdate = Column(String())
    categories = Column(JSON())
    article_body = Column(Text())
    tags = Column(JSON())
    external_links = Column(JSON())
