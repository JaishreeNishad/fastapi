from fastapi import FastAPI

app = FastAPI()


@app.get("/first")
def index():
    return {"message": "Hello World"}

#http://myntra.com/items/item_id 
#example of path parameter

@app.get("/items/{item_id}")
def index(item_id :int): # apply validate (item_id: int)
         return {"producut_id":item_id}