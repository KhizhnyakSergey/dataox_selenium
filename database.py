from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE
from sqlalchemy.engine.url import URL
from sqlalchemy import Column, Integer, String, Float

engine = create_engine(URL(**DATABASE))
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)

    img_src = Column(String)
    title = Column(String)
    currency = Column(String)
    price = Column(Float)
    location = Column(String)
    date_posted = Column(String)
    description = Column(String)
    bedrooms = Column(String)


Base.metadata.create_all(engine)
