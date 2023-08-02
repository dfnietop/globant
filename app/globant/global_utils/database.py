from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from globant.global_utils import config


SQLALCHEMY_DATABASE_URL = config.DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()