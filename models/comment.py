from config.db import db
from config.ma import ma

MAX_COMMENT = 250


class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(MAX_COMMENT), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    isbn = db.Column(db.String, db.ForeignKey("book.isbn"), nullable=False)
    book = db.relationship("Book", back_populates="comments")

    def validate(self):
        assert 0 < int(self.isbn) < 9999999999, "non-empty book title is required"
        assert (
            self.comment and 0 < len(self.comment) <= MAX_COMMENT
        ), "non-empty comment < 250 characters is required"


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        dump_only = ("comment_id",)
        exclude = ("book",)
        load_instance = True


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
