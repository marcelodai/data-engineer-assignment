from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

from db.models import Base

# DB Path
db_url = "sqlite:///squirrel_census.db" # Use SQLite for simplicity

def init_db():
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    # Session
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, session