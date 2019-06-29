import sys
from sqlalchemy import
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import
declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Produce(Base):
	__tablename__ = 'produce'

class ProduceItem(Base):
	__tablename__ = 'produce_item'
	
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	price = Column(String(8))



engine = create_engine(
'sqlite:///producemenu.db')

Base.metadata.create_all(engine)