from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email

class RegisterForm(FlaskForm):
    """Form for registering users"""
    username = StringField("Username",  validators = [InputRequired("Please enter your username.")])
    email = StringField("Email", validators = [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    image_url = StringField("Profile image", default = "https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1489&q=80")
    password = PasswordField("Password", validators =[InputRequired("Please enter your valid password.")])

class LoginForm(FlaskForm):
    """Form for user login"""
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])