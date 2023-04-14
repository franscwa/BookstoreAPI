Clone repo

git clone https://github.com/franscwa/BookstoreAPI.git
Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate
Install packages

pip install -r requirements.txt
Create .env file

touch .env
Set required environment variables in .env file

FLASK_RUN_PORT='8080'
FLASK_APP='app.py'
FLASK_DEBUG='True'
SECRET_KEY='some_secret_key'
SQLALCHEMY_TRACK_MODIFICATIONS='False'
<!-- Use one of the following: -->
SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite' # sqlite
SQLALCHEMY_DATABASE_URI='sqlite:///:memory:' # in-memory sqlite
SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost:5432/bookstore' # postgresql
Run tests

pytest
Run app db commands

flask db migrate
flask db seed
flask db drop
Start app

python3 app.py