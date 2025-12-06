from fastapi import FastAPI
from . import schemas

from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models import Blogs

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.post("/")
def create(blog:schemas.Blogs):
    return "created"