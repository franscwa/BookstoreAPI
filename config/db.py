# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        # port="8000",
        user='postgres',
        password='212426')
