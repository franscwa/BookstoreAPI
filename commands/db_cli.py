import click
from flask.cli import AppGroup, with_appcontext
from config.db import db
from models.book import Book

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
    book1 = Book(
        title="The Hobbit",
        description="A great book",
        price=10.99,
        genre="Fantasy Fiction",
        quantity_sold=1000,
        rating=5,
        publisher="George Allen & Unwin",
    )
    book2 = Book(
        title="The Silmarillion",
        description="A great book",
        price=11.99,
        genre="Fantasy Fiction",
        quantity_sold=999,
        rating=4,
        publisher="George Allen & Unwin",
    )
    book3 = Book(
        title="The Fellowship of the Ring",
        description="A great book",
        price=12.99,
        genre="Fantasy Fiction",
        quantity_sold=888,
        rating=3,
        publisher="George Allen & Unwin",
    )
    book4 = Book(
        title="The Two Towers",
        description="A great book",
        price=13.99,
        genre="Fantasy Fiction",
        quantity_sold=777,
        rating=2,
        publisher="George Allen & Unwin",
    )
    book5 = Book(
        title="The Return of the King",
        description="A great book",
        price=15.99,
        genre="Fantasy Fiction",
        quantity_sold=888,
        rating=1,
        publisher="George Allen & Unwin",
    )
    book6 = Book(
        title="To Kill a Mockingbird",
        description="A classic novel",
        price=9.99,
        genre="Fiction",
        quantity_sold=500,
        rating=5,
        publisher="J. B. Lippincott & Co.",
    )
    book7 = Book(
        title="1984",
        description="A dystopian novel",
        price=8.99,
        genre="Fiction",
        quantity_sold=700,
        rating=4,
        publisher="Secker & Warburg",
    )
    book8 = Book(
        title="The Great Gatsby",
        description="A classic novel",
        price=11.99,
        genre="Fiction",
        quantity_sold=600,
        rating=5,
        publisher="Charles Scribner's Sons",
    )
    book9 = Book(
        title="The Catcher in the Rye",
        description="A coming-of-age novel",
        price=10.99,
        genre="Fiction",
        quantity_sold=800,
        rating=4,
        publisher="Little, Brown and Company",
    )
    book10 = Book(
        title="Pride and Prejudice",
        description="A classic novel",
        price=12.99,
        genre="Fiction",
        quantity_sold=900,
        rating=5,
        publisher="T. Egerton, Whitehall",
    )
    books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]
    db.session.add_all(books)
    db.session.commit()
    print("db seeded")


db_cli.add_command(migrate)
db_cli.add_command(drop)
db_cli.add_command(seed)
