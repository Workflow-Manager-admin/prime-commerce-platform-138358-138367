"""
Database connection management for the e-commerce FastAPI backend.
Uses environment variables to connect to 'amazon_clone_database' container.
"""
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv
load_dotenv()

# PUBLIC_INTERFACE
def get_database_url():
    """Load DB connection info from environment."""
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise Exception("DB_URL must be set in the environment (.env)")
    return db_url

DATABASE_URL = get_database_url()
engine = sqlalchemy.create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# PUBLIC_INTERFACE
def get_db():
    """
    Yields a new database session for use with FastAPI dependencies.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
