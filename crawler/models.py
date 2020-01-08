from uuid import uuid4
from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.dialects.postgresql import UUID

from crawler import settings


DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Article(DeclarativeBase):
    __tablename__ = 'article'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String())
    pubdate = Column(String())
    categories = Column(String())
    article_body = Column(Text())
    tags = Column(String())
    external_links = Column(String())
