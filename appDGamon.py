from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, String, Integer, Float
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from models import *
from models.book import *
from models.user import *
from models.wishlist import *
from models.wishlist_books import *




#run in Python interpretor
#from app import db
#db.create_all()

app = Flask(__name__)

app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/bookstore'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)








@app.route('/api/v1/user/<int:userid>/wishlist', methods = ['POST'])
def create_a_wishlist(userid):
    
    data = request.get_json()
    
    user_data = request.get_json()
    
    get_userid = user_data.get('userid')


    new_wishlist = Wishlist(wishlist_name = data.get('wishlist_name'),
                       user_id = data.get('userid') 
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
    
    
    
    
@app.route('/api/v1/user/<int:userid>/wishlist/<int:wishlistid>/book/<int:isbn>', methods = ['DELETE'])

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
    app.run(host = "0.0.0.0", port = app.config["FLASK_RUN_POST"])
    
   