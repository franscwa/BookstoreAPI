from config.db import db


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
