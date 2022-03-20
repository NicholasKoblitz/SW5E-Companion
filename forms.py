from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField

class SignupForm(FlaskForm):
    """User's sign up form"""

    username = StringField("Username")
    password = PasswordField("Password")

class LoginForm(FlaskForm):
    """User's Login Form"""

    username = StringField("Username")
    password = PasswordField("Password")

class AbilityScoresForm(FlaskForm):
    """Character Ability Scores Form"""

    strength = SelectField("Strength", choices=[(15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    dexterity = SelectField("Dexterity", choices=[(15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    constitution = SelectField("Constitution", choices=[(15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    intelligence = SelectField('Intelligence', choices=[(15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    wisdom = SelectField("Wisdom", choices=[(15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])
    charisma = SelectField("Charisma", choices=[(15,15), (14,14), (13,13), (12,12), (10,10), (8,8)])


class DescriptionForm(FlaskForm):
    """Character Description Form"""

    name = StringField("Name")
    # image_url = StringField("Image URL")
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
    background = SelectField("Backgrounds", choices=[
        ("Agent", "Agent"), 
        ("Bounty Hunter", "Bounty Hunter"), 
        ("Criminal", "Criminal")
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
    appearance = StringField('Appearance')
    backstory = StringField("Backstory")