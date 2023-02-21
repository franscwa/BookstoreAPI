from flask.cli import AppGroup
from config.db import db
from models.book import Book
from models.genre import Genre
from models.author import Author
# from models.rating import Rating

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


@db_cli.command("seed")
def seed():
    """Seed the database with data."""

    genre1 = Genre(name="Fantasy")
    genre2 = Genre(name="Adventure")
    genre3 = Genre(name="Science-Fiction")
    genres = [genre1, genre2, genre3]
    db.session.add_all(genres)
    db.session.commit()

    author1 = Author(
        first_name="J.R.R.",
        last_name="Tolkien",
        biography="J. R. R. Tolkien was an English writer, poet, philologist, and university professor.",
        publisher="Houghton Mifflin Harcourt",
    )
    db.session.add(author1)

    book1 = Book(
        title="The Hobbit",
        isbn="0000000000001",
        description="A great book",
        price=10.99,
        publisher="Houghton Mifflin Harcourt",
        year=1937,
        copies_sold=10,
        genre=genre2,
        author=author1,
        rating = 0
    )
    book2 = Book(
        title="The Silmarillion",
        isbn="0000000000002",
        description="A great book",
        price=11.99,
        publisher="Houghton Mifflin Harcourt",
        year=1977,
        copies_sold=15,
        genre=genre3,
        author=author1,
        rating = 0
    )
    book3 = Book(
        title="The Fellowship of the Ring",
        isbn="0000000000003",
        description="A great book",
        price=12.99,
        publisher="Houghton Mifflin Harcourt",
        year=1954,
        copies_sold=20,
        genre=genre1,
        author=author1,
        rating = 0
    )
    book4 = Book(
        title="The Two Towers",
        isbn="0000000000004",
        description="A great book",
        price=13.99,
        publisher="Houghton Mifflin Harcourt",
        year=1954,
        copies_sold=25,
        genre=genre1,
        author=author1,
        rating = 0
    )
    book5 = Book(
        title="The Return of the King",
        isbn="0000000000005",
        description="A great book",
        price=15.99,
        publisher="Houghton Mifflin Harcourt",
        year=1955,
        copies_sold=30,
        genre=genre1,
        author=author1,
        rating = 0
    )
    books = [book1, book2, book3, book4, book5]
    db.session.add_all(books)

    db.session.commit()
    print("db seeded")


@db_cli.command("update")
def update():
    """Update the seed data in the database."""

    book1 = Book.query.filter_by(isbn="0000000000001").first()
    book1.title = "The Hobbit"
    book1.description = "A great book"
    book1.price = 12.99
    book1.copies_sold = 20
    book1.rating = 0

    book2 = Book.query.filter_by(isbn="0000000000002").first()
    book2.title = "The Silmarillion"
    book2.description = "A great book (Updated)"
    book2.price = 13.99
    book2.copies_sold = 25
    book2.rating = 0

    book3 = Book.query.filter_by(isbn="0000000000003").first()
    book3.title = "The Fellowship of the Ring"
    book3.description = "A great book"
    book3.price = 14.99
    book3.copies_sold = 30
    book3.rating = 0

    book4 = Book.query.filter_by(isbn="0000000000004").first()
    book4.title = "The Two Towers"
    book4.description = "A great book"
    book4.price = 15.99
    book4.copies_sold = 35
    book4.rating = 0

    book5 = Book.query.filter_by(isbn="0000000000005").first()
    book5.title = "The Return of the King"
    book5.description = "A great book"
    book5.price = 16.99
    book5.copies_sold = 40
    book5.rating = 0

    db.session.commit()
    print("db updated")


db_cli.add_command(migrate)
db_cli.add_command(drop)
db_cli.add_command(seed)
db_cli.add_command(update)