from flask import Blueprint, request, jsonify
from werkzeug.exceptions import NotFound
from models.book import Book, book_schema, books_schema
from models.author import Author
from http.client import OK, CREATED
from config.db import db


books_bp = Blueprint(name="books_bp", import_name=__name__, url_prefix="/api/v1/books")


@books_bp.get("/<isbn>")
def get_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        raise NotFound(f"Book [isbn={isbn}] not found.")
    return book_schema.jsonify(book), OK


@books_bp.post("")
def create_book():
    book = book_schema.load(request.json)
    book.validate()
    db.session.add(book)
    db.session.commit()
    # return "", CREATED
    return book_schema.jsonify(book), CREATED


@books_bp.get("/author/<author_id>")
def get_books_by_author(author_id):
    author = Author.query.get(author_id)
    if author is None:
        raise NotFound(f"Author [author_id={author_id}] not found.")
    return books_schema.jsonify(author.books), OK