"SQLAlchemhy Models for Can Cook App"
from flask_bcrypt import Bcrypt 
from flask_sqlalchemy import SQLAlchemy 

bcrypt = Bcrypt()  
db = SQLAlchemy()  

def connect_db(app):
    """
        Connect this database to provided Flask app.
        You should call this in your Flask app.
    """
    db.app = app
    db.init_app(app)
    db.create_all()

# Default picture for users
URL_PHOTO_DEFAULT = "./asset/default-pic.png"


# TODO: USER model
class User(db.Model):
    """ User Table """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    image_url = db.Column(db.Text, default = URL_PHOTO_DEFAULT)
    password = db.Column(db.Text, nullable=False)

    # Relationship between User and Favorite
    favorite = db.Relationship('Favorite', backref="user", cascade="all,delete")

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
        
class Favorite(db.Model):
    """ Favorite Table """
    __tablename__ = 'favorite'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))
    recipe_id = db.Column(db.Integer)



