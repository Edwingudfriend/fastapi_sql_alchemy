import sys
import os

# Add parent directory to the sys.path list
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234567890@localhost:5432/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234567890@localhost:5432/postgres"
#SQLALCHEMY_DATABASE_URL = "postgresql://{postgres}:{1234567890}@{localhost}:{5432}/{postgres}"
#SQLALCHEMY_DATABASE_URL = "postgresql://{postgres}:{1234567890}@{localhost}:5432/{postgres}"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234567890@localhost:5432/edwin"




#engine = create_engine(
# SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": True}
#)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base = declarative_base()


# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a sessionmaker to create session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()