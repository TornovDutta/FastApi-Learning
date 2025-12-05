from fastapi import FastAPI
from typing import Optional
from  pydantic import BaseModel
app = FastAPI()
class Blogs(BaseModel):
    title:str
    published:bool
    date:Optional[str]

@app.get("/")
def index():
    return {"data": "this is blogs page"}

@app.get("/about")
def about():
    return {"data": "this is about page"}

@app.get("/blogs/published")
def published():
    return {"data": "page for published blogs"}

@app.get("/blogs/{id}")
def blogs(id: int):
    return {"data": f"{id} blogs are there"}

@app.get("/blogs")
def query(limit=10,published:bool=True, sort:Optional[bool]=None):
    if published:
        return {"data":f"{limit} of published bolgs"}
    else:
        return {"data":f"{limit} of bolgs"}
    
@app.post("/blogs")
def postRounter(blogs:Blogs):
    return blogs

