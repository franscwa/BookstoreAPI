## Getting Started

1.  Clone repo
    ```
    git clone https://github.com/franscwa/BookstoreAPI.git
    ```
2.  Create and activate virtual environment
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install packages
    ```
    pip install -r requirements.txt
    ```
4.  Create .**env** file
    ```
    touch .env
    ```
5.  Set required environment variables in **.env** file

    ```
    FLASK_RUN_PORT='8080'
    FLASK_APP='app.py'
    FLASK_DEBUG='True'
    SECRET_KEY='some_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS='False'
    <!-- Use one of the following: -->
    SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite' # sqlite
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:' # in-memory sqlite
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost:5432/bookstore' # postgresql
    ```

6.  Run tests
    ```
    pytest
    ```
7.  Run app db commands
    ```
    flask db migrate
    flask db seed
    flask db drop
    ```
8.  Start app
    ```
    python3 app.py
    ```

1. Create a virtual environment
    > python3 -m venv venv
2. Install packages
    > pip install -r requirements.txt
3. Create .env file
    > touch .env
4. Set environment variables
    > echo "PORT=8080\n\nFLASK_DEBUG=1\nFLASK_APP=app.py\n\nSQLALCHEMY_TRACK_MODIFICATIONS=False\nSQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite" >> .env
5. Start app
    > python3 app.py

OR run this command:
> make first-setup
