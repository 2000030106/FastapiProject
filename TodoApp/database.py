
#"postgresql://postgresql+psycopg2//postgres:S%40isrujan123@localhost:5433/TodoApplicationDatabase"
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")  # ✅ safe way

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
# {
#   "username": "satyasai",
#   "email": "sai@gmail.com",
#   "first_name": "satya",
#   "last_name": "sai",
#   "password": "satyasai123",
#   "role": "admin"
# }