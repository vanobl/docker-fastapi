from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# строка подключения к базе
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:mysecretpassword@db-server:5432/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@db-server:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()