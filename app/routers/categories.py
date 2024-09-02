from fastapi import APIRouter,Request,HTTPException,Depends
from typing import Annotated,List
from database import  get_db
from sqlalchemy.orm import Session 
import models
from schemas import CategoryCreate,MessageResponse,CategoryUpdate

router = APIRouter()
db_dependency = Annotated[Session , Depends(get_db)]

@router.get("/")
async def get_categories(db:db_dependency):

    categories = db.query(models.Category).all()
    return categories


@router.post("/")
async def create_category(data: CategoryCreate, db: db_dependency):

    category = db.query(models.Category).filter(models.Category.name == data.name).first()
    if category:
        raise HTTPException(status_code=400, detail="Category Name already exists. Please choose a new category name")

    new_category = models.Category(name=data.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    print(new_category)
    return MessageResponse(message=f'Category {new_category.name} created successfully')


@router.put("/{category_id}")
async def update_category(category_id: int, data: CategoryUpdate, db: db_dependency):
    
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category.name = data.name
    db.commit()
    db.refresh(category)
    return MessageResponse(message = f'Category {category.name} updated successfully')


@router.delete("/{category_id}")
async def delete_category(category_id: int, db: db_dependency):

    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(category)
    db.commit()
    return MessageResponse(message=f'Category {category.name} deleted successfully')