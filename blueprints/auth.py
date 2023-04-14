from flask import Blueprint, request
from models.user import User, user_schema
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import NotFound, BadRequest
from http import HTTPStatus
from datetime import datetime, timedelta
from config.db import db
from config.config import app_config
import jwt


auth_bp = Blueprint(name="auth_bp", import_name=__name__, url_prefix="/api/v1/auth")


@auth_bp.post("/login")
def login():
    email = request.json.get("email")
    user = User.query.filter_by(email=email).first()
    if user is None:
        raise BadRequest("Invalid email or password.")
    password = request.json.get("password")
    if not check_password_hash(user.password, password):
        return "", HTTPStatus.UNAUTHORIZED
    token = jwt.encode(
        {"user_id": user.user_id, "exp": datetime.utcnow() + timedelta(hours=1)},
        app_config["SECRET_KEY"],
        algorithm="HS256",
    )
    return token, HTTPStatus.OK


@auth_bp.post("/register")
def register():
    user = user_schema.load(request.json)
    user.validate()
    if user.email in {u.email for u in User.query.all()}:
        raise BadRequest(f"User [email={user.email}] already exists.")
    user.password = generate_password_hash(user.password)
    db.session.add(user)
    db.session.commit()
    return "", HTTPStatus.CREATED
