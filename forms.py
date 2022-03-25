from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length

class SignupForm(FlaskForm):
    """User's sign up form"""

    username = StringField("Username", validators=[InputRequired(message="Must enter username")])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, message="Password must be at least 8 characters long")])

class LoginForm(FlaskForm):
    """User's Login Form"""

    username = StringField("Username", validators=[InputRequired(message="Must enter username")])
    password = PasswordField("Password", validators=[InputRequired(message="Must enter password")])

class AbilityScoresForm(FlaskForm):
    """Character Ability Scores Form"""

    strength = SelectField("Strength", choices=[(None, "Select Score"), (15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    dexterity = SelectField("Dexterity", choices=[(None, "Select Score"), (15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    constitution = SelectField("Constitution", choices=[(None, "Select Score"), (15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    intelligence = SelectField('Intelligence', choices=[(None, "Select Score"), (15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    wisdom = SelectField("Wisdom", choices=[(None, "Select Score"), (15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    charisma = SelectField("Charisma", choices=[(None, "Select Score"), (15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])


class DescriptionForm(FlaskForm):
    """Character Description Form"""

    name = StringField("Name")
    alignment = SelectField("Choose Charatcer Alignment", choices=[
        ("Lawful Light", "Lawful Light"), 
        ("Neutral Light", "Neutral Light"), 
        ("Chaotic Light", "Chaotic Light"), 
        ("Lawful Balanced", "Lawful Balanced"), 
        ("Neutral Balanced", "Neutral Balanced"), 
        ("Chaotic Balanced", "Chaotic Balanced"), 
        ("Lawful Dark", "Lawful Dark"), 
        ("Neutral Dark", "Neutral Dark"), 
        ("Chaotic Dark", "Chaotic Dark")
        ])
    personality_trait = StringField("Personality Traits")
    ideal = StringField("Ideal")
    bond = StringField("Bond")
    flaw = StringField("Flaw")
    gender = StringField("Gender")
    place_of_birth = StringField("Place of Birth")
    age = StringField("Age")
    height = StringField("Height")
    weight = StringField("Weight")
    hair = StringField("Hair")
    eyes = StringField("Eyes")
    skin = StringField('Skin')
    appearance = TextAreaField('Appearance')
    backstory = TextAreaField("Backstory")