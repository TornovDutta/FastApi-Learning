from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def root():
    return "hello world"

@app.get("/home")
def home():
    return {"home":{
        "dashboard",
        "homepage"
    },
    "hello":{
        "hello world",
        "hey!!"
    }}

@app.get("/param/{id}")
def param(id):
    return int(id) 