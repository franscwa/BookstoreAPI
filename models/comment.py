from config.db import db
from config.ma import ma

MAX_COMMENT = 250


class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(MAX_COMMENT), nullable=False)
    books_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    timestamp = db.Column(db.DateTime, nullable=False)

    def validate(self):
        assert int(self.books_id) and int(self.books_id) > 0, "non-empty book title is required"
        assert self.comment and 0 < len(self.comment) <= MAX_COMMENT, "non-empty comment < 250 characters is required"


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        dump_only = ("comment_id",)
        load_instance = True
