from flask import Blueprint, request
from config.db import conn

from werkzeug.exceptions import NotFound
from models.book import Book
from schemas.book import BookSchema
from http.client import OK, CREATED, NO_CONTENT, BAD_REQUEST
from config.db import conn


books_bp = Blueprint(name="book", import_name=__name__, url_prefix="/books")
# book_schema = BookSchema()
# books_schema = BookSchema(many=True)


# @books_bp.get("")
# def get_books():
#     all_books = Book.query.all()
#     return books_schema.jsonify(all_books)
#
#
# @books_bp.get("/<book_id>")
# def get_book(book_id):
#     book = Book.query.get(book_id)
#     return book_schema.jsonify(book)
#
#
# @books_bp.post("")
# def add_book():
#     new_book = book_schema.load(request.json)
#     db.session.add(new_book)
#     db.session.commit()
#     return book_schema.jsonify(new_book)
#
#
# @books_bp.delete("/<book_id>")
# def delete_book(book_id):
#     book = Book.query.get(book_id)
#     if book is None:
#         raise NotFound(f"Book [book_id={book_id}] not found.")
#     db.session.delete(book)
#     db.session.commit()
#     return "", NO_CONTENT
