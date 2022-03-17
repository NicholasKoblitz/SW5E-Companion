from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class SignupForm(FlaskForm):
    """User's sign up form"""

    username = StringField("Username")
    password = PasswordField("Password")

class LoginForm(FlaskForm):
    """User's Login Form"""

    username = StringField("Username")
    password = PasswordField("Password")