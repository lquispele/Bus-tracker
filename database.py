from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base
DATABASE_URL= "sqlite:///./buses.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal= sessionmaker(bind=engine, autocommit=False, autoflush= False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
Base = declarative_base()