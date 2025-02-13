from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

app=FastAPI()


class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str]= Field(default=None, title="Description of the book", min_length=1, max_length=100)
    rating: int =Field(gt=-1, lt=101)


BOOKS=[]


@app.get("/")
async def read_all_books(books_to_return: Optional[int]=None):
    if len(BOOKS) < 1:
        create_books_no_api()
    
    if books_to_return and len(BOOKS) >= books_to_return >0:
        i=1
        new_books=[]
        while i<=books_to_return:
            new_books.append(BOOKS[i-1])
            i+=1
        return new_books
    return BOOKS

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book

def create_books_no_api():
    book_1=Book(id="3ab0d53f-6669-4353-8f19-c42bb6788d6b",
            title="Title_1",
            author="Author_1",
            description="Description_1",
            rating=100)

    book_2=Book(id="e81d51d3-1512-4f9c-ae74-71b4a8acd21f",
            title="Title_2",
            author="Author_2",
            description="Description_2",
            rating=100)

    book_3=Book(id="b661f82f-91bd-4622-b242-4d4a0488e521",
            title="Title_3",
            author="Author_3",
            description="Description_3",
            rating=100)

    book_4=Book(id="d521cdd1-a000-4d97-b43c-98a38b617fdf",
            title="Title_4",
            author="Author_4",
            description="Description_4",
            rating=100)

    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
