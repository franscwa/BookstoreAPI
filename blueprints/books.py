from flask import Blueprint, request, jsonify
from werkzeug.exceptions import NotFound
from models.book import Book, book_schema, books_schema
from http.client import OK, CREATED, NO_CONTENT
from config.db import db
from sqlalchemy import select, desc


books_bp = Blueprint(name="books", import_name=__name__, url_prefix="/api/v1/books")


@books_bp.get("")
def get_books():
    all_books = Book.query.all()
    return books_schema.jsonify(all_books)


@books_bp.get("/<isbn>")
def get_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        raise NotFound(f"Book [isbn={isbn}] not found.")
    return book_schema.jsonify(book), OK


@books_bp.post("")
def create_book():
    new_book = book_schema.load(request.json)
    new_book.validate()
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book), CREATED


@books_bp.put("/<book_id>")
def update_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        raise NotFound(f"Book [book_id={book_id}] not found.")
    updated_book = book_schema.load(request.json)
    updated_book.validate()
    book.title, book.description, book.price = (
        updated_book.title,
        updated_book.description,
        updated_book.price,
    )
    db.session.commit()
    return book_schema.jsonify(book), OK


@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        raise NotFound(f"Book [book_id={book_id}] not found.")
    db.session.delete(book)
    db.session.commit()
    return "", NO_CONTENT
