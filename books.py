from fastapi import FastAPI
from typing import Optional
from enum import Enum

app=FastAPI()

Books={
    'book_1':{'title':'Title_One', 'author':'Author_One'},
    'book_2':{'title':'Title_Two', 'author':'Author_Two'},
    'book_3':{'title':'Title_Three', 'author':'Author_Three'},
    'book_4':{'title':'Title_Four', 'author':'Author_Four'},
    'book_5':{'title':'Title_Five', 'author':'Author_Five'}
}

class DirectionName(str, Enum):
    north="North"
    south="South"
    east="East"
    west="West"

# Decorators
# Reading all books with skip option
@app.get("/")
async def read_all_books(skip_book: Optional[str] =None):
    if skip_book:
        new_books=Books.copy()
        del new_books[skip_book]
        return new_books
    return Books

# Reading a Book by getting the specified book
@app.get("/{book_name}")
async def read_book(book_name:str):
    return Books[book_name]

# Creating a Book
@app.post("/")
async def create_book(book_title, book_author):
    current_book_id=0
    if len(Books)>0:
        for book in Books:
            x=int(book.split('_')[-1])
            if x>current_book_id:
                current_book_id=x
    Books[f'book_{current_book_id+1}']={'title': book_title, 'author': book_author}
    return Books[f'book_{current_book_id+1}']

# Updating book
@app.put("/{book_name}")
async def update_book(book_name:str, book_title:str, book_author:str):
    book_information={'title':book_title, 'author':book_author}
    Books[book_name]=book_information
    return book_information

# Deleting a Book using the Book name
@app.delete("/{book_name}")
async def delete_book(book_name):
    del Books[book_name]
    return f'Book_{book_name} has deleted'

# Assignment

@app.get("/assignment/")
async def read_book(book_name:str):
    return Books[book_name]

@app.delete("/delete/")
async def delete_book(book_name:str):
    del Books[book_name]
    return f'Book_{book_name} has deleted'