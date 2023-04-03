from flask import Blueprint, request, jsonify
from werkzeug.exceptions import NotFound
from http.client import OK, CREATED, NO_CONTENT, BAD_REQUEST
from config.db import db
from models.book import Book, book_schema, books_schema
from models.comment import Comment, comment_schema, comments_schema
from datetime import datetime

comments_bp = Blueprint(
    name="comments", import_name=__name__, url_prefix="/api/v1/book"
)


@comments_bp.get("/comments")
def get_comments():
    print("HERE")
    all_comments = Comment.query.all()
    return comments_schema.jsonify(all_comments), OK


@comments_bp.get("/<isbn>/comments")
def get_comments_by_book(isbn):
    comment_query = Comment.query.filter(Comment.isbn == isbn)
    if not comment_query:
        return jsonify(message="There are no comments for this book.")
    return comments_schema.jsonify(comment_query)


@comments_bp.post("/<isbn>/comments")
def create_comment(isbn):
    book = Book.query.get(isbn)
    print(book)
    if book is None:
        raise NotFound(f"Book [isbn={isbn}] not found.")
    res = request.json
    new_comment = Comment(
        comment=res["comment"],
        book=book,
        isbn=isbn,
        user_id=res["user_id"],
        timestamp=datetime.now(),
    )
    new_comment.validate()
    db.session.add(new_comment)
    db.session.commit()
    return comment_schema.jsonify(new_comment), CREATED
