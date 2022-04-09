import os
from random import randint
from flask import Flask, render_template, redirect, flash, session, g, request
from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User, Character, Class, TechPowers, ForcePowers, Specie, Background, CharacterArmor, CharacterWeapon, CharacterAdventuringGear, Armor, Weapon, AdventureingGear, CharacterTechPower, CharacterForcePower
from forms import SignupForm, LoginForm, AbilityScoresForm, DescriptionForm

USER_KEY = "current_user"
ARMORS = []
WEAPONS = []
GEAR = []


app = Flask(__name__)


# uri = os.getenv("DATABASE_URL")  # or other relevant config var
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
# # rest of connection code using the connection string `uri`


app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///sw5e'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "kdkkdiieiei1242easndado")

connect_db(app)

#------------------Before the first request------------------------------
@app.before_request
def add_user_to_g():
    """Checks if the user is loged in"""

    if USER_KEY in session:
        g.user = User.query.get(session[USER_KEY])

    else:
        g.user = None


def check_attrubutes(ability_score):
    """Checks the value of the attrubutes"""

    if ability_score == 1:
        return -5
    elif ability_score == 2 or ability_score == 3:
        return -4
    elif ability_score == 4 or ability_score == 5:
        return -3
    elif ability_score == 6 or ability_score == 7:
        return -2
    elif ability_score == 8 or ability_score == 9:
        return -1
    elif ability_score == 10 or ability_score == 11:
        return 0
    elif ability_score == 12 or ability_score == 13:
        return 1
    elif ability_score == 14 or ability_score == 15:
        return 2
    elif ability_score == 16 or ability_score == 17:
        return 3
    elif ability_score == 18 or ability_score == 19:
        return 4
    elif ability_score == 20 or ability_score == 21:
        return 5
    elif ability_score == 22 or ability_score == 23:
        return 6
    elif ability_score == 24 or ability_score == 25:
        return 7
    elif ability_score == 26 or ability_score == 27:
        return 8
    elif ability_score == 28 or ability_score == 29:
        return 9
    elif ability_score == 30:
        return 10

def check_proficiency(level):
    """Finds charatcer's proficiency bonus"""

    if level in range(1,5):
        return 2
    elif level in range(5,9):
        return 3
    elif level in range(9,13):
        return 4
    elif level in range(13,17):
        return 5
    elif level in range(17,21):
        return 6


def check_passive_perception(ability_score, level):
    """Finds the character's passive perception"""

    bonus = check_attrubutes(ability_score)
    proficiency = check_proficiency(level)

    value = 10 + (bonus + proficiency)
    
    return value

def check_armor_class(ability_score):
    """Finds character's armor class"""

    bonus = check_attrubutes(ability_score)

    value = 10 + bonus
    
    return value


def find_class_roll_die(_class):
    """Returns the highest dice value for teh given class"""

    if _class == "Berserker":
        return 12
    elif _class == "Counsular":
        return 6
    elif _class == "Egineer":
        return 8
    elif _class == "Fighter":
        return 10
    elif _class == "Guardian":
        return 10
    elif _class == "Monk":
        return 8
    elif _class == "Operative":
        return 8
    elif _class == "Scholar":
        return 8
    elif _class == "Scout":
        return 10
    elif _class == "Sentinel":
        return 8

def roll_hit_dice(ability_score, level, _class):
    """Finds the characters hit points"""

    modifier = check_attrubutes(ability_score)
    hit_points = 0
    value = 0
    class_die = find_class_roll_die(_class)

    if level == 1:

        hit_points = 10 + modifier
        return hit_points

    else:

        hit_points = 10 + modifier
        for i in range(2, level + 1):
            value = randint(1, class_die)
            hit_points = hit_points + value
    
    hit_points = hit_points + modifier

    return hit_points
        
#--------------------------------------------------------------------------


@app.route("/")
def home_page():
    """Displays the home page for the site"""

    for item in list(session.keys()):
        if item != USER_KEY and item != "csrf_token":
           session.pop(item)


    return render_template("homepage.html", user = User)

#-----------------------Sign Up and Login Routes-------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Signs up the user"""

    form = SignupForm()

    if form.validate_on_submit():

        try:

            user = User.signup(username=form.username.data, password=form.password.data)
            db.session.commit()

        except IntegrityError:

            flash("Username already taken")
            return render_template("signup.html", form=form)

        session[USER_KEY] = user.id
        return redirect(f"/user/{user.id}")

    else:
        return render_template("signup.html", form=form)
       

@app.route("/login", methods=["GET", "POST"])
def login():
    """Logs in the user"""

    form = LoginForm()

    if form.validate_on_submit():

        user = User.authenticate(form.username.data, form.password.data)

        if user:
            session[USER_KEY] = user.id
            return redirect(f"/user/{user.id}")

        flash("Invalid Password")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():

    if USER_KEY in session:
       del session[USER_KEY]

    return redirect('/')

#--------------------------------------------------------------------------

#------------------------User Route----------------------------------------
@app.route("/user/<int:user_id>")
def display_user(user_id):
    """Displays the user's dashboard"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    user = User.query.get_or_404(user_id)

    return render_template("user_dashboard.html", user=user)

#--------------------------------------------------------------------------

#--------------------Character Creation Routes-----------------------------
@app.route("/character/species")
def get_species():
    """Displays species selection"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    species = Specie.query.all()

    return render_template("species.html", species=species)


@app.route("/character/species/<int:species_id>")
def get_specie(species_id):
    """Displays a single specie information"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

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
        flash("Please Sign In")
        return redirect("/")

    classes = Class.query.all()

    return render_template("classes.html", classes=classes)


@app.route("/character/classes/<int:class_id>")
def get_class(class_id):
    """Displays a single class"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    _class = Class.query.get_or_404(class_id)

    return render_template("class.html", _class=_class)


@app.route("/character/classes/<int:class_id>", methods=["POST"])
def save_class_choice(class_id):
    """Saves user's class choice"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    class_ = Class.query.get(class_id)

    _class = request.form["class"]
    skills = []


    if _class in ["Berserker", "Counsular", "Fighter", "Guardian", "Monk"]:
        skill_1 = request.form["0"]
        skill_2 = request.form["1"]


        if skill_1 == skill_2:
            flash(f"You selected the same skill. Please select again")
            return redirect(f"/character/classes/{class_id}")


        skills.append(skill_1)
        skills.append(skill_2)


    elif _class == "Operative":
        skill_1 = request.form["0"]
        skill_2 = request.form["1"]
        skill_3 = request.form["2"]
        skill_4 = request.form["3"]

        skills.append(skill_1)
        skills.append(skill_2)
        skills.append(skill_3)
        skills.append(skill_4)

        if skills.count(skill_1) > 1:
            flash(f"You selected the same skill. Please select again")
            return redirect(f"/character/classes/{class_id}")
        elif skills.count(skill_2) > 1:
            flash(f"You selected the same skill. Please select again")
            return redirect(f"/character/classes/{class_id}")
        elif skills.count(skill_3) > 1:
            flash(f"You selected the same skill. Please select again")
            return redirect(f"/character/classes/{class_id}")
        elif skills.count(skill_4) > 1:
            flash(f"You selected the same skill. Please select again")
            return redirect(f"/character/classes/{class_id}")

    else:
        skill_1 = request.form["0"]
        skill_2 = request.form["1"]
        skill_3 = request.form["2"]

        skills.append(skill_1)
        skills.append(skill_2)
        skills.append(skill_3)

        if skills.count(skill_1) > 1:
            flash(f"You selected the same skill. Please select again")
            return redirect(f"/character/classes/{class_id}")
        elif skills.count(skill_2) > 1:
            flash(f"You selected the same skill. Please select again")
            return redirect(f"/character/classes/{class_id}")
        elif skills.count(skill_3) > 1:
            flash(f"You selected the same skill. Please select again")
            return redirect(f"/character/classes/{class_id}")

    session["skills"] = skills
    session["class"] = _class

    return redirect("/character/backgrounds")


@app.route("/character/backgrounds")
def get_backgrounds():
    """Displays all backgrounds"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    backgrounds = Background.query.all()

    return render_template("backgrounds.html", backgrounds=backgrounds)


@app.route("/character/backgrounds/<int:background_id>")
def get_single_background(background_id):
    """Displays a single background"""

    background = Background.query.get_or_404(background_id)

    return render_template("single_background.html", background=background)

@app.route("/character/backgrounds/<int:background_id>", methods=["POST"])
def save_background_choice(background_id):
    """Saves user's background choice"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    skills = []
    background = request.form["background"]
    session["background"] = background

    skill_1 = request.form["0"]
    skill_2 = request.form["1"]

    skills.append(skill_1)
    skills.append(skill_2)

    for skill in skills:
        if skill in session["skills"] or skill_1 == skill_2:
            flash(f"{skill} was already selected in Class selection")
            background = Background.query.get_or_404(background_id)

            return render_template("single_background.html", background=background)

        else:
            session["skills"].append(skill_1)
            session["skills"].append(skill_2)

            return redirect("/character/ability-scores")


@app.route("/character/ability-scores", methods=["GET", "POST"])
def get_ability_scores():
    """Displays the character ability scores"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    form = AbilityScoresForm()

    if form.validate_on_submit():

        abilities = [form.strength.data, form.dexterity.data, form.constitution.data, form.intelligence.data, form.wisdom.data, form.charisma.data]

        for ability in abilities:
            
            for ability in abilities:
                count = abilities.count(ability)

                if count > 1:
                    flash('You selected two or more abilities with the same score!')
                    return render_template("ability_scores.html", form=form)

        session['strength'] = abilities[0]
        session["dexterity"] = abilities[1]
        session["constitution"] = abilities[2]
        session["intelligence"] = abilities[3]
        session["wisdom"] = abilities[4]
        session["charisma"] = abilities[5]

        return redirect("/character/description")
    
    return render_template("ability_scores.html", form=form)

@app.route("/character/description", methods=["GET", "POST"])
def get_description():
    """Displays the character description form"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    form = DescriptionForm()

    if form.validate_on_submit():

        session["name"] = form.name.data
        session["alignment"] = form.alignment.data
        session["level"] = form.level.data
        session["personality_trait"] = form.personality_trait.data
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
        session["backstory"] = form.backstory.data

        return redirect("/character/powers")
    
    return render_template("description.html", form=form)

@app.route("/character/powers")
def get_powers():
    """Shows powers page"""

    _class = Class.query.filter_by(name=session["class"]).first()
    force_powers = ForcePowers.query.all()
    tech_powers = TechPowers.query.all()
    level = session["level"]

    if "Techcasting" in _class.description_by_level["1"]["Features"] or "Forcecasting" in _class.description_by_level["1"]["Features"]:
        return render_template("powers.html", _class=_class, forces=force_powers, techs=tech_powers, level=level)
    else:
        return redirect("/character/equipment")



@app.route("/character/powers", methods=["POST"])
def save_powers():

    powers = []

    _class = Class.query.filter_by(name=session["class"]).first()



    if "Techcasting" in _class.description_by_level["1"]["Features"]:

        count =  _class.description_by_level[session["level"]]["Tech Powers Known"]

        for item in range(1, int(count) + 1):
            if request.form[str(item)] in powers:
                flash("You Selected the same powers. Please select again.")
                return redirect("/character/powers")
            else:
                powers.append(request.form[str(item)])

    elif "Forcecasting" in _class.description_by_level["1"]["Features"]:
        
        count =  _class.description_by_level[session["level"]]["Force Powers Known"]

        for item in range(1, int(count) + 1):
            if request.form[str(item)] in powers:
                flash("You Selected the same powers. Please select again.")
                return redirect("/character/powers")
            else:
                powers.append(request.form[str(item)])


    session["powers"] = powers

    return redirect("/character/equipment")



@app.route("/character/equipment")
def get_equipment():
    """Displays Equipment Page"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")


    return render_template('equipment.html')


@app.route("/character/equipment/armors")
def get_armor():
    """Display Armors page"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    armors = Armor.query.all()

    return render_template("armors.html", armors=armors)

@app.route("/character/equipment/armors", methods=["POST"])
def choose_armor():
    """Saves armor choice to session"""


    ARMORS.append(request.form["armor"])
    session["armor"] = ARMORS

    return redirect("/character/equipment")


# @app.route("/character/equipment/armors/delete", methods=["POST"])
# def delete_equipment():
#     """Deletes Equipment """

#     if not g.user:
#         flash("Please Sign In")
#         return redirect("/")


#     data = request.form["armor"]

#     print(data)
    
#     armors = session["armor"]
#     i = ARMORS.index(data)
#     print(i)
#     armors.pop(i)
#     print(ARMORS)

#     session.pop('armor',None)
#     session["armor"] = armors



#     return render_template("equipment.html")
#     return redirect(url_for('get_equipment', armors=armors))



@app.route("/character/equipment/weapons")
def get_weapons():
    """Displays Weapons Page"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    weapons = Weapon.query.all()

    return render_template("weapons.html", weapons=weapons)


@app.route("/character/equipment/weapons", methods=["POST"])
def choose_weapon():
    """Saves weapon choice to session"""

    WEAPONS.append(request.form["weapon"])

    session["weapon"] = WEAPONS

    return redirect("/character/equipment")



@app.route("/character/equipment/adventure-gear")
def get_adventure_gear():
    """Displays Adventure Gear Page"""

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    gear = AdventureingGear.query.all()

    return render_template("adventure_gear.html", gear=gear)


@app.route("/character/equipment/adventure-gear", methods=["POST"])
def choose_gear():
    """Saves adventure gear choice to session"""

    GEAR.append(request.form["gear"])

    session["gear"] = GEAR

    return redirect("/character/equipment")



    




@app.route("/character/create-character", methods=["POST"])
def get_create_character():
    """Creates the user's character"""


    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    _class = Class.query.filter_by(name=session["class"]).first()
    background = Background.query.filter_by(name=session["background"]).first()
    specie = Specie.query.filter_by(name=session["species"]).first()

    character = Character(
        user_id = g.user.id,
        name = session["name"],
        class_id = _class.id,
        species_id = specie.id,
        background_id = background.id,
        level = session["level"],
        class_saving_throw_pros = _class.saving_throw_proficiencies,
        xp_points = 0,
        strength = int(session["strength"]),
        str_saving_throw = check_attrubutes(int(session["strength"])),
        athletics = check_attrubutes(int(session["strength"])),
        dexterity = int(session["dexterity"]),
        dex_saving_throw = check_attrubutes(int(session["dexterity"])),
        acrobatics = check_attrubutes(int(session["dexterity"])),
        sleight_of_hand = check_attrubutes(int(session["dexterity"])),
        stealth = check_attrubutes(int(session["dexterity"])),
        constitution = int(session["constitution"]),
        con_saving_thorw = check_attrubutes(int(session["constitution"])),
        intelligence = int(session["intelligence"]),
        int_saving_throw = check_attrubutes(int(session["intelligence"])),
        investagation = check_attrubutes(int(session["intelligence"])),
        lore = check_attrubutes(int(session["intelligence"])),
        nature = check_attrubutes(int(session["intelligence"])),
        piloting = check_attrubutes(int(session["intelligence"])),
        technology = check_attrubutes(int(session["intelligence"])),
        wisdom = int(session["wisdom"]),
        wis_saving_throw = check_attrubutes(int(session['wisdom'])),
        animal_handling = check_attrubutes(int(session['wisdom'])),
        insight = check_attrubutes(int(session['wisdom'])),
        medicine = check_attrubutes(int(session['wisdom'])),
        perception = check_attrubutes(int(session['wisdom'])), 
        survival = check_attrubutes(int(session['wisdom'])),
        charisma = int(session["charisma"]),
        cha_saving_throw = check_attrubutes(int(session["charisma"])),
        deception = check_attrubutes(int(session["charisma"])),
        intimidation = check_attrubutes(int(session["charisma"])),
        performance = check_attrubutes(int(session["charisma"])),
        persuasion = check_attrubutes(int(session["charisma"])),
        passive_perception = check_passive_perception(int(session["wisdom"]), int(session["level"])),
        proficiency_bonus = check_proficiency(int(session["level"])),
        initiative = check_attrubutes(int(session["dexterity"])),
        armor_class = check_armor_class(int(session["dexterity"])),
        hit_points = roll_hit_dice(int(session["constitution"]), int(session['level']), session['class']),
        hit_dice = _class.hit_dice,
        base_speed = specie.speed_val,
        vision = "Normal Vision" if "Darvision" not in specie.traits else "Darkvision",
        credits = background.credits,
        proficiencies = [_class.armor_proficiencies, _class.weapon_proficiencies, _class.tool_proficiencies, background.tool_proficiencies],
        skills = session["skills"],
        languages = specie.language_vals,
        alignment = session["alignment"],
        personality_traits = session["personality_trait"],
        ideal = session["ideal"],
        bond = session["bond"],
        flaw = session["flaw"],
        gender = session["gender"],
        place_of_birth = session["place_of_birth"],
        age = session["age"],
        heigth = session["height"],
        weigth = session["weight"],
        hair = session["hair"],
        eyes = session["eyes"],
        skin = session["skin"],
        appearance = session["appearance"],
        backstory = session["backstory"]
    )

    db.session.add(character)
    db.session.commit()

    if "armor" in session:
        for item in session["armor"]:
            armor = Armor.query.filter_by(name=item).first()
            ca = CharacterArmor(aromr_id=armor.id, character_id=character.id)
            db.session.add(ca)
            db.session.commit()
    elif "weapon" in session:
        for item in session["weapon"]:
            weapon = Weapon.query.filter_by(name=item).first()
            cw = CharacterWeapon(weapon_id=weapon.id, character_id=character.id)
            db.session.add(cw)
            db.session.commit()
    elif "gear" in session:
        for item in session["gear"]:
            gear = AdventureingGear.query.filter_by(name=item).first()
            ca = CharacterAdventuringGear(adventuring_gear_id=gear.id, character_id=character.id)
            db.session.add(ca)
            db.session.commit()

    if "Techcasting" in _class.description_by_level["1"]["Features"]:
        for item in session["powers"]:
            tech = TechPowers.query.filter_by(name=item).first()
            ct = CharacterTechPower(char_id=character.id, tech_power_id=tech.id)
            db.session.add(ct)
            db.session.commit()
    elif "Forcecasting" in _class.description_by_level["1"]["Features"]:
        for item in session["powers"]:
            power = ForcePowers.query.filter_by(name=item).first()
            cp = CharacterForcePower(char_id=character.id, force_power_id=power.id)
            db.session.add(cp)
            db.session.commit()


    for item in list(session.keys()):
        if item != USER_KEY and item != "csrf_token":
           session.pop(item)

    armors = []
    weapons = []
    advent_gear = []
    skills = []
    return redirect(f'/character/{character.id}')



@app.route("/character/<int:character_id>")
def get_character(character_id):

    if not g.user:
        flash("Please Sign In")
        return redirect("/")

    character = Character.query.get_or_404(character_id)

    return render_template("overview.html", character=character)


@app.route("/character/<int:character_id>/delete", methods=["POST"])
def delete_character(character_id):
    """Deletes a character"""

    character = Character.query.filter_by(id=character_id).delete()
    user = User.query.get(g.user.id)

    db.session.commit()

    return redirect(f"/user/{user.id}")

#--------------------------------------------------------------------------
