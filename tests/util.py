import random
from http import HTTPStatus
from werkzeug.datastructures import Headers


def setup_admin_login(client):
    user = get_random_admin_user()
    response = client.post("/api/v1/auth/register", json=user)
    assert response.status_code == HTTPStatus.CREATED
    form = {"email": user["email"], "password": user["password"]}
    response = client.post("/api/v1/auth/login", json=form)
    assert response.status_code == HTTPStatus.OK
    return response.get_data(as_text=True)


def get_headers(token):
    assert token is not None and len(token) > 0
    return Headers({"Authorization": f"Bearer {token}"})


def get_random_admin_user():
    return {
        "first_name": "Admin",
        "last_name": "User",
        "email": f"admin-{random.randint(1000000000000, 9999999999999)}@example.com",
        "password": "password",
        "role_name": "ADMIN",
    }


def get_dummy_author():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "biography": "The biography for this author.",
        "publisher": "Some Publisher",
    }


def get_dummy_book():
    return {
        "isbn": str(random.randint(1000000000000, 9999999999999)),
        "title": "Some Book" + str(random.randint(1000000000000, 9999999999999)),
        "description": "Some description.",
        "price": random.randint(1, 100),
        "publisher": "Some Publisher",
        "year": random.randint(1900, 2020),
        "copies_sold": random.randint(0, 100),
        "genre_name": "Fantasy",
        "author_id": 1,
    }
