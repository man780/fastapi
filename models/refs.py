from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from models import Base


class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer)
    wiki_data_id = Column(String)
    name = Column(String)
    code = Column(String)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
