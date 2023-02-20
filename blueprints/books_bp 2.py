from flask import Blueprint, request
from werkzeug.exceptions import NotFound, BadRequest
from models.book import Book, book_schema, books_schema
from models.author import Author
from models.genre import Genre
from http import HTTPStatus
from config.db import db


books_bp = Blueprint(name="books_bp", import_name=__name__, url_prefix="/api/v1/books")


@books_bp.get("/<isbn>")
def get_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        raise NotFound(f"Book [isbn={isbn}] not found.")
    return book_schema.jsonify(book), HTTPStatus.OK


@books_bp.post("")
def create_book():
    book = book_schema.load(request.json)
    book.validate()
    if book.isbn in {b.isbn for b in Book.query.all()}:
        raise BadRequest(f"Book [isbn={book.isbn}] already exists.")
    if book.author_id not in {a.author_id for a in Author.query.all()}:
        raise NotFound(f"Author [author_id={book.author_id}] not found.")
    if book.genre_name not in {g.name for g in Genre.query.all()}:
        raise NotFound(f"Genre [genre_name={book.genre_name}] not found.")
    db.session.add(book)
    db.session.commit()
    return "", HTTPStatus.CREATED


@books_bp.get("/author/<author_id>")
def get_books_by_author(author_id):
    author = Author.query.get(author_id)
    if author is None:
        raise NotFound(f"Author [author_id={author_id}] not found.")
    return books_schema.jsonify(author.books), HTTPStatus.OK
