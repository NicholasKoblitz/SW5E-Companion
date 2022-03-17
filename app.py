import os
import re
from flask import Flask, render_template, redirect, flash, session, g
from models import db, connect_db, User, Character, Class, ClassFeatures, Archetype, FightingMastery, FightingStyles, LightsaberForms, TechPowers, ForcePowers, Specie, SpecieTraits, Background, Feat, PersonalityTraits, Ideals, Bonds, Flaws, CharacterArmor, CharacterWeapon, CharacterAdventuringGear, Armor, Weapon, AdventureingGear, CharacterConditions, Condition
from forms import SignupForm, LoginForm

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


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Signs up the user"""

    form = SignupForm()

    if form.validate_on_submit():

        user = User.signup(username=form.username.data, password=form.password.data)
        db.session.commit()
        session[USER_KEY] = user.id

        return redirect("/user/dashboard")
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