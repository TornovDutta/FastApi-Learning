from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine

url="sqlite:///./database.db"
engine=create_engine(url,connect_args={"check_same_thread":False})

sessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base =declarative_base()