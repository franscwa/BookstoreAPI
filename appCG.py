import json
from urllib import response
from flask import Flask, request, request_finished
from flask_restx import Api, Resource

app=Flask(__name__)

api=Api(app)


BASE_URL = 'http://127.0.0.1:5500/'

def create_user(username, password, name=None, email=None, address=None):
    user = {'username': username, 'password': password}
    if name:
        user['name'] = name
    if email:
        user['email'] = email
    if address:
        user['address'] = address
    headers = {'Content-Type': 'application/json'}
    response = request_finished.post(BASE_URL, headers=headers, data=json.dumps(user))
    if response.ok:
        print('User created successfully')
    else:
        print('Error creating user')

def get_user(username):
    url = BASE_URL + '/' + username
    response = request.get(url)
    if response.ok:
        user = json.loads(response.content)
        print('User:', user)
    else:
        print('User not found')

def update_user(username, field, value):
    url = BASE_URL + '/' + username
    user = {field: value}
    headers = {'Content-Type': 'application/json'}
    response = request.put(url, headers=headers, data=json.dumps(user))
    if response.ok:
        print('User updated successfully')
    else:
        print('Error updating user')

def create_credit_card(username, credit_card):
    url = BASE_URL + '/' + username + '/credit-cards'
    headers = {'Content-Type': 'application/json'}
    response = request.post(url, headers=headers, data=json.dumps(credit_card))
    if response.ok:
        print('Credit card created successfully')
    else:
        print('Error creating credit card')

# Example usage:
create_user('john', 'password', 'John Smith', 'john@example.com', '123 Main St')
get_user('john')
update_user('john2', 'email', 'john.smith@example.com')
create_credit_card('john', {'number': '1234-5678-9012-3456', 'expiry': '12/24', 'cvv': '123'})

