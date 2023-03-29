from flask import Blueprint, request
from config.db import db
from models.author import author_schema
from http import HTTPStatus


authors_bp = Blueprint(
    name="authors_bp", import_name=__name__, url_prefix="/api/v1/authors"
)


@authors_bp.post("")
def create_author():
    author = author_schema.load(request.json)
    author.validate()
    db.session.add(author)
    db.session.commit()
    return "", HTTPStatus.CREATED
