from app import app
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bctypt = Bcrypt()

def connect_db(app):
    """Connects the app to the database"""

    db.app = app
    db.init_app(app)


# User and Character Tables

class User(db.Model):
    """Users Table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)


class Character(db.Model):
    """Characters Table"""

    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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


# Classes table and all associated tables

class Class(db.Model):
    """Classes Table"""

    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    intro = db.Column(db.Text, nullable=False)
    description_1_name = db.Column(db.Text, nullable=False)
    description_1_info = db.Column(db.Text, nullable=False)
    description_2_name = db.Column(db.Text, nullable=False)
    description_2_info = db.Column(db.Text, nullable=False)
    hit_dice = db.Column(db.Text, nullable=False)
    hit_points_at_1st_level = db.Column(db.Text, nullable=False)
    hit_ponits_at_higher_levels = db.Column(db.Text, nullable=False)
    armor_proficiencies = db.Column(db.Text, nullable=False)
    weapon_proficiencies = db.Column(db.Text, nullable=False)
    tool_proficiencies = db.Column(db.Text, nullable=False)
    saving_throw_proficiencies = db.Column(db.PickleType, nullable=False)
    skills = db.Column(db.Text, nullable=False)
    starting_equipment = db.Column(db.Text, nullable=False)
    variant_starting_wealth = db.Column(db.Text, nullable=False)
    description_by_level = db.Column(db.PickleType, nullable=False)


class ClassFeatures(db.Model):
    """Class Features Table"""

    __tablename__ = "class_features"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))


class Archetype(db.Model):
    """Archetypes table"""

    __tablename__ = "archetypes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    caster_type = db.Column(db.Text, nullable=False)
    features = db.Column(db.PickleType, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))


class FightingStyles(db.Model):
    """Fighting Styles Table"""

    __tablename__ = "fighting styles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    aspects = db.Column(db.PickleType, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))


class FightingMastery(db.Model):
    """Fighting Mastery Table"""

    __tablename__ = "fighting masteries"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    aspects = db.Column(db.PickleType, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))


class LightsaberForms(db.Model):
    """Lightsaber Forms Table"""

    __tablename__ = "lightsaber forms"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prerequiste = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))


class TechPowers(db.Model):
    """Tech-Power Table"""

    __tablename__ = "tech powers"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    force_alignment = db.Column(db.Text, nullable=False)
    casting_period = db.Column(db.Text, nullable=False)
    range = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Text, nullable=False)
    concentration = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))
    

class ForcePowers(db.Model):
    """Force Powers Table"""

    __tablename__ = "force powers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    force_alignment = db.Column(db.Text, nullable=False)
    casting_period = db.Column(db.Text, nullable=False)
    range = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Text, nullable=False)
    concentration = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))


# Speces and associated tables

class Specie(db.Model):
    """Species Table"""

    __tablename__ = "species"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    bio_and_appeaerance = db.Column(db.Text, nullable=False)
    society_and_culture = db.Column(db.Text, nullable=False)
    names = db.Column(db.Text, nullable=False)
    ability_score_increase = db.Column(db.Text, nullable=False)
    age = db.Column(db.Text, nullable=False)
    alignment = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    speed = db.Column(db.Text, nullable=False)
    languages = db.Column(db.Text, nullable=False)


class SpecieTraits(db.Model):
    """Species Traits Table"""

    __tablename__ = "species_traits"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey("species.id"))


# Backgrounds and associated Tables

class Background(db.Model):
    """Backgrounds Table"""

    __tablename__ = "backgrounds"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    intro = db.Column(db.Text, nullable=False)
    skill_proficiencies = db.Column(db.Text, nullable=False)
    languages = db.Column(db.Text, nullable=False)
    background_feature_name = db.Column(db.Text, nullable=False)
    background_feature_details = db.Column(db.Text, nullable=False)


class Feat(db.Model):
    """Feats table"""

    __tablename__ = "feats"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"))
    feats = db.Column(db.PickleType, nullable=False)


class PersonalityTraits(db.Model):
    """Personality Traits Table"""

    __tablename__ = "personality_traits"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"))
    traits = db.Column(db.PickleType, nullable=False)

class Ideals(db.Model):
    """Ideals Table"""

    __tablename__ = "ideals"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"))
    ideals = db.Column(db.PickleType, nullable=False)


class Bonds(db.Model):
    """Bonds Table"""

    __tablename__ = "bonds"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"))
    bonds = db.Column(db.PickleType, nullable=False)

class Flaws(db.Model):
    """Flaws Table"""

    __tablename__ = "flaws"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"))
    flaws = db.Column(db.PickleType, nullable=False)


# Equipment Tables


class CharacterEquipment(db.Model):
    """Character's Equipment Table"""

    __tablename__ = "character_equipment"

    aromr_id = db.Column(db.Integer, db.ForeignKey("armors.id"))
    weapon_id = db.Column(db.Integer, db.ForeignKey("weapons.id"))
    adventuring_gear_id = db.Column(db.Integer, db.ForeignKey("adventuring_gears.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"))




class Armor(db.Model):
    """Armor table"""

    __tablename__ = "armors"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    properties = db.Column(db.PickleType, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    armor_class = db.Column(db.Text, nullable=False)
    stealth = db.Column(db.Text, nullable=False)


class Weapon(db.Model):
    """Weapons Table"""

    __tablename__ = "weapons"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    properties = db.Column(db.PickleType, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    damage = db.Column(db.Text, nullable=False)


class AdventureingGear(db.Model):
    """Adventuring Gear Table"""

    __tablename__ = "adventuring_gears"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)