# Creator: Daniel Gamon

# (Create and activate virtual environment)
# python -m venv env
# env/scripts/activate

# (Install packages)
# pip install -r requirements.txt

# (Create .env file)
# touch .env

# (Set required environment variables in .env file)
# FLASK_RUN_PORT = '5500'
# FLASK_APP = 'appDGamon.py'
# FLASK_DEBUG = 'True'
# SECRET_KEY = 'some_secret_key'
# SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/bookstore'

# (Run tests)
# pytest

# (Run app db commands)
# flask db migrate
# flask db seed
# flask db drop (Only use when feature is completely demoed as it wipes the database clean)

# (start app)
# python appDGamon.py (or run in appDGamon file)



from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, String, Integer, Float
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from models import *
from models.user import *
from models.book import *
from models.wishlist import *
from config.db import db
from config.ma import ma
from config.config import load_config
from commands.db_cli import db_cli
from blueprints.admin import admin_bp
from blueprints.auth import auth_bp
from blueprints.authors import authors_bp
from blueprints.books import books_bp
from blueprints.ratings import ratings_bp
from blueprints.comments import comments_bp
import jwt




app = Flask(import_name=__name__, static_folder=None)

config = load_config()
app.config.from_mapping(config)

ma.init_app(app)
db.init_app(app)

app.cli.add_command(db_cli)

app.register_blueprint(admin_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(authors_bp)
app.register_blueprint(books_bp)
app.register_blueprint(ratings_bp)
app.register_blueprint(comments_bp)

app.app_context().push()





@app.route('/api/v1/user/<int:user_id>/wishlist', methods = ['POST'])
def create_a_wishlist(user_id):
    
    data = request.get_json()
    
    user_data = request.get_json()
    
    get_user_id = user_data.get('user_id')


    new_wishlist = Wishlist(wishlist_name = data.get('wishlist_name'),
                       user_id = data.get('user_id') 
    )
        
    new_wishlist.save()
    
    db.session.commit()

    serializer = WishlistSchema()

    data = serializer.dump(new_wishlist)

    return jsonify(
    ), 201
# Route and code for creating a wishlist    
    





@app.route('/api/v1/user/<int:userid>/wishlist/<int:wishlistid>/book', methods = ['POST'])

def add_a_wishlist_book(userid, wishlistid):
    
    user = User.get_user(userid)
    
    wishlist_data = request.get_json()
    
    get_the_wishlistid = wishlist_data.get('wishlistid')
    
    book_data = request.get_json()
    
    get_isbn = book_data.get('isbn')
        
    get_wishlistid = Wishlist.query.filter_by(wishlistid = wishlistid).first()
    get_book_to_add = Book.query.filter_by(isbn = get_isbn).first()
    
    get_wishlistid.wishlistbooks.append(get_book_to_add)
    
    db.session.commit()      
    
    return jsonify(
    ), 200
# Route and code for adding a book to the wishlist    
    
    
    
    
@app.route('/api/v1/user/<int:userid>/wishlist/<int:wishlistid>/book/<string:isbn>', methods = ['DELETE'])

def delete_wishlist_book(userid, wishlistid, isbn):
    
    user = User.get_user(userid)
        
    wishlist_data = request.get_json()
    
    book_data = request.get_json()
    
    get_wishlist_data = wishlist_data.get('wishlistid')
    
    get_book_data = book_data.get('isbn')
        
    get_wishlistid = Wishlist.query.filter_by(wishlistid = wishlistid).first()
    get_book_to_delete = Book.query.filter_by(isbn = isbn).first()
             
    get_wishlistid.wishlistbooks.remove(get_book_to_delete)
    
    db.session.commit()    
    
    return jsonify(
    ), 200    
# Route and code for deleteing a book from the wishlist    
   
    
    
    
@app.route('/api/v1/user/<int:userid>/wishlist/<int:wishlistid>/book', methods = ['GET'])

def get_all_wishlist_books(userid, wishlistid):
    
    userid = User.get_user(userid)
    
    wishlist_data = request.get_json()

    get_wishlist_data = wishlist_data.get('wishlistid')
    
    wishlistid = Wishlist.get_wishlist(wishlistid)        

    wishlistbooks = wishlistid.wishlistbooks   
        
    serializer = BookSchema(many = True)
    
    data = serializer.dump(wishlistbooks)
    
    return jsonify(
        data
    ), 200
# Route and code for obtaining all books in a wishlist    
    
 
    
    
    
        
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = app.config["FLASK_RUN_PORT"])
    
    
   