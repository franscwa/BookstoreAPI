from flask import Blueprint, request
from config.db import db
from models.author import author_schema
from models.role import Roles
from http import HTTPStatus
from config.authn import requires_authn
from config.authz import requires_roles

authors_bp = Blueprint(
    name="authors_bp", import_name=__name__, url_prefix="/api/v1/authors"
)


@authors_bp.post("")
@requires_authn
@requires_roles([Roles.ADMIN])
def create_author():
    author = author_schema.load(request.json)
    author.validate()
    db.session.add(author)
    db.session.commit()
    return "", HTTPStatus.CREATED
