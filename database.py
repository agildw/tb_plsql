from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://bumi:acumalaka@47.254.123.28/tb_plsql')

# Buat session
Session = sessionmaker(bind=engine)
session = Session()

def create_session():
    return session