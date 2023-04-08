from flask import Blueprint, request
from config.db import db
from models.author import author_schema
from models.role import Roles
from http import HTTPStatus
from config.authn import jwt_required
from config.authz import roles_required

authors_bp = Blueprint(
    name="authors_bp", import_name=__name__, url_prefix="/api/v1/authors"
)


@authors_bp.post("")
@jwt_required
@roles_required([Roles.ADMIN])
def create_author():
    author = author_schema.load(request.json)
    author.validate()
    db.session.add(author)
    db.session.commit()
    return "", HTTPStatus.CREATED
