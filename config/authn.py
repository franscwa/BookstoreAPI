from flask import request, g
from http import HTTPStatus
from functools import wraps
from config.config import app_config
from models.user import User
import jwt


def requires_authn(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if auth_header is None:
            return "", HTTPStatus.UNAUTHORIZED
        parts = auth_header.split(" ")
        if len(parts) != 2 or parts[0] != "Bearer":
            return "", HTTPStatus.UNAUTHORIZED
        token = parts[1]
        if token is None:
            return "", HTTPStatus.UNAUTHORIZED
        try:
            decoded_token = jwt.decode(
                token, app_config["SECRET_KEY"], algorithms=["HS256"]
            )
            user_id = decoded_token["user_id"]
            user = User.query.filter_by(user_id=user_id).first()
            if user is None:
                return "", HTTPStatus.UNAUTHORIZED
            g.user_id = user.user_id
            g.user_role = user.role_name
        except Exception as e:
            return "", HTTPStatus.UNAUTHORIZED
        return func(*args, **kwargs)

    return wrapper
