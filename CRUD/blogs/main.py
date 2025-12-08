from fastapi import FastAPI,Depends,status,HTTPException
from . import schemas
from .database import engine,Base,SessionLocal
from . import model
from sqlalchemy.orm import Session
def create_db():
    Base.metadata.create_all(engine)
app=FastAPI()
create_db()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/create",status_code=status.HTTP_201_CREATED)
def create(requested:schemas.Blogs,db:Session=Depends(get_db)):
    new_blogs=model.Blogs(title=requested.title,body=requested.body)
    db.add(new_blogs)
    db.commit()
    db.refresh(new_blogs)

    return new_blogs

@app.get("/",status_code=status.HTTP_200_OK)
def get_all(db:Session=Depends(get_db)):
    return db.query(model.Blogs).all()

@app.get("/{id}",status_code=status.HTTP_200_OK)
def get(id:int ,db:Session=Depends(get_db)):
    return db.query(model.Blogs).filter(model.Blogs.id==id).first()


@app.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id: int, requested: schemas.Blogs, db: Session = Depends(get_db)):
    blog_query = db.query(model.Blogs).filter(model.Blogs.id == id)
    blog = blog_query.first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,details="Blog not found")

    blog_query.update({
        "title": requested.title,
        "body": requested.body
    })

    db.commit()
    return blog_query.first()

# @app.delete("/delete",status_code=status.HTTP_204_NO_CONTENT)
