from flask import g
from http import HTTPStatus
from functools import wraps
from models.role import is_valid_role


def requires_roles(roles):
    def decorator(func):
        role_names = set([role.value for role in roles])

        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = g.get("user_role")
            if not is_valid_role(user_role) or user_role not in role_names:
                return "", HTTPStatus.UNAUTHORIZED
            return func(*args, **kwargs)

        return wrapper

    return decorator
