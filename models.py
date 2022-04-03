# from app import app
from ctypes import alignment
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()

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

    character = db.relationship("Character", backref="user")

    @classmethod
    def signup(cls, username, password):
        """Signs up the user"""

        hashed_password = bcrypt.generate_password_hash(password).decode("UTF-8")

        user = User(
            username = username,
            password = hashed_password
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):


        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user
                
        return False



class Character(db.Model):
    """Characters Table"""

    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="cascade"), )
    name = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id",ondelete="cascade"))
    species_id = db.Column(db.Integer, db.ForeignKey("species.id", ondelete="cascade"))
    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id", ondelete="cascade"))
    level = db.Column(db.Integer, nullable=False)
    class_saving_throw_pros = db.Column(db.PickleType, nullable=False)
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
    hit_points = db.Column(db.Integer, nullable=False)
    hit_dice = db.Column(db.Text, nullable=False)
    base_speed = db.Column(db.Text, nullable=False)
    vision = db.Column(db.Text, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    proficiencies = db.Column(db.PickleType, nullable=False)
    skills = db.Column(db.PickleType, nullable=False)
    languages = db.Column(db.PickleType, nullable=False)
    alignment = db.Column(db.Text, nullable=False)
    personality_traits = db.Column(db.Text)
    ideal = db.Column(db.Text)
    bond = db.Column(db.Text)
    flaw = db.Column(db.Text)
    gender = db.Column(db.Text)
    place_of_birth = db.Column(db.Text)
    age = db.Column(db.Text)
    heigth = db.Column(db.Text)
    weigth = db.Column(db.Text)
    hair = db.Column(db.Text)
    eyes = db.Column(db.Text)
    skin = db.Column(db.Text)
    appearance = db.Column(db.Text)
    backstory = db.Column(db.Text)


    character_class = db.relationship("Class", backref="character")
    character_species = db.relationship("Specie", backref="character")
    character_background = db.relationship("Background", backref="character")



# Classes table and all associated tables

class Class(db.Model):
    """Classes Table"""

    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    intro = db.Column(db.PickleType, nullable=False)
    description_1_name = db.Column(db.Text, nullable=False)
    description_1_info = db.Column(db.Text, nullable=False)
    description_2_name = db.Column(db.Text, nullable=False)
    description_2_info = db.Column(db.Text, nullable=False)
    hit_dice = db.Column(db.Text, nullable=False)
    hit_points_at_1st_level = db.Column(db.Text, nullable=False)
    hit_points_at_higher_levels = db.Column(db.Text, nullable=False)
    armor_proficiencies = db.Column(db.Text, nullable=False)
    weapon_proficiencies = db.Column(db.Text, nullable=False)
    tool_proficiencies = db.Column(db.Text, nullable=False)
    saving_throw_proficiencies = db.Column(db.PickleType, nullable=False)
    skills = db.Column(db.Text, nullable=False)
    skill_vals = db.Column(db.PickleType, nullable=False)
    starting_equipment = db.Column(db.PickleType, nullable=False)
    variant_starting_wealth = db.Column(db.Text, nullable=False)
    description_by_level = db.Column(db.PickleType, nullable=False)


class ClassFeatures(db.Model):
    """Class Features Table"""

    __tablename__ = "class_features"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    levels = db.Column(db.PickleType, nullable=False)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="features")

    

class Archetype(db.Model):
    """Archetypes table"""

    __tablename__ = "archetypes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    caster_type = db.Column(db.Text, nullable=False)
    features = db.Column(db.PickleType, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="archetypes")



class FightingStyles(db.Model):
    """Fighting Styles Table"""

    __tablename__ = "fighting_styles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    to_class = db.relationship("Class", secondary="character_fighting_styles", backref="fighting_styles")



class FightingMastery(db.Model):
    """Fighting Mastery Table"""

    __tablename__ = "fighting_masteries"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    to_class = db.relationship("Class", secondary="character_fighting_masteries", backref="fighting_masteries")



class LightsaberForms(db.Model):
    """Lightsaber Forms Table"""

    __tablename__ = "lightsaber_forms"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    prerequisite = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)

    to_class = db.relationship("Class", secondary="character_lightsaber_forms", backref="lightsaber_forms")



class TechPowers(db.Model):
    """Tech-Power Table"""

    __tablename__ = "tech_powers"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    casting_period = db.Column(db.Text, nullable=False)
    range = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Text, nullable=False)
    concentration = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    to_class = db.relationship("Class", secondary="character_tech_powers", backref="tech_powers")

    

class ForcePowers(db.Model):
    """Force Powers Table"""

    __tablename__ = "force_powers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    force_alignment = db.Column(db.Text, nullable=False)
    casting_period = db.Column(db.Text, nullable=False)
    range = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Text, nullable=False)
    concentration = db.Column(db.Text, nullable=False)
    prerequisite = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    to_class = db.relationship("Class", secondary="character_force_powers", backref="force_powers")

# Class specific abilities
class BerserkerInstincts(db.Model):
    """Berserker Instincts Table"""

    __tablename__ = "berserker_instincts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    prerequisite = db.Column(db.Text)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="instincts")


class ForceEmpoweredCasting(db.Model):
    """Force-empowered Casting Table"""

    __tablename__ = "force-empowered casting"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))
    
    to_class = db.relationship("Class", backref="force_empowered")

class Maneuver(db.Model):
    """Maneuvers Table"""

    __tablename__ = "maneuvers"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="maneuver")

class GuardianAura(db.Model):
    """Guardian Aura Table"""

    __tablename__ = "guardian_aura"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="aura")


class MonasticVows(db.Model):
    """Monastic Vows Table"""

    __tablename__ = "monastic_vows"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    prerequisite = db.Column(db.Text)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="vows")


class OperativeExploits(db.Model):
    """Operative Exploits Table"""

    __tablename__ = "operative_exploits"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    prerequisite = db.Column(db.Text)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="exploits")


class ScholarDiscovery(db.Model):
    """Scholar's Discoveries Table"""

    __tablename__ = "scholar_discoveries"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    prerequisite = db.Column(db.Text)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="discoveries")


class ScoutRoutine(db.Model):
    """Scout Routines Table"""

    __tablename__ = "scout_routines"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="routines")


class SentinelIdeals(db.Model):
    """Sentinel Ideals Table"""

    __tablename__ = "sentinel_ideals"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    to_class = db.relationship("Class", backref="ideals")



# Many-to-many tables
class CharacterFightingStyle(db.Model):
	
	__tablename__ = "character_fighting_styles"
	
	class_id = db.Column(db.Integer,  db.ForeignKey("classes.id", ondelete="cascade"), primary_key=True)
	fighting_style_id = db.Column(db.Integer,  db.ForeignKey("fighting_styles.id", ondelete="cascade"), primary_key=True)
	

class CharacterForcePower(db.Model):
	
	__tablename__ = "character_force_powers"
	
	class_id = db.Column(db.Integer,  db.ForeignKey("classes.id", ondelete="cascade"), primary_key=True)
	force_power_id = db.Column(db.Integer,  db.ForeignKey("force_powers.id", ondelete="cascade"), primary_key=True)
	
class CharacterTechPower(db.Model):
	
	__tablename__ = "character_tech_powers"

	class_id = db.Column(db.Integer,  db.ForeignKey("classes.id", ondelete="cascade"), primary_key=True)
	tech_power_id = db.Column(db.Integer,  db.ForeignKey("tech_powers.id", ondelete="cascade"), primary_key=True)
	
	
class CharacterFightingMastery(db.Model):
	
	__tablename__ = "character_fighting_masteries"
	
	class_id = db.Column(db.Integer,  db.ForeignKey("classes.id", ondelete="cascade"), primary_key=True)
	fighting_mastery_id = db.Column(db.Integer,  db.ForeignKey("fighting_masteries.id", ondelete="cascade"), primary_key=True)

class CharacterLightsaberForms(db.Model):

    __tablename__ = "character_lightsaber_forms"
    
    class_id = db.Column(db.Integer,  db.ForeignKey("classes.id", ondelete="cascade"), primary_key=True)
    lightsaber_form_id = db.Column(db.Integer,  db.ForeignKey("lightsaber_forms.id", ondelete="cascade"), primary_key=True)


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
    speed_val = db.Column(db.Text, nullable=False)
    languages = db.Column(db.Text, nullable=False)
    language_vals = db.Column(db.PickleType, nullable=False)


class SpecieTraits(db.Model):
    """Species Traits Table"""

    __tablename__ = "traits"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)

    to_species = db.relationship("Specie", secondary="species_traits", backref="traits")

class SpeciesToTraits(db.Model):
    """Join Table for Speices and thier traits"""

    __tablename__ = "species_traits"

    species_id = db.Column(db.Integer, db.ForeignKey("species.id"), primary_key=True)
    trait_id = db.Column(db.Integer, db.ForeignKey("traits.id"), primary_key=True)

# Backgrounds and associated Tables

class Background(db.Model):
    """Backgrounds Table"""

    __tablename__ = "backgrounds"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    intro = db.Column(db.Text, nullable=False)
    skill_proficiencies = db.Column(db.Text, nullable=False)
    tool_proficiencies = db.Column(db.Text)
    skill_vals = db.Column(db.PickleType, nullable=False)
    languages = db.Column(db.Text)
    equipment = db.Column(db.Text, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    background_feature_name = db.Column(db.Text, nullable=False)
    background_feature_details = db.Column(db.Text, nullable=False)


class Feat(db.Model):
    """Feats table"""

    __tablename__ = "feats"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)

    to_background = db.relationship("Background", secondary="feats_backgrounds", backref="feats")


class PersonalityTraits(db.Model):
    """Personality Traits Table"""

    __tablename__ = "personality_traits"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    details = db.Column(db.Text, nullable=False)

    to_background = db.relationship("Background", secondary="personality_traits_backgrounds", backref="traits")


class Ideals(db.Model):
    """Ideals Table"""

    __tablename__ = "ideals"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)

    to_background = db.relationship("Background", secondary="ideals_backgrounds", backref="ideals")


class Bonds(db.Model):
    """Bonds Table"""

    __tablename__ = "bonds"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    details = db.Column(db.Text, nullable=False)

    to_background = db.relationship("Background", secondary="bonds_backgrounds", backref="bonds")


class Flaws(db.Model):
    """Flaws Table"""

    __tablename__ = "flaws"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    details = db.Column(db.Text, nullable=False)

    to_background = db.relationship("Background", secondary="flaws_backgrounds", backref="flaws")


# Many-to-Many Tables

class FeatsBackround(db.Model):
    """Background Feats"""

    __tablename__ = "feats_backgrounds"

    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"), primary_key=True)
    feat_id = db.Column(db.Integer, db.ForeignKey("feats.id"), primary_key=True)


class PersonalityBackground(db.Model):
    """Background Personality Traits"""

    __tablename__ = "personality_traits_backgrounds"

    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"), primary_key=True)
    personality_trait_id = db.Column(db.Integer, db.ForeignKey("personality_traits.id"), primary_key=True)

class IdealsBackgrounds(db.Model):
    """Background Ideals"""

    __tablename__ = "ideals_backgrounds"

    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"), primary_key=True)
    ideal_id = db.Column(db.Integer, db.ForeignKey("ideals.id"), primary_key=True)


class BondsBackgrounds(db.Model):
    """Background Bonds"""

    __tablename__ = "bonds_backgrounds"

    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"), primary_key=True)
    bond_id = db.Column(db.Integer, db.ForeignKey("bonds.id"), primary_key=True)


class FlawsBackgrounds(db.Model):
    """Background Flaws"""

    __tablename__ = "flaws_backgrounds"

    background_id = db.Column(db.Integer, db.ForeignKey("backgrounds.id"), primary_key=True)
    flaw_id = db.Column(db.Integer, db.ForeignKey("flaws.id"), primary_key=True)


# Equipment Tables


class CharacterArmor(db.Model):
    """Character's Armor Table"""

    __tablename__ = "character_armors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aromr_id = db.Column(db.Integer, db.ForeignKey("armors.id",ondelete="cascade"))
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id", ondelete="cascade"))



class CharacterWeapon(db.Model):
    """Character's Weapons Table"""

    __tablename__ = "character_weapons"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weapon_id = db.Column(db.Integer, db.ForeignKey("weapons.id", ondelete="cascade"))
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id", ondelete="cascade"))


class CharacterAdventuringGear(db.Model):
    """Character's Adventuring Gear Table"""
    
    __tablename__ = "character_adventuring_gears"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adventuring_gear_id = db.Column(db.Integer, db.ForeignKey("adventuring_gears.id", ondelete="cascade"))
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id", ondelete="cascade"))


class Armor(db.Model):
    """Armor table"""

    __tablename__ = "armors"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    properties = db.Column(db.PickleType)
    cost = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    armor_class = db.Column(db.Text, nullable=False)
    stealth = db.Column(db.Text)
    details = db.Column(db.Text)

    to_character = db.relationship("Character", secondary="character_armors", backref="armor")


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

    to_character = db.relationship("Character", secondary="character_weapons", backref="weapon")



class AdventureingGear(db.Model):
    """Adventuring Gear Table"""

    __tablename__ = "adventuring_gears"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    details = db.Column(db.Text)

    to_character = db.relationship("Character", secondary="character_adventuring_gears", backref="adventuring_gear")


# Conditions Tables

class CharacterConditions(db.Model):
    """Character's Conditions table"""

    __tablename__ = "character_conditions"
    condition_id = db.Column(db.Integer, db.ForeignKey("conditions.id"), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"), primary_key=True)


class Condition(db.Model):
    """Conditions Table"""

    __tablename__ = "conditions"

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    details = db.Column(db.Text, nullable=False)

    to_character = db.relationship("Character", secondary="character_conditions", backref="conditions")
