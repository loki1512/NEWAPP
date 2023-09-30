from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    username=db.Column(db.String(50),primary_key=True)
    password=db.Column(db.String(50),nullable=False)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    #cart=db.relationship('Products',secondary='user_cart',backref=db.backref('users'))
    
class Admins(db.Model):
    username=db.Column(db.String(50),primary_key=True)
    password=db.Column(db.String(50),nullable=False)
    
class Products(db.Model):
    product_id=db.Column(db.Integer,primary_key=True)
    product_name=db.Column(db.String(50),nullable=False)
    product_price=db.Column(db.Integer,nullable=False)
    inventory_count=db.Column(db.Integer,nullable=False)
    image_url=db.Column(db.String(100),nullable=False)
    category=db.Column(db.String(50),nullable=False)
    
class User_cart(db.Model):
    entry_id=db.Column(db.Integer,auto_increment=True,primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    product_id = db.Column(db.Integer,nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_cost = db.Column(db.Integer)  # No need to specify ForeignKey for unit_cost
    cost = db.Column(db.Integer, nullable=False)
    category=db.Column(db.String(50),nullable=False)
    image_url=db.Column(db.String(100),nullable=False)

    # # Establish the relationship with the Users table using the 'username' foreign key
    # user = db.relationship("Users", backref=db.backref("cart_items", foreign_keys=[username]))
    # # Establish the relationship with the Products table using the 'product_id' foreign key
    # product = db.relationship("Products", backref=db.backref("cart_users", foreign_keys=[product_id]))
    
class Categories(db.Model):
    cat_name = db.Column(db.String(50),primary_key=True)

    


    