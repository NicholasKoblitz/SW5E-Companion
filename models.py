from app import app
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bctypt = Bcrypt()

def connect_db(app):
    """Connects the app to the database"""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Users Table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)


class Character(db.Model):
    """Characters Table"""

    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))
    species_id = db.Column(db.Integer, db.ForeignKey("speces.id"))
    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"))
    xp_points = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    str_saving_throw = db.Column(db.Integer, nullable=False)
    athletics = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    dex_saving_throw = db.Column(db.Integer, nullable=False)
    acrobatics = db.Column(db.Integer, nullable=False)
    sleight_of_hand = db.Column(db.Integer, nullable=False)
    stealth = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    con_saving_thorw = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    int_saving_throw = db.Column(db.Integer, nullable=False)
    investagation = db.Column(db.Integer, nullable=False)
    lore = db.Column(db.Integer, nullable=False)
    nature = db.Column(db.Integer, nullable=False)
    piloting = db.Column(db.Integer, nullable=False)
    technology = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    wis_saving_throw = db.Column(db.Integer, nullable=False)
    animal_handling = db.Column(db.Integer, nullable=False)
    insight = db.Column(db.Integer, nullable=False)
    medicine = db.Column(db.Integer, nullable=False)
    perception = db.Column(db.Integer, nullable=False)
    survival = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    cha_saving_throw = db.Column(db.Integer, nullable=False)
    deception = db.Column(db.Integer, nullable=False)
    intimidation = db.Column(db.Integer, nullable=False)
    performance = db.Column(db.Integer, nullable=False)
    persuasion = db.Column(db.Integer, nullable=False)
    passive_perception = db.Column(db.Integer, nullable=False)
    proficiency_bonus = db.Column(db.Integer, nullable=False)
    initiative = db.Column(db.Integer, nullable=False)
    armor_class = db.Column(db.Integer, nullable=False)
    hit_ponits = db.Column(db.Integer, nullable=False)
    hit_dice = db.Column(db.Integer, nullable=False)
    base_speed = db.Column(db.Text, nullable=False)
    vision = db.Column(db.Text, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    weapons = db.Column(db.PickleType, nullable=False)
    equipment = db.Column(db.PickleType)
    proficiencies = db.Column(db.Text, nullable=False)
    languages = db.Column(db.Text, nullable=False)


class Class(db.Model):
    """Classes Table"""

    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)