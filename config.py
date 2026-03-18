from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Rachana%408@localhost:5432/todo-back"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush= False , bind= engine)