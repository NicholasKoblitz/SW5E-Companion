import os
from random import seed
import re
from flask import Flask, render_template, redirect, flash, session, g, request
from models import db, connect_db, User, Character, Class, ClassFeatures, Archetype, FightingMastery, FightingStyles, LightsaberForms, TechPowers, ForcePowers, Specie, SpecieTraits, Background, Feat, PersonalityTraits, Ideals, Bonds, Flaws, CharacterArmor, CharacterWeapon, CharacterAdventuringGear, Armor, Weapon, AdventureingGear, CharacterConditions, Condition
from forms import SignupForm, LoginForm, AbilityScoresForm, DescriptionForm

USER_KEY = "current_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///SW5E'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "kdkkdiieiei1242easndado")

connect_db(app)


@app.before_request
def add_user_to_g():
    """Checks if the user is loged in"""

    if USER_KEY in session:
        g.user = User.query.get(session[USER_KEY])

    else:
        g.user = None


@app.route("/")
def home_page():
    """Displays the home page for the site"""

    return render_template("homepage.html", user = User)

#-----------------------Sign Up and Login Routes-------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Signs up the user"""

    form = SignupForm()

    if form.validate_on_submit():

        user = User.signup(username=form.username.data, password=form.password.data)
        db.session.commit()
        session[USER_KEY] = user.id

        return redirect(f"/user/{user.id}")
    else:
        return render_template("signup.html", form=form)
       

@app.route("/login", methods=["GET", "POST"])
def login():
    """Logs in the user"""

    form = LoginForm()

    if form.validate_on_submit():

        user = User.authenticate(username=form.username.data, password=form.password.data)

        if user:
            session[USER_KEY] = user.id
            redirect("/user/dashboard")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():

   if USER_KEY in session:
       del session[USER_KEY]

#--------------------------------------------------------------------------

#------------------------User Route---------------------------------------
@app.route("/user/<int:user_id>")
def display_user(user_id):
    """Displays the user's dashboard"""

    if not g.user:
       redirect("/")

    user = User.query.get_or_404(user_id)

    return render_template("user_dashboard.html", user=user)

#--------------------------------------------------------------------------

#--------------------Character Creation Routes-----------------------------
@app.route("/character/species")
def get_species():
    """Displays species selection"""

    if not g.user:
       redirect("/")

    species = Specie.query.all()

    return render_template("species.html", species=species)


@app.route("/character/species/<int:species_id>")
def get_specie(species_id):
    """Displays a single specie information"""

    if not g.user:
       redirect("/")

    specie = Specie.query.get_or_404(species_id)

    return render_template("single_species.html", specie=specie)


@app.route("/character/species/<int:species_id>", methods=["POST"])
def save_specie_choice(species_id):
    """Saves user's species choice"""

    specie = request.form["specie"]
    session["species"] = specie

    return redirect("/character/classes")


@app.route("/character/classes")
def get_classes():
    "Displays character classes"

    if not g.user:
       redirect("/")

    classes = Class.query.all()

    return render_template("classes.html", classes=classes)


@app.route("/character/classes/<int:class_id>")
def get_class(class_id):
    """Displays a single class"""

    if not g.user:
       redirect("/")

    _class = Class.query.get_or_404(class_id)

    return render_template("class.html", _class=_class)


@app.route("/character/classes/<int:class_id>", methods=["POST"])
def save_class_choice(class_id):
    """Saves user's class choice"""

    session["class"] = request.form["class"]

    return redirect("/character/ability-scores")


@app.route("/character/ability-scores", methods=["GET", "POST"])
def get_ability_scores():
    """Displays the character ability scores"""

    if not g.user:
       redirect("/")

    form = AbilityScoresForm()

    if form.validate_on_submit():

        session['strength'] = form.strength.data
        session["dexterity"] = form.dexterity.data
        session["constitution"] = form.constitution.data
        session["intelligence"] = form.intelligence.data
        session["wisdom"] = form.wisdom.data
        session["charisma"] = form.charisma.data

        return redirect("/character/description")
    
    return render_template("ability_scores.html", form=form)

@app.route("/character/description")
def get_description():
    """Displays the character description form"""

    if not g.user:
       redirect("/")

    form = DescriptionForm()

    if form.validate_on_submit():

        session["name"] = form.name.data
        # session["image_url"] = form.image_url.data or 
        session["alignment"] = form.alignment.data
        session["background"] = Background.query.filter_by(name = form.background.data).first()
        session["personality_trait"] = form.personality_trait
        session["ideal"] = form.ideal.data
        session["bond"] = form.bond.data
        session["flaw"] = form.flaw.data
        session["gender"] = form.gender.data
        session["place_of_birth"] = form.place_of_birth.data
        session["age"] = form.age.data
        session["height"] = form.height.data
        session["weight"] = form.weight.data
        session["hair"] = form.hair.data
        session["eyes"] = form.eyes.data
        session["skin"] = form.skin.data
        session["appearance"] = form.appearance.data
        session["background"] = form.background.data

        return redirect("/character/equipment")
    
    return render_template("description.html")

#--------------------------------------------------------------------------
