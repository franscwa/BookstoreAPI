# When you clone the repo

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
