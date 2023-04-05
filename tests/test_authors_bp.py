from http import HTTPStatus
from tests.util import setup_admin_login, get_dummy_author, get_headers

token = None


def test_authors_bp_setup(client):
    global token
    token = setup_admin_login(client)


def test_create_valid_author(client):
    author = get_dummy_author()
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.CREATED


def test_create_invalid_author_with_empty_first_name(client):
    author = get_dummy_author()
    author["first_name"] = ""
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_no_first_name(client):
    author = get_dummy_author()
    author["first_name"] = None
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_empty_last_name(client):
    author = get_dummy_author()
    author["last_name"] = ""
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_no_last_name(client):
    author = get_dummy_author()
    author["last_name"] = None
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_empty_biography(client):
    author = get_dummy_author()
    author["biography"] = ""
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_no_biography(client):
    author = get_dummy_author()
    author["biography"] = None
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_no_publisher(client):
    author = get_dummy_author()
    author["publisher"] = None
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_empty_publisher(client):
    author = get_dummy_author()
    author["publisher"] = ""
    response = client.post("/api/v1/authors", json=author, headers=get_headers(token))
    assert response.status_code == HTTPStatus.BAD_REQUEST
