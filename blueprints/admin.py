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
    "I want to read it again.",
]


@admin_bp.delete("/drop_all")
def drop_all():
    db.drop_all()
    return jsonify(code=200, message="All tables dropped"), OK


@admin_bp.put("/migrate")
def create_all():
    db.create_all()
    return jsonify(code=201, message="All tables migrated"), CREATED


@admin_bp.put("/seed")
def seed_db():
    books = list()
    books.append(
        Book(
            isbn="1234567890",
            title="The Hobbit",
            description="A trilogy",
            price=10.99,
            publisher="TheHouse",
            year="1990",
            copies_sold=1500,
            avg_rating=4.5,
        )
    )

    books.append(
        Book(
            isbn="1234567891",
            title="1984",
            description="A good book",
            price=10.99,
            publisher="NewYorkHouse",
            year="2010",
            copies_sold=750,
            avg_rating=3.1,
        )
    )

    books.append(
        Book(
            isbn="1234567892",
            title="The Silmarillion",
            description="A story",
            price=15.99,
            publisher="TheOtherHouse",
            year="1910",
            copies_sold=100,
            avg_rating=1.5,
        )
    )

    db.session.add_all(books)
    db.session.commit()

    ratings = list()
    ratings.append(Rating(rating=5, book=books[0], user_id=1, timestamp=datetime.now()))
    ratings.append(Rating(rating=4, book=books[1], user_id=2, timestamp=datetime.now()))
    ratings.append(Rating(rating=3, book=books[2], user_id=3, timestamp=datetime.now()))
    ratings.append(Rating(rating=2, book=books[0], user_id=4, timestamp=datetime.now()))
    db.session.add_all(ratings)
    db.session.commit()

    comments = list()
    comments.append(
        Comment(
            comment=dummy_comments[0],
            book=books[0],
            user_id=1,
            timestamp=datetime.now(),
        )
    )
    comments.append(
        Comment(
            comment=dummy_comments[1],
            book=books[1],
            user_id=2,
            timestamp=datetime.now(),
        )
    )
    comments.append(
        Comment(
            comment=dummy_comments[2],
            book=books[2],
            user_id=3,
            timestamp=datetime.now(),
        )
    )
    comments.append(
        Comment(
            comment=dummy_comments[3],
            book=books[0],
            user_id=4,
            timestamp=datetime.now(),
        )
    )
    db.session.add_all(comments)
    db.session.commit()

    return jsonify(code=201, message="database seeded"), CREATED
