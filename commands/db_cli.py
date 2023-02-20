from flask.cli import AppGroup
from config.db import db
from models.book import Book
from models.genre import Genre
from models.author import Author

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
    )
    books = [book1, book2, book3, book4, book5]
    db.session.add_all(books)

    db.session.commit()
    print("db seeded")


db_cli.add_command(migrate)
db_cli.add_command(drop)
db_cli.add_command(seed)