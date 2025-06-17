from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
def about():
    return {"message": "Welcome to new series!!! FastAPI "}


@app.get('/')
def home():
    return {"message": "Welcome back! Enjoy the Show...."}
    

'''
from fastapi import FastAPI

app = FastAPI()

@app.route('/')
def home():
    return {"message": "Welcome back! Enjoy the Show...."}
    
'''
