from fastapi import FastAPI,status,Depends
from .database import engine,Base,sessionLocal
from sqlalchemy.orm import Session
from . import models

def create_db():
    Base.metadata.create_all(bind=engine)
create_db()
app=FastAPI()
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/",status_code=status.HTTP_200_OK)
def getAll(db: Session = Depends(get_db)):
    return db.query(models.Users).all()
