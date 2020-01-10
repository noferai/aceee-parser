from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from crawler.models import db_connect, create_table, Article


class CrawlerPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        article = Article(**item)
        try:
            session.merge(article)
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise
        finally:
            session.close()

        return item
