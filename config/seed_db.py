from config.db import db
from models.book import Book
from schemas.book import BookSchema


books_schema = BookSchema(many=True)


