from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


db = {}


class Item(BaseModel):
    name: str
    desc: str


@app.post("/")
def create(item: Item):
    db[item.name] = item.desc
    return {"Item": item}

@app.get("/")
def get_all_data():
    return db


@app.delete("/")
def delete_data(name:str):
    del db[name]
    return db


@app.put("/")
def update_data(item: Item):
     db[item.name] = item.desc
     return db

# @app.get("/first")
# def index():
#     return {"message": "Hello World"}

#http://myntra.com/items/item_id 
#example of path parameter

# @app.get("/items/{item_id}")
# def index(item_id :int=0): # apply validate (item_id: int)
#          return {"producut_id":item_id}
     
# #query parameter

# @app.get("/items/")
# def index(q:int,m:Optional[int]=10): #optional parameter
#     return {"product is":q,"m":m}


# @app.get("/items/{file_path:path}")
# def index(file_path:str):
#     return{"file_path":file_path}

# 

