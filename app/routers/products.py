from fastapi import APIRouter,Request,HTTPException,Depends
from typing import Annotated,List
from database import  get_db
from sqlalchemy.orm import Session 
import models
from schemas import MessageResponse,ProductCreate,ProductUpdate

router = APIRouter()
db_dependency = Annotated[Session , Depends(get_db)]

@router.get("/")
async def get_products(db: db_dependency):
    
    get_products = db.query(models.Product).all()
    print(get_products)
    return get_products

@router.post("/")
async def create_product(product: ProductCreate, db: db_dependency):

    # Check if category exists
    category = db.query(models.Category).filter(models.Category.id == product.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")
    
    new_product = models.Product(name=product.name, price=product.price, category_id=product.category_id)

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return MessageResponse(message="Product created successfully")

@router.put("/{product_id}")
async def update_product(product_id: int, product: ProductUpdate, db: db_dependency):

    #Check if category exists
    category = db.query(models.Category).filter(models.Category.id == product.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")

    product_to_update = db.query(models.Product).filter(models.Product.id == product_id).first()

    if product_to_update:
        product_to_update.name = product.name
        product_to_update.price = product.price
        db.commit()
        db.refresh(product_to_update)
        return MessageResponse(message="Product updated successfully")
    
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/{product_id}")
async def delete_product(product_id: int, db: db_dependency):
    product_to_delete = db.query(models.Product).filter(models.Product.id == product_id).first()

    if product_to_delete:
        db.delete(product_to_delete)
        db.commit()
        return MessageResponse(message="Product deleted successfully")
    
    raise HTTPException(status_code=404, detail="Product not found")