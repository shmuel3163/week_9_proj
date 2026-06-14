from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Literal
from database.book_db import booki
router = APIRouter()


@router.get("/{id}/borrow/{member_id}")
def borrow_book(id: int, member_id: int):
    print(id, member_id)
    active_borrows_dict = booki.count_active_borrows_by_member(member_id)
    print(active_borrows_dict["active_borrows"])
    
    if active_borrows_dict['active_borrows'] < 4:
        data = booki.set_available(id=id, value=0, member_id=member_id)
        return data
    else:
        return {}


@router.get("/{id}")
def get_book_by_id(id: int):
    data = booki.get_book_by_id(id)
    return data

@router.get("/")
def get_all_books():
   all_books = booki.get_all_books()
   return all_books


class Update_Book(BaseModel):
    title : Optional[str] | None = None
    author : Optional[str] | None = None
    genre :  Literal['Fiction', 'Non-Fiction','Science','History', 'Other']


class New_Book(BaseModel):
    title : str
    author : str
    genre :  Literal['Fiction', 'Non-Fiction','Science','History', 'Other']    

@router.put("/{id}")
def update_book(id, data: Update_Book):
    data = data.model_dump()
    print(data)
    result = booki.update_book(id=id, data=data)
    return result

@router.post("/")
def add_new_book(data: New_Book):
    new_book = data.model_dump()
    return booki.create_book(new_book)



        
    






