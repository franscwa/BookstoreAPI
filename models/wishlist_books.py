from appDGamon import db


wishlist_books = db.Table('wishlist_books',
    db.Column('wishlistid', db.Integer, db.ForeignKey('wishlist.wishlistid'), primary_key = True) ,
    db.Column('isbn', db.Integer, db.ForeignKey('book.isbn'), primary_key = True)                    
)    