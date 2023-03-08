from flask import Blueprint, request
from werkzeug.exceptions import NotFound
from models.book import Book
from schemas.book import BookSchema
from http.client import OK, CREATED, NO_CONTENT, BAD_REQUEST
from config.db import db


books_bp = Blueprint(name="book", import_name=__name__, url_prefix="/books")
book_schema = BookSchema()
books_schema = BookSchema(many=True)


@books_bp.get("")
def get_books():
    all_books = Book.query.all()
    return books_schema.jsonify(all_books)


@books_bp.get("/<book_id>")
def get_book(book_id):
    book = Book.query.get(book_id)
    return book_schema.jsonify(book)


@books_bp.post("")
def add_book():
    new_book = book_schema.load(request.json)
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book)


@books_bp.put("/<book_id>")
def update_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        raise NotFound(f"Book [book_id={book_id}] not found.")
    assert (
        "title" in request.json and len(request.json["title"]) > 0
    ), "Book Title non-empty is required."
    assert (
        "description" in request.json and len(request.json["description"]) > 0
    ), "Book Description non-empty is required."
    assert (
        "price" in request.json and request.json["price"] > 0
    ), "Book Price greater than 0 is required."
    book.title = request.json["title"]
    book.description = request.json["description"]
    book.price = request.json["price"]
    db.session.commit()
    return book_schema.jsonify(book)


@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        raise NotFound(f"Book [book_id={book_id}] not found.")
    db.session.delete(book)
    db.session.commit()
    return "", NO_CONTENT
