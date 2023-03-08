import click
from flask.cli import AppGroup, with_appcontext
from config.db import db
from models.book import Book
from models.rating import Rating
from datetime import datetime

db_cli = AppGroup(name="db")


@db_cli.command("migrate")
def migrate():
    """Migrate the database models."""
    db.create_all()
    print("db migrated")


@db_cli.command("drop")
def drop():
    """Drop the database tables."""
    db.drop_all()
    print("db tables dropped")


@db_cli.command("seed_books")
def seed_books():
    """Seed the database with data."""
    book1 = Book(
        title="The Hobbit",
        description="A great book",
        price=10.99,
    )
    book2 = Book(
        title="The Silmarillion",
        description="A great book",
        price=11.99,
    )
    book3 = Book(
        title="The Fellowship of the Ring",
        description="A great book",
        price=12.99,
    )
    book4 = Book(
        title="The Two Towers",
        description="A great book",
        price=13.99,
    )
    book5 = Book(
        title="The Return of the King",
        description="A great book",
        price=15.99,
    )
    books = [book1, book2, book3, book4, book5]
    db.session.add_all(books)
    db.session.commit()
    print("books db seeded")

@db_cli.command("seed_ratings")
def seed_ratings():
    """Seed the database with data."""
    rating1 = Rating(rating=5, books_id=2, timestamp=datetime.now())
    rating2 = Rating(rating=4, books_id=3, timestamp=datetime.now())
    rating3 = Rating(rating=3, books_id=1, timestamp=datetime.now())
    rating4 = Rating(rating=2, books_id=2, timestamp=datetime.now())

    ratings = [rating1, rating2, rating3, rating4]
    db.session.add_all(ratings)
    db.session.commit()
    print("ratings db seeded")





db_cli.add_command(migrate)
db_cli.add_command(drop)
db_cli.add_command(seed_books)
db_cli.add_command(seed_ratings)

