from fastapi import APIRouter
from database.book_db import booki
router = APIRouter()


@router.get("/")
def get_all_books():
   all_books = booki.get_all_books()
   return all_books