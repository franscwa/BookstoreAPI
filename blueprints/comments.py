from flask import Blueprint, request, jsonify
from werkzeug.exceptions import NotFound
from http.client import OK, CREATED, NO_CONTENT, BAD_REQUEST
from config.db import db
from models.book import Book, BookSchema
from models.comment import Comment, CommentSchema
from datetime import datetime


comments_bp = Blueprint(name="comments", import_name=__name__, url_prefix="/api/v1/book")
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
book_schema = BookSchema()


@comments_bp.get("/comments")
def get_comments():
    print("HERE")
    all_comments = Comment.query.all()
    return comments_schema.jsonify(all_comments), OK


@comments_bp.get("/<book_id>/comments")
def get_comments_by_book(book_id):
    comment_query = Comment.query.filter(Comment.books_id == book_id)
    if not comment_query:
        return jsonify(message="There are no comments for this book.")
    return comments_schema.jsonify(comment_query)


@comments_bp.post("/<book_id>/comments")
def create_comment(book_id):
    book = Book.query.get(booko_id)
    print(book)
    if book is None:
        raise NotFound(f"Book [book_id={book_id}] not found.")
    res = request.json
    new_comment = Comment(comment=res["comment"], books_id=book_id, timestamp=datetime.now())
    new_comment.validate()
    db.session.add(new_comment)
    db.session.commit()
    return comment_schema.jsonify(new_comment), CREATED




