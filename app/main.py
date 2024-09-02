from fastapi import FastAPI,Request,HTTPException,Depends
from database import SessionLocal,engine
from typing import Annotated,List

from fastapi.templating import Jinja2Templates
from routers import *
import models
import schemas

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

fakeDatabase = {
    1: {'task': 'Clean Car'},
    2: {'task': 'Buy groceries'},
    3: {'task': 'Do homework'},
    4: {'task': 'Go to the gym'}
}


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello World"})



# @app.post("/{id}")
# async def get_task(id: int,body = Body()):
#     print(body)
#     # print(rating)
#     return fakeDatabase[id]

@app.post("/")
async def add_product(product: schemas.ProductBase):
    print()

app.include_router(categories_router, prefix="/categories", tags=["categories"])
app.include_router(products_router, prefix="/products", tags=["products"])