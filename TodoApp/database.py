import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]
#"postgresql://postgresql+psycopg2//postgres:S%40isrujan123@localhost:5433/TodoApplicationDatabase"
engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# {
#   "username": "satyasai",
#   "email": "sai@gmail.com",
#   "first_name": "satya",
#   "last_name": "sai",
#   "password": "satyasai123",
#   "role": "admin"
# }