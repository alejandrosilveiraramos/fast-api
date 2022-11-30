from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#Create a postgres sql engine instance
engine = create_engine("**************")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create a SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

