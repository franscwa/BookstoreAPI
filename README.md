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

## Tutorial

    https://www.youtube.com/watch?v=EAokwpPMVdc
