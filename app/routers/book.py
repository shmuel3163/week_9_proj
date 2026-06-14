from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Literal
from database.book_db import booki
router = APIRouter()

@router.get("/")
def get_all_books():
   all_books = booki.get_all_books()
   return all_books


class Update_Book(BaseModel):
    title : Optional[str] | None = None
    author : Optional[str] | None = None
    genre :  Literal['Fiction', 'Non-Fiction','Science','History', 'Other']    

@router.put("/{id}")
def update_book(id, data: Update_Book):
    data = data.model_dump()
    print(data)
    result = booki.update_book(id=id, data=data)
    return result

@router.get
   