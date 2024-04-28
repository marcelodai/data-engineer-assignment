from db.session import init_db
from src.etl import load_data
from src.queries import run_queries

if __name__=="__main__":
    engine, session = init_db()
    
    # Load data into database
    load_data(engine)

    # Run queries
    run_queries(session)
    