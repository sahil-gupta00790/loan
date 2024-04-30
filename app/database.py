from sqlalchemy import create_engine , MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from .config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = automap_base()

Base.prepare(engine, reflect=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
