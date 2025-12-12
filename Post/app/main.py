from fastapi import FastAPI,status,Depends,HTTPException
from .database import engine,Base,sessionLocal
from sqlalchemy.orm import Session
from . import models,schemas,hasing
from passlib.context import CryptContext

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

@app.get("/{id}",status_code=status.HTTP_200_OK)
def getById(id:int ,db:Session=Depends(get_db)):
    user=db.query(models.Users).filter(models.Users.id==id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,deatils="id is wrong")
    return user

@app.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.UsersResponse,tags=["users"])
def create_user(requested: schemas.Requestedusers, db: Session = Depends(get_db)):
    hashPassword=hasing.Hasing.hash_password(requested.password)
    new_user=models.Users(name=requested.name,email=requested.email,password=hashPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

