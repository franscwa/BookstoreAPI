from flask import Blueprint, request, jsonify
from models.rating import Rating, RatingSchema
from werkzeug.exceptions import NotFound
from http.client import OK, CREATED, NO_CONTENT, BAD_REQUEST
from config.db import db
from models.book import Book, BookSchema
from models.comment import Comment, CommentSchema
from datetime import datetime


admin_bp = Blueprint(name="admin", import_name=__name__, url_prefix="/admin")
dummy_comments = [
        "This book is fantastic!!!",
        "I can't believe that I went so long without this book!",
        "OMG, it's just so good!",
        "I want to read it again."
    ]

@admin_bp.delete("/drop_all")
def drop_all():
    db.drop_all()
    return jsonify(code=200, message="All tables dropped"), OK


@admin_bp.put("/migrate")
def create_all():
    db.create_all()
    return jsonify(code=201, message="All tables migrated"), CREATED


@admin_bp.put("/seedBooks")
def seed_books_db():
    books = list()
    books.append(Book(title="The Hobbit", description="A great book", price=10.99))
    books.append(Book(title="The Silmarillion", description="A great book", price=11.99))
    books.append(Book(title="The Fellowship of the Ring", description="A great book", price=12.99))
    books.append(Book(title="The Two Towers", description="A really great book", price=13.99))
    books.append(Book(title="The Return of the King", description="A great book", price=15.99))
    books.append(Book(title="A New Hope", description="A great book", price=24.99))
    db.session.add_all(books)
    db.session.commit()
    return jsonify(code=201, message="database seeded with books"), CREATED


@admin_bp.put("/seedRatings")
def seed_ratings_db():
    ratings = list()
    ratings.append(Rating(rating=5, books_id=2, timestamp=datetime.now()))
    ratings.append(Rating(rating=4, books_id=3, timestamp=datetime.now()))
    ratings.append(Rating(rating=3, books_id=1, timestamp=datetime.now()))
    ratings.append(Rating(rating=2, books_id=2, timestamp=datetime.now()))
    db.session.add_all(ratings)
    db.session.commit()
    return jsonify(code=201, message="database seeded with ratings"), CREATED


@admin_bp.put("/seedComments")
def seed_comments_db():
    comments = list()
    comments.append(Comment(comment=dummy_comments[0], books_id=2, timestamp=datetime.now()))
    comments.append(Comment(comment=dummy_comments[1], books_id=3, timestamp=datetime.now()))
    comments.append(Comment(comment=dummy_comments[2], books_id=1, timestamp=datetime.now()))
    comments.append(Comment(comment=dummy_comments[3], books_id=2, timestamp=datetime.now()))
    db.session.add_all(comments)
    print('okay')
    db.session.commit()
    return jsonify(code=201, message="database seeded with comments"), CREATED


@admin_bp.put("/seed")
def seed_db():
    books = list()
    books.append(Book(title="The Hobbit", description="A great book", price=10.99))
    books.append(Book(title="The Silmarillion", description="A great book", price=11.99))
    books.append(Book(title="The Fellowship of the Ring", description="A great book", price=12.99))
    books.append(Book(title="The Two Towers", description="A really great book", price=13.99))
    books.append(Book(title="The Return of the King", description="A great book", price=15.99))
    books.append(Book(title="A New Hope", description="A great book", price=24.99))

    db.session.add_all(books)
    db.session.commit()

    ratings = list()
    ratings.append(Rating(rating=5, books_id=2, timestamp=datetime.now()))
    ratings.append(Rating(rating=4, books_id=3, timestamp=datetime.now()))
    ratings.append(Rating(rating=3, books_id=1, timestamp=datetime.now()))
    ratings.append(Rating(rating=2, books_id=2, timestamp=datetime.now()))
    db.session.add_all(ratings)
    db.session.commit()

    comments = list()
    comments.append(Comment(comment=dummy_comments[0], books_id=2, timestamp=datetime.now()))
    comments.append(Comment(comment=dummy_comments[1], books_id=3, timestamp=datetime.now()))
    comments.append(Comment(comment=dummy_comments[2], books_id=1, timestamp=datetime.now()))
    comments.append(Comment(comment=dummy_comments[3], books_id=2, timestamp=datetime.now()))
    db.session.add_all(comments)
    db.session.commit()

    return jsonify(code=201, message="database seeded"), CREATED


