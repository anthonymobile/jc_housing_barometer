# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer, DateTime, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
	engine = create_engine('sqlite:///../data/jc_permits.db') # todo update engine for real mysql backend
	Session = sessionmaker(bind=engine)
	session = Session
	return session

class Permit(Base):
	__tablename__='permits'
	__table_args__ = {'extend_existing': True}

	# summary
	control_number = Column(Integer(), primary_key=True)
	url = Column(String(1024))
	issue_date = Column(DateTime())
	permit_number = Column(Integer(), primary_key=True)
	location = Column(String(255), index=True)
	owner = Column(String(255))
	work_type = Column(String(255))
	work_description = Column(String(255))
	subcodes = Column(String(255)) # parse these out into separate variables first?
	status = Column(String(255))

	# detail
	# todo finalize mapping of fields added in PermitScraper.scrape_permit_detail
	description = Column(String(255))
	comments = Column(String(255))
	use_group = Column(String(255))
	total_construction_costs = Column(String(255))
	permit_fee = Column(String(255))
	dca_state_fee = Column(String(255))
	total_due = Column(String(255))
	total_paid = Column(String(255))
	remaining_balance = Column(String(255))

	# todo  if field = 'Related Permits'
	# e.g. {{'permit_number':'34343','url':'http://abc.com'},{'permit_number':'34343','url':'http://abc.com'}}
	# related_permits = Column(JSON) or https: // www.michaelcho.me / article / json - field - type - in -sqlalchemy - flask - python

	
	def __repr__(self):
		return "Permit()".format(self=self)

