from typing import List, Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    category_id: int

class ProductUpdate(ProductBase):
    category_id: int

class ProductResponse(ProductBase):
    id: int
    category_id: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    products: List[ProductResponse] = []

    class Config:
        from_attributes = True

class MessageResponse(BaseModel):
    message: str