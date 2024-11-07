from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/first")
def index():
    return {"message": "Hello World"}

#http://myntra.com/items/item_id 
#example of path parameter

@app.get("/items/{item_id}")
def index(item_id :int=0): # apply validate (item_id: int)
         return {"producut_id":item_id}
     
#query parameter

@app.get("/items/")
def index(q:int):
    return {"product is":q}