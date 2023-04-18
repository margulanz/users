from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	username = Column(String, default = '')
	id = Column(Integer, primary_key = True)
	images = Column(String)
	bio = Column(Text)
	country = Column(String)
	is_verified = Column(Boolean, default = False)
	linkedin_link = Column(String)
	git_link = Column(String)
	stackexchange_link = Column(String)
	timezone = Column(String)
	rank = Column(Integer)
	orgs = relationship('Org', back_populates = 'admin')



class Org(Base):
	__tablename__ = 'orgs'
	id = Column(Integer, primary_key = True)
	name = Column(String, index = True)
	admin_id = Column(Integer, ForeignKey('users.id'))
	admin = relationship('User', back_populates = 'orgs')
