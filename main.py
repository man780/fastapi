import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models.book import Author as ModelAuthor
from models.book import Book as ModelBook
from schemas.book import Author as SchemaAuthor
from schemas.book import Book as SchemaBook

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/health_check")
async def root():
    return {"success": True}


@app.post("/add-book/", response_model=SchemaBook)
def add_book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating, author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.post("/add-author/", response_model=SchemaAuthor)
def add_author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author


@app.get("/books/")
def get_books():
    books = db.session.query(ModelBook).all()

    return books


@app.get("/authors/")
def get_authors():
    authors = db.session.query(ModelAuthor).all()

    return authors


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
