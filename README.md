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
4.  Create .env file and set environment variables
    ```
    touch .env
    ```
5.  Run tests
    ```
    python3 -m pytest -v
    ```
6.  Run app commands
    ```
    flask db migrate
    flask db seed
    flask db drop
    ```
7.  Start app only
    ```
    python3 app.py
    ```
7.  Start app and postgres in docker
    ```
    docker compose up
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
