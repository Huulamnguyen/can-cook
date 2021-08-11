"SQLAlchemhy Models for Can Cook App"
from flask_bcrypt import Bcrypt 
from flask_sqlalchemy import SQLAlchemy 

bcrypt = Bcrypt()  
db = SQLAlchemy()  

# Default picture for users
URL_PHOTO_DEFAULT = "https://t4.ftcdn.net/jpg/02/15/84/43/240_F_215844325_ttX9YiIIyeaR7Ne6EaLLjMAmy4GvPC69.jpg"

def connect_db(app):
    """
    Connect this database to provided Flask app.
    You should call this in your Flask app.
    """
    db.app = app
    db.init_app(app)
    db.create_all()


# TODO: FAVORITE model
class Favorite(db.Model):
    """ Favorite Table """
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipe_id = db.Column(db.Integer)

    # todo: relationship between User and Favorite
    user = db.relationship("User", backref="favorites")

# TODO: USER model
class User(db.Model):
    """ User Table """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    image_url = db.Column(db.Text, default = URL_PHOTO_DEFAULT)
    password = db.Column(db.Text, nullable=False)

    # TODO: REGISTER METHOD, CREATE NEW USERNAME AND PASSWORD THEN STORE IT AT DATABASE
    @classmethod
    def register(cls, username, email, image_url, password):
        """Register user w/hashed password & return user."""
        hashed_pwd = bcrypt.generate_password_hash(password).decode("utf8")
        user = User(username = username, email = email, image_url = image_url, password = hashed_pwd)
        db.session.add(user)
        #return instance of user w/username and hashed pwd
        return user
    
    # TODO: AUTHENTICATE METHOD, WHEN USER INPUT PASSWORD FROM FORM AND COMPARE IT TO DATABASE
    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct. Return user if valid; else return False."""
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password, pwd):
            #return user instance
            return u
        else:
            return False