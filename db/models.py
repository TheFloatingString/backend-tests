from sqlalchemy import Table, Column, Integer, Float, String, MetaData, DateTime, Boolean
from sqlalchemy	import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

import os

from uuid import uuid4

import random
import datetime

engine = create_engine(os.environ["DATABASE_URL"], echo = True)

meta = MetaData()
Base = declarative_base()

class Article(Base):
	__tablename__ = "articles"

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid4)
	title = Column(String())
	content = Column(String())
	date_created = Column(DateTime())
	date_modified = Column(DateTime())

	def create_article(self, title, content):
		 self.title = title
		 self.content = content
		 self.date_created = datetime.datetime.now()
		 self.date_modified = datetime.datetime.now()

	def modify_article(self, title, content):
		self.title = title
		self.content = content
		self.date_modified = datetime.datetime.now()
		
if __name__ == "__main__":
	Base.metadata.create_all(engine)