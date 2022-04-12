from modulefinder import STORE_NAME
from multiprocessing import BufferTooShort

from sqlalchemy import over
from app import app
from models import SpeciesToTraits, db, Class, ClassFeatures, TechPowers, ForcePowers, Specie, SpecieTraits, Background, Feat, PersonalityTraits, Ideals, Bonds, Flaws, Armor, Weapon, AdventureingGear, FeatsBackround, PersonalityBackground, IdealsBackgrounds, BondsBackgrounds, FlawsBackgrounds


db.drop_all()
db.create_all()


# ---------------------Creates Classes-----------------------
berserker = Class(
    name="Berserker",
    intro=["A massive wookiee hunter prowls through the forest, hefting his vibroaxe. With a roar he charges at the pair of trandoshans who dared poach his kin.", "A gamorrean snarls at the latest challenger to his authority over their savage tribe, ready to break his neck with his bare hands as he did to the last six rivals.", "Frothing at the mouth, a nikto slams his helmet into the face of his foe, then turns to drive his armored elbow into the gut of another.", "These berserkers, different as they might be, are defined by their rage: unbridled, unquenchable, and unthinking fury. More than a mere emotion, their anger is the ferocity of a cornered predator, the unrelenting assault of a storm, the churning turmoil of the sea. For every berserker, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength."],
    description_1_name="Primal Instinct",
    description_1_info="People of towns and cities take pride in how their civilized ways set them apart from animals, as if denying one’s own nature was a mark of superiority. To a berserker, though, civilization is no virtue, but a sign of weakness. The strong embrace their animal nature keen instincts, primal physicality, and ferocious rage. Berserkers are uncomfortable when hedged in by walls and crowds. They thrive where the civilized don’t. Berserkers come alive in the chaos of combat. They can enter a berserk state where rage takes over, giving them superhuman strength and resilience. A berserker can draw on this reservoir of fury only a few times without resting, but those few rages are usually sufficient to defeat whatever threats arise.",
    description_2_name="A Life of Danger",
    description_2_info="Not every person deemed “berserkers” by scions of civilized society has the berserker class. A true berserker among these people is as uncommon as a skilled fighter in a town, and he or she plays a similar role as a protector of the people and a leader in times of war. Life in the wild places of the world is fraught with peril: rival tribes, deadly weather, and terrifying monsters. Berserkers charge headlong into that danger so that their people don’t have to. Their courage in the face of danger makes berserkers perfectly suited for adventuring. Wandering is often a way of life for their native tribes, and the rootless life of the adventurer is little hardship for a berserker. Some berserkers miss the close-knit family structures of the tribe, but eventually find them replaced by the bonds formed among the members of their adventuring parties. When creating a berserker character, think about where your character comes from and his or her place in the world. Talk with your GM about an appropriate origin for your berserker. Did you come from a remote planet, making you a stranger in the area of the campaign? Or is the campaign set in a rough-and-tumble frontier where berserkers are common? What led you to take up the adventuring life? Were you lured to settled planets by the promise of riches? Did you join forces with soldiers of those lands to face a shared threat? Did monsters or an invading horde drive you out of your homeland, making you a rootless refugee? Perhaps you were a prisoner of war, brought in chains to 'civilized' lands and only now able to win your freedom. Or you might have been cast out from your people because of a crime you committed, a taboo you violated, or a coup that removed you from a position of authority.",
    hit_dice="1d12 per Berserker level",
    hit_points_at_1st_level="12+ your Constitution modifier",
    hit_points_at_higher_levels="1d12 (or 7) + your Constitution per berserker level after 1st",
    armor_proficiencies="Light armor, Medium armor",
    weapon_proficiencies="All vibroweapons, simple blasters",
    tool_proficiencies="None",
    saving_throw_proficiencies=["Strength", "Constitution"],
    skills="Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival",
    skill_vals = [2, "Animal Handling", "Athletics", "Intimidation", "Nature", "Perceprion", "Survival"],
    starting_equipment=[
        "(a) A martial vibroweapon and a light or medium physical shield or (b) Two martial vibroweapons", 
        "(a) Two techaxes or (b) Two vibrospears", "An explorer's pack"
        ],
    variant_starting_wealth= "5d4 x 100 cr",
    description_by_level={
        "1": {
            "Proficiency Bonus": "+2",
            "Features": ["Rage", "Unarmored Defense"],
            "Rages": "2",
            "Rage Damage": "+2",
            "Berserker Instincts": "-"
        },
        "2": {
            "Proficiency Bonus": "+2",
            "Features": ["Reckless Attack", "Berserker Instincts"],
            "Rages": "2",
            "Rage Damage": "+2",
            "Berserker Instincts": "2"
        },
        "3": {
            "Proficiency Bonus": "+2",
            "Features": ["Danger Sense", "Berserker Approach"],
            "Rages": "3",
            "Rage Damage": "+2",
            "Berserker Instincts": "2"
        },
        "4": {
            "Proficiency Bonus": "+2",
            "Features": ["Ability Score Improvement"],
            "Rages": "3",
            "Rage Damage": "+2",
            "Berserker Instincts": "2"
        },
        "5": {
            "Proficiency Bonus": "+3",
            "Features": ["Extra Attack"],
            "Rages": "3",
            "Rage Damage": "+2",
            "Berserker Instincts": "2"
        },
        "6": {
            "Proficiency Bonus": "+3",
            "Features": ["Approach feature"],
            "Rages": "4",
            "Rage Damage": "+2",
            "Berserker Instincts": "2"
        },
        "7": {
            "Proficiency Bonus": "+3",
            "Features": ["Feral Impulse"],
            "Rages": "4",
            "Rage Damage": "+2",
            "Berserker Instincts": "3"
        },
        "8": {
            "Proficiency Bonus": "+3",
            "Features": ["Ability Score Improvement"],
            "Rages": "4",
            "Rage Damage": "+2",
            "Berserker Instincts": "3"
        },
        "9": {
            "Proficiency Bonus": "+4",
            "Features": ["Brutal Critical (one die)"],
            "Rages": "4",
            "Rage Damage": "+3",
            "Berserker Instincts": "3"
        },
        "10": {
            "Proficiency Bonus": "+4",
            "Features": ["Approach feature"],
            "Rages": "4",
            "Rage Damage": "+3",
            "Berserker Instincts": "3"
        },
        "11": {
            "Proficiency Bonus": "+4",
            "Features": ["Relentless Rage"],
            "Rages": "4",
            "Rage Damage": "+2",
            "Berserker Instincts": "3"
        },
        "12": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Rages": "5",
            "Rage Damage": "+3",
            "Berserker Instincts": "3"
        },
        "13": {
            "Proficiency Bonus": "+5",
            "Features": ["Brutal Critical (two dice)"],
            "Rages": "5",
            "Rage Damage": "+3",
            "Berserker Instincts": "4"
        },
        "14": {
            "Proficiency Bonus": "+5",
            "Features": ["Approach feature"],
            "Rages": "5",
            "Rage Damage": "+3",
            "Berserker Instincts": "4"
        },
        "15": {
            "Proficiency Bonus": "+5",
            "Features": ["Persistent Rage"],
            "Rages": "5",
            "Rage Damage": "+3",
            "Berserker Instincts": "4"
        },
        "16": {
            "Proficiency Bonus": "+5",
            "Features": ["Ability Score Improvement"],
            "Rages": "5",
            "Rage Damage": "+4",
            "Berserker Instincts": "4"
        },
        "17": {
            "Proficiency Bonus": "+6",
            "Features": ["Brutal Critical (three dice)"],
            "Rages": "6",
            "Rage Damage": "+4",
            "Berserker Instincts": "5"
        },
        "18": {
            "Proficiency Bonus": "+6",
            "Features": ["Indomitable Might"],
            "Rages": "6",
            "Rage Damage": "+4",
            "Berserker Instincts": "5"
        },
        "19": {
            "Proficiency Bonus": "+6",
            "Features": ["Ability Score Improvement"],
            "Rages": "6",
            "Rage Damage": "+4",
            "Berserker Instincts": "5"
        },
        "20": {
            "Proficiency Bonus": "+6",
            "Features": ["Primal Champion"],
            "Rages": "∞",
            "Rage Damage": "+4",
            "Berserker Instincts": "5"
        }
    }
)
consular = Class(
    name = "Counsular",
    intro = [
        "Sitting cross-legged on a dense patch of grass, a miraluka mystic meditates on the Force. With every breath, the trees sway with a rhythmic breeze. Though she lacks simple vision, she can see the Force as it moves everything around her.",
        "Sitting cross-legged on a dense patch of grass, a miraluka mystic meditates on the Force. With every breath, the trees sway with a rhythmic breeze. Though she lacks simple vision, she can see the Force as it moves everything around her.",
        "A drably-robed human focuses inward, channeling the Force into the ground around him. Slowly, all the debris within arms reach rises into the air around him; with a flick of his wrist, he clears the air, sending his projectiles to pound on the approaching tank.",
        "Consulars are the supreme wielders of the Force, defined and united by the powers they cast. Drawing on the omnipresent Force that permeates the universe, consulars cast powers of rejuvenating healing and destructive lightning, draining life-force and manipulating minds; the most powerful with the Force can even experience brief glimpses of the future."
    ],
    description_1_name = "Strong with the Force",
    description_1_info = "Refraining from drawing their lightsabers except as a measure of last resort, consulars spend a great deal of time studying the mysteries of the Force. Their knowledge allows them to channel the Force to greater heights, unlocking unrivaled power, and twisting those powers to greater effect.",
    description_2_name = "Sage or Sorcerer",
    description_2_info = "Consulars who follow the light side of the Force, using their powers to better their communities and people, are often called sages, while consulars who fall to the dark side and subjugate or cast aside all in their path are commonly called sorcerers. Alternatively, they may tend toward the middle, refraining from politics and war, spending their time in isolation and study. While creating your consular, consider your personal philosophy in regards to the Force and its most famous practitioners - the Jedi and the Sith. Are you a member of one of the two orders, or do you walk a different path? Perhaps you were ostracized from your primitive village out of superstition or jealousy. You may have been brutally trained from a young age in the dark side, fueling your innate thirst for power, or perhaps you were trained as a padawan in one of the Jedi temples. How do you treat strangers, and how do they treat you once they know your abilities? What was your family like, or what did you have instead of a family? Do you see the Force as light and dark, or an impartial river of gray?",
    hit_dice = "1d6 per Consular level",
    hit_points_at_1st_level = "6 + your Constitution modifier",
    hit_points_at_higher_levels = "1d4 (or 4) + your Constitution modifier per Consular level   after 1st",
    armor_proficiencies = "None",
    weapon_proficiencies = "Simple lightweapons, Simple vibroweapons",
    tool_proficiencies = "None",
    saving_throw_proficiencies = ["Wisdom", "Charisma"],
    skills = "Choose two from Deception, Insight, Intimidation, Investigation, Lore, Medicine, and Persuasion",
    skill_vals = [2, "Deception", "Insight", "Intimidation", "Investigation", "Lore", "Medicine", "Persuasion"],
    starting_equipment = [
        "(a) A simple lightweapon or (b) A simple vibroweapon",
        "(a) A scholar's pack (b) An explorer's pack (c) A diplomat's pack"
    ],
    variant_starting_wealth = "5d4 x 100 cr",
    description_by_level = {
        "1": {
            "Proficiency Bonus" : "+2",
            "Features": ["Forcecasting", "Force Recovery"],
            "Force Powers Known": "9",
            "Force Points": "4",
            "Max Power Level": "1st"
        },
        "2": {
            "Proficiency Bonus" : "+2",
            "Features": ["Force-Empowered Casting", "Force Shield"],
            "Force Powers Known": '11',
            "Force Points": '8',
            "Max Power Level": '1st'
        },
        "3": {
            "Proficiency Bonus" : "+2",
            "Features": ["Force Affinity", "Consular Tradition"],
            "Force Powers Known": '13',
            "Force Points": '12',
            "Max Power Level": '2nd'
        },
        "4": {
            "Proficiency Bonus" : "+2",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": '15',
            "Force Points": '16',
            "Max Power Level": '2nd'
        },
        "5": {
            "Proficiency Bonus" : "+3",
            "Features": ["-"],
            "Force Powers Known": '17',
            "Force Points": '20',
            "Max Power Level": '3rd'
        },
        "6": {
            "Proficiency Bonus" : "+3",
            "Features": ["Tradition feature"],
            "Force Powers Known": '19',
            "Force Points": '24',
            "Max Power Level": '3rd'
        },
        "7": {
            "Proficiency Bonus" : "+3",
            "Features": ["-"],
            "Force Powers Known": '21',
            "Force Points": '28',
            "Max Power Level": '4th'
        },
        "8": {
            "Proficiency Bonus" : "+3",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": '23',
            "Force Points": '32',
            "Max Power Level": '4th'
        },
        "9": {
            "Proficiency Bonus" : "+4",
            "Features": ["Force-Empowered Casting (three options)"],
            "Force Powers Known": '25',
            "Force Points": '36',
            "Max Power Level": '5th'
        },
        "10": {
            "Proficiency Bonus" : "+4",
            "Features": ["Tradition feature"],
            "Force Powers Known": '26',
            "Force Points": '40',
            "Max Power Level": '5th'
        },
        "11": {
            "Proficiency Bonus" : "+4",
            "Features": ["-"],
            "Force Powers Known": '28',
            "Force Points": '44',
            "Max Power Level": '6th'
        },
        "12": {
            "Proficiency Bonus" : '+4',
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": '29',
            "Force Points": '48',
            "Max Power Level": '6th'
        },
        "13": {
            "Proficiency Bonus" : "+5",
            "Features": ["-"],
            "Force Powers Known": '31',
            "Force Points": '52',
            "Max Power Level": '7th'
        },
        "14": {
            "Proficiency Bonus" : "+5",
            "Features": ["Tradition feature"],
            "Force Powers Known": '32',
            "Force Points": '56',
            "Max Power Level": '7th'
        },
        "15": {
            "Proficiency Bonus" : "+5",
            "Features": ["-"],
            "Force Powers Known": '34',
            "Force Points": '60',
            "Max Power Level": '8th'
        },
        "16": {
            "Proficiency Bonus" : '+5',
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": '35',
            "Force Points": '64',
            "Max Power Level": '8th'
        },
        "17": {
            "Proficiency Bonus" : '+6',
            "Features": ["Force-Empowered Casting (four options)"],
            "Force Powers Known": '37',
            "Force Points": '68',
            "Max Power Level": '9th'
        },
        "18": {
            "Proficiency Bonus" : "+6",
            "Features": ["Tradition feature"],
            "Force Powers Known": '38',
            "Force Points": '72',
            "Max Power Level": '9th'
        },
        "19": {
            "Proficiency Bonus" : "+6",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": '39',
            "Force Points": '76',
            "Max Power Level": '9th'
        },
        "20": {
            "Proficiency Bonus" : "+6",
            "Features": ["One with the Force"],
            "Force Powers Known": '40',
            "Force Points": '80',
            "Max Power Level": '9th'
        },
    }
)
engineer = Class(
    name = "Engineer",
    intro = [
        "Flinching occasionally as a blaster bolt hits the nearby bulkhead, a Sullustan mechanic quickly solders a large wire. He peers through his tinted goggles, ignoring the shouts of his ship captain as the enemy descends on the hanger. Finally he shouts with pride as the repaired coupling powers up, causing the frigate to hum with energy. He gathers his tools and runs into the ship moments before it finally takes off.",
        "Inside, the human captain jumps into the cockpit. She nods to her droid co-pilot, who quickly begins charting a course home. Before the calculations can be completed, enemy Starfighters scream in from the clouds. The pilot rolls the ship, nimbly evading incoming fire. She reroutes the power to shields, leaving just enough for astronavigation. Just as the energy reserves near depletion, the exosphere and stars beyond blur into streaks of light. In a flash, they warp to safety.",
        "A Cerean officer surveys the battlefield, looking for weaknesses. When he identifies a potential problem, he keys in a quick combination in his wristpad. In a blink, a custom suit of armor assembles itself around him. As the helmet locks into place, the officer leaps into the air, flying overhead and raining destruction on the opposition.",
        "A Cerean officer surveys the battlefield, looking for weaknesses. When he identifies a potential problem, he keys in a quick combination in his wristpad. In a blink, a custom suit of armor assembles itself around him. As the helmet locks into place, the officer leaps into the air, flying overhead and raining destruction on the opposition."
    ],
    description_1_name = "Behind the Curtain",
    description_1_info = "While perhaps not as intimidating as a heavily-armored trooper, or as exotic as a lighsaber-wielding guardian, engineers are no less vital to group dynamic. They are armorers and gunsmiths, electricians and welders, or any other facet to be found in facilities across the galaxy. Their work, often unsung, is what keeps starships (and their crew) intact.",
    description_2_name = "Unflappable",
    description_2_info = "It takes bravery for a soldier to enter a battlefield. It perhaps takes more for someone who is unarmed, and untrained in combat, to do the same. Engineers put their lives on the line for a living, whether by choice or acknowledging their plights as an occupational hazard. Whether they come from an elite training academy or learned their talents surviving in the slums, they are no strangers to danger and conflict. While creating your engineer character, consider what your primary skill set is and how you use it. You could be a street-smart mechanic who taught yourself how to fix swoop bikes as a teenager. Perhaps you are the recent graduate of an esteemed medical college, or a rookie pilot in the fledgling Rebel Alliance. What is the number one skill you are known for? Why are you willing to enter battles when you have no combat training? How do you view the more adventurous members of your group, and how do they see you and your role?",
    hit_dice = "1d8 per engineer level",
    hit_points_at_1st_level = "8 + your Constitution modifier",
    hit_points_at_higher_levels = "1d8 (or 5) + your Constitution modifier per engineer level after 1st",
    armor_proficiencies = "Light armor",
    weapon_proficiencies = "Simple blasters, Simple vibroweapons",
    tool_proficiencies = "Tinker's implements, one of our choice",
    saving_throw_proficiencies = ["Constitution", "Intelligence"],
    skills = "Choose three from Investigation, Lore, Medicine, Nature, Piloting, and Technology",
    skill_vals = [3, "Investigation", "Lore", "Medicine", "Nature", "Piloting", "Technology"],
    starting_equipment = [
        "(a) a simple vibroweapon or (b) a simple blaster and two power cells",
        "(a) a dungeoneer’s pack or (b) an explorer’s pack",
        "Combat suit, a set of tinker’s implements, a vibrodagger, and a wristpad"
    ],
    variant_starting_wealth = '6d4 x 100 cr',
    description_by_level = {
        "1" : {
            "Proficiency Bonus": "+2",
            "Features": ["Techcasting", "Potent Aptitude"],
            "Tech Powers Known": "6",
            "Tech Points": "2",
            "Max Power Level": "1st",
            "Potent Aptitude": "d4",
            "Modification Slots": "-"
        },
        "2" : {
            "Proficiency Bonus": "+2",
            "Features": ["Infuse Item (+1)", "Tool Expertise"],
            "Tech Powers Known": "7",
            "Tech Points": "4",
            "Max Power Level": "1st",
            "Potent Aptitude": "d4",
            "Modification Slots": "-"
        },
        "3" : {
            "Proficiency Bonus": "+2",
            "Features": ["Engineering Discipline"],
            "Tech Powers Known": "9",
            "Tech Points": "6",
            "Max Power Level": "2nd",
            "Potent Aptitude": "d4",
            "Modification Slots": "4"
        },
        "4" : {
            "Proficiency Bonus": "+2",
            "Features": ["Ability Score Improvement"],
            "Tech Powers Known": "10",
            "Tech Points": "8",
            "Max Power Level": "2nd",
            "Potent Aptitude": "d4",
            "Modification Slots": "4"
        },
        "5" : {
            "Proficiency Bonus": "+3",
            "Features": ["-"],
            "Tech Powers Known": "12",
            "Tech Points": "10",
            "Max Power Level": "3rd",
            "Potent Aptitude": "d6",
            "Modification Slots": "5"
        },
        "6" : {
            "Proficiency Bonus": "+3",
            "Features": ["Discipline feature"],
            "Tech Powers Known": "13",
            "Tech Points": "12",
            "Max Power Level": "3rd",
            "Potent Aptitude": "d6",
            "Modification Slots": "5"
        },
        "7" : {
            "Proficiency Bonus": "+3",
            "Features": ["-"],
            "Tech Powers Known": "15",
            "Tech Points": "14",
            "Max Power Level": "4th",
            "Potent Aptitude": "d6",
            "Modification Slots": "5"
        },
        "8" : {
            "Proficiency Bonus": "+3",
            "Features": ["Ability Score Improvement"],
            "Tech Powers Known": "16",
            "Tech Points": "16",
            "Max Power Level": "4th",
            "Potent Aptitude": "d6",
            "Modification Slots": "5"
        },
        "9" : {
            "Proficiency Bonus": "+4",
            "Features": ["-"],
            "Tech Powers Known": "18",
            "Tech Points": "18",
            "Max Power Level": "5th",
            "Potent Aptitude": "d8",
            "Modification Slots": "6"
        },
        "10" : {
            "Proficiency Bonus": "+4",
            "Features": ["Infuse Item (+2)"],
            "Tech Powers Known": "19",
            "Tech Points": "20",
            "Max Power Level": "5th",
            "Potent Aptitude": "d8",
            "Modification Slots": "6"
        },
        "11" : {
            "Proficiency Bonus": "+4",
            "Features": ["-"],
            "Tech Powers Known": "21",
            "Tech Points": "22",
            "Max Power Level": "6th",
            "Potent Aptitude": "d8",
            "Modification Slots": "7"
        },
        "12" : {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Tech Powers Known": "22",
            "Tech Points": "24",
            "Max Power Level": "6th",
            "Potent Aptitude": "d8",
            "Modification Slots": "7"
        },
        "13" : {
            "Proficiency Bonus": "+5",
            "Features": ["-"],
            "Tech Powers Known": "23",
            "Tech Points": "26",
            "Max Power Level": "7th",
            "Potent Aptitude": "d10",
            "Modification Slots": "8"
        },
        "14" : {
            "Proficiency Bonus": "+5",
            "Features": ["Discipline feature"],
            "Tech Powers Known": "24",
            "Tech Points": "28",
            "Max Power Level": "7th",
            "Potent Aptitude": "d10",
            "Modification Slots": "8"
        },
        "15" : {
            "Proficiency Bonus": "+5",
            "Features": ["Infuse Item (+3)"],
            "Tech Powers Known": "25",
            "Tech Points": "30",
            "Max Power Level": "8th",
            "Potent Aptitude": "d10",
            "Modification Slots": "8"
        },
        "16" : {
            "Proficiency Bonus": "+5",
            "Features": ['Ability Score Improvement'],
            "Tech Powers Known": "26",
            "Tech Points": "32",
            "Max Power Level": "8th",
            "Potent Aptitude": "d10",
            "Modification Slots": "8"
        },
        "17" : {
            "Proficiency Bonus": "+6",
            "Features": ["-"],
            "Tech Powers Known": "27",
            "Tech Points": "34",
            "Max Power Level": "9th",
            "Potent Aptitude": "d12",
            "Modification Slots": "9"
        },
        "18" : {
            "Proficiency Bonus": "+6",
            "Features": ["Discipline feature"],
            "Tech Powers Known": "28",
            "Tech Points": "36",
            "Max Power Level": "9th",
            "Potent Aptitude": "d12",
            "Modification Slots": "9"
        },
        "19" : {
            "Proficiency Bonus": "+6",
            "Features": ["Ability Score Improvement"],
            "Tech Powers Known": "29",
            "Tech Points": "38",
            "Max Power Level": "9th",
            "Potent Aptitude": "d12",
            "Modification Slots": "9"
        },
        "20" : {
            "Proficiency Bonus": "+6",
            "Features": ["Tech Mastery"],
            "Tech Powers Known": "30",
            "Tech Points": "40",
            "Max Power Level": "9th",
            "Potent Aptitude": "d12",
            "Modification Slots": "9"
        }
    }
)
fighter = Class(
    name = "Fighter",
    intro = [
        "A Trandoshan runs frantically across rooftops, constantly looking over his shoulder. As he prepares to leap a gap, a blaster bolt hits him in the back and renders him unconscious. His blurry vision barely makes out the figure of a masked woman who casually approaches, ready to collect her bounty.",
        "With his muscular arms held wide, a grizzled-looking Wookiee grins to his bloodthirsty crowd. He turns back to his arena opponent just in time to see the Besalisk take a swing. He ducks, punching the four-armed fighter in the gut. Two wild haymakers later, and he stands alone as the gladiatorial champion.",
        "Taking a deep breath, a Republic soldier looks out onto the war zone waging across the frozen surface of Ilum. He grips his blaster rifle tightly then, with a nod to the dozen squad-mates beside him, he charges onto the battlefield.",
        "Fighters combine discipline with martial skills to become the best pure warriors in the galaxy. Fighters can be stalwart defenders of those in need, cruel marauders, or brave advent-urers. They fight for glory, honor, to right wrongs, to gain power, to acquire wealth, or simple for the thrill of battle."
    ],
    description_1_name = "All in a Day's Work",
    description_1_info = "Many fighters see adventures, raids on enemy strongholds, and dangerous missions as their jobs. Some want to defend those who can’t defend themselves while others seek to use their muscle to carve their own place of importance in the galaxy. Fighters can take the form of guards, champions, bounty hunters, enforcers, mercenaries, freedom fighters, or simply armed explorers.",
    description_2_name = "Code Red",
    description_2_info = "Most fighters come to the profession after receiving at least some amount of formal training from a military organization. Some attend formal academies; others are self-taught and well tested. A fighter may have taken up his weapon to escape a mundane life while another may be following a proud family tradition. Whatever their origins, most fighters share an unshakeable loyalty. Fighters follow orders with little hesitation, as failure can often mean death. While creating your fighter character, consider where your loyalties lie. You could be part of a formal military, one of countless troopers fighting for your enterprise. Perhaps you are a gun-for-hire, traveling the galaxy in search of your next gig. What weapons do you prefer and specialize in? Who or what do you fight for? Do you have aspirations of a life beyond the battlefield, or have you been at war so long you know of nothing else?",
    hit_dice = "1d10 per Fighter level",
    hit_points_at_1st_level = "10 + your Constitution modifier",
    hit_points_at_higher_levels = "1d10 (or 6) + your Constitution modifier per fighter level after 1st",
    armor_proficiencies = "All armor",
    weapon_proficiencies = "All blasters, All vibroweapons",
    tool_proficiencies = "None",
    saving_throw_proficiencies = ["Strength", "Constitution"],
    skills = 'Choose two skills from Acrobatics, Animal Handling, Athletics, Lore, Insight, Intimidation, Perception, and Survival',
    skill_vals = [2, "Acrobatics", "Animal Handling", "Athletics", "Lore", "Insight", "Indimidation", "Perception", "Survival"],
    starting_equipment = [
        "(a) mesh armor or (b) combat suit, blaster rifle, and two power cells",
        "(a) a martial vibroweapon and a light or medium physical shield or (b) two martial vibroweapons",
        "(a) a hold-out and a power cell or (b) two vibrodaggers",
        "(a) a dungeoneer’s pack or (b) an explorer’s pack"
        ],
    variant_starting_wealth = "8d4 x 100 cr",
    description_by_level = {
        '1': {
            'Proficiency Bonus': "+2",
            'Features': ["Fighting Style", "Second Wind"],
            'Combat Superiority': "-",
            'Superiority Dice': "-",
            'Maneuvers Known': "-",
        },
        '2': {
            'Proficiency Bonus': "+2",
            'Features': ["Action Surge (one use)", "Combat Superiority"],
            'Combat Superiority': "d4",
            'Superiority Dice': "2",
            'Maneuvers Known': "2",
        },
        '3': {
            'Proficiency Bonus': "+2",
            'Features': ["Fighting Mastery", "Fighter Specialty"],
            'Combat Superiority': "d4",
            'Superiority Dice': "2",
            'Maneuvers Known': "2",
        },
        '4': {
            'Proficiency Bonus': "+2",
            'Features': ["Ability Score Improvement"],
            'Combat Superiority': "d4",
            'Superiority Dice': "2",
            'Maneuvers Known': "2",
        },
        '5': {
            'Proficiency Bonus': "+3",
            'Features': ["Extra Attack"],
            'Combat Superiority': "d6",
            'Superiority Dice': "2",
            'Maneuvers Known': "2",
        },
        '6': {
            'Proficiency Bonus': "+3",
            'Features': ["Ability Score Improvement"],
            'Combat Superiority': "d6",
            'Superiority Dice': "2",
            'Maneuvers Known': "2",
        },
        '7': {
            'Proficiency Bonus': "+3",
            'Features': ["Specialty feature"],
            'Combat Superiority': "d6",
            'Superiority Dice': "3",
            'Maneuvers Known': "3",
        },
        '8': {
            'Proficiency Bonus': "+3",
            'Features': ["Ability Score Improvement"],
            'Combat Superiority': "d6",
            'Superiority Dice': "3",
            'Maneuvers Known': "3",
        },
        '9': {
            'Proficiency Bonus': "+4",
            'Features': ["Indomitable (one use)"],
            'Combat Superiority': "d8",
            'Superiority Dice': "3",
            'Maneuvers Known': "3",
        },
        '10': {
            'Proficiency Bonus': "+4",
            'Features': ["Specialty feature"],
            'Combat Superiority': "d8",
            'Superiority Dice': "3",
            'Maneuvers Known': "3",
        },
        '11': {
            'Proficiency Bonus': "+4",
            'Features': ["Greater Extra Attack"],
            'Combat Superiority': "d8",
            'Superiority Dice': "4",
            'Maneuvers Known': "4",
        },
        '12': {
            'Proficiency Bonus': "+4",
            'Features': ["Ability Score Improvement"],
            'Combat Superiority': "d8",
            'Superiority Dice': "4",
            'Maneuvers Known': "4",
        },
        '13': {
            'Proficiency Bonus': "+5",
            'Features': ["Indomitable (two uses"],
            'Combat Superiority': "d10",
            'Superiority Dice': "4",
            'Maneuvers Known': "4",
        },
        '14': {
            'Proficiency Bonus': "+5",
            'Features': ["Ability Score Improvement"],
            'Combat Superiority': "d10",
            'Superiority Dice': "4",
            'Maneuvers Known': "4",
        },
        '15': {
            'Proficiency Bonus': "+5",
            'Features': ["Specialty feature"],
            'Combat Superiority': "d10",
            'Superiority Dice': "5",
            'Maneuvers Known': "5",
        },
        '16': {
            'Proficiency Bonus': "+5",
            'Features': ["Ability Score Improvement"],
            'Combat Superiority': "d10",
            'Superiority Dice': "5",
            'Maneuvers Known': "5",
        },
        '17': {
            'Proficiency Bonus': "+6",
            'Features': ["Action Surge (two uses)", "Indomitable (three uses)"],
            'Combat Superiority': "d12",
            'Superiority Dice': "5",
            'Maneuvers Known': "5",
        },
        '18': {
            'Proficiency Bonus': "+6",
            'Features': ["Specialty feature"],
            'Combat Superiority': "d12",
            'Superiority Dice': "5",
            'Maneuvers Known': "5",
        },
        '19': {
            'Proficiency Bonus': "+6",
            'Features': ["Ability Score Improvement"],
            'Combat Superiority': "d12",
            'Superiority Dice': "5",
            'Maneuvers Known': "5",
        },
        '20': {
            'Proficiency Bonus': "+6",
            'Features': ["Master of Combat"],
            'Combat Superiority': "d12",
            'Superiority Dice': "5",
            'Maneuvers Known': "5",
        }
    }
)
guardian = Class(
    name = "Guardian",
    intro = [
        "A dark-skinned human quickly runs down a corridor, the metal armor under his grey cloak clanking with each step. He rounds the corner into the prison while the lights and power are still out, urging the weakened prisoners to escape. Just then a handful of slavers arrive and ready their blasters. The man draws and ignites a white-bladed lightsaber, ready to die for the strangers behind him.",
        "A sith pureblood, clad head to toe in black and red armor, charges towards a line of soldiers. Shot after shot deflects off his armor until he reaches his prey, where he unleashes his fury in a series of devastating lightsaber sweeps.",
        "A zabrak general dramatically leaps to his soon-to-be overrun squad, landing with a flurry of lightsaber attacks. At the arrival of this powerful Jedi, the attackers fall back.",
        "Guardians are the master of the art of lightsaber combat. They focus on utilizing the everpresent power of the Force to enable devastating attacks, often single-handedly turning the tide of battle."
    ],
    description_1_name = "Protector or Destroyer",
    description_1_info = "An unstoppable agent of the Force, the guardian channels the power flowing through him into his weapons. Their skills with a lightsaber are unrivalled. Subduing their enemies and bolstering their allies, the guardian uses the Force to control what happens around them.",
    description_2_name = "Natural Leaders",
    description_2_info = "The guardian’s command of the Force lends them a powerful presence. Whether through fear and intimidation or respect and admiration, the guardian is one of the greatest generals on the battlefield. They are a symbol of power to their followers. While creating your guardian, consider your attraction to the Force and its most famous practitioners - the Jedi and the Sith. Are you a member of one of the two orders, or do you walk a different path? Are you a soldier tapping into a latent Force-sensitivity? Were you trained in the force from a young age, or did you discover it as an adult? How do you treat those weaker than you? What was your family like? Do you see the Force as light and dark, or an impartial river of gray?",
    hit_dice = "1d10 per Guardian level",
    hit_points_at_1st_level = "10 + your Constitution modifier",
    hit_points_at_higher_levels = "1d10 (or 6) + your Constitution modifier per Guardian level after 1st",
    armor_proficiencies = "Light armor, Medium armor",
    weapon_proficiencies = "All lightweapons, All vibroweapons",
    tool_proficiencies = "None",
    saving_throw_proficiencies = ["Constitution", "Charisma"],
    skills = "Choose two from Acrobatics, Athletics, Deception, Insight, Intimidation, Lore, Perception, Persuasion, and Piloting",
    skill_vals = [2, "Acrobatics", "Athletics", "Deception", "Insight", "Indimidation", "Lore", "Perception", "Persuasion", "Piloting"],
    starting_equipment = [
        "(a) a lightweapon or vibroweapon and a light or medium physical shield or (b) two lightweapons or vibroweapons",
        "(a) combat suit and a light physical shield or (b) mesh armor",
        "(a) a priest’s pack or (b) an explorer’s pack"
        ],
    variant_starting_wealth = "8d4 x 100cr",
    description_by_level = {
        "1": {
            "Proficiency Bonus": "+2",
            "Features": ["Forcecasting", "Channel the Force"],
            "Force Powers Known": "5",
            "Force Points": "2",
            "Max Power Level": "1st",
            "Focused Strikes": "-"
        },
        "2": {
            "Proficiency Bonus": "+2",
            "Features": ["Force-Empowered Strikes", "Fighting Style"],
            "Force Powers Known": "7",
            "Force Points": "4",
            "Max Power Level": "1st",
            "Focused Strikes": "2d8"
        },
        "3": {
            "Proficiency Bonus": "+2",
            "Features": ["Guardian Aura", "Guardian Focus"],
            "Force Powers Known": "9",
            "Force Points": "6",
            "Max Power Level": "1st",
            "Focused Strikes": "2d8"
        },
        "4": {
            "Proficiency Bonus": "+2",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "10",
            "Force Points": "8",
            "Max Power Level": "1st",
            "Focused Strikes": "2d8"
        },
        "5": {
            "Proficiency Bonus": "+3",
            "Features": ["Extra Attack"],
            "Force Powers Known": "12",
            "Force Points": "10",
            "Max Power Level": "2nd",
            "Focused Strikes": "3d8"
        },
        "6": {
            "Proficiency Bonus": "+3",
            "Features": ["Force Purity"],
            "Force Powers Known": "13",
            "Force Points": "12",
            "Max Power Level": "2nd",
            "Focused Strikes": "3d8"
        },
        "7": {
            "Proficiency Bonus": "+3",
            "Features": ["Focus feature"],
            "Force Powers Known": "14",
            "Force Points": "14",
            "Max Power Level": "2nd",
            "Focused Strikes": "3d8"
        },
        "8": {
            "Proficiency Bonus": "+3",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "15",
            "Force Points": "16",
            "Max Power Level": "2nd",
            "Focused Strikes": "3d8"
        },
        "9": {
            "Proficiency Bonus": "+4",
            "Features": ["Guardian Aura (15-foot radius)"],
            "Force Powers Known": "17",
            "Force Points": "18",
            "Max Power Level": "3rd",
            "Focused Strikes": "4d8"
        },
        "10": {
            "Proficiency Bonus": "+4",
            "Features": ["Guardian Aura (two auras)"],
            "Force Powers Known": "18",
            "Force Points": "20",
            "Max Power Level": "3rd",
            "Focused Strikes": "4d8"
        },
        "11": {
            "Proficiency Bonus": "+4",
            "Features": ["Improved Force-Empowered Strikes"],
            "Force Powers Known": "19",
            "Force Points": "22",
            "Max Power Level": "3rd",
            "Focused Strikes": "4d8"
        },
        "12": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "20",
            "Force Points": "24",
            "Max Power Level": "3rd",
            "Focused Strikes": "4d8"
        },
        "13": {
            "Proficiency Bonus": "+5",
            "Features": ["-"],
            "Force Powers Known": "22",
            "Force Points": "26",
            "Max Power Level": "4th",
            "Focused Strikes": "5d8"
        },
        "14": {
            "Proficiency Bonus": "+5",
            "Features": ["Cleansing Touch"],
            "Force Powers Known": "23",
            "Force Points": "28",
            "Max Power Level": "4th",
            "Focused Strikes": "5d8"
        },
        "15": {
            "Proficiency Bonus": "+5",
            "Features": ["Focus feature"],
            "Force Powers Known": "24",
            "Force Points": "30",
            "Max Power Level": "4th",
            "Focused Strikes": "5d8"
        },
        "16": {
            "Proficiency Bonus": "+5",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "25",
            "Force Points": "32",
            "Max Power Level": "4th",
            "Focused Strikes": "5d8"
        },
        "17": {
            "Proficiency Bonus": "+6",
            "Features": ["Guardian Aura (30-foot radius)"],
            "Force Powers Known": "27",
            "Force Points": "34",
            "Max Power Level": "5th",
            "Focused Strikes": "6d8"
        },
        "18": {
            "Proficiency Bonus": "+6",
            "Features": ["Guardian Aura (three auras)"],
            "Force Powers Known": "28",
            "Force Points": "36",
            "Max Power Level": "5th",
            "Focused Strikes": "6d8"
        },
        "19": {
            "Proficiency Bonus": "+6",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "29",
            "Force Points": "38",
            "Max Power Level": "5th",
            "Focused Strikes": "6d8"
        },
        "20": {
            "Proficiency Bonus": "+6",
            "Features": ["Focus feature"],
            "Force Powers Known": "30",
            "Force Points": "40",
            "Max Power Level": "5th",
            "Focused Strikes": "6d8"
        }

    }
)
monk = Class(
    name = "Monk",
    intro = [
        "Her vibrostaff a blur as they deflect an incoming hail of blaster bolts, a human springs over a barricade and throws herself into the massed ranks of pirates on the other side. She whirls among them, knocking their blows aside and sending them reeling, until at last she stands alone.",
        "Taking a deep breath, a zabrak covered in tattoos settles into a battle stance. As the first charging mercenaries reach him, he exhales and a blast of negative energy courses from his hands, engulfing his foes.",
        "Moving with the silence of the night, a black-clad mirialan steps into a shadow beneath an arch and nimbly climbs to the balcony a stone’s throw above her. She slides her blade free of its cloth-wrapped scabbard and peers through the open window at the warlord, so vulnerable in the grip of sleep.",
        "Whatever their discipline, monks are united in their ability to harness the energy that flows in their bodies. Whether channeled as a striking display of combat prowess or a subtler focus of defensive ability and speed, this energy infuses all that a monk does."
    ],
    description_1_name = "The Power of Focus",
    description_1_info = "Monks make careful study of a mystical energy that most monastic orders call focus. This energy is an element of the power that suffuses the galaxy�specifically, the element that flows through living bodies. Monks harness this energy within themselves to create powerful effects and exceed their bodies’ physical capabilities, and some of their special attacks can hinder the flow of focus in their opponents. Using this energy, monks channel uncanny speed and strength into their unarmed strikes. As they gain experience, their martial training and their mastery of focus gives them more power over their bodies and the bodies of their foes.",
    description_2_name = "Training and Asceticism",
    description_2_info = "Most monks live entirely apart from the surrounding population, secluded from anything that might impede their spiritual progress. Others are sworn to isolation, emerging only to serve as spies or assassins at the command of their leader, a noble patron, or some other power. The majority of monks don’t shun their neighbors, making frequent visits to nearby towns or villages and exchanging their service for food and other goods. As versatile warriors, monks often end up protecting their neighbors from monsters or brigands. For a monk, becoming an adventurer means leaving a structured, communal lifestyle to become a wanderer. This can be a harsh transition, and monks don’t undertake it lightly. Those who leave their cloisters take their work seriously, approaching their adventures as personal tests of their physical and spiritual growth. As you make your monk character, think about your connection to the monastery where you learned your skills and spent your formative years. Were you an orphan or a child left on the monastery's threshold? Did your parents promise you to the monastery in gratitude for a service performed by the monks? Did you enter this secluded life to hide from a crime you committed? Or did you choose the monastic life for yourself? Consider why you left. Did the head of your monastery choose you for a particularly important mission beyond the cloister? Perhaps you were cast out because of some violation of the community's rules. Did you dread leaving, or were you happy to go? Is there something you hope to accomplish outside the monastery? Are you eager to return to your home? As a result of the structured life of a monastic community and the discipline required to harness focus, monks are typically lawful in alignment.",
    hit_dice = "1d8 per Monk level",
    hit_points_at_1st_level = "8 + your Constitution modifier",
    hit_points_at_higher_levels = "1d8 (or 5) + your Constitution modifier per monk level after 1st",
    armor_proficiencies = "None",
    weapon_proficiencies = "Simple blasters, Simple vibroweapons, Chakrams, Techblades",
    tool_proficiencies = "None",
    saving_throw_proficiencies = ["Strength", "Dexterity"],
    skills = "Choose two from Acrobatics, Athletics, Insight, Lore, Perception, and Stealth",
    skill_vals = [2, "Acrobatics", "Athletics", "Insight", "Lore", "Perception", "Stealth"],
    starting_equipment = [
        "(a) a chakram, (b) a techblade, (c) a simple vibroweapon, or (d) a simple blaster and a power cell",
        "(a) a dungeoneer’s pack or (b) an explorer’s pack",
        "10 vibrodarts"
    ],
    variant_starting_wealth = "4d4 x 100 cr",
    description_by_level = {
        "1": {
            "Proficiency Bonus": "+2",
            "Features": ["Martial Arts", "Unarmored Defense"],
            "Martial Arts": "d4",
            "Focus Points": "-",
            "Monastic Vows": "-",
            "Unarmored Movement": "-"
        },
        "2": {
            "Proficiency Bonus": "+2",
            "Features": ["ocus", "Monastic Vows"],
            "Martial Arts": "d4",
            "Focus Points": "2",
            "Monastic Vows": "2",
            "Unarmored Movement": "-"
        },
        "3": {
            "Proficiency Bonus": "+2",
            "Features": ["Unarmored Movement", "Deflect Missiles", "Monastic Order"],
            "Martial Arts": "d4",
            "Focus Points": "3",
            "Monastic Vows": "2",
            "Unarmored Movement": "+10 ft."
        },
        "4": {
            "Proficiency Bonus": "+2",
            "Features": ["Ability Score Improvement", "Slow Fall"],
            "Martial Arts": "d4",
            "Focus Points": "4",
            "Monastic Vows": "2",
            "Unarmored Movement": "+10 ft."
        },
        "5": {
            "Proficiency Bonus": "+3",
            "Features": ["Extra Attack", "Stunning Strike"],
            "Martial Arts": "d6",
            "Focus Points": "5",
            "Monastic Vows": "2",
            "Unarmored Movement": "+15 ft."
        },
        "6": {
            "Proficiency Bonus": "+3",
            "Features": ["Enhanced Strikes", "Order feature"],
            "Martial Arts": "d6",
            "Focus Points": "6",
            "Monastic Vows": "2",
            "Unarmored Movement": "+15 ft."
        },
        "7": {
            "Proficiency Bonus": "+3",
            "Features": ["Evasion", "Stillness of Mind"],
            "Martial Arts": "d6",
            "Focus Points": "7",
            "Monastic Vows": "3",
            "Unarmored Movement": "+15 ft."
        },
        "8": {
            "Proficiency Bonus": "+3",
            "Features": ["Ability Score Improvement"],
            "Martial Arts": "d6",
            "Focus Points": "8",
            "Monastic Vows": "3",
            "Unarmored Movement": "+15 ft."
        },
        "9": {
            "Proficiency Bonus": "+4",
            "Features": ["Unarmored Movement Improvement"],
            "Martial Arts": "d8",
            "Focus Points": "9",
            "Monastic Vows": "3",
            "Unarmored Movement": "+20 ft."
        },
        "10": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Martial Arts": "d8",
            "Focus Points": "10",
            "Monastic Vows": "3",
            "Unarmored Movement": "+20 ft."
        },
        "11": {
            "Proficiency Bonus": "+4",
            "Features": ["Order feature"],
            "Martial Arts": "d8",
            "Focus Points": "11",
            "Monastic Vows": "3",
            "Unarmored Movement": "+20 ft."
        },
        "12": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Martial Arts": "d8",
            "Focus Points": "12",
            "Monastic Vows": "3",
            "Unarmored Movement": "+20 ft."
        },
        "13": {
            "Proficiency Bonus": "+5",
            "Features": ["Purity of Body"],
            "Martial Arts": "d10",
            "Focus Points": "13",
            "Monastic Vows": "4",
            "Unarmored Movement": "+25 ft."
        },
        "14": {
            "Proficiency Bonus": "+5",
            "Features": ["Diamond Soul"],
            "Martial Arts": "d10",
            "Focus Points": "14",
            "Monastic Vows": "4",
            "Unarmored Movement": "+25 ft."
        },
        "15": {
            "Proficiency Bonus": "+5",
            "Features": ["Timeless Vessel"],
            "Martial Arts": "d10",
            "Focus Points": "15",
            "Monastic Vows": "4",
            "Unarmored Movement": "+25 ft."
        },
        "16": {
            "Proficiency Bonus": "+5",
            "Features": ["Ability Score Improvement"],
            "Martial Arts": "d10",
            "Focus Points": "16",
            "Monastic Vows": "4",
            "Unarmored Movement": "+25 ft."
        },
        "17": {
            "Proficiency Bonus": "+6",
            "Features": ["Order feature"],
            "Martial Arts": "d12",
            "Focus Points": "17",
            "Monastic Vows": "5",
            "Unarmored Movement": "+30 ft."
        },
        "18": {
            "Proficiency Bonus": "+6",
            "Features": ["Empty Body"],
            "Martial Arts": "d12",
            "Focus Points": "18",
            "Monastic Vows": "5",
            "Unarmored Movement": "+30 ft."
        },
        "19": {
            "Proficiency Bonus": "+6",
            "Features": ["Ability Score Improvement"],
            "Martial Arts": "d12",
            "Focus Points": "19",
            "Monastic Vows": "5",
            "Unarmored Movement": "+30 ft."
        },
        "20": {
            "Proficiency Bonus": "+6",
            "Features": ["Perfect Self"],
            "Martial Arts": "d12",
            "Focus Points": "20",
            "Monastic Vows": "5",
            "Unarmored Movement": "+30 ft."
        },
    }
)
operative = Class(
    name = "Operative",
    intro = [
        "A Bothan spy takes a moment to adjust her infrared goggles. Nimbly sidestepping the laser grid in the room, she slips to the computer at the far end. Counting down the seconds in her head, she slices the mainframe. Twenty seconds. Ten seconds. A handful of soldiers bursts into the room, but she is already gone � with the data in hand.",
        "With a wary eye on the door, a scruffy-looking Duros plays pazaak in a seedy cantina. When two city guards appear at the exit, he smiles and reaches under the table. Before they can move in, the smuggler flips the table and opens fire. The crowd scatters in panic, giving him just enough cover to escape.",
        "A gorgeous young human dances before an intoxicated senator in his parlor. She winks enticingly through her golden blonde hair as she sways closer. Leaning in for a kiss, the senator is instead surprised by the barrel of a hold-out blaster pistol shoved into his mouth. He has no time to shout before the assassin pulls the trigger.",
        "Operatives, whether good, bad, or neutral, are those who focus on a specific practice and utilize it to get the upper hand. They can come from any world or region in the galaxy, with origins from the lowliest scoundrel to the once social elite."
    ],
    description_1_name = "Evading Danger",
    description_1_info = "Operatives have a knack for getting out of trouble. They have an instinct for self-preservation that keeps them alive, but it’s usually tempered with a need to experience the thrills that their profession has to offer, and many adventurous operatives are also saddled with a sense of honor that sometimes makes them go against their natural inclinations. No matter what their immediate concerns may be, survival is the name of the game.",
    description_2_name = "Outside the Law",
    description_2_info = "Operatives don’t often start out seeking to defy authority and break the law. Some are thrust into the profession as a means of rebellion. Others wind up on the wrong side of the law due to bad luck, poor decisions, or circumstances beyond their control. The skills they pick up along the way make them great members of any mission team. While creating your operative character, consider how you first started on your path. Maybe you were raised on the street and fell into the criminal element as a means of survival. You could be a simple trader who decided to strike against the Sith Empire when it encroached on your business. What would you say is your greatest skill set? What is your core, the truest essence about yourself that keeps you focused? Why would society treat you as a criminal, yet your allies hold you as a loyal companion?",
    hit_dice = "1d8 per Operative level",
    hit_points_at_1st_level = "8 + your Constitution modifier",
    hit_points_at_higher_levels = "1d8 (or 5) + your Constitution modifier per Operative level after 1st",
    armor_proficiencies = "Light armor",
    weapon_proficiencies = "Simple blasters, Simple vibroweapons, Blaster pistol, Hidded blade, Techblade, and Vibrorapier",
    tool_proficiencies = "One specialist's kit of your choice",
    saving_throw_proficiencies = ["Dexterity", "Intelligence"],
    skills = "Choose any four",
    skill_vals = [4, "Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Investigation", "Lore", "Nature", "Piloting", "Technology", "Animal Handling", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"],
    starting_equipment = [
        "(a) a vibrorapier, (b) a hidden blade, (c) a simple blaster and a power cell, or (d) a simple vibroweapon",
        "a) a simple blaster and two power cells or (b) a simple vibroweapon and a light physical shield",
        "(a) a burglar’s pack, (b) a dungeoneer’s pack, or (c) an explorer’s pack",
        "A tool with which you are proficien",
        "Combat suit and a vibrodagger"
    ],
    variant_starting_wealth = "7d4 x 100 cr",
    description_by_level = {
        "1": {
            "Proficiency Bonus": "+2",
            "Features": ["Expertise", "Sneak Attack"],
            "Sneak Attack": "1d6",
            "Operative Exploits": "-"
        },
        "2": {
            "Proficiency Bonus": "+2",
            "Features": ["Cunning Action", "Operative Exploits"],
            "Sneak Attack": "1d6",
            "Operative Exploits": "2"
        },
        "3": {
            "Proficiency Bonus": "+2",
            "Features": ["Bad Feeling", "Operative Practice"],
            "Sneak Attack": "2d6",
            "Operative Exploits": "2"
        },
        "4": {
            "Proficiency Bonus": "+2",
            "Features": ["Ability Score Improvement"],
            "Sneak Attack": "2d6",
            "Operative Exploits": "2"
        },
        "5": {
            "Proficiency Bonus": "+3",
            "Features": ["Uncanny Dodge"],
            "Sneak Attack": "3d6",
            "Operative Exploits": "2"
        },
        "6": {
            "Proficiency Bonus": "+3",
            "Features": ["Expertise"],
            "Sneak Attack": "3d6",
            "Operative Exploits": "2"
        },
        "7": {
            "Proficiency Bonus": "+3",
            "Features": ["Evasion"],
            "Sneak Attack": "4d6",
            "Operative Exploits": "3"
        },
        "8": {
            "Proficiency Bonus": "+3",
            "Features": ["Ability Score Improvement"],
            "Sneak Attack": "4d6",
            "Operative Exploits": "3"
        },
        "9": {
            "Proficiency Bonus": "+4",
            "Features": ["Practice feature"],
            "Sneak Attack": "5d6",
            "Operative Exploits": "3"
        },
        "10": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Sneak Attack": "5d6",
            "Operative Exploits": "3"
        },
        "11": {
            "Proficiency Bonus": "+4",
            "Features": ["Reliable Talent"],
            "Sneak Attack": "6d6",
            "Operative Exploits": "3"
        },
        "12": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Sneak Attack": "6d6",
            "Operative Exploits": "3"
        },
        "13": {
            "Proficiency Bonus": "+5",
            "Features": ["Practice feature"],
            "Sneak Attack": "7d6",
            "Operative Exploits": "4"
        },
        "14": {
            "Proficiency Bonus": "+5",
            "Features": ["Blindsense"],
            "Sneak Attack": "7d6",
            "Operative Exploits": "4"
        },
        "15": {
            "Proficiency Bonus": "+5",
            "Features": ["Slippery Mind"],
            "Sneak Attack": "8d6",
            "Operative Exploits": "4"
        },
        "16": {
            "Proficiency Bonus": "+5",
            "Features": ["Ability Score Improvement"],
            "Sneak Attack": "8d6",
            "Operative Exploits": "4"
        },
        "17": {
            "Proficiency Bonus": "+6",
            "Features": ["Practice feature"],
            "Sneak Attack": "9d6",
            "Operative Exploits": "5"
        },
        "18": {
            "Proficiency Bonus": "+6",
            "Features": ["Elusive"],
            "Sneak Attack": "9d6",
            "Operative Exploits": "5"
        },
        "19": {
            "Proficiency Bonus": "+6",
            "Features": ["Ability Score Improvement"],
            "Sneak Attack": "10d6",
            "Operative Exploits": "5"
        },
        "20": {
            "Proficiency Bonus": "+6",
            "Features": ["Stroke of Luck"],
            "Sneak Attack": "10d6",
            "Operative Exploits": "5"
        }
    }
)
scholar = Class(
    name = "Scholar",
    intro = [
        "An overwhelming horde of tusken raiders bears down on a chiss and her fellow adventurers. She gives the order and her allies unleash a single coordinated attack cutting deep into their lines. Under her command the enemy is quickly routed against all odds, all according to plan.",
        "Deep within the once thought abandoned ruins, a nautolan tends to his companions wounds as they rest. Countless long nights of study and training have conditioned him to keep going even when all others have exhausted themselves. He will see them through this.",
        "A twi’lek in fine vestments addresses a gathering crowd. What was the making of an angry mob begins to disperse, his mere presence putting them at ease, giving his companions time to make their escape.",
        "Scholars are master of the mundane arts, using methodical practices to turn the tables to their advantage. From years of study and testing, scholars take in the situation around them and quickly formulate the means to achieve whatever they have minds set to. Whatever pursuit they follow, a scholar will have a plan for anything that comes their way."
    ],
    description_1_name = "The Pursuit of Knowledge",
    description_1_info = "A true scholar is never satisfied. They are always seeking out a new answer to a new question. This often goes hand-in-hand with seeking a life of adventure, to explore new, hidden areas, or accompany those that do. The life of a scholar often times begins in the mundane, as a teacher or sage. Sometimes they serve as doctors, diplomats, or as officers in the military.",
    description_2_name = "To Learn, To Know",
    description_2_info = "For scholars, mundane life is often too slow. When life becomes stagnant or when an answer cannot be found, the call to adventure rings louder. Scholars will often go to ancient, forgotten, and often dangerous places to find something to quench their thirst for knowledge. As you create a scholar, it's important to think of where you gained your knowledge. Did you serve as an apprentice under a master? Did you attend college or other formal education? Perhaps you gained it on your own, searching out and pouring over dusty tomes found in forgotten places. Where did your thirst for knowledge come from? Insatiable curiosity? Always wanting to know the right answer? Or do you have something to prove? Think about what field you wish to pursue and think of what is driving you in that direction.",
    hit_dice = "1d8 per Scholar level",
    hit_points_at_1st_level = "8 + your Constitution modifier",
    hit_points_at_higher_levels = "1d8 (or 5) + your Constitution modifier per scholar level after 1st",
    armor_proficiencies = "Light armor",
    weapon_proficiencies = "Simple blasters, Simple vibroweapons, Techblades",
    tool_proficiencies = "Any one",
    saving_throw_proficiencies = ["Wisdom", "Intelligence"],
    skills = "Choose three from Deception, Insight, Intimidation, Investigation, Lore, Medicine, Nature, Persuasion, and Survival",
    skill_vals = [3, "Deception", "Insight", "Intimidation", "Investigation", "Lore", "Medicine", "Nature", "Persuasion", "Survival"],
    starting_equipment = [
        "(a) a simple vibroweapon or (b) a simple blaster and two power cells",
        "(a) scholar’s pack or (b) explorer’s pack",
        "a combat suit",
        "any tool of your choice"
    ],
    variant_starting_wealth = "6d4 x 100 cr",
    description_by_level = {
        "1": {
            "Proficiency Bonus": "+2",
            "Features": ["Academic Superiority", "Critical Analysis"],
            "Academic Superiority": "d4",
            "Superiority Dice": "2",
            "Maneuvers Known": "2",
            "Discoveries": "-"
        },
        "2": {
            "Proficiency Bonus": "+2",
            "Features": ["Discovery", "Sage Advice (long rest)"],
            "Academic Superiority": "d4",
            "Superiority Dice": "2",
            "Maneuvers Known": "2",
            "Discoveries": "2"
        },
        "3": {
            "Proficiency Bonus": "+2",
            "Features": ["Expertise", "Academic Pursuit"],
            "Academic Superiority": "d4",
            "Superiority Dice": "4",
            "Maneuvers Known": "4",
            "Discoveries": "4"
        },
        "4": {
            "Proficiency Bonus": "+3",
            "Features": ["Ability Score Improvement"],
            "Academic Superiority": "d4",
            "Superiority Dice": "4",
            "Maneuvers Known": "4",
            "Discoveries": "4"
        },
        "5": {
            "Proficiency Bonus": "+3",
            "Features": ["Multitasker"],
            "Academic Superiority": "d6",
            "Superiority Dice": "4",
            "Maneuvers Known": "4",
            "Discoveries": "5"
        },
        "6": {
            "Proficiency Bonus": "+3",
            "Features": ["Pursuit feature"],
            "Academic Superiority": "d6",
            "Superiority Dice": "4",
            "Maneuvers Known": "4",
            "Discoveries": "5"
        },
        "7": {
            "Proficiency Bonus": "+3",
            "Features": ["-"],
            "Academic Superiority": "d6",
            "Superiority Dice": "6",
            "Maneuvers Known": "6",
            "Discoveries": "5"
        },
        "8": {
            "Proficiency Bonus": "",
            "Features": ["Ability Score Improvement"],
            "Academic Superiority": "d6",
            "Superiority Dice": "6",
            "Maneuvers Known": "6",
            "Discoveries": "5"
        },
        "9": {
            "Proficiency Bonus": "+4",
            "Features": ["Pursuit feature"],
            "Academic Superiority": "d8",
            "Superiority Dice": "6",
            "Maneuvers Known": "6",
            "Discoveries": "6"
        },
        "10": {
            "Proficiency Bonus": "+4",
            "Features": ["Expertise"],
            "Academic Superiority": "d8",
            "Superiority Dice": "6",
            "Maneuvers Known": "6",
            "Discoveries": "6"
        },
        "11": {
            "Proficiency Bonus": "+4",
            "Features": ["-"],
            "Academic Superiority": "d8",
            "Superiority Dice": "8",
            "Maneuvers Known": "8",
            "Discoveries": "7"
        },
        "12": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Academic Superiority": "d8",
            "Superiority Dice": "8",
            "Maneuvers Known": "8",
            "Discoveries": "7"
        },
        "13": {
            "Proficiency Bonus": "+5",
            "Features": ["Sage Advice (short rest)"],
            "Academic Superiority": "d10",
            "Superiority Dice": "8",
            "Maneuvers Known": "8",
            "Discoveries": "8"
        },
        "14": {
            "Proficiency Bonus": "+5",
            "Features": ["Calm and Collected"],
            "Academic Superiority": "d10",
            "Superiority Dice": "8",
            "Maneuvers Known": "8",
            "Discoveries": "8"
        },
        "15": {
            "Proficiency Bonus": "+5",
            "Features": ["-"],
            "Academic Superiority": "d10",
            "Superiority Dice": "10",
            "Maneuvers Known": "10",
            "Discoveries": "8"
        },
        "16": {
            "Proficiency Bonus": "+5",
            "Features": ["Ability Score Improvement"],
            "Academic Superiority": "d10",
            "Superiority Dice": "10",
            "Maneuvers Known": "10",
            "Discoveries": "8"
        },
        "17": {
            "Proficiency Bonus": "+6",
            "Features": ["Pursuit feature"],
            "Academic Superiority": "d12",
            "Superiority Dice": "10",
            "Maneuvers Known": "10",
            "Discoveries": "9"
        },
        "18": {
            "Proficiency Bonus": "+6",
            "Features": ["Adaptable Intellectual"],
            "Academic Superiority": "d12",
            "Superiority Dice": "10",
            "Maneuvers Known": "10",
            "Discoveries": "9"
        },
        "19": {
            "Proficiency Bonus": "+6",
            "Features": ["Ability Score Improvement"],
            "Academic Superiority": "d12",
            "Superiority Dice": "10",
            "Maneuvers Known": "10",
            "Discoveries": "9"
        },
        "20": {
            "Proficiency Bonus": "+6",
            "Features": ["Knowledge Unbound"],
            "Academic Superiority": "d12",
            "Superiority Dice": "10",
            "Maneuvers Known": "10",
            "Discoveries": "9"
        }
    }
)
scout = Class(
    name = "Scout",
    intro = [
        "Rough and grizzled looking, a human stalks alone through the shadows of trees, hunting the quarry he knows is planning a raid on a nearby settlement. Clutching a techblade in each hand, he becomes a whirlwind of steel, cutting down one enemy after another.",
        "After tumbling away from the shrapnel of a missile’s explosion, a bothan finds her feet and quick-fires two shots from her carbine at the oncoming tank. Shrugging off the wave of fear that threatens to permeate her entire being, she strafes around her foe, firing shot after shot to try to penetrate the tank’s thick armor.",
        "Glancing at his wristpad, a sullustan looks through the eyes of his tracker droid. Transmitting instructions, he sends his droid to distract the houk he’s been tracking while he readies his sniper rifle for the shot.",
        "Scouts are the first on the trail and the last to lose it, tracking their quarry for miles unimpeded. They are adaptable, wielding both tech powers and their weaponry to overcome their foes."
    ],
    description_1_name = "Deadly Hunters",
    description_1_info = "Warriors in their own right, scouts specialize in tracking and hunting the monsters that threaten civilization�humanoid raiders, rampaging beasts and monstrosities, terrible Force-wielders, and renegade droids. They learn to track their quarry as a predator does, moving stealthily through any terrain and hiding themselves in brush and rubble. Scouts focus their combat training on techniques that are particularly useful against their specific favored foes. Scouts acquire the ability to cast tech powers through utilization of a wristpad. Their powers, like their combat abilities, emphasize speed, stealth, and the hunt. A scout’s talents and abilities are honed with deadly focus on the grim task of protecting the civilization.",
    description_2_name = "Independent Adventures",
    description_2_info = "Though a scout might make a living as a bounty hunter, a guide, or a tracker, a scout’s true calling is to defend civilization from the ravages of monsters and humanoid hordes that press in. In some places, scouts gather in secretive orders, though many scouts are independent almost to a fault, knowing that, when a rancor or a band of pirates attacks, a scout might be the first�and possibly the last�line of defense. This fierce independence makes scouts well suited to adventuring, since they are accustomed to life far from the comforts of a dry bed and a hot bath. Faced with city-bred adventurers who grouse and whine about the hardships of the wild, scouts respond with some mixture of amusement, frustration, and compassion. But they quickly learn that other adventurers who can carry their own weight in a fight against civilization’s foes are worth any extra burden. Coddled city folk might not know how to feed themselves or find fresh water in the wild, but they make up for it in other ways. As you create your scout character, consider the nature of the training that gave you your particular capabilities. Did you train with a single mentor, tracking together until you mastered the scout's ways? Did you leave your apprenticeship, or was your mentor slain-perhaps by some kind of bestial monstrosity on which you've sworn revenge? Or perhaps you learned your skills as part of a band of mercenaries. What's the source of your particular hatred of a certain kind of enemy? Did a monster kill someone you loved or destroy your home village? Or did you see too much of the destruction these monsters cause and commit yourself to reining in their depredations? Is your adventuring career a continuation of your work, or a significant change? What made you join up with a band of adventurers? Do you find it challenging to teach new allies the ways of the wild, or do you welcome the relief from solitude that they offer?",
    hit_dice = "1d10 per Scout level",
    hit_points_at_1st_level = "10 + your Constitution modifier",
    hit_points_at_higher_levels = "1d10 (or 6) + your Constitution modifier per scout level after 1st",
    armor_proficiencies = "Light armor, Medium armor",
    weapon_proficiencies = "All blasters, All vibroweapons",
    tool_proficiencies = "None",
    saving_throw_proficiencies = ["Strength", "Dexterity"],
    skills = "Choose three from Animal Handling, Athletics, Insight, Investigation, Perception, Piloting, Stealth, Survival, and Technology",
    skill_vals = [3, "Animal Handling", "Athletics", "Insight", "Investigation", "Perception", "Piloting", "Stealth", "Survival", "Technology"],
    starting_equipment = [
        "(a) mesh armor or (b) combat suit, blaster carbine, and two power cells",
        "(a) a simple vibroweapon and a light or medium physical shield or (b) two simple vibroweapons",
        "(a) a hold-out and a power cell or (b) two vibrodaggers",
        "(a) a dungeoneer’s pack or (b) an explorer’s pack",
        "A wristpad"
    ],
    variant_starting_wealth = "8d4 x 100 cr",
    description_by_level = {
        "1": {
            "Proficiency Bonus": "+2",
            "Features": ["Ranger's Quarry", "Pathfinder"],
            "Ranger's Quarry": "d4",
            "Tech Powers Known": "-",
            "Tech Points": "-",
            "Max Power Level": "-"
        },
        "2": {
            "Proficiency Bonus": "+2",
            "Features": ["Techcasting", "Fighting Style"],
            "Ranger's Quarry": "d4",
            "Tech Powers Known": "4",
            "Tech Points": "2",
            "Max Power Level": "1st"
        },
        "3": {
            "Proficiency Bonus": "+2",
            "Features": ["Scout Routine", "Scout Technique"],
            "Ranger's Quarry": "d4",
            "Tech Powers Known": "5",
            "Tech Points": "3",
            "Max Power Level": "1st"
        },
        "4": {
            "Proficiency Bonus": "+2",
            "Features": ["Ability Score Improvement"],
            "Ranger's Quarry": "d4",
            "Tech Powers Known": "6",
            "Tech Points": "4",
            "Max Power Level": "1st"
        },
        "5": {
            "Proficiency Bonus": "+3",
            "Features": ["Extra Attack"],
            "Ranger's Quarry": "d6",
            "Tech Powers Known": "7",
            "Tech Points": "5",
            "Max Power Level": "2nd"
        },
        "6": {
            "Proficiency Bonus": "+3",
            "Features": ["Expertise"],
            "Ranger's Quarry": "d6",
            "Tech Powers Known": "8",
            "Tech Points": "6",
            "Max Power Level": "2nd"
        },
        "7": {
            "Proficiency Bonus": "+3",
            "Features": ["Technique feature", "Scout Routine (two routines)"],
            "Ranger's Quarry": "d6",
            "Tech Powers Known": "9",
            "Tech Points": "7",
            "Max Power Level": "2nd"
        },
        "8": {
            "Proficiency Bonus": "+3",
            "Features": ["Ability Score Improvement"],
            "Ranger's Quarry": "d6",
            "Tech Powers Known": "10",
            "Tech Points": "8",
            "Max Power Level": "2nd"
        },
        "9": {
            "Proficiency Bonus": "+4",
            "Features": ["Scout Routine (15-foot radius)"],
            "Ranger's Quarry": "d8",
            "Tech Powers Known": "12",
            "Tech Points": "9",
            "Max Power Level": "3rd"
        },
        "10": {
            "Proficiency Bonus": "+4",
            "Features": ["Commando"],
            "Ranger's Quarry": "d8",
            "Tech Powers Known": "13",
            "Tech Points": "10",
            "Max Power Level": "3rd"
        },
        "11": {
            "Proficiency Bonus": "+4",
            "Features": ["Technique feature"],
            "Ranger's Quarry": "d8",
            "Tech Powers Known": "14",
            "Tech Points": "11",
            "Max Power Level": "3rd"
        },
        "12": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Ranger's Quarry": "d8",
            "Tech Powers Known": "15",
            "Tech Points": "12",
            "Max Power Level": "3rd"
        },
        "13": {
            "Proficiency Bonus": "+5",
            "Features": ["-"],
            "Ranger's Quarry": "d10",
            "Tech Powers Known": "16",
            "Tech Points": "13",
            "Max Power Level": "4th"
        },
        "14": {
            "Proficiency Bonus": "+5",
            "Features": ["Expertise", "Combat Tech"],
            "Ranger's Quarry": "d10",
            "Tech Powers Known": "17",
            "Tech Points": "14",
            "Max Power Level": "4th"
        },
        "15": {
            "Proficiency Bonus": "+5",
            "Features": ["Technique feature", "Scout Routine (three routines)"],
            "Ranger's Quarry": "d10",
            "Tech Powers Known": "18",
            "Tech Points": "15",
            "Max Power Level": "4th"
        },
        "16": {
            "Proficiency Bonus": "+5",
            "Features": ["Ability Score Improvement"],
            "Ranger's Quarry": "d10",
            "Tech Powers Known": "19",
            "Tech Points": "16",
            "Max Power Level": "4th"
        },
        "17": {
            "Proficiency Bonus": "+6",
            "Features": ["Scout Routine (30-foot radius)"],
            "Ranger's Quarry": "d12",
            "Tech Powers Known": "20",
            "Tech Points": "17",
            "Max Power Level": "5th"
        },
        "18": {
            "Proficiency Bonus": "+6",
            "Features": ["Supreme Awareness"],
            "Ranger's Quarry": "d12",
            "Tech Powers Known": "21",
            "Tech Points": "18",
            "Max Power Level": "5th"
        },
        "19": {
            "Proficiency Bonus": "+6",
            "Features": ["Ability Score Improvement"],
            "Ranger's Quarry": "d12",
            "Tech Powers Known": "22",
            "Tech Points": "19",
            "Max Power Level": "5th"
        },
        "20": {
            "Proficiency Bonus": "+6",
            "Features": ["Foe Slayer"],
            "Ranger's Quarry": "d12",
            "Tech Powers Known": "23",
            "Tech Points": "20",
            "Max Power Level": "5th"
        },
    }
)
sentinel = Class(
    name = "Sentinel",
    intro = [
        "Clad in black robes, the rattataki pulls his hood forward and steps into the shadowy alcove, only to reappear further down the hall. As his quarry walks past, he presses the hilt of his lightsaber to the back of their head, quickly toggling it on-and-off. He is gone before the corpse hits the ground.",
        "The togruta dashes across the battlefield, doublesaber deflecting blaster shots to the ground. She pulls her wounded padawan to her feet, and guides her away from the warzone.",
        "Green-bladed lightsaber a blur, the cathar ferociously presses the attack. With each strike, she guides her opponent closer to the ravine’s edge. A flurry of blows followed by a quick force push and her foe tumbles over the edge.",
        "Sentinels are the masters of blending force powers with weapon attacks. They weave the two together so expertly that their foes have trouble predicting them."
    ],
    description_1_name = "The Middle of the Road",
    description_1_info = "The sentinel uses stealth and subterfuge to accomplish the will of the Force. Where the consular focuses on mastery of the Force and the guardian focuses on the mastery of the lightsaber, the sentinel focuses on merging the two.",
    description_2_name = "Solitary Action",
    description_2_info = "Sentinels are notoriously independent, most comfortable acting alone and without backup; where some use a team to make up for their weaknesses, the sentinel uses the Force to overcome theirs. While some take this independent streak to the extreme, they are usually accepting of authority, as long as they are allowed to carry out directions using their preferred methods. While creating your sentinel, consider your personal philosophy in regards to the Force and its most famous practitioners - the Jedi and the Sith. Are you a member of one of the two orders, or do you walk a different path? Are you an operative tapping into a latent Force-sensitivity? Were you trained in the force from a young age, or did you discover it as an adult? How do you treat those weaker than you? What was your family like? Do you see the Force as light and dark, or an impartial river of gray?",
    hit_dice = "1d8 per Sentinel level",
    hit_points_at_1st_level = "8 + your Constitution modifier",
    hit_points_at_higher_levels = "1d8 (or 5) + your Constitution modifier per sentinel level after 1st",
    armor_proficiencies = "Light armor",
    weapon_proficiencies = "Simple vibroweapons, Simple lightweapons, Chakram, Doubleblade, Doublesaber, Doubleshoto, Doublesword, Hidden blade, Lightfoil, Light ring, Saberwhip, Vibrorapier, Vibrowhip",
    tool_proficiencies = "One specialist's kit of your choice",
    saving_throw_proficiencies = ["Dexterity", "Charisma"],
    skills = "Choose three from Acrobatics, Animal Handling, Insight, Intimidation, Perception, Persuasion, Piloting, Stealth, and Technology",
    skill_vals = [3, "Acrobatics", "Animal Handling", "Insight", "Intimidation", "Perception", "Persuasion", "Piloting", "Stealth", "Technology"],
    starting_equipment = [
        "(a) two simple lightweapons or vibroweapons or (b) one martial lightweapon or vibroweapon with which you are proficient",
        "(a) a dungeoneer’s pack or (b) an explorer’s pack",
        "(a) a demolitions kit, (b) a security kit, or (c) a slicer’s kit",
        "a combat suit and a light physical shield"
    ],
    variant_starting_wealth = "6d4 x 100 cr",
    description_by_level = {
        "1": {
            "Proficiency Bonus": "+2",
            "Features": ["Forcecasting", "Led by the Force"],
            "Force Powers Known": "7",
            "Force Points": "3",
            "Max Power Level": "1st",
            "Kinetic Combat": "-"
        },
        "2": {
            "Proficiency Bonus": "+2",
            "Features": ["Force-Empowered Self", "Sentinel Ideals"],
            "Force Powers Known": "9",
            "Force Points": "6",
            "Max Power Level": "1st",
            "Kinetic Combat": "d4"
        },
        "3": {
            "Proficiency Bonus": "+2",
            "Features": ["Sentinel Calling"],
            "Force Powers Known": "11",
            "Force Points": "9",
            "Max Power Level": "2nd",
            "Kinetic Combat": "d4"
        },
        "4": {
            "Proficiency Bonus": "+2",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "13",
            "Force Points": "12",
            "Max Power Level": "2nd",
            "Kinetic Combat": "d4"
        },
        "5": {
            "Proficiency Bonus": "+3",
            "Features": ["Extra Attack"],
            "Force Powers Known": "15",
            "Force Points": "15",
            "Max Power Level": "2nd",
            "Kinetic Combat": "d6"
        },
        "6": {
            "Proficiency Bonus": "+3",
            "Features": ["Sentinel Ideals (three ideals)"],
            "Force Powers Known": "17",
            "Force Points": "18",
            "Max Power Level": "3rd",
            "Kinetic Combat": "d6"
        },
        "7": {
            "Proficiency Bonus": "+3",
            "Features": ["Calling feature"],
            "Force Powers Known": "18",
            "Force Points": "21",
            "Max Power Level": "3rd",
            "Kinetic Combat": "d6"
        },
        "8": {
            "Proficiency Bonus": "+3",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "19",
            "Force Points": "24",
            "Max Power Level": "3rd",
            "Kinetic Combat": "d6"
        },
        "9": {
            "Proficiency Bonus": "+4",
            "Features": ["Sentinel Ideals (three manifestations)"],
            "Force Powers Known": "21",
            "Force Points": "27",
            "Max Power Level": "4th",
            "Kinetic Combat": "d8"
        },
        "10": {
            "Proficiency Bonus": "+4",
            "Features": ["Battle Readiness"],
            "Force Powers Known": "22",
            "Force Points": "30",
            "Max Power Level": "4th",
            "Kinetic Combat": "d8"
        },
        "11": {
            "Proficiency Bonus": "+4",
            "Features": ["Sentinel Ideals (four ideals)"],
            "Force Powers Known": "24",
            "Force Points": "33",
            "Max Power Level": "5th",
            "Kinetic Combat": "d8"
        },
        "12": {
            "Proficiency Bonus": "+4",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "25",
            "Force Points": "36",
            "Max Power Level": "5th",
            "Kinetic Combat": "d8"
        },
        "13": {
            "Proficiency Bonus": "+5",
            "Features": ["Calling feature"],
            "Force Powers Known": "26",
            "Force Points": "39",
            "Max Power Level": "5th",
            "Kinetic Combat": "d10"
        },
        "14": {
            "Proficiency Bonus": "+5",
            "Features": ["-"],
            "Force Powers Known": "28",
            "Force Points": "42",
            "Max Power Level": "6th",
            "Kinetic Combat": "d10"
        },
        "15": {
            "Proficiency Bonus": "+5",
            "Features": ["Enlightened Evasion"],
            "Force Powers Known": "29",
            "Force Points": "45",
            "Max Power Level": "6th",
            "Kinetic Combat": "d10"
        },
        "16": {
            "Proficiency Bonus": "+5",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "30",
            "Force Points": "48",
            "Max Power Level": "6th",
            "Kinetic Combat": "d10"
        },
        "17": {
            "Proficiency Bonus": "+6",
            "Features": ["Sentinel Ideals (four manifestations)"],
            "Force Powers Known": "32",
            "Force Points": "51",
            "Max Power Level": "7th",
            "Kinetic Combat": "d12"
        },
        "18": {
            "Proficiency Bonus": "+6",
            "Features": ["Calling feature"],
            "Force Powers Known": "33",
            "Force Points": "54",
            "Max Power Level": "7th",
            "Kinetic Combat": "d12"
        },
        "19": {
            "Proficiency Bonus": "+6",
            "Features": ["Ability Score Improvement"],
            "Force Powers Known": "34",
            "Force Points": "57",
            "Max Power Level": "7th",
            "Kinetic Combat": "d12"
        },
        "20": {
            "Proficiency Bonus": "+6",
            "Features": ["Center of the Force"],
            "Force Powers Known": "35",
            "Force Points": "60",
            "Max Power Level": "7th",
            "Kinetic Combat": "d12"
        },
    }
)

db.session.add_all([berserker, consular, engineer, fighter, guardian, monk, operative, scholar, scout, sentinel])
db.session.commit()
# ------------------------------------------------------------

# --------------------Creates Class Features------------------
#? Berserker Features
rage = ClassFeatures(
    name = "Rage",
    levels = ['1st'],
    details = "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action if you aren’t wearing heavy armor. While raging, you gain the following benefits: You have advantage on Strength checks and Strength saving throws. When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a berserker, as shown in the Rage Damage column of the berserker table. You have resistance to kinetic and energy damage. If you are able to cast powers, you can’t cast them or concentrate on them while raging. Your rage lasts for 1 minute. It ends early if you are knocked unconscious, you don heavy armor, or if your turn ends and you haven’t taken a hostile action or taken damage since your last turn. You can also end your rage on your turn as a bonus action. You can enter a rage a number of times as shown for your berserker level in the Rages column of the berserker table. You regain all expended uses when you complete a long rest.",
    class_id = 1,
)
unarmored_defense = ClassFeatures(
    name = "Unarmored Defense",
    levels = ["1st"],
    details = "While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
    class_id = 1,
)
reckless_attack = ClassFeatures(
    name = "Reckless Attack",
    levels = ["2nd"],
    details = "You can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.",
    class_id = 1,
)
berserker_instincts = ClassFeatures(
    name = "Berserker Instincts",
    levels = ["2nd"],
    details = "You can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.",
    class_id = 1,
)
danger_sense = ClassFeatures(
    name = "Danger Sense",
    levels = ["3rd"],
    details = "You gain an uncanny sense of when things nearby aren’t as they should be, giving you an edge when you dodge away from danger. You have advantage on Dexterity saving throws against effects that you can see, such as traps and powers. To gain this benefit, you can’t be blinded, deafened, or incapacitated.",
    class_id = 1,
)
berserker_approach = ClassFeatures(
    name = "Berserker Approach",
    levels = ["3rd", "6th", "10th", "14th"],
    details = "You choose an approach that shapes the nature of your rage ",
    class_id = 1,
)
ability_score_improvement_berserker = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["4th", "8th", "12th", "16th", "19th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 1,
)
extra_attack_berserker = ClassFeatures(
    name = "Extra Attack",
    levels = ["5th"],
    details = "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
    class_id = 1,
)
feral_impulse = ClassFeatures(
    name = "Feral Impulse",
    levels = ["7th"],
    details = "Your instincts are so honed that you have advantage on initiative rolls. Additionally, if you are surprised at the start of combat and aren’t incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.",
    class_id = 1,
)
brutal_critical =ClassFeatures(
    name = "Brutal Critical",
    levels = ["9th", "13th", "17th"],
    details = "You can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack. This increases to two additional dice at 13th level and three additional dice at 17th level.",
    class_id = 1,
)
relentless_rage = ClassFeatures(
    name = "Relentless Rage",
    levels = ["11th"],
    details = "Your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you’re raging and don’t die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead. Each time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10.",
    class_id = 1,
)
presistent_rage = ClassFeatures(
    name = "Presistent Rage",
    levels = ["15th"],
    details = "Your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it.",
    class_id = 1,
)
indomitable_might = ClassFeatures(
    name = "Indomitable Might",
    levels = ["18th"],
    details = "If your total for a Strength check is less than your Strength score, you can use that score in place of the total.",
    class_id = 1,
)
primal_champion = ClassFeatures(
    name = "Primal Champion",
    levels = ["20th"],
    details = "You embody the power of the wilds. Your Strength or Dexterity score increases by 2, and your Constitution score increases by 2. Your maximum for those scores increases by 2. Additionally, you can enter rage an unlimited number of times, and entering rage no longer requires your bonus action on your turn.",
    class_id = 1,
)

db.session.add_all([rage, unarmored_defense, reckless_attack, berserker_instincts, danger_sense, berserker_approach, ability_score_improvement_berserker, extra_attack_berserker, feral_impulse, brutal_critical, relentless_rage, presistent_rage, indomitable_might, primal_champion])
db.session.commit()

#? Consular Features
forcecasting_consular = ClassFeatures(
    name = "Forcecasting",
    levels = ["1st"],
    details = "In your meditations on the force, you have learned powers, fragments of knowledge that imbue you with an abiding force ability. You learn 9 force powers of your choice, and you learn more at higher levels, as shown in the Force Powers Known column of the consular table. You may not learn a force power of a level higher than your Max Power Level, and you may learn a force power at the same time you learn its prerequisite. You have a number of force points equal to your consular level x 4 + your Wisdom or Charisma modifier (your choice). You use these force points to cast force powers. You regain all expended force points when you finish a long rest. Many force powers can be overpowered, consuming more force points to create a greater effect. You can overpower these abilities to a maximum level, which increases at higher levels. You may only cast force powers at 6th, 7th, 8th, and 9th-level once. You regain the ability to do so after a long rest. Your forcecasting ability varies based on the alignment of the powers you cast. You use Wisdom for light side powers, Charisma for dark side powers, and Wisdom or Charisma for universal powers (your choice). You use this ability score modifier whenever a power refers to your forcecasting ability. Additionally, you use this ability score modifier when setting the saving throw DC for a force power you cast and when making an attack roll with one. Force save DC = 8 + your proficiency bonus + your forcecasting ability modifier. Force attack modifier = your proficiency bonus + your forcecasting ability modifier.",
    class_id = 2
)
force_recovery = ClassFeatures(
    name = "Force Recovery",
    levels = ["1st"],
    details = "You have learned to regain some of your energy by briefly meditating. When you finish a short rest, you can regain a number of force points equal to half your consular level (rounded down) + your Wisdom or Charisma modifier (your choice, minimum of one). Once you’ve used this feature, you must complete a long rest before you can use it again.",
    class_id = 2
)
force_empowered_casting = ClassFeatures(
    name = "Force-Empowered Casting",
    levels = ["2nd", "9th", "17th"],
    details = "You gain the ability to twist your powers to suit your needs. When you cast a force power, you can expend additional force points to modify the power. You gain two of the following Force-Empowered Casting options of your choice. You gain another one at 9th and 17th level. You can use only one Force-Empowered Casting option on a power when you cast it, unless otherwise noted.",
    class_id = 2
)
force_shield = ClassFeatures(
    name = "Force Shield",
    levels = ["2nd"],
    details = "You learn how to defend yourself purely through your strength with the Force. When you are hit by an attack, you can use your reaction to shroud yourself in Force energy. Until the start of your next turn, you have a bonus to AC equal to your Wisdom or Charisma modifier (your choice, minimum of +1). This includes the triggering attack. You can use this feature a number of times equal to your proficiency bonus, as shown in the consular table. You regain all expended uses when you finish a long rest.",
    class_id = 2
)
force_affinity = ClassFeatures(
    name = "Force Affinity",
    levels = ["3rd"],
    details = "You’ve developed an affinity for one of the three aspects of the Force: the Ashla, the Bendu, or the Bogan. Choose one from the following: Ashla - When you successfully cast a light side power, either your or the target’s (your choice) hit point maximum and current hit points increase by an amount equal to the power’s level. This effect lasts for 1 minute. You can only have one instance of this effect active at a time.Bendu - You can add both your Wisdom and Charisma modifier to your maximum number of force points, instead of just one. Bogan - When you roll a 1 on a damage die for a dark side power, you can reroll the die and must use the new roll, even if the new roll is a 1.",
    class_id = 2
)
consular_tradition = ClassFeatures(
    name = "Consular Tradition",
    levels = ["3rd", "6th", "10th", "14th", "18th"],
    details = "You choose a consular tradition",
    class_id = 2
)
ability_score_improvement_consular = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["3rd", "6th", "10th", "14th", "18th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 2
)
one_with_the_force = ClassFeatures(
    name = "One with the Force",
    levels = ["20th"],
    details = "Your attunement to the Force is absolute. Your Wisdom or Charisma score increases by 4, and your maximum for this score increases by 4. Additionally, you gain mastery over a single force power, and can cast it with little effort. Choose one 3rd-level force power that you know as your signature power. You can cast it once at 3rd level without expending force points. When you do so, you can’t do so again until you finish a short or long rest. If you want to cast it at a higher level, you must expend force points as normal.",
    class_id = 2
)

db.session.add_all([forcecasting_consular, force_recovery, force_empowered_casting, force_shield, force_affinity, consular_tradition, ability_score_improvement_consular, one_with_the_force])
db.session.commit()

#? Enginner Features
techcasting_engineer = ClassFeatures(
    name = "Techcasting",
    levels = ["1st"],
    details = "During your training you have derived powers from schematics with the aid of your wristpad. You learn 6 tech powers of your choice, and you learn more at higher levels. You may not learn a tech power of a level higher than your Max Power Level. You have a number of tech points equal to your engineer level x 2 + your Intelligence modifier. You use these tech points to cast tech powers. You regain all expended tech points when you finish a short or long rest. Many tech powers can be overcharged, consuming more tech points to create a greater effect. You can overcharge these powers to a maximum level. You may only cast tech powers at 6th, 7th, 8th, and 9th-level once. You regain the ability to do so after a long rest. Intelligence is your techcasting ability for your tech powers. You use your Intelligence whenever a power refers to your techcasting ability. Additionally, you use your Intelligence modifier when setting the saving throw DC for a tech power you cast and when making an attack roll with one. Tech save DC = 8 + your proficiency bonus + your Intelligence modifier. Tech attack modifier = your proficiency bonus + your Intelligence modifier.",
    class_id = 3
)
potent_aptitude = ClassFeatures(
    name = "Potent Aptitude",
    levels = ["1st"],
    details = "Your technological experience lends you an uncommon insight that you can use to bolster your allies. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Potent Aptitude die, a d4. This die changes as you gain engineer levels. Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 beforedeciding to use the Potent Aptitude die, but must decide before the GM says whether the roll succeeds or fails. Once the Potent Aptitude die is rolled, it is lost. A creature can have only one Potent Aptitude die at a time. You can use this feature a number of times equal to your proficiency bonus, as shown in the engineer table. You regain any expended uses when you finish a short or long rest.",
    class_id = 3
)
infuse_item = ClassFeatures(
    name = "Infuse Item",
    levels = ["2nd"],
    details = "You gain the ability to temporarily enhance a weapon or armor. At the end of a long rest, you can touch one unenhanced object that is a suit of armor, a shield, or a simple or martial weapon. Until the end of your next long rest or until you die, the object becomes an enhanced item, granting a +1 bonus to AC if it’s armor or a shield or a +1 bonus to attack and damage rolls if it’s a weapon. Once you’ve used this feature, you can’t use it again until you finish a long rest. This bonus increases to +2 at 10th level and +3 at 15th level.",
    class_id = 3
)
tool_expertise = ClassFeatures(
    name = "Tool Expertise",
    levels = ["2nd"],
    details = "You gain expertise in any tool proficiencies you gain from this class.",
    class_id = 3
)
engineering_discipline = ClassFeatures(
    name = "Engineering Discipline",
    levels = ["3rd", "6th", "14th", "18"],
    details = "You begin to focus on a specific engineering discipline",
    class_id = 3
)
ability_score_improvement_engineer = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["3rd", "6th", "14th", "18th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 3
)
tech_mastery = ClassFeatures(
    name = "Tech Mastery",
    levels = ["20th"],
    details = "Your mastery of technology is unrivaled. Your Constitution and Intelligence scores increase by 2. Your maximum for those scores increases by 2. Additionally, when you roll initiative and have no uses of Potent Aptitude left, you regain one use.",
    class_id = 3
)

db.session.add_all([techcasting_engineer, potent_aptitude, infuse_item, tool_expertise, engineering_discipline, ability_score_improvement_engineer, tech_mastery])
db.session.commit()

#? Fighter Features
fighting_style = ClassFeatures(
    name = "Fighting Style",
    levels = ["1st"],
    details = "You adopt a particular style of fighting as your specialty.",
    class_id = 4
)
second_wind = ClassFeatures(
    name = "Second Wind",
    levels = ["1st"],
    details = "You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you’ve used this feature, you must finish a short or long rest before you can use it again.",
    class_id = 4
)
action_surge = ClassFeatures(
    name = "Action Surge",
    levels = ["2nd"],
    details = "You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action on top of your regular action and a possible bonus action. Once you’ve used this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn.",
    class_id = 4
)
combat_superiority = ClassFeatures(
    name = "Combat Superiority",
    levels = ["2nd"],
    details = "You learn maneuvers that are fueled by special dice called superiority dice. You learn two maneuvers of your choice. Many maneuvers enhance an attack in some way. You can use only one maneuver per attack, and you may only use each maneuver once per turn. Each time you learn new maneuvers, you can also replace one maneuver you know with a different one. You have two superiority dice, which are d4s, and you earn more at higher levels. This die changes as you gain fighter levels A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest. Some of your maneuvers require your target to make a saving throw to resist the maneuver’s effects. The saving throw DC is calculated as follows: Maneuver save DC = 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice)",
    class_id = 4
)
fighting_mastery = ClassFeatures(
    name = "Fighting Mastery",
    levels = ["3rd"],
    details = "You’ve mastered a particular style of fighting. Choose one of the Fighting Mastery options",
    class_id = 4
)
fighter_specialty = ClassFeatures(
    name = "Fighter Specialty",
    levels = ["3rd", "7th", "10th", "15th", "18th"],
    details = "You choose a specialty that you strive to emulate in your combat styles and techniques.",
    class_id = 4
)
ability_score_improvement_fighter = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["4th", "6th", "8th", "12th", "14th", "16th", "19th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 4
)
extra_attack_fighter = ClassFeatures(
    name = "Extra Attack",
    levels = ["5th"],
    details = "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
    class_id = 4
)
indomitable = ClassFeatures(
    name = "Indomitable",
    levels = ["9th"],
    details = "You can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can’t use this feature again until you finish a long rest. You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level.",
    class_id = 4
)
greater_extra_attack = ClassFeatures(
    name = "Greater Extra Attack",
    levels = ["11th"],
    details = "You can attack three times, instead of once, whenever you take the Attack action on your turn. Additionally, when you use a bonus action to engage in Double- or Two-Weapon Fighting, you can make two attacks, instead of one.",
    class_id = 4
)
master_of_combat = ClassFeatures(
    name = "Master of Combat",
    levels = ["20th"],
    details = "You are the master of combat. Your Strength or Dexterity score increases by 2, and your Constitution score increases by 2. Your maximum for those scores increases by 2. Additionally, you can attack four times, instead of once, whenever you take the Attack action on your turn.",
    class_id = 4
)

db.session.add_all([fighting_style, second_wind, action_surge, combat_superiority, fighting_mastery, fighter_specialty, ability_score_improvement_fighter, extra_attack_fighter, indomitable, greater_extra_attack, master_of_combat])
db.session.commit()

#? Guardian Features
forcecasting_guardian = ClassFeatures(
    name = "Forcecasting",
    levels = ["1st"],
    details = "In your meditations on the force, you have learned powers, fragments of knowledge that imbue you with an abiding force ability. You learn 9 force powers of your choice, and you learn more at higher levels, as shown in the Force Powers Known column of the consular table. You may not learn a force power of a level higher than your Max Power Level, and you may learn a force power at the same time you learn its prerequisite. You have a number of force points equal to your consular level x 4 + your Wisdom or Charisma modifier (your choice). You use these force points to cast force powers. You regain all expended force points when you finish a long rest. Many force powers can be overpowered, consuming more force points to create a greater effect. You can overpower these abilities to a maximum level, which increases at higher levels. You may only cast force powers at 6th, 7th, 8th, and 9th-level once. You regain the ability to do so after a long rest. Your forcecasting ability varies based on the alignment of the powers you cast. You use Wisdom for light side powers, Charisma for dark side powers, and Wisdom or Charisma for universal powers (your choice). You use this ability score modifier whenever a power refers to your forcecasting ability. Additionally, you use this ability score modifier when setting the saving throw DC for a force power you cast and when making an attack roll with one. Force save DC = 8 + your proficiency bonus + your forcecasting ability modifier. Force attack modifier = your proficiency bonus + your forcecasting ability modifier.",
    class_id = 5
)
channel_the_force = ClassFeatures(
    name = "Channel the Force",
    levels = ["1st"],
    details = "You know how to channel the Force to create a unique effect. You start with your choice of one from two such effects: Cause Harm or Lend Aid. At 3rd level, your Guardian Focus grants you an additional effect. When you use your Channel the Force, you choose which effect to create. Some Channel the Force effects require saving throws. When you use such an effect from this class, the DC equals your universal force save DC. Cause Harm: As an action, you can expend a use of your Channel the Force to sap the life from a hostile creature you can see within 60 feet. That creature must make a Constitution saving throw. On a failed save, the creature takes necrotic damage equal to your guardian level + your Charisma modifier (minimum of one), or half as much on a successful one. Lend Aid: As a bonus action, you can expend a use of your Channel the Force and touch a beast or humanoid within 5 feet of you. That creature regains hit points equal to your guardian level + your Wisdom modifier (minimum of one). Alternatively, if the beast or humanoid is poisoned or diseased, you neutralize the poison or disease. If more than one poison or disease afflicts the target, you neutralize one poison or disease that you know is present, or you neutralize one at random.",
    class_id = 5
)
force_empowered_strikes = ClassFeatures(
    name = "Force Empowered Strikes",
    levels = ["2nd"],
    details = "When you hit a creature with a melee weapon attack, you can expend force points to deal additional damage to the target, which is the same type as the weapon’s damage. The additional damage is 1d8 for each point spent in this way.",
    class_id = 5
)
fighting_style = ClassFeatures(
    name = "Fighting Style",
    levels = ["2nd"],
    details = "You adopt a particular style of fighting as your specialty.",
    class_id = 5
)
guardian_aura = ClassFeatures(
    name = "Guardian Aura",
    levels = ["3rd", "9th", "19th", "17th", "18th"],
    details = "When you reach 3rd level, you gain an aura of your choice, as detailed at the end of the class description. The range of your auras increases to 15 feet at 9th level and 30 feet at 17th level, and you gain an additional aura at 10th and 18th level.",
    class_id = 5
)
guardian_focus = ClassFeatures(
    name = "Guardian Focus",
    levels = ["3rd", "7th", "15th", "20th"],
    details = "You begin to focus your studies on a specific lightsaber form",
    class_id = 5
)
ability_score_improvement_guardian = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["4th", "8th", "12th", "16th", "19th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 5
)
extra_attack_guardian = ClassFeatures(
    name = "Extra Attack",
    levels = ["5th"],
    details = "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
    class_id = 5
)
force_purity = ClassFeatures(
    name = "Force Purity",
    levels = ["6th"],
    details = "The Force flowing through you makes you immune to poison and disease.",
    class_id = 5
)
imporved_force_empowered_strike = ClassFeatures(
    name = "Improved Force-Empowered Strikes",
    levels = ["11th"],
    details = "You are so in tune with the Force that all your melee weapon strikes carry the power of the Force with them. Whenever you hit a creature with a melee weapon attack, the creature takes an extra 1d8 damage. If you also use your Force-Empowered Strikes with an attack, you add this damage to the extra damage of your Force-Empowered Strikes. The damage is the same type as the weapon’s damage.",
    class_id = 5
)
cleansing_touch = ClassFeatures(
    name = "Clensing Touch",
    levels = ["14th"],
    details = "You can use your action and expend a use of your Channel the Force ability to end one force power on yourself or on one willing creature that you touch.",
    class_id = 5
)

db.session.add_all([forcecasting_guardian, channel_the_force, force_empowered_strikes, fighting_style, guardian_aura, guardian_focus, ability_score_improvement_guardian, extra_attack_guardian, force_purity, imporved_force_empowered_strike, cleansing_touch])
db.session.commit()

#? Monk Features
martial_arts = ClassFeatures(
    name = "Martial Arts",
    levels = ["1st"],
    details = "Your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are chakrams, techblades, and any simple vibroweapons that don’t have the two-handed property. You gain the following benefits while you are unarmed or wielding only monk weapons and you aren’t wearing armor or wielding a shield: Your unarmed strikes and monk weapons gain the finesse property. You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the monk table. You can use Dexterity instead of Strength whenever you would make a Strength (Athletics) check to grapple, shove, or trip a creature. When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. You can take the Dash and Disengage actions as a bonus action.",
    class_id = 6
)
unarmored_defense_monk = ClassFeatures(
    name = "Unarmored Defense",
    levels = ["1st"],
    details = "While you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom or Charisma modifier (your choice).",
    class_id = 6
)
focus  = ClassFeatures(
    name = "Focus",
    levels = ["2nd", "11th"],
    details = "Your training allows you to harness the mystic energy of focus. Your access to this energy is represented by a number of focus points. Your monk level determines the number of points you have. You can spend these points to fuel various focus features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more focus features as you gain levels in this class. When you spend a focus point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended focus back into yourself. You must spend at least 30 minutes of the rest meditating to regain your focus points. You use your choice of Wisdom or Charisma for your focus ability. You use the chosen ability modifier whenever a feature refers to your focus ability. Additionally, you use the chosen ability modifier when making an attack with a focus feature or setting the saving throw DC for one. Focus save DC = 8 + your proficiency bonus + your Wisdom or Charisma modifier (your choice). Focus attack modifier = your proficiency bonus + your Wisdom or Charisma modifier (your choice). Flurry of Blows: When you make your Martial Arts bonus action attack, you can spend 1 focus point to make an additional unarmed strike (no action required). At 11th level, you can instead spend 2 focus points to make two additional unarmed strikes. Patient Defense: When you use your bonus action to Disengage, you can spend 1 focus point to also Dodge (no action required). At 11th level, you can instead spend 2 focus points to Dodge and gain an additional reaction until the start of your next turn. You can only take one reaction per turn. Step of the Wind: When you use your bonus action to Dash, you can spend 1 focus point to double your jump distance for the turn. At 11th level, you can instead spend 2 focus points to gain a flying speed equal to your walking speed until the end of your turn, though you fall if you end your speed in the air and nothing else is holding you aloft.",
    class_id = 6
)
monastic_vows = ClassFeatures(
    name = "Monastic Vows",
    levels = ["2nd", "7th", "13th", "17th"],
    details = "You’ve sworn two vows, as detailed at the end of the class description. You swear an additional vow at 7th, 13th, and 17th level.",
    class_id = 6
)
unarmored_movement = ClassFeatures(
    name = "Unarmored Movement",
    levels = ["3rd", "9th"],
    details = "Your speed increases by 10 feet while you are not wearing armor or wielding a shield. This bonus increases when you reach certain monk levels, as shown in the Unarmored Movement column of the monk table. At 9th level, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the move.",
    class_id = 6
)
deflect_missiles = ClassFeatures(
    name = "Deflect Missiles",
    levels = ["3rd"],
    details = "You can use your reaction to deflect a projectile when you are dealt damage by a ranged weapon attack. When you do so, the damage you take from the attack is reduced by 1d10 + your Dexterity modifier + your monk level. If you reduce the damage to 0, and the damage is kinetic, energy, or ion, you can redirect it at another target if you have a weapon capable of doing so. You can spend 1 focus point to make a ranged attack as you deflect the projectile, as part of the same reaction. You make this attack with proficiency, regardless of your weapon proficiencies, and the projectile counts as a monk weapon for the attack.",
    class_id = 6
)
monastic_order = ClassFeatures(
    name = "Monastic Order",
    levels = ["3rd", "6th", "11th", "17th"],
    details = "You commit yourself to one monastic order",
    class_id = 6
)
ability_score_improvement_monk = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["4th" ,"8th", "10th", "12th", "16th", "19th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 6
)
slow_fall  = ClassFeatures(
    name = "Slow Fall",
    levels = ["4th"],
    details = "You can use your reaction when you fall to reduce any falling damage you take by an amount equal to five times your monk level.",
    class_id = 6
)
extra_attack_monk = ClassFeatures(
    name = "Extra Attack",
    levels = ["5th"],
    details = "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
    class_id = 6
)
stunning_strike = ClassFeatures(
    name = "Stunning Strike",
    levels = ["5th"],
    details = "You can interfere with an opponent’s body. When you hit another creature with a melee weapon attack, you can spend 1 focus point to attempt a stunning strike. The target must succeed on a Constitution saving throw or be stunned until the end of your next turn.",
    class_id = 6
)
enhanced_strikes = ClassFeatures(
    name = "Enhanced Strike",
    levels = ["6th"],
    details = "Your unarmed strikes count as enhanced for the purpose of overcoming resistance and immunity to unenhanced attacks and damage.",
    class_id = 6
)
evasion = ClassFeatures(
    name = "Evasion",
    levels = ["7th"],
    details = "Your instinctive agility lets you dodge out of the way of certain area effects. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on a saving throw, and only half damage if you fail.",
    class_id = 6
)
stillness_of_mind = ClassFeatures(
    name = "Stillness of Mind",
    levels = ["7th"],
    details = "You can use your action or bonus action to end one effect on yourself that is causing you to be charmed or frightened.",
    class_id = 6
)
purity_of_body = ClassFeatures(
    name = "Purity of Body",
    levels = ["13th"],
    details = "You are immune to disease and poison and resistant to poison damage.",
    class_id = 6
)
diamond_soul = ClassFeatures(
    name = "Diamond Soul",
    levels = ["14th"],
    details = "Your mastery of focus grants you proficiency in all saving throws, and when you fail a saving throw, you can spend 1 focus point to reroll it, taking the new roll.",
    class_id = 6
)
timeless_vessel = ClassFeatures(
    name = "Timeless Vessel",
    levels = ["15th"],
    details = "Your focus sustains you so that you suffer none of the frailty of old age, and you can’t be aged abnormally. You can still die of old age, however. Additionally, when you complete a short rest, you can expend a Hit Die to remove 1 level of exhaustion or slowed.",
    class_id = 6
)
empty_body = ClassFeatures(
    name = "Empty Body",
    levels = ["18th"],
    details = "You can use your action to spend 4 focus points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage.",
    class_id = 6
)
perfect_self = ClassFeatures(
    name = "Perfect Self",
    levels = ["20th"],
    details = "You’ve gained perfect control over your body. Your Dexterity and Wisdom or Charisma scores (your choice) increase by 2. Your maximum for those scores increases by 2. Additionally, when you roll for initiative and have fewer than 6 focus points remaining, you regain up to 6 focus points.",
    class_id = 6
)

db.session.add_all([martial_arts, unarmored_defense_monk, focus, monastic_vows, unarmored_movement, deflect_missiles, monastic_order, ability_score_improvement_monk, slow_fall, extra_attack_monk, stunning_strike, enhanced_strikes, evasion, stillness_of_mind, purity_of_body, diamond_soul, timeless_vessel, empty_body, perfect_self])
db.session.commit()

#? Operative Features
expertise = ClassFeatures(
    name = "Expertise",
    levels = ["1st", "6th"],
    details = "Choose two of your skill proficiencies, or one of skill proficiencies and one of your tool proficiencies, or two of your tool proficiencies. You gain expertise in those skills or tools. At 6th level, you can choose two more of your proficiencies (in skills or tools) to gain this benefit.",
    class_id = 7
)
sneak_attack = ClassFeatures(
    name = "Sneack Attack",
    levels = ["1st"],
    details = "You know how to strike subtly and exploit a foe’s distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with a weapon attack if you have advantage on the attack roll. This damage is the same as the weapon’s damage, and the attack must use a finesse or a ranged weapon. You don’t need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn’t incapacitated, and you don’t have disadvantage on the attack roll. The amount of the extra damage increases as you gain levels in this class.",
    class_id = 7
)
cunning_action = ClassFeatures(
    name = "Cunning Action",
    levels = ["2nd"],
    details = "Your quick thinking and agility allow you to move and act quickly. You can take a bonus action on each of your turns in combat. This action can be used only to take the Dash, Disengage, or Hide action.",
    class_id = 7
)
operative_exploits = ClassFeatures(
    name = "Operative Exploits",
    levels = ["2nd", "7th", "13th", "17th"],
    details = "You’ve adopted two exploits. You adopt an additional exploit at 7th, 13th, and 17th level.",
    class_id = 7
)
bad_feeling = ClassFeatures(
    name = "Bad Feeling",
    levels = ["3rd"],
    details = "You have a wary eye, bordering on paranoia. When you roll for initiative, you can move up to your speed. This movement happens before the initiative order is determined. Once you’ve used this feature, you can’t use it again until you finish a long rest.",
    class_id = 7
)
operative_practice = ClassFeatures(
    name = "Operative Practice",
    levels = ["3rd", "9th", "13th", "17th"],
    details = "You choose a practice that you emulate in the exercise of your operative abilities, which is detailed at the end of the class description. Your practice choice grants you features at 3rd level and then again at 9th, 13th, and 17th level.",
    class_id = 7
)
ability_score_improvement_operative = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["4th", "8th", "10th", "12th", "16th", "19th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 7
)
uncanny_dodge = ClassFeatures(
    name = "Uncanny Dodge",
    levels = ["5th"],
    details = "When an attacker that you can see deals damage to you with an attack, you can use your reaction to halve the attack’s damage against you.",
    class_id = 7
)
evasion_operative = ClassFeatures(
    name = "Evasion",
    levels = ["7th"],
    details = "When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on a saving throw, and only half damage if you fail.",
    class_id = 7
)
reliable_talent = ClassFeatures(
    name = "Reliable Talent",
    levels = ["11th"],
    details = "You have refined your chosen skills until they approach perfection. Whenever you make an ability check that lets you add your proficiency bonus, you can treat a d20 roll of 9 or lower as a 10.",
    class_id = 7
)
blindsense = ClassFeatures(
    name = "Blindsense",
    levels = ["14th"],
    details = "If you are able to hear, you are aware of the location of any hidden or invisible creature within 10 feet of you.",
    class_id = 7
)
slippery_mind = ClassFeatures(
    name = "Slippery Mind",
    levels = ["15th"],
    details = "You have acquired greater mental strength. You gain proficiency in Wisdom saving throws.",
    class_id = 7
)
elusive = ClassFeatures(
    name = "Elusive",
    levels = ["18th"],
    details = "You are so evasive that attackers rarely gain the upper hand against you. No attack roll has advantage against you while you aren’t incapacitated.",
    class_id = 7
)
stroke_of_luck = ClassFeatures(
    name = "Stroke of Luck",
    levels = ["20th"],
    details = "You have an uncanny knack for succeeding when you need to. Your Dexterity and Intelligence scores increase by 2. Your maximum for those scores increases by 2. Additionally, if your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20. Once you’ve used this feature, you can’t use it again until you finish a short or long rest.",
    class_id = 7
)

db.session.add_all([expertise, sneak_attack, cunning_action, operative_exploits, bad_feeling, operative_practice, ability_score_improvement_operative, uncanny_dodge, evasion_operative, reliable_talent, blindsense, slippery_mind, elusive, stroke_of_luck])
db.session.commit()

#? Scholar Features
academic_superiority = ClassFeatures(
    name = "Academic Superiority",
    levels = ["1st"],
    details = "You learn maneuvers that are fueled by special dice called superiority dice. You know two maneuvers of your choice, which are detailed under “Maneuvers” below, and you earn more at higher levels, as shown in the Maneuvers Known column of the scholar table. Many maneuvers enhance an attack in some way. You can use only one maneuver per attack, and you may only use each maneuver once per turn. Each time you learn new maneuvers, you can also replace one maneuver you know with a different one. You have two superiority dice, which are d4s, and you earn more at higher levels, as shown in the Superiority Dice column of the scholar table. This die changes as you gain scholar levels, as shown in the Academic Superiority column of the scholar table. A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest. Some of your maneuvers require your target to make a saving throw to resist the maneuver’s effects. The saving throw DC is calculated as follows: Maneuver save DC = 8 + your proficiency bonus + your Intelligence modifier",
    class_id = 8
)
critical_analysis = ClassFeatures(
    name = "Critical Analysis",
    levels = ["1st"],
    details = "You are able to analyze a target, develop a plan on how to best overcome any potential obstacle, and execute that plan with ruthless efficiency. As a bonus action on your turn, you can analyze a target you can see within 60 feet of you. For the next minute, or until you analyze another target, you gain the following benefits: When you analyze a hostile creature, your attack and damage rolls made with weapons with the finesse property or blaster weapons against that target may use your Intelligence modifier instead of Strength or Dexterity. When you analyze a friendly creature, the target can end your Critical Analysis on them (no action required) to add your Intelligence modifier to one attack roll, ability check, or saving throw. Once a friendly creature has benefited from this ability, they can not do so again until they complete a short or long rest.",
    class_id = 8
)
discovery = ClassFeatures(
    name = "Discovery",
    levels = ["2nd"],
    details = "As you adventure, your studies have helped you discover new practices you can apply to your skills. You master two discoveries of your choice. When you gain certain scholar levels, you gain additional discoveries of your choice. Additionally, when you gain a level in this class, you can choose one of the discoveries you know and replace it with another discovery that you could learn at that level.",
    class_id = 8
)
sage_advice = ClassFeatures(
    name = "Sage Advice",
    levels = ["2nd"],
    details = "You can spend 1 minute spreading your knowledge and experience, advising those around you. When you do so, choose a skill or tool you are proficient with and a number of friendly creatures up to your Intelligence modifier within 30 feet of you who can hear you and who can understand you. Once within the next hour, the next time each creature would make an ability check with the chosen skill or tool, they may add their proficiency bonus to the roll if they are not already proficient. A creature may only benefit from this feature once. If a creature is targeted by this feature again before using it, they can choose to retain the first benefit or replace it with the new skill or tool instead. Once you’ve used this feature, you can’t use it again until you finish a long rest. Starting at 13th level, you regain the ability to use it after you complete a short or long rest.",
    class_id = 8
)
expertise_scholar = ClassFeatures(
    name = "Expertise",
    levels = ["3rd", "10th"],
    details = "Choose two of your skill proficiencies, or one of skill proficiencies and one of your tool proficiencies, or two of your tool proficiencies. You gain expertise in those skills or tools. At 10th level, you can choose another two proficiencies (in skills or tools) to gain this benefit.",
    class_id = 8
)
academic_pursuit = ClassFeatures(
    name = "Academic Pursuit",
    levels = ["4th", "6th", "9th", "17th"],
    details = "Also at 3rd level, you dedicate your studies towards a pursuit",
    class_id = 8
)
ability_score_improvement_scholar = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["4th", "6th", "9th", "17th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 8
)
multitasker = ClassFeatures(
    name = "Multitasker",
    levels = ["5th"],
    details = "You can take a second reaction each round. You can only take one reaction per turn. Additionally, when a friendly creature you can see that can hear you is forced to make a saving throw, you can use your reaction to target them with your Critical Analysis feature.",
    class_id = 8
)
calm_and_collected = ClassFeatures(
    name = "Calm and Collected",
    levels = ["14th"],
    details = "When you make a saving throw caused by an effect you can see, you may gain a bonus to the saving throw equal to your Intelligence modifier. You can use this feature a number of times equal to your proficiency bonus, as shown in the scholar table. You regain all expended uses when you complete a long rest.",
    class_id = 8
)
adaptable_intellectual = ClassFeatures(
    name = "Adaptable Intellectual",
    levels = ["18th"],
    details = "You are able to effectively prepare for any mission on hand. At the end of a long rest, you may choose one of the discoveries you know and replace it with another discovery that you could learn at that level.",
    class_id = 8
)
knowledge_unbound = ClassFeatures(
    name = "Knowledge Unbound",
    levels = ["20th"],
    details = "You are the pinnacle of your pursuit. Your Intelligence score increases by 4. Your maximum for that score increases by 4. Additionally, you can use any maneuver you know without expending a superiority die, rolling a d4 instead.",
    class_id = 8
)

db.session.add_all([academic_superiority, critical_analysis, discovery, sage_advice, expertise_scholar, academic_pursuit, ability_score_improvement_scholar, multitasker, calm_and_collected, adaptable_intellectual, knowledge_unbound])
db.session.commit()

#? Scout Features
pathfinder = ClassFeatures(
    name = "Pathfinder",
    levels = ["1st"],
    details = "You are skilled at navigating the untamed wilds. You ignore difficult terrain, and when traveling for an hour or more, you gain the following benefits: Difficult terrain doesn’t slow your group, provided they can see and hear you. You can’t become lost by unenhanced means. Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger. If you are traveling alone, you can move stealthily at a normal pace. When you forage, you find twice as much food. You have advantage on Survival checks.",
    class_id = 9
)
techcasting_scout  = ClassFeatures(
    name = "techcasting",
    levels = ["2nd"],
    details = "You have derived powers from schematics with the aid of your wristpad. See chapter 10 for the general rules of techcasting and chapter 12 for the tech powers list. You learn 4 tech powers of your choice, and you learn more at higher levels. You may not learn a tech power of a level higher than your Max Power Level. You have a number of tech points equal to your scout level + your Intelligence modifier. You use these tech points to cast tech powers. You regain all expended tech points when you finish a short or long rest. Many tech powers can be overcharged, consuming more tech points to create a greater effect. You can overcharge these powers to a maximum level, which increases at higher levels. You may only cast tech powers at 4th and 5th-level once. You regain the ability to do so after a long rest. Intelligence is your techcasting ability for your tech powers. You use your Intelligence whenever a power refers to your techcasting ability. Additionally, you use your Intelligence modifier when setting the saving throw DC for a tech power you cast and when making an attack roll with one. Tech save DC = 8 + your proficiency bonus + your Intelligence modifier. Tech attack modifier = your proficiency bonus + your Intelligence modifier. You use a wristpad as a tech focus for your tech powers.",
    class_id = 9
)
fighting_style_scout = ClassFeatures(
    name = "Fighting Style",
    levels = ["2nd"],
    details = "You adopt a particular style of fighting as your specialty. Choose one of the fighting style options.",
    class_id = 9
)
scout_routine = ClassFeatures(
    name = "Scout Routine",
    levels = ["3rd", "7th", "9th", "15th", "17th"],
    details = "You’ve developed one routine. You develop an additional routine at 7th and 15th level. At 9th level, the range of your routines increases to 15 feet, and at 17th level, the range of these routines increases to 30 feet",
    class_id = 9
)
scout_technique = ClassFeatures(
    name = "Scout Technique",
    levels = ["3rd", "7th", "11th", "15th"],
    details = "You choose to focus on a specific scout technique",
    class_id = 9
)
ability_score_improvement_scout = ClassFeatures(
    name = "Ability Score Improvement",
    levels = ["4th", "8th", "12th", "16th", "19th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 9
)
extra_attack_scout = ClassFeatures(
    name = "Extra Attack",
    levels = ["5th"],
    details = "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
    class_id = 9
)
expertise_scout = ClassFeatures(
    name = "Expertise",
    levels = ["6th", "14th"],
    details = "Choose two of your skill proficiencies, or one of skill proficiencies and one of your tool proficiencies, or two of your tool proficiencies. You gain expertise in those skills or tools. At 14th level, you can choose another two proficiencies (in skills or tools) to gain this benefit.",
    class_id = 9
)
commando = ClassFeatures(
    name = "Commando",
    levels = ["10th"],
    details = "You can take the Dash or Hide actions as a bonus action on each of your turns. Additionally, you can remain perfectly still for long periods of time to set up ambushes. When you attempt to hide on your turn, you can opt to not move on that turn. If you avoid moving, creatures that attempt to detect you take a -10 penalty to their Wisdom (Perception) checks until the start of your next turn. You lose this benefit if you move or fall prone, either voluntarily or because of some external effect. You are still automatically detected if any effect or action causes you to no longer be hidden. If you are still hidden on your next turn, you can continue to remain motionless and gain this benefit until you are detected. Finally, you can no longer be tracked by unenhanced means, unless you choose to leave a trail.",
    class_id = 9
)
combat_tech = ClassFeatures(
    name = "Comabt Tech",
    levels = ["14th"],
    details = "When you use your action to cast a tech power, you can make one weapon attack as a bonus action.",
    class_id = 9
)
supreme_awareness = ClassFeatures(
    name = "Supreme Awareness",
    levels = ["18th"],
    details = "You gain preternatural senses that help you fight creatures you can’t see. When you attack a creature you can’t see, your inability to see it doesn’t impose disadvantage on your attack rolls against it. You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn’t hidden from you and you aren’t blinded or deafened.",
    class_id = 9
)
foe_slayer = ClassFeatures(
    name = "Foe Slayer",
    levels = ["20th"],
    details = "You become an unparalleled hunter. Your Strength or Dexterity score increases by 2, and your Intelligence score increases by 2. Your maximum for those scores increases by 2. Additionally, once on each of your turns, you can add your Intelligence modifier to the attack roll or the damage roll of an attack you make. You can choose to use this feature before or after the roll, but before any effects of the roll are applied.",
    class_id = 9
)

db.session.add_all([pathfinder, techcasting_scout, fighting_style_scout, scout_routine, scout_technique, ability_score_improvement_scout, extra_attack_scout, expertise_scout, commando, combat_tech, supreme_awareness, foe_slayer])
db.session.commit()

#? Sentinel Features
forcecasting_sentinel = ClassFeatures(
    name = "Forcecasting",
    levels = ["1st"],
    details = "In your meditations on the force, you have learned powers, fragments of knowledge that imbue you with an abiding force ability. You learn 7 force powers of your choice, and you learn more at higher levels. You may not learn a force power of a level higher than your Max Power Level, and you may learn a force power at the same time you learn its prerequisite. You have a number of force points equal to your sentinel level x 3 + your Wisdom or Charisma modifier (your choice). You use these force points to cast force powers. You regain all expended force points when you finish a long rest. Many force powers can be overpowered, consuming more force points to create a greater effect. You can overpower these abilities to a maximum level, which increases at higher levels. You may only cast force powers at 5th, 6th, and 7th-level once. You regain the ability to do so after a long rest. Your forcecasting ability varies based on the alignment of the powers you cast. You use Wisdom for light side powers, Charisma for dark side powers, and Wisdom or Charisma for universal powers (your choice). You use this ability score modifier whenever a power refers to your forcecasting ability. Additionally, you use this ability score modifier when setting the saving throw DC for a force power you cast and when making an attack roll with one. Force save DC = 8 + your proficiency bonus + your forcecasting ability modifier. Force attack modifier = your proficiency bonus + your forcecasting ability modifier.",
    class_id = 10
)
led_by_the_force = ClassFeatures(
    name = "Led by the Force",
    levels = ["1st"],
    details = "You can add half your proficiency bonus, rounded down, to any ability check you make that doesn’t already include your proficiency bonus.",
    class_id = 10
)
force_empowered_self = ClassFeatures(
    name = "Force-Empowered Self",
    levels = ["2nd"],
    details = "Your training allows you to harness the mystical energy of the Force throughout your body. When you hit a creature with a melee weapon attack, you can spend 1 force point to use a Force-Empowered Self effect. Each effect uses a d4, which changes as you gain sentinel levels, as shown in the Kinetic Combat column of the sentinel table. You have three such effects: Deflection, Double Strike, and Slow Time. You can only use each effect once per turn, and you can only use one effect per hit. Deflection: You can roll a Kinetic Combat die and add it to your AC against one attack before the start of your next turn. Double Strike: You can roll a Kinetic Combat die and deal additional damage of the same type equal to the amount rolled. Slow Time: You can roll a Kinetic Combat die to increase your speed by 5 x the amount rolled until the end of your turn.",
    class_id = 10
)
sentinel_ideals = ClassFeatures(
    name = "",
    levels = ["2nd", "6th", "9th", "11th", "17th"],
    details = "You adopt ideals that exemplify your bond with the Force. You adopt two ideals of your choice. You adopt an additional ideal at 6th and 11th level. You can manifest your ideals a combined total of twice. You gain an additional use at 9th and 17th level. You regain all expended uses when you finish a long rest.",
    class_id = 10
)
sentinel_calling = ClassFeatures(
    name = "",
    levels = ["3rd", "7th", "13th", "18th"],
    details = "You choose a sentinel calling",
    class_id = 10
)
ability_score_improvement_sentinel = ClassFeatures(
    name = "Ability Score improvement",
    levels = ["4th", "8th", "12th", "16th", "19th"],
    details = "You can increase one ability score by 2, or you can increase two ability scores by 1. You can’t increase an ability score above 20 using this feature.",
    class_id = 10
)
extra_attack_sentinel = ClassFeatures(
    name = "Extra Attack",
    levels = ["5th"],
    details = "You can attack twice, instead of once, whenever you take the Attack action on your turn.",
    class_id = 10
)
battle_readiness = ClassFeatures(
    name = "Battle Readiness",
    levels = ["10th"],
    details = "You have fully learned how to meld your physical self with the Force. When you take the Dodge or Disengage actions, or use your action to cast a force power, you can make one melee weapon attack as a bonus action.",
    class_id = 10
)
enlightened_evasion = ClassFeatures(
    name = "Enlightened Evasion",
    levels = ["15th"],
    details = "When you are subjected to an effect that forces you to make a saving throw, you can spend 2 force points to add your Wisdom or Charisma modifier (your choice, minimum of one) to the saving throw if doesn’t already include that modifier. If you do so, you instead take no damage if you succeed on the saving throw, and only half damage if you fail. You can wait until after you roll the d20 to use this feature, but you must decide before the GM says it succeeds or fails.",
    class_id = 10
)
center_of_the_force = ClassFeatures(
    name = "Center of the Force",
    levels = ["20th"],
    details = "You are perfectly centered with the Force. Your Dexterity and Wisdom or Charisma scores (your choice) increase by 2. Your maximum for those scores increases by 2. Additionally, once per turn, when you would roll a Kinetic Combat die, you can instead choose the maximum.",
    class_id = 10
)

db.session.add_all([forcecasting_sentinel, led_by_the_force, force_empowered_self, sentinel_ideals, sentinel_calling, ability_score_improvement_sentinel, extra_attack_sentinel, battle_readiness, enlightened_evasion, center_of_the_force])
db.session.commit()
# ------------------------------------------------------------

#--------------------Tech Powers-------------------------------
#? At-Will
acid_splash = TechPowers(
    name = "Acid Splash",
    level = 0,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You emit a burst of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage. This power’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
)
acidic_strike = TechPowers(
    name = "Acidic Strike",
    level = 0,
    casting_period = "1 action",
    range = "varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and it becomes sheathed in a thick acidic slime until the start of your next turn. Until the start of your next turn, if the target becomes grappled, or succeeds in grappling or maintaining a grapple, the slime is pressed into its body, causing it to immediately take 1d8 acid damage. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 acid damage to the target, and the damage the target takes for taking grappling or maintaining a grapple increases to 2d8. Both damage rolls increase by 1d8 at 11th level and 17th level."
)
assess_the_situation = TechPowers(
    name = "Assess the Situation",
    level = 0,
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 round",
    concentration = "Concentration",
    description = "You take a sensory snapshot of a target within range. Your tech grants you a brief insight into the target’s defenses. You have advantage on the next attack roll you make against the target before the end of your next turn. This power benefits additional attacks at higher levels: two attacks at 5th level, three attacks at 11th level, and four attacks at 17th level."
)
combustive_shot = TechPowers(
    name = "Combustive Shot",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a ranged weapon attack against one creature within your weapon’s range, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and it ignites in flame. At the start of your next turn, the creature takes fire damage equal to your techcasting ability modifier. If the target or a creature within 5 feet of it uses an action to put out the flames, or if some other effect douses the flames, the effect ends. This power’s damage increases when you reach higher levels. At 5th level, the ranged attack deals an extra 1d6 fire damage to the target, and the damage at the start of your next turn increases to 1d4 + your tech casting ability modifier. Both damage rolls increase by 1d6 and 1d4, respectively, at 11th level and 17th level."
)
cryogenic_burst = TechPowers(
    name = "Cryogenic Burst",
    level = 0,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You emit a burst of cold energy at a creature within range. Make a ranged tech attack against the target. On a hit, it takes 1d8 cold damage, and gains 1 slowed level until the start of your next turn. The power’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
)
echo_blast = TechPowers(
    name = "Echo Blast",
    level = 0,
    casting_period = "1 action",
    range = "30 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You emit a reverberating pulse of sound at a target within range. The target must succeed on a Wisdom saving throw or take 1d8 sonic damage. This power can hit multiple targets in succession when you reach higher levels: two targets at 5th level, three targets at 11th level, and four targets at 17th level. Each target must be within 30 feet of the previous target, and the last target must be no further than 30 feet away from you. You can not target the same creature twice in succession."
)
electrical_burst = TechPowers(
    name = "Electrical Burst",
    level = 0,
    casting_period = "1 action",
    range = "Self (5-foot sphere)",
    duration = "Instantaneous",
    concentration = "-",
    description = "You emit a burst of electricity. Each creature within range, other than you, must succeed on a Dexterity saving throw or take 1d6 lightning damage. This power’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
)
electroshock = TechPowers(
    name = "Electroshock",
    level = 0,
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    description = "Lightning springs from you to deliver a shock to a creature you try to touch. Make a melee tech attack against the target. You have advantage on the attack roll if the target is made of metal or wearing armor made of metal. On a hit, the target takes 1d8 lightning damage and becomes shocked until the start of its next turn. This power’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
)
encrypted_message = TechPowers(
    name = "Encrypted Message",
    level = 0,
    casting_period = "1 action",
    range = "120 feet",
    duration = "1 round",
    concentration = "-",
    description = "You point your finger toward a creature within range that possesses a commlink and whisper a message. The target (and only the target) hears the message and can send an encrypted reply that only you can hear. These messages cannot be intercepted or decrypted by unenhanced means. You can cast this power through solid objects if you are familiar with the target and know it is beyond the barrier. 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the power. The power doesn’t have to follow a straight line and can travel freely around corners or through openings."
)
extinguish = TechPowers(
    name = "Extinguish",
    level = 0,
    casting_period = "1 action",
    range = "30 feet (5-foot cube)",
    duration = "Instantaneous",
    concentration = "-",
    description = "You spray carbon foam in a 5-foot cube originating from a point within range. Flames within the affected area are instantly quenched, and objects within the affected area cannot be ignited for at least one minute. Any creature in the affected area must make a Constitution saving throw or take 1d4 cold damage. When you reach 5th level, this power can instead target a 10-foot cube within range. You gain additional options of increasing size when you reach 11th level (15-foot cube), and 17th level (20-foot cube)."
)
haywire = TechPowers(
    name = "Haywire",
    level = 0,
    casting_period = "1 action",
    range = "30 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You momentarily surround a creature you can see within range with electronic interference and holographic illusions. The target must succeed on an Intelligence saving throw, or it takes 1d6 lightning damage and moves 5 feet in a random direction if it can move and its speed is at least 5 feet. Roll a d4 for the direction: 1, north; 2, south; 3, east; or 4, west. This movement doesn’t provoke opportunity attacks, and if the direction rolled is blocked, the target doesn’t move. The power’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
)
illusory_strike = TechPowers(
    name = "Illusory Strike",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and you create an illusory duplicate of yourself in your space that only the target can see. The target has disadvantage on the next attack roll it makes against you before the start of your next turn. This power creates multiple duplicates when you reach higher levels. At 5th level, you create a second illusory duplicate, and the target has disadvantage on the next two attacks it makes against you before the start of your next turn. The number of duplicates and attacks with disadvantage increases to three at 11th level and four at 17th level."
)
ion_blast = TechPowers(
    name = "Ion Blast",
    level = 0,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You create a blast of ion energy. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d4 ion damage This power’s damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4)."
)
ionic_strike = TechPowers(
    name = "Ionic Strike",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and it becomes wreathed in an ionic discharge. If the target willingly takes a reaction before the start of your next turn, it immediately takes 1d6 ion damage, and the power ends. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d6 ion damage to the target, and the damage the target takes for taking reactions increases to 2d6. Both damage rolls increase by 1d6 at 11th level and 17th level."
)
jet_of_flame = TechPowers(
    name = "Jet of Flame",
    level = 0,
    casting_period = "1 action",
    range = "Self (30-foot sphere)",
    duration = "10 minutes",
    concentration = "-",
    description = "A flickering flame appears in your hand. The flame remains there for the duration and harms neither you nor your equipment. The flame sheds bright light in a 10-foot radius and dim light for an additional 10 feet. The power ends if you dismiss it as an action or if you cast it again. You can also attack with the flame, although doing so ends the power. When you cast this power, or as an action on a later turn, you can hurl the flame at a creature within 30 feet of you. Make a ranged tech attack. On a hit, the target takes 1d8 fire damage. The fire ignites any flammable objects in the area that aren’t being worn or carried. This power’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
)
light = TechPowers(
    name = "Light",
    level = 0,
    casting_period = "1 action",
    range = "Touch",
    duration = "1 hour",
    concentration = "-",
    description = "You touch one object that is no larger than 10 feet in any dimension. Until the power ends, the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet. The light can be colored as you like. Completely covering the object with something opaque blocks the light. The power ends if you cast it again or dismiss it as an action. If you target an object held or worn by a hostile creature, that creature must succeed on a Dexterity saving throw to avoid the power."
)
mending = TechPowers(
    name = "Mending",
    level = 0,
    casting_period = "1 minute",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    description = "This ability repairs a single break or tear in an object you touch, such as broken chain link, two halves of a broken key, a torn strap, or a leaking cup. As long as the break or tear is no larger than 1 foot in any dimension, you mend it, leaving no trace of the former damage."
)
minor_defibrillation = TechPowers(
    name = "Minor Defibrillation",
    level = 0,
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    description = "You generate a static charge that can aid or harm a creature you touch. Make a melee tech attack against the target. On a hit, the target takes 1d10 lightning damage. If the target is a living creature that has 0 hit points, it immediately gains one death saving throw success instead of taking damage. This power’s damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10)."
)
minor_hologram = TechPowers(
    name = "Minor Hologram",
    level = 0,
    casting_period = "1 action",
    range = "10 feet",
    duration = "Up to 1 hour",
    concentration = "-",
    description = "This ability is a minor tech trick that creates one of the following effects within range. You create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor, You instantaneously light or snuff out a source of light, You instantaneously clean or soil an object no larger than 1 cubic foot, You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour, You make a color, a small mark, or a symbol appear on an object or a surface for 1 hour, You create a trinket or an illusory image that can fit in your hand and that lasts until the end of your next turn. If you use this power multiple times, you can have up to three of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action."
)
mobile_lights = TechPowers(
    name = "Mobile Lights",
    level = 0,
    casting_period = "1 action",
    range = "120 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    description = "You create up to four orbs of light within range that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius. As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this power, and a light winks out if it exceeds the power’s range."
)
on_off = TechPowers(
    name = "On/Off",
    level = 0,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "This power allows you to activate or deactivate any electronic device within range, as long as the device is not being wielded by a creature, and has a clearly defined on or off function that can be easily accessed from the outside of the device. Any device that requires a software-based shutdown sequence to activate or deactivate cannot be affected by on/off."
)
pheromone_burst = TechPowers(
    name = "Pheromone Burst",
    level = 0,
    casting_period = "1 action",
    range = "Self (5-foot sphere)",
    duration = "Instantaneous",
    concentration = "-",
    description = "You expel a burst of mood-altering pheromones around you. Each creature within range other than you must succeed on a Charisma saving throw or take 1d4 poison damage and become frightened of you until the start of its next turn. A creature that is immune to the poisoned condition is not frightened. This power’s damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4)."
)
posion_spray = TechPowers(
    name = "Posion Spray",
    level = 0,
    casting_period = "1 action",
    range = "10 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You extend your hand toward a creature you can see within range and project a puff of noxious gas. The creature must succeed on a Constitution saving throw or take 1d12 poison damage. This power’s damage increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), and 17th level (4d12)."
)
pressure_crush = TechPowers(
    name = "Pressure Crush",
    level = 0,
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    description = "You attempt to crush the body of a creature you touch. The target must make a Strength saving throw. If the creature is grappled or restrained by you or an effect you control, it makes the saving throw with disadvantage. On a failed save, the creature takes 1d12 kinetic damage. This power’s damage increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), and 17th level (4d12)."
)
reboot = TechPowers(
    name = "Reboot",
    level = 0,
    casting_period = "1 action",
    range = "60 feet",
    duration = "1 round",
    concentration = "-",
    description = "Choose a Medium or smaller droid or construct you can see. The target must make a Charisma saving throw. On a failed save, it is incapacitated until the start of your next turn. Each time the creature takes damage or is the target of a hostile power while incapacitated in this way, it can repeat this saving throw, ending the effect on a success."
)
rime_shot = TechPowers(
    name = "Rime Shot",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a ranged weapon attack against one creature within your weapon’s range, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and the creature gains 1 slowed level until the end of its turn as the air around it turns frigid. This power deals additional damage when you reach higher levels. At 5th level the ranged attack deals an extra 1d6 cold damage. This damage increases by 1d6 again at 11th level and 17th level."
)
rime_strike = TechPowers(
    name = "Rime Strike",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and gains 1 slowed level until the start of your next turn, as the cold energy seeps into its being. Additionally, if the target doesn’t move at least 5 feet before the start of your next turn, it immediately takes 1d8 cold damage, and the power ends. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 cold damage to the target, and the damage the target takes for not moving increases to 2d8. Both damage rolls increase by 1d8 at 11th level and 17th level."
)
short_circuit = TechPowers(
    name = "Short Circuit",
    level = 0,
    casting_period = "1 action",
    range = "120 feet",
    duration = "1 round",
    concentration = "-",
    description = "You electrocute a creature within range. Make a ranged tech attack against the creature. On a hit, the target takes 1d8 lightning damage. If the target is a droid, construct, or has a tech focus, it has disadvantage on the first attack roll it makes against you until the end of your next turn. This power’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
)
sonic_shot = TechPowers(
    name = "Sonic Shot",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a ranged weapon attack against one creature within your weapon’s range, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and it becomes wreathed in a sonic barrier until the start of your next turn. If the target willingly moves before then, it immediately takes sonic damage equal to your techcasting modifier, becomes deafened until the start of your next turn, and the power ends. This power’s damage increases when you reach higher levels. At 5th level, the ranged attack deals an extra 1d6 sonic damage to the target, and the damage the target takes for moving increases to 1d6 + your techcasting ability modifier. Both damage rolls increase by an additional 1d6 at 11th and 17th level."
)
sonic_strike = TechPowers(
    name = "Sonic Strike",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and you begin to emanate a disturbing hum. If a hostile creature ends its turn within 5 feet of you before the start of your next turn, it takes 1d4 sonic damage. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 sonic damage to the target, and the secondary damage increases by 1d4. Both damage rolls increase by 1d8 and 1d4, respectively, at 11th level and 17th level."
)
spectrum_ray = TechPowers(
    name = "Spectrum Ray",
    level = 0,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You shoot a beam of energy at a creature that you can see within range. You choose acid, cold, fire, lightning, poison, or sonic for the type of beam you create, and then make a ranged tech attack against the target. If the attack hits, the creature takes 1d8 damage of the type you chose. This power’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8) and 17th level (4d8)."
)
stroming_shot = TechPowers(
    name = "Storming Shot",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As a part of the action used to cast this power, you must make a ranged weapon attack against one creature within your weapon’s range, otherwise the power fails. On a hit, the target suffers the attack’s normal effects and becomes shocked until the end of your next turn. When this power hits a target, if there is a creature within 30 feet who is shocked, an arc of lightning courses between the two creatures, dealing 1d6 lightning damage to both of them. If there are multiple other creatures who are shocked, the lightning leaps to the closest creature. The power’s damage increases when you reach higher levels. At 5th level, the effects of both the ranged weapon attack and discharge deal an extra 1d6 lightning damage. Both damage rolls increase by an additional 1d6 at 11th and 17th level."
)
targeting_shot = TechPowers(
    name = "Targeting Shot",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a ranged weapon attack against one creature within your weapon’s range, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and a small target only visible to you marks it. The next attack roll you make against the creature before the end of your next turn can’t suffer from disadvantage. This power deals additional damage when you reach higher levels. At 5th level, the ranged attack deals an extra 1d6 damage. This damage increases by 1d6 again at 11th level and 17th level. The damage is the same type as the weapon’s damage."
)
temporary_boost = TechPowers(
    name = "Tempoary Boost",
    level = 0,
    casting_period = "1 action",
    range = "Touch",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    description = "You touch one willing creature. Once before the power ends, the target can roll a d4 and add the number rolled to one ability check of its choice. It can roll the die before or after making the ability check. The power then ends. This power’s die increases at higher levels: to a d6 at 5th level, a d8 at 11th level, and a d10 at 17th level."
)
venomous_strike = TechPowers(
    name = "Venomous Strike",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "Instantaneous",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and if you were hidden from it, it takes an additional 1d4 poison damage. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 poison damage to the target, and the damage the target takes when you are hidden from it increases to 2d4. Both damage rolls increase by 1d8 and 1d4, respectively, at 11th level and 17th level."
)
vortex_shot = TechPowers(
    name = "Vortex Shot",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "Instantaneous",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a ranged weapon attack against one creature within your weapon’s range, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and each Large or smaller creature within 10 feet of the target must succeed on a Strength saving throw or be pulled to the nearest unoccupied space adjacent to the target. This power deals additional damage when you reach higher levels. At 5th level, the ranged attack deals an extra 1d6 damage. This damage increases by 1d6 again at 11th level and 17th level. The damage is the same type as the weapon’s damage."
)
ward = TechPowers(
    name = "Ward",
    level = 0,
    casting_period = "1 action",
    range = "Self",
    duration = "1 round",
    concentration = "-",
    description = "You emit a powerful force field that deflects incoming attacks. Until the end of your next turn, you have resistance against kinetic, energy, and ion damage dealt by weapon attacks."
)
warding_shot = TechPowers(
    name = "Warding Shot",
    level = 0,
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    description = "As part of the action used to cast this power, you must make a ranged weapon attack against one creature within your weapon’s range, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and a dim barrier surrounds it. The first time it would deal damage before the start of your next turn, that damage is reduced by 1d6. This power’s damage reduction increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
)
wire_line = TechPowers(
    name = "Wire Line",
    level = 0,
    casting_period = "1 action",
    range = "30 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You launch a grappling wire toward a creature you can see within range. Make a melee tech attack against the target. If the attack hits, the creature takes 1d6 kinetic damage, and if the creature is Large or smaller, you pull the creature up to 10 feet closer to you. This power’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
)

db.session.add_all([acid_splash, acidic_strike, assess_the_situation, combustive_shot, cryogenic_burst, echo_blast, electrical_burst, electroshock, encrypted_message, extinguish, haywire, illusory_strike, ion_blast, ionic_strike, jet_of_flame, light, mending, minor_defibrillation, minor_hologram, mobile_lights, on_off, pheromone_burst, posion_spray, pressure_crush, reboot, rime_shot, rime_strike, short_circuit, sonic_shot, sonic_strike, spectrum_ray, stroming_shot, targeting_shot, temporary_boost, venomous_strike, vortex_shot, ward, warding_shot, wire_line])
db.session.commit()
#? 1st level
absorb_energy = TechPowers(
    name = "Absorb Energy",
    level = 1,
    casting_period = "1 reaction, which you take when you take acid, cold, energy, fire, ion, kinetic, lightning, or sonic damage",
    range = "Self",
    duration = "1 round",
    concentration = "-",
    description = "The power captures some of the incoming energy, lessening its effect on you and storing it for your next melee attack. You have resistance to the triggering damage type until the start of your next turn. Also, the first time you hit with a melee attack on your next turn, the target takes an extra 1d6 damage of the triggering type, and the power ends. Overcharge Tech. When you cast this power using a power slot of 2nd level or higher, the extra damage increases by 1d6 for each slot level above 1st."
)
acid_wind = TechPowers(
    name = "Acid Wind",
    level = 1,
    casting_period = "1 action",
    range = "Self (15-foot cube)",
    duration = "Instantaneous",
    concentration = "-",
    description = "You produce a breeze full of stinging acid droplets. Each creature in a 15-foot cube originating from you must make a Constitution saving throw. On a failed save, a creature takes 2d4 acid damage and is blinded until the end of your next turn. On a successful save, the creature takes half as much damage and isn’t blinded. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the damage increases by 1d4 for each slot level above 1st."
)
alarm = TechPowers(
    name = "Alarm",
    level = 1,
    casting_period = "1 minute",
    range = "30 feet",
    duration = "8 hours",
    concentration = "-",
    description = "You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the power ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the power, you can designate creatures that won’t set off the alarm. You also choose whether the alarm is mental or audible. A silent alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet."
)
analyze = TechPowers(
    name = "Analyze",
    level = 1,
    casting_period = "1 minute",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    description = "You choose one object that you must touch throughout the casting of the power. If it is an enhanced or modified item, you learn its properties and how to use them, whether it requires attunement to use, and how many charges it has, if any. You learn whether any powers are affecting the item and what they are. If the item was created by a power, you learn which power created it. If you instead touch a creature throughout the casting, you learn what tech powers, if any, are currently affecting it."
)
bacta_pack = TechPowers(
    name = "Bacta Pack",
    level = 1,
    casting_period = "1 action",
    range = "60 feet",
    duration = "1 minute",
    concentration = "-",
    description = "You create a luminescent pack of bacta in any space, occupied or unoccupied, within range. The pack remains in its space until it is activated by any creature you choose. If the space you choose is occupied by a creature you have designated, it can use its reaction to immediately activate the pack; otherwise, a creature within 5 feet of the pack can use a bonus action to touch it and activate it. When the pack is activated by a designated creature, that creature regains hit points equal to 1d6 + your techcasting modifier, and the pack is consumed. If the power ends before the pack has been activated, it becomes useless and disintegrates. This power has no effect on droids or constructs. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, you may either increase the healing of a single pack by 1d6 for each slot level above 1st, or create another pack in a separate space, with one additional pack for each slot level above 1st."
)
buffer = TechPowers(
    name = "Buffer",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "1 hour",
    concentration = "-",
    description = "You gain 1d4 + 4 temporary hit points for the duration. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, you gain 5 additional temporary hit points for each slot level above 1st."
)
condense_vaporize = TechPowers(
    name = "Condense/Vaporize",
    level = 1,
    casting_period = "1 action",
    range = "30 feet",
    duration = "Instantaneou",
    concentration = "-",
    description = "In an open container, you can create up to 10 gallons of drinkable water. You may also produce a rain that falls within a 30-foot cube and extinguishes open-air flames. You can destroy the same amount of water in an open container, or destroy a 30-foot cube of fog. Overcharge Tech When you cast this power using a tech slot of 2nd level or higher, the amount of water you can create increases by 10 gallons, or the size of the cube increases by 5 feet, for each slot level above 1st."
)
copy = TechPowers(
    name = "Copy",
    level = 1,
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    description = "This power creates a perfect duplicate of any written, drawn, or digital visual, audio or text-based data that you touch onto a datapad or datacard you supply. You can copy up to 10 pages of text or 10 minutes of visual or audio data with one casting of this power. Enhanced documents, such as datacrons, blueprints, or encrypted documents, can’t be copied with this power."
)
countermeasures = TechPowers(
    name = "Countermeasures",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "10 minutes",
    concentration = "-",
    description = "For the duration, you gain the following benefits: You are immune to the homing rockets tech power, You and objects you are wearing or carrying cannot be detected by tech powers that reveal your location, such as scan area or frequency scan, unless the caster makes a successful Intelligence saving throw, Creatures have disadvantage on Wisdom (Survival) checks to track you."
)
cryogenic_blast = TechPowers(
    name = "Cryogenic Blast",
    level = 1,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You release a shard of cryogenic energy at one creature within range. Make a ranged tech attack against the target. On a hit, the target takes 1d10 kinetic damage. Hit or miss, the shard then explodes. The target and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 2d6 cold damage. Overcharge Tech. When you cast this power using a tech slot of 2nd level or higher, the cold damage increases by 1d6 for each slot level above 1st."
)
cryogenic_wave = TechPowers(
    name = "Cryogenic Wave",
    level = 1,
    casting_period = "1 action",
    range = "Self (15-foot cone)",
    duration = "Instantaneous",
    concentration = "-",
    description = "A wave of cold energy spreads out from you. Each creature in a 15-foot cone must make a Constitution saving throw. On a failed save, a creature takes 2d6 cold damage and gains 1 slowed level until the end of its next turn. On a success, it takes half as much damage, and suffers no additional effect. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st. At 3rd level or above, a creature gains 2 slowed levels on a failed save. At 5th level or above, a creature gains 3 slowed levels on a failed save. At 7th level or above, a creature gains 4 slowed levels on a failed save."
)
decryption_program = TechPowers(
    name = "Decryption Program",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "Up to 1 hour",
    concentration = "Concentration",
    description = "You gain insight into an encrypted message you are holding when you cast this power, granting you advantage on ability checks you make to decipher the document."
)
detect_enhancement = TechPowers(
    name = "Detect Enhancement",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "Up to 10 minutes",
    concentration = "Concentration",
    description = "For the duration, you sense the presence of any enhancements within 30 feet of you. If you sense an enhancement in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears an enhancement. The power is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."
)
energy_shield = TechPowers(
    name = "Energy Shield",
    level = 1,
    casting_period = "1 reaction, which you take when you are hit by an attack",
    range = "Self",
    duration = "1 round",
    concentration = "-",
    description = "You quickly create an energy shield. Until the start of your next turn, you have a +5 bonus to AC. This includes the triggering attack."
)
expeditious_retreat = TechPowers(
    name = "Expeditious Retreat",
    level = 1,
    casting_period = "1 bouns action",
    range = "Self",
    duration = "Up to 10 minutes",
    concentration = "Concentration",
    description = "This power gives you a burst of adrenaline that allows you to move at an incredible pace. When you cast this power, and then as a bonus action on each of your turns until the power ends, you can take the Dash action."
)
flame_sweep = TechPowers(
    name = "Flame Sweep",
    level = 1,
    casting_period = "1 action",
    range = "Self (15-foot cone)",
    duration = "Instantaneous",
    concentration = "-",
    description = "A thin sheet of flames shoots forth from you. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one. The fire ignites any flammable objects in the area that aren’t being worn or carried. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."
)
flash = TechPowers(
    name = "Flash",
    level = 1,
    casting_period = "1 action",
    range = "90 feet",
    duration = "1 round",
    concentration = "-",
    description = "You create a massive flash of light and explosion of sound at a point within range. Roll 6d10; the total is how many hit points of creatures this power can affect. Creatures within 20 feet of the point are affected in ascending order of their current hit points (ignoring unconscious creatures). Starting with the creature that has the lowest current hit points, each creature affected by this power is blinded until the end of your next turn. Subtract each creature’s hit points from the total before moving on to the creature with the next lowest hit points. A creature’s hit points must be equal to or less than the remaining total for that creature to be affected. Overcharge Tech. When you cast this power using a tech slot of 2nd level or higher, roll an additional 2d10 for each slot level above 1st."
)
gleaming_outline = TechPowers(
    name = "Gleaming Outline",
    level = 1,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Up to 1 minute",
    concentration = "-",
    description = "Each object in a 20-foot cube within range is outlined in blue, green, or violet light (your choice). Any creature in the area when the power is cast is also outlined in light if it fails a Dexterity saving throw. For the duration, objects and affected creatures shed dim light in a 10-foot radius. Any attack roll against an affected creature or object has advantage if the attacker can see it, and the affected creature or object can’t benefit from being invisible."
)
hologram = TechPowers(
    name = "Hologram",
    level = 1,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Up to 10 minutes",
    concentration = "COncentration",
    description = "You create an image that is no larger than a 15-foot cube. The image appears at a spot within range and lasts for the duration. The image is purely visual. If anything passes through it, it is revealed to be an illusion. You can use your action to cause the image to move to any spot within range. As the image changes location, you can alter its appearance so that its movements appear natural for the image. A creature that uses its action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your tech save DC. If a creature discerns the illusion for what it is, the creature can see through the image."
)
holographic_disguise = TechPowers(
    name = "Holographic Disguise",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "1 hour",
    concentration = "-",
    description = "Until the power ends or you use an action to dismiss it, you can disguise yourself through the use of a hologram emitter. You can appear to be shorter or taller by about a foot and change the appearance of your body weight, but you cannot change the basic structure of your body. The hologram can include your clothes, armor, weapons, and other belongings on your person. The illusion is only visual, so any sort of physical contact will only interact with the real size and shape of you. A creature can use its action to make an Intelligence (Investigation) check against your tech save DC, seeing through the hologram on a success."
)
homing_rockets = TechPowers(
    name = "Homing Rockets",
    level = 1,
    casting_period = "1 action",
    range = "120 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You lock on to one or more targets within range and expel a series of three small explosives. Each explosive hits a creature of your choice that you can see within range. An explosive deals 1d4 + 1 fire damage to its target. The explosives all strike simultaneously, and you can direct them to hit one creature or several. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the power creates one more explosive for each slot level above 1st."
)
ionic_bond = TechPowers(
    name = "Ionic Bond",
    level = 1,
    casting_period = "1 bouns action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    description = "A beam of ion energy lances out toward a creature within range, forming a sustained line between you and the target. Make a ranged tech attack against that creature. On a hit, the target takes 1d8 ion damage, and on each of your turns for the duration, you can use a bonus action to deal 1d8 ion damage to the target automatically. The power ends if you use your bonus action to do anything else. The power also ends if the target is ever outside the power’s range or if it has total cover from you. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the initial damage increases by 1d8 for each slot level above 1st."
)
kolto_pack = TechPowers(
    name = "Kolto Pack",
    level = 1,
    casting_period = "1 bonus action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "A creature of your choice that you can see within range regains hit points equal to 1d4 + your techcasting ability modifier. This power has no effect on droids or constructs. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the healing increases by 1d4 for each slot level above 1st."
)
oil_slick = TechPowers(
    name = "Oil Slick",
    level = 1,
    casting_period = "1 action",
    range = "60 feet",
    duration = "1 minute",
    concentration = "-",
    description = "You cover the ground in a 10-foot square within range in oil. For the duration, it is difficult terrain. When the oil appears, each creature standing in its area must succeed on a Dexterity saving throw or fall prone. A creature that enters the area or ends its turn there must also succeed on a Dexterity saving throw. The oil is flammable. Any 5 foot square of the oil exposed to fire burns away in one round. Each creature who enters the fire or starts it turn there must make a Dexterity saving throw, taking 3d6 fire damage on a failed save, or half as much on a successful one. The fire ignites any flammable objects in the area that aren’t being worn or carried."
)
overload = TechPowers(
    name = "Overload",
    level = 1,
    casting_period = "1 action",
    range = "Self (15-foot cube)",
    duration = "Instantaneous",
    concentration = "-",
    description = "You expel a burst of power. Each creature in a 15-foot cube originating from you must make a Dexterity saving throw. On a failed save, a creature takes 2d6 ion damage and is pushed 10 feet away from you. On a successful save, the creature takes half as much damage and isn’t pushed. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."
)
posion_dart = TechPowers(
    name = "Posion Dart",
    level = 1,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "Make a ranged tech attack against a creature within range. On hit, the target takes 2d8 poison damage and must make a Constitution save. On a failed save, it is also poisoned until the end of your next turn. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st."
)
preparedness = TechPowers(
    name = "Preparedness",
    level = 1,
    casting_period = "1 minute",
    range = "Touch",
    duration = "8 hours",
    concentration = "-",
    description = "You touch a willing creature. For the duration, the target can add 1d8 to its initiative rolls."
)
repair_droid = TechPowers(
    name = "Repair Droid",
    level = 1,
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    description = "A droid or construct you touch regains a number of hit points equal to 1d8 + your techcasting ability modifier. This power only effects droids and constructs. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st."
)
ring_of_fire = TechPowers(
    name = "Ring of Fire",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    description = "A wall of flames erupts out of the ground in a ring around you with a radius of 15 feet and a height of 10 feet. Creatures who start their turn in the ring of fire or pass through it on their turn take 1d6 fire damage. Creatures within the ring of fire who willingly try to move through the fire to escape must succeed on a Wisdom saving throw to do so. Creatures who are immune to fear or fire automatically succeed on this saving throw. Overcharge Tech. When you cast this power using a tech slot of 2nd level or higher, the damage of the ring of fire increases by 1d6 for each slot level above 1st."
)
smoke_cloud = TechPowers(
    name = "Smoke Cloud",
    level = 1,
    casting_period = "1 action",
    range = "120 feet",
    duration = "Up to 1 hour",
    concentration = "Concentration",
    description = "You cause thick smoke to erupt from a point within range, filling a 20-foot-radius sphere. The sphere spreads around corners, and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the radius of the smoke cloud increases by 20 feet for each slot level above 1st."
)
sonic_fists = TechPowers(
    name = "Sonic Fists",
    level = 1,
    casting_period = "1 bonus action",
    range = "Self",
    duration = "1 minute",
    concentration = "-",
    description = "You enhance your fists or analogous appendages with sonic energy. For the duration, you have a natural weapon which deals 1d10 sonic damage on a hit. Every time you hit a creature that is no more than one size larger than you with a melee attack with this weapon, you can push it 5 feet away from you."
)
spot_the_weakness = TechPowers(
    name = "Spot the Weakness",
    level = 1,
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    description = "Up to three creatures of your choice that you can see within range must make Dexterity saving throws. The first time each turn a target that fails this saving throw makes an attack roll or a saving throw before the power ends, the target must roll a d4 and subtract the number rolled from the attack roll or saving throw. Overcharge Tech: When you cast this power with a tech slot of 3rd level or higher, you can target one additional creature for every two slot levels above 1st. When you cast this power at 3rd, 6th, or 9th level, the die increases to d6, d8, and d10, respectively."
)
stack_the_deck = TechPowers(
    name = "Stack the Deck",
    level = 1,
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    description = "You boost up to three creatures of your choice within range. Whenever a target makes an attack roll or a saving throw before the power ends, the target can roll a d4 and add the number rolled to the attack roll or saving throw. Overcharge Tech: When you cast this power with a tech slot of 3rd level or higher, you can target one additional creature for every two slot levels above 1st. When you cast this power at 3rd, 6th, or 9th level, the die increases to d6, d8, and d10, respectively."
)
tactical_barrier = TechPowers(
    name = "Tactical Barrier",
    level = 1,
    casting_period = "1 bonus action",
    range = "60 feet",
    duration = "Up to 10 minutes",
    concentration = "Concentration",
    description = "A shimmering field appears and surrounds a creature of your choice within range, granting it a +2 bonus to AC for the duration."
)
target_lock = TechPowers(
    name = "Target Lock",
    level = 1,
    casting_period = "1 bonus action",
    range = "90 feet",
    duration = "Up to 1 hour",
    concentration = "Concentration",
    description = "You choose a creature you can see within range and mark it as your quarry. Until the power ends, you deal an extra 1d6 damage to the target whenever you hit it with a weapon attack, the target gains no benefit from one-quarter, half, and three-quarters cover against you, and if the target is invisible, you can see it as if it were visible. If the target drops to 0 hit points before this power ends, you can use a bonus action on a subsequent turn of yours to mark a new creature. Overcharge Tech: When you cast this power using a tech slot of 3rd or 4th level, you can maintain your concentration on the power for up to 8 hours. When you use a tech slot of 5th level or higher, you can maintain your concentration on the power for up to 24 hours."
)
toxin_scan = TechPowers(
    name = "Toxin Scan",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "Up to 10 minutes",
    concentration = "Concentration",
    description = "For the duration, you can see the presence and location of poisons and diseases within 30 feet of you. You also identify the kind of poison or disease in each case."
)
tracer_bolt = TechPowers(
    name = "Tracer bolt",
    level = 1,
    casting_period = "1 action",
    range = "120 feet",
    duration = "1 round",
    concentration = "-",
    description = "A flash of light streaks toward a creature of your choice within range. Make a ranged tech attack against the target. On a hit, the target takes 4d6 energy damage, and the next attack roll made against this target before the end of your next turn has advantage. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."
)
tranquilizer = TechPowers(
    name = "Tranquilizer",
    level = 1,
    casting_period = "1 action",
    range = "90 feet",
    duration = "1 minute",
    concentration = "-",
    description = "You emit a tranquilizing dart that knocks a creature unconscious. Roll 5d8; if the creature’s remaining hit points are less than the total, the creature falls unconscious until the power ends, the sleeper takes damage, or someone uses an action to shake or slap the sleeper awake. This power has no effect on droids or constructs. Overcharge Tech. When you cast this power using a tech slot of 2nd level or higher, you can target an additional creature for each slot level above 1st. For each target, roll 5d8 separately."
)
translation_program = TechPowers(
    name = "Translation Program",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "1 hour",
    concentration = "-",
    description = "For the duration, you understand the literal meaning of any spoken registered language that you hear, as long as you have your tech focus. You also understand any written language that you see, but you must be within reach of the surface on which the words are written. It takes about 1 minute to read one page of text. This power doesn’t decode secret messages in a text, nor does it interpret a glyph, such as an ancient Sith rune, that isn’t part of a written language."
)
voltaic_shielding = TechPowers(
    name = "Voltaic Shielding",
    level = 1,
    casting_period = "1 action",
    range = "Self",
    duration = "1 hour",
    concentration = "-",
    description = "A protective barrier surrounds you, manifesting as crackling lightning that covers you and your gear. You gain 5 temporary hit points for the duration. If a creature hits you with a melee attack while you have these hit points, the creature takes 5 lightning damage. Overcharge Tech: When you cast this power using a tech slot of 2nd level or higher, both the temporary hit points and the lightning damage increase by 5 for each slot."
)

db.session.add_all([absorb_energy, acid_wind, alarm, analyze, bacta_pack, buffer, condense_vaporize, copy, countermeasures, cryogenic_blast, cryogenic_wave, decryption_program, detect_enhancement, energy_shield, expeditious_retreat, flame_sweep, flash, gleaming_outline, hologram, holographic_disguise, homing_rockets, ionic_bond, kolto_pack, oil_slick, overload, posion_dart, preparedness, repair_droid, ring_of_fire, smoke_cloud, sonic_fists, spot_the_weakness, stack_the_deck, tactical_barrier, target_lock, toxin_scan, tracer_bolt, tranquilizer, translation_program, voltaic_shielding])
db.session.commit()
#--------------------------------------------------------------

#-----------------Force Powers---------------------------------
#? At-Will
affect_mind = ForcePowers(
    name = "Affect Mind", 
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "Choose a target within range that isn’t hostile toward you. The target must make a Wisdom saving throw. On a failed save, you have advantage on all Charisma checks directed at that target. On a successful save, the creature does not realize that you tried to use the Force to influence its mood, but it becomes immune to this power for one day. This power has no effect on droids or constructs."
)
battle_insight = ForcePowers(
    name = "Battle Insight",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 round",
    concentration = "Concentration",
    prerequisite = "-",
    description = "You center your focus on a target within range. Through the Force, you gain a brief insight into the target’s defenses. On your next turn, you gain advantage on your first attack roll against the target, provided that this power hasn’t ended. This power benefits additional attacks at higher levels: two attacks at 5th level, three attacks at 11th level, and four attacks at 17th level."
)
burst = ForcePowers(
    name = "Burst",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self (5-foot sphere)",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You cause the earth to burst from beneath your feet. Each creature within range, other than you, must succeed on a Dexterity saving throw or take 1d8 kinetic damage. This power’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
)
denounce = ForcePowers(
    name = "Denounce",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "A target of your choice within range must make a Charisma saving throw. On a failed save, when the target makes their next attack roll or saving throw they must roll a d4 and subtract the number from it. The power then ends."
)
enfeeble = ForcePowers(
    name = "Enfeeble",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "Dark energy courses from your hand at a creature within range. The target must succeed on a Wisdom saving throw. If it is missing any hit points, it takes 1d12 necrotic damage. Otherwise, it takes 1d8. The power’s damage increases by one die when you reach 5th, 11th, and 17th level."
)
feedback = ForcePowers(
    name = "Feedback",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You unleash a burst of psychic energy at a target within range. If the target can hear you (though it need not understand you), it must succeed on an Intelligence saving throw or take 1d4 psychic damage and have disadvantage on the next attack roll it makes before the end of its next turn. This power’s damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4)."
)
force_disarm = ForcePowers(
    name = "Force Disarm",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You select a weapon or object being worn or carried by a Large or smaller creature within range. The creature must make a Strength or Dexterity saving throw (the creature chooses the ability to use). If the item is being carried, this save is made with advantage. On a failed save, the item is pulled directly to you. If you have a free hand, you catch the weapon. Otherwise, it lands at your feet."
)
force_imbuement = ForcePowers(
    name = "Force Imbuement",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 bonus action",
    range = "Touch",
    duration = "1 minute",
    concentration = "-",
    prerequisite = "-",
    description = "The crystal inside of a simple lightweapon or the material of a simple vibroweapon or an improvised weapon you are holding is imbued with the power of the Force. For the duration, you can use your forcecasting ability instead of Strength for the attack and damage rolls of melee attacks using that weapon, and the weapon’s damage die becomes a d8. The weapon also becomes enhanced, if it isn’t already, and you become proficient with it, if you aren’t already. The power ends if you cast it again or if you let go of the weapon."
)
force_leap = ForcePowers(
    name = "Force Leap",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 bonus action",
    range = "Self",
    duration = "1 round",
    concentration = "-",
    prerequisite = "-",
    description = "Until the end of your next turn, you can use your forcecasting ability score instead of your Strength score when you jump, and always count as having made a running start before jumping."
)
force_pull_push = ForcePowers(
    name = "Force Pull/Push",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You gain the minor ability to move or manipulate creatures and objects with the Force. You can exert fine control on objects with your telekinetic grip, such as manipulating a simple tool, opening a door or a container, stowing or retrieving an item from an open container, or pouring the contents from a vial. Alternatively, you can push or pull a creature or object you can see. You use the Force to move a Medium or smaller creature or object not being worn or carried within range. The target must make a Strength saving throw. An object automatically fails this saving throw. On a failed save, the creature or object moves a number of feet in a direction of your choice based on its size. A Tiny creature or object can be moved up to 20 feet, a Small creature or object can be moved up to 10 feet, and a Medium creature or object can be moved up to 5 feet. If at the end of this movement the creature or object strikes another creature or object, it must make a Dexterity saving throw. An object automatically fails this saving throw. On a failed save, they both take 1d4 kinetic damage. This power improves when you reach higher levels. At 5th level, you can move a Tiny creature or object up to 30 feet, a Small creature or object up to 20 feet, a Medium creature or object up to 10 feet, and the power’s damage increases to 2d4 kinetic damage. At 11th level, you can move a Small creature or object up to 30 feet, a Medium creature up to 20 feet, and the power’s damage increases to 3d4 kinetic damage. At 17th level, you can move a Medium creature to up 30 feet, and the power’s damage increases to 4d4 kinetic damage."
)
force_shut = ForcePowers(
    name = "Force Shut",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You use the Force to thrust a creature you can see to the ground. The target must make a Strength saving throw. On a failed save, a creature takes 1d4 kinetic damage and falls prone. This power’s damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4)."
)
force_technique = ForcePowers(
    name = "Force Technique",
    level = 0,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    prerequisite = "-",
    description = "You imbue your weapon with the purifying light of the Force. As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and it becomes wreathed in a glowing barrier of force energy until the start of your next turn. If the target willingly moves before then, it immediately takes 1d8 force damage, and the power ends. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 force damage to the target, and the damage the target takes for moving increases to 2d8. Both damage rolls increase by 1d8 at 11th level and 17th level."
)
force_whisper = ForcePowers(
    name = "Force Whisper",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "120 feet",
    duration = "1 round",
    concentration = "-",
    prerequisite = "-",
    description = "You use the Force to carry a message in your voice to another creature within range. The target (and only the target) hears the message and can reply in a whisper that only you can hear. You can cast this power through solid objects if you are familiar with the target and know it is beyond the barrier. An enhanced silence effect, 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the power. The power doesn’t have to follow a straight line and can travel freely around corners or through openings."
)
give_life = ForcePowers(
    name = "Give Life",
    level = 0,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "Placing your hand on another creature you can transfer your own life force to them. You spend and roll one of your hit dice and the creature regains that many hit points. This power has no effect on droids or constructs."
)
guidance = ForcePowers(
    name = "Guidance",
    level = 0,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Touch",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "You touch one willing creature. Once before the power ends, the target can roll a d4 and add the number rolled to one ability check of its choice. It can roll the die before or after making the ability check. The power then ends. This power’s die increases at higher levels: to a d6 at 5th level, a d8 at 11th level, and a d10 at 17th level."
)
lightning_charge = ForcePowers(
    name = "Lightning Charge",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "Varies",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You imbue your weapon with debilitating force lightning. As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and the lightning leaps from the target to a different creature of your choice that you can see within 5 feet of it. The second creature takes lightning damage equal to your forcecasting ability modifier.  This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 lightning damage to the target, and the lightning damage to the second creature increases to 1d8 + your forcecasting ability modifier. Both damage rolls increase by 1d8 at 11th level and 17th level."
)
mind_trick = ForcePowers(
    name = "Mind Trick",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "Choose a target within range that isn’t hostile toward you. The target must make a Wisdom saving throw. On a failed save, the target has disadvantage on Wisdom (Perception) and Intelligence (Investigation) checks. On a successful save, the creature realizes that you tried to use the Force to influence its awareness and becomes hostile toward you. A creature prone to violence might attack you. Another creature might seek retribution in other ways (at the GM’s discretion), depending on the nature of your interaction with it. This power has no effect on droids or constructs."
)
necrotic_charge = ForcePowers(
    name = "Necrotic Charge",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    prerequisite = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and you can choose to deal up to 1d8 of necrotic damage, which you suffer as well. This damage can’t be reduced or negated in any way. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 necrotic damage to the target, and you can increase the secondary damage to 2d8. Both damage rolls increase by 1d8 at 11th level and 17th level."
)
necrotic_touch = ForcePowers(
    name = "Necrotic Touch",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "Touch",
    duration = "1 round",
    concentration = "-",
    prerequisite = "-",
    description = "You attempt to drain the essence from a creature. Make a melee force attack against the target. If the attack hits, the creature takes 1d6 necrotic damage, and you gain temporary hit points equal to the damage dealt until the end of your next turn. This power’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
)
psychic_chrage = ForcePowers(
    name = "Psychic Charge",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    prerequisite = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and its mouth is covered by a violet veil until the start of your next turn. If the target willingly speaks before then, it immediately takes 1d8 psychic damage, and the power ends. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 psychic damage to the target, and the damage the target takes for speaking increases to 2d8. Both damage rolls increase by 1d8 at 11th level and 17th level."
)
rebuke = ForcePowers(
    name = "Rebuke",
    level = 0,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You strike a creature with the righteous fury of the Force. Make a melee force attack against the target, if the attack hits, the target takes force damage depending on its alignment: a dark-aligned creature takes 1d12 force damage, a balanced creature takes 1d10 force damage, and a light-aligned creature takes 1d8 force damage The power’s damage increases by one die when you reach 5th, 11th, and 17th level."
)
resistance = ForcePowers(
    name = "Resistance",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Touch",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "You touch one willing creature. Once before the power ends, the target can roll a d4 and add the number rolled to one saving throw of its choice. It can roll the die before or after the saving throw. The power then ends. This power’s die increases at higher levels: to a d6 at 5th level, a d8 at 11th level, and a d10 at 17th level."
)
saber_throw = ForcePowers(
    name = "Saber Throw",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "As a part of the action used to cast this power, you must make a ranged force attack with a lightweapon or vibroweapon against one target within the power’s range, otherwise the power fails. On a hit, the target takes 1d8 damage of the same type as the weapon’s damage. The weapon then immediately returns to your hand. This power can hit multiple targets when you reach higher levels: two targets at 5th level, three targets at 11th level, and four targets at 17th level. Each target must be within 30 feet of the previous target, you must make a separate attack roll for each target, and the last target must be no further than 30 feet away from you. You can not hit the same target twice in succession."
)
saber_ward = ForcePowers(
    name = "Saber Ward",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "ou take a defensive stance. Until the end of your next turn, you have resistance against kinetic, energy, and ion damage dealt by weapons."
)
seethe = ForcePowers(
    name = "Seethe",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "Self",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You seethe with anger, letting the dark side of the Force flow through and empower you. As part of the action to cast this power, you spend one of your Hit Dice to recover hit points."
)
shock = ForcePowers(
    name = "Shock",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "120 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You hurl a bolt of lightning at a target within range, making a ranged force attack. On a hit, the target takes 1d10 lightning damage. The lightning ignites flammable objects in the area that aren’t being worn or carried. This power’s damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10)."
)
slow = ForcePowers(
    name = "Slow",
    level = 0,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "15 feet",
    duration = "1 hour",
    concentration = "-",
    prerequisite = "-",
    description = "A hostile creature of your choice must make a Constitution saving throw. On a failed save, the target gains 1 slowed level until the power ends. At the end of each of the creature’s turns, it repeats this saving throw, ending the effect on a success. This power can affect multiple targets when you reach higher levels: two targets at 5th level, three targets at 11th level, and four targets at 17th level."
)
sonic_charge = ForcePowers(
    name = "Sonic Charge",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Varies",
    duration = "1 round",
    concentration = "-",
    prerequisite = "-",
    description = "As part of the action used to cast this power, you must make a melee weapon attack against one creature within your reach, otherwise the power fails. On a hit, the target suffers the attack’s normal effects, and you begin to emanate a disturbing hum until the start of your next turn. If a hostile creature ends its turn within 5 feet of you, it takes 1d4 sonic damage. This power’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 sonic damage to the target, and the secondary damage increases by 1d4. Both damage rolls increase by 1d8 and 1d4, respectively, at 11th level and 17th level."
)
sound_trick = ForcePowers(
    name = "Sound Trick",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "30 feet",
    duration = "1 minute",
    concentration = "-",
    prerequisite = "-",
    description = "You use the Force to produce an effect within range. You create one of the following special effects within range: Your voice booms up to three times as loud as normal, and you can alter its tone, for 1 minute, You cause harmless tremors in the ground for 1 minute, You create an instantaneous sound that originates from a point of your choice within range, such as a rumble of thunder, the cry of a bird, or ominous whispers, You gain the ability to speak like another species for 1 minute, allowing you to speak in a language you know but otherwise lack the physical ability to speak, such as a Wookiee speaking Basic, You create an instantaneous, harmless sensory effect, such as falling leaves, a puff of wind, a billowing of someone’s clothes, or a flickering of unenhanced light fixtures within range. A wary creature can use its action to make an Intelligence (Investigation) check against your force save DC, discerning that the effects are illusory on a success. If you cast this power multiple times, you can have up to three of its 1-minute effects active at a time, and you can dismiss such an effect as an action."
)
spare_the_dying = ForcePowers(
    name = "Spare the Dying",
    level = 0,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You touch a living creature that has 0 hit points. The creature becomes stable. This power has no effect on droids or constructs."
)
spirit_blade = ForcePowers(
    name = "Spirit Blade",
    level = 0,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You conjure a blade of spirit energy and attempt to strike one creature. Make a melee force attack against the target. If the attack hits, the creature takes 1d10 necrotic damage. This power can make multiple attacks at higher levels: two attacks at 5th level, three attacks at 11th level, and four attacks at 17th level. Each attack can target the same creature or different ones. Make a separate attack roll for each target."
)
turbulance = ForcePowers(
    name = "Turbulance",
    level = 0,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "Choose one creature, or choose two creatures that are within 5 feet of each other, within range. A target must succeed on a Dexterity saving throw or take 1d6 force damage. This power’s damage increases by 1d6 when you reach 5th, 11th, and 17th level."
)
db.session.add_all([affect_mind, battle_insight, burst, denounce, enfeeble, feedback, force_disarm, force_imbuement, force_leap, force_pull_push, force_shut, force_technique, force_whisper, give_life, guidance, lightning_charge, mind_trick, necrotic_charge, necrotic_touch, psychic_chrage, rebuke, resistance, saber_throw, saber_ward, seethe, shock, slow, sonic_charge, sound_trick, spare_the_dying, spirit_blade, turbulance])
db.session.commit()

#? 1st level
armor_of_abeloth = ForcePowers(
    name = "Armor of Abeloth", 
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "Self",
    duration = "1 hour",
    concentration = "-",
    prerequisite = "-",
    description = "A protective force surrounds you, manifesting as shimmering light that covers you and your gear. You gain 5 temporary hit points for the duration. If a creature hits you with a melee attack while you have these hit points, the creature takes 5 psychic damage. Force Potency. When you cast this power using a force slot of 2nd level or higher, both the temporary hit points and the psychic damage increase by 5 for each slot."
)
battle_precognition = ForcePowers(
    name = "Battle Precognition",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "8 hours",
    concentration = "-",
    prerequisite = "-",
    description = "Your attunement to the Force warns you when you are about to enter danger. Until the power ends, your base AC becomes 13 + your Dexterity modifier. This power has no effect if you are wearing armor."
)
beast_trick = ForcePowers(
    name = "Beast Trick",
    level = 1,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "30 feet",
    duration = "24 hours",
    concentration = "-",
    prerequisite = "-",
    description = "This power lets you distract a beast. Choose a beast that you can see within range. If the beast’s Intelligence is 4 or higher, the power fails. Otherwise, the beast must succeed on a Wisdom saving throw or be charmed by you for the power’s duration. If you or one of your companions harms the target, the power ends. Force Potency: When you cast this power using a force slot of 2nd level or higher, you can affect one additional beast for each slot level above 1st."
)
breath_control = ForcePowers(
    name = "Breath Control",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "10 minutes",
    concentration = "-",
    prerequisite = "-",
    description = "You are able to slow your metabolism in such a way that you can stop breathing and resist the effect of toxins in your body. If you are poisoned, you neutralize the poison. If more than one poison afflicts you, you neutralize one poison that you know is present, or you neutralize one at random. For the duration, you have advantage on saving throws against being poisoned, resistance to poison damage, and you no longer need to breathe."
)
burst_of_speed = ForcePowers(
    name = "Burst of Speed",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Touch",
    duration = "1 hour",
    concentration = "-",
    prerequisite = "-",
    description = "You touch a creature. The target’s speed increases by 10 feet until the power ends. Force Potency: When you cast this power using a force slot of 2nd level or higher, you can target one additional creature for each slot level above 1st."
)
cloud_mind = ForcePowers(
    name = "Cloud Mind",
    level = 1,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "90 feet",
    duration = "1 minute",
    concentration = "-",
    prerequisite = "-",
    description = "Roll 5d8; the total is how many hit points of creatures this power can affect. Creatures within 20 feet of a point you choose are affected in order of their current hit points. Starting with the creature that has the lowest current hit points, each creature affected by this power falls unconscious. If the power ends, the sleeper takes damage, or someone uses an action wake the sleeper, they will be awoken Subtract each creature’s hit points from the total before moving on to the creature with the next lowest hit points. A creature’s hit points must be equal to or less than the remaining total for that creature to be affected. This power has no effect on droids or constructs. Force Potency: When you cast this power using a force slot of 2nd level or higher, you can roll an additional 2d8 for each slot level above 1st."
)
comprehend_speech = ForcePowers(
    name = "Comprehend Speech",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "1 hour",
    concentration = "-",
    prerequisite = "-",
    description = "For the duration, you understand the literal meaning of any spoken language that you hear."
)
curse = ForcePowers(
    name = "Cirse",
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "Denounce",
    description = "Up to three creatures of your choice that you can see within range must make Charisma saving throws. The first time each turn a target that fails this saving throw makes an attack roll or a saving throw before the power ends, the target must roll a d4 and subtract the number rolled from the attack roll or saving throw. Force Potency. When you cast this power with a force slot of 3rd level or higher, you can target one additional creature for every two slot levels above 1st. When you cast this power at 3rd, 6th, or 9th level, the die increases to d6, d8, and d10, respectively."
)
dark_side_tendrils = ForcePowers(
    name = "Dark Side Tendrils",
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "Self (10-foot radius)",
    duration = "Instatntaneous",
    concentration = "-",
    prerequisite = "-",
    description = "Tendrils of dark energy erupt from you and batter all creatures within 10 feet of you. Each creature in that area must make a Strength saving throw. On a failed save, a target takes 2d6 necrotic damage and can’t take reactions until its next turn. On a successful save, the creature takes half damage, but suffers no other effect. Force Potency. When you cast this power using a power slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."
)
dun_moch = ForcePowers(
    name = "Dun Moch",
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 bonus action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "You attempt to manipulate a creature into fighting you. One creature that you can see within range must make a Wisdom saving throw. On a failed save, the creature is drawn to you, compelled by your demands. For the duration, it has disadvantage on attack rolls against creatures other than you, and must make a Wisdom saving throw each time it attempts to move to a space that is more than 30 feet away from you; if it succeeds on this saving throw, this power doesn’t restrict the target’s movement for that turn. The power ends if you attack any other creature, if you cast a power that targets a hostile creature other than the target, if a creature friendly to you damages the target or casts a harmful power on it, or if you end your turn more than 30 feet away from the target. This power has no effect on droids or constructs."
)
fear = ForcePowers(
    name = "Fear",
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "You awaken the sense of mortality in one creature you can see within range. The target must succeed on a Wisdom saving throw or become frightened for the duration. A target with 25 hit points or fewer makes the saving throw with disadvantage. A frightened creature can repeat this save at the end of each of its turns, ending this effect on a success. This power has no effect on constructs or droids."
)
force_blinding = ForcePowers(
    name = "Force Blinding",
    level = 1,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Self (15-foot cone)",
    duration = "1 round",
    concentration = "-",
    prerequisite = "-",
    description = "You use the Force to emit a blinding flash of light from your hand. Roll 6d10, the total is how many hit points of creatures this power can effect. Creatures in a 15-foot cone originating from you are affected in ascending order of their current hit points (ignoring unconscious creatures and creatures that can’t see). Starting with the creature that has the lowest current hit points, each creature affected by this power is blinded until the power ends. Subtract each creature’s hit points from the total before moving on to the creature with the next lowest hit points. A creature’s hit points must be equal to or less than the remaining total for the creature to be affected. Force Potency: When you cast this power using a force slot of 2nd level or higher, roll an additional 2d10 for each slot level above 1st."
)
force_body = ForcePowers(
    name = "Force Body",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "1 hour",
    concentration = "-",
    prerequisite = "-",
    description = "This power enables you to use your health to fuel your force powers. For the duration, when you cast a force power, half the cost is paid by your force points (rounded up) and half the cost is paid by your hit points (rounded down). Additionally, your maximum hit points are decreased by this amount while the power is active. You may end this effect at any time. If you cast a force power that would reduce your hit points to 0, the power automatically fails and this effect ends."
)
force_focus = ForcePowers(
    name = "Force Focus",
    level = 1,
    force_alignment = "Light",
    casting_period = "1 bonus action",
    range = "Self",
    duration = "Up to 1 minute",
    concentration = "-",
    prerequisite = "Force Technique",
    description = "You let the Force guide you, empowering your strikes. Until the power ends, your weapon attacks deal an extra 1d4 force damage on a hit."
)
force_jump = ForcePowers(
    name = "Force Jump",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "Force Leap",
    description = "Using the Force to augment the strength in your legs, you leap up to 30 feet to an unoccupied space you can see. Force Potency: When you cast this power using a force slot of 2nd level or higher, your jump distance increases by 5 feet for each slot level above 1st."
)
force_mask = ForcePowers(
    name = "Force Mask",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "1 hour",
    concentration = "-",
    prerequisite = "Mind Trick",
    description = "Until the power ends or you use an action to dismiss it, you can disguise yourself through use of the Force in many ways. You can appear to be shorter or taller by about a foot and change the appearance of your body and weight, but you cannot change the basic structure of your body. This effect can include your clothes, weapons, and other belongings on your person. This effect is only visual, so any sort of physical contact will only interact with the real size and shape of you. A creature that uses its action to examine you can identify this effect with a successful Intelligence (Investigation) check against your force save DC. This power has no effect on droids or constructs."
)
force_propel = ForcePowers(
    name = "Force Propel",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "Force Push/Pull",
    description = "Choose one or more creatures or objects not being worn or carried within 60 feet that weigh up to a combined total of 15 pounds. The creatures or objects immediately move 60 feet in a direction of your choice. If the creatures or objects end this movement in the air, they immediately fall to the ground. If the creatures or objects collide with any one target during its travel, both the creatures or objects and the target take 3d8 kinetic damage. If the target is a creature, it must make a Dexterity saving throw. On a failed save, it takes 3d8 kinetic damage, or half as much on a successful one. Force Potency: When you cast this power using a force slot of 2nd level or higher, the maximum weight increases by 15 pounds and the damage increases by 1d8 for each slot level above 1st."
)
heal = ForcePowers(
    name = "Heal",
    level = 1,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "A creature you touch regains a number of hit points equal to 1d8 + your forcecasting ability modifier. This power has no effect on droids or constructs. Force Potency: When you cast this power using a force slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st."
)
heroism = ForcePowers(
    name = "Heroism",
    level = 1,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Touch",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "A willing creature you touch is imbued with bravery. Until the power ends, the creature is immune to being frightened and gains temporary hit points equal to your forcecasting ability modifier at the start of each of its turns. When the power ends, the target loses any remaining temporary hit points from this power. This power has no effect on droids or constructs. Force Potency: When you cast this power using a force slot of 2nd level or higher, you can target one additional creature for each slot level above 1st."
)
hex = ForcePowers(
    name = "Hex",
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 bonus action",
    range = "90 feet",
    duration = "Up to 1 hour",
    concentration = "Concentration",
    prerequisite = "-",
    description = "You curse an opponent within range. Until the power ends, you deal an extra 1d6 necrotic damage to the target whenever you hit it with an attack. Also, choose one ability when you cast the power. The target has disadvantage on ability checks made with the chosen ability. If the target drops to 0 hit points before this power ends, you can use a bonus action on a subsequent turn of yours to curse a new creature. Force Potency: When you cast this power using a force slot of 3rd or 4th level, you can maintain your concentration on the power for up to 8 hours. When you use a force slot of 5th level or higher, you can maintain your concentration on the power for up to 24 hours."
)
improved_feedback = ForcePowers(
    name = "Improved Feedback",
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "Feedback",
    description = "You unleash a blast of psychic energy at a target within range. If the target can hear you (though it need not understand you), it must succeed on an Intelligence saving throw. On a failed save, it takes 3d6 psychic damage and must immediately use its reaction, if available, to move as far as its speed allows away from you. The creature doesn’t move into obviously dangerous ground, such as a fire or a pit. On a successful save, the target takes half as much damage and doesn’t have to move away. A deafened creature automatically succeeds on the save. Force Potency: When you cast this power using a force slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."
)
malacia = ForcePowers(
    name = "Malacia",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "Mind Trick",
    description = "A creature of your choice that you can see within range is overcome with a sense of dizziness and nausea, as you disturb its equilibrium with the Force. The creature must make a Wisdom saving throw or fall prone, becoming incapacitated and unable to stand up for the duration. At the end of each of its turns, and each time it takes damage, the target can make another Wisdom saving throw. The target has advantage on the saving throw if it’s triggered by damage. On a success, the power ends. This power has no effect on droids or constructs."
)
phasestrike = ForcePowers(
    name = "Phasestrike",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 bonus action",
    range = "Self",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "-",
    description = "Until the power ends, your movement doesn’t provoke opportunity attacks. Once before the power ends, you can give yourself advantage on one weapon attack roll on your turn. That attack deals an extra 1d8 force damage on a hit. Whether you hit or miss, your walking speed increases by 30 feet until the end of that turn."
)
project = ForcePowers(
    name = "Project",
    level = 1,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "120 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You lift three piles of debris or small objects from the ground and hurl them. Each pile hits a creature of your choice that you can see within range. The pile deals 1d4+1 force damage to its target. The piles all strike simultaneously and you can direct them to hit one creature or several. Force Potency. When you cast this power using a force slot of 2nd level or higher, you lift and throw an additional pile of debris for each slot level above 1st."
)
sanctuary = ForcePowers(
    name = "Sanctuary",
    level = 1,
    force_alignment = "Light",
    casting_period = "1 bonus action",
    range = "30 feet",
    duration = "1 minute",
    concentration = "-",
    prerequisite = "-",
    description = "Until the power ends, any creature who targets the warded creature with an attack, a harmful power, or a hostile action must first make a Wisdom saving throw. On a failed save, the creature must choose a new target or lose the attack or power. This power doesn’t protect the warded creature from area effects. If the warded creature makes an attack, casts a power that affects an enemy creature, or takes a hostile action this power ends."
)
sense_emotion = ForcePowers(
    name = "Sense Emotion",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "Up to 10 minutes",
    concentration = "Concentration",
    prerequisite = "-",
    description = "You attune your senses to pick up the emotions of others for the duration. When you cast the power, and as your action on each turn until the power ends, you can focus your senses on one humanoid you can see within 30 feet of you. You instantly learn the target’s prevailing emotion, whether it’s love, anger, pain, fear, calm, or something else, and you have advantage on Wisdom (Insight) checks against the target. If the target isn’t actually humanoid or it is immune to being charmed, you sense that it is calm."
)
sense_force = ForcePowers(
    name = "Sense Force",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "Up to 10 minutes",
    concentration = "Concentration",
    prerequisite = "-",
    description = "For the duration, you sense the use of the Force, or its presence in an inanimate object within 30 feet of you. If you sense the Force in this way, you can use your action to determine the direction from which it originates and, if it’s in line of sight, you see a faint aura around the person or object from which the Force emanates. Force Potency: When you cast this power using a 3rd-level force slot, the range increases to 60 feet. When you use a 5th-level force slot, the range increases to 500 feet. When you use a 7th-level force slot, the range increases to 1 mile. When you use a 9th-level force slot, the range increases to 10 miles."
)
sustained_lightning = ForcePowers(
    name = "Sustained Lightning",
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "Shock",
    description = "You lash out against a creature within range with continual jolts of Force lightning. Make a ranged force attack against that creature. On a hit, the target takes 1d12 lightning damage, and on each of your turns for the duration, you can use your action to deal 1d12 lightning damage to the target automatically. The power ends if you use your action to do anything else. The power also ends if the target is ever outside the power’s range or if it has total cover from you. Force Potency: When you cast this power using a force slot of 2nd level or higher, the initial damage increases by 1d12 for each slot level above 1st."
)
tremor = ForcePowers(
    name = "Tremor",
    level = 1,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Touch",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "Burst",
    description = "You cause a tremor in the ground within range. Each creature other than you in a 5-foot-radius sphere centered on that point must make a Dexterity saving throw. On a failed save, a creature takes 1d8 kinetic damage and is knocked prone. On a successful save, the creature takes half as much damage and isn’t knocked prone. If the ground in that area is loose earth or stone, it becomes difficult terrain until cleared, with each 5-foot-diameter portion requiring at least 1 minute to clear by hand. Force Potency: When you cast this power using a force slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st."
)
wound = ForcePowers(
    name = "Wound",
    level = 1,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "-",
    description = "You make a piercing gesture at a creature within range. Make a ranged force attack against the target. On a hit, the target takes 2d8 necrotic damage and must make a Constitution saving throw. On a failed save, it is also poisoned until the end of your next turn. Force Potency: When you cast this power using a force slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st."
)

db.session.add_all([armor_of_abeloth, battle_precognition, beast_trick, breath_control, burst_of_speed, cloud_mind, comprehend_speech, curse, dark_side_tendrils, dun_moch, fear, force_blinding, force_body, force_focus, force_jump, force_mask, force_propel, heal, heroism, hex, improved_feedback, malacia, phasestrike, project, sanctuary, sense_emotion, sense_force, sustained_lightning, tremor, wound])
db.session.commit()
#--------------------------------------------------------------

#--------------------Species-----------------------------------
bith = Specie(
    name = "Bith",
    bio_and_appeaerance = "Bith are craniopods with pale pink, yellow, or green skin, large heads, large lidless eyes, toeless feet, and long fingers. Their thumb and small finger were both fully opposable. The bith’s internal systems are different from most humanoids, as the bith have only one lung, and exhale through their skin. Bith also lack a proper nose, instead having highly sensitive olfactory organs hidden in the skin-flaps of their cheeks. The other bith senses are also acute. Bith can sense the tonal qualities of sound as well as other species sensed colors. Their eyes, as big as a Menahuun’s, can see microscopic details of nearby objects, but are extremely nearsighted as a result. An interesting side effect of their incredible sensors is the effect of sonic grenades, or screamers, on them. It is described as causing their heads to explode. Similarly, bith have high manual dexterity which helps them manipulate fine tools, though their physical prowess with gross motor skills was only average.",
    society_and_culture = "Bith are one of the galaxy’s most ancient civilizations, with a history going back millions of years. This antiquity garners respect in certain quarters, such as among the Gree, who gave them more respect than other, “younger” species. Their society is highly regimented, with everything from mate selection to political leadership controlled by sophisticated computer programs.",
    names = "Bith names are quite diverse. Some names look complicated and difficult to pronounce, while others are quite simple. Male Names. Fedu, Jenkiss, Kabadons, Ph’teumkiass Female Names. Duhia, F’hubama, R’hothal, Thidus, Surnames. D’intes, Hern, K’sarorn, Nimum, Rumo",
    ability_score_increase = "Your Intelligence score increases by 2, and your Dexterity score increases by 1.",
    age = "Bith reach adulthood in their late teens and live less than a century.",
    alignment = " Biths’ benevolent nature causes them to tend toward the light side, though there are exceptions.",
    size = "Bith typically stand 5 to 6 feet tall and generally weigh about 120 lbs. Regardless of your position in that range, your size is Medium.",
    speed = "Your base walking speed is 30 feet.",
    speed_val = "30ft",
    languages = "You can speak, read, and write Galactic Basic, Bith, and one more language of your choice.",
    language_vals =["Galactic Basic", "Bith"]
)
bothan = Specie(
    name = "Bothan",
    bio_and_appeaerance = "Bothans are a short species of furry humanoids. Bothans are covered in fur which shifted in response to their emotional state by way of gentle ripplings. It is this trait, named Wrendui, that betrays them when members of their kind intend to be duplicitous in their dealings with others. They possess tapered pointed ears, and both males and females were known to sport beards. Bothans are able to interbreed with the other species, though it is rare that they do so. Such hybrids somewhat resembled baseline humans with haunches, hooves, fur, pointed ears and a long tail.",
    society_and_culture = "Bothan culture is guided by the philosophy and principles from the ancient text known as The Way, written by Golm Fervse’dra. In this “Bothan Way”, the pursuit of power and influence is paramount. Thus, individual bothans put their own political and economic success above all other concerns, and as a species, bothans put their own advancement ahead of other intergalactic interests. The volume of backstabbing, subtle character assassination and political maneuvering in bothan society is dizzying, and results in many species stereotyping bothans as untrustworthy. In fact, most bothans are habitually paranoid, believing that anyone who’s not working with them, is working against them. In times of crisis, the focus of bothan society shifts to a survivalist state known as “ar’krai”. When engaged in ar’krai, all fit bothans volunteer to defend their species from impending extinction.",
    names = "Male bothan names are often trickey while female’s are soft. Surnames are familial. Male Names. Garc, Hibriak, Nith, Tramom, Ventagt, Female Names. Ceerriah, Dhaim, Gnam, Meenn, Vit, Surnames. Bwif’livi, Gra’kit, Hia’faitu, Main’dil",
    ability_score_increase = "Your Intelligence score increases by 2, and your Dexterity score increases by 1.",
    age = "Bothans reach adulthood in their late teens and live less than a century.",
    alignment = "Bothans’ duplicitous nature causes them to tend toward the dark side, though there are exceptions.",
    size = "Bothans stand 4-5 feet tall and weigh under 100 pounds. Regardless of your position in that range, your size is Medium.",
    speed = "Your base walking speed is 30 feet.",
    speed_val = "30ft",
    languages = "You can speak, read, and write Galactic Basic and Bothese. Bothese had a great influence on the forming of Galactic Basic; the two languages share many cognates.",
    language_vals =["Galactic Basic", "Bothese"]

)
cathar = Specie(
    name = "Cathar",
    bio_and_appeaerance = "The Cathar have fur-covered bodies with thick manes as well as prominent, retractable claws that can deliver powerful killing attacks on foes and prey. Their bodies also possess rapid healing abilities. These traits make them the perfect hand-to-hand specialists. The Cathar species also has two subspecies, known as the Juhani and the Myr Rho. Both of these are notably less catlike than mainline Cathar. Cathar are born into a litter. The Cathar species is biologically similar to the Bothan species.",
    society_and_culture = "On their homeworld, Cathar live in cities built into giant trees, and are organized into clans governed by elders. Stories of their great heroes were often carved into the trunks of these tree-homes for following generations to see. The Cathar mate for life, to the extent that when one mate dies, the survivor never has a relationship with another. Cathar clan society includes great pageants and celebrations, especially for their heroes. Their religion includes a ritual known as the “Blood Hunt,” in which Cathar warriors individually engaged in combat against entire nests of Kiltik in order to gain honor and purge themselves of inner darkness. The native language of the Cathar is Catharese, which included the emphasis of some spoken words with a growl.",
    names = "Cathar names can sound both melodic and fairly gutteral, but they almost always sound strong and fierce. Female names are typically longer than male names. Surnames are usually one syllable. Male Names. Crurbirr, Isyrr, Nynorr, Suro, Tukarr, Female Names. Cuwin, Jyvohr, Mulahr, Solyri, Surnames. Jin, Ki, Mak, Rhir, Ta",
    ability_score_increase = "Your Dexterity score increases by 2, and your Charisma score increases by 1.",
    age = "Cathar reach adulthood in their late teens and live less than a century.",
    alignment = "Cathar tend toward no particular alignment. The best and worst are found among them.",
    size = "Cathar range from 5 to 7 feet tall, and can weigh up to 300 lbs. Regardless of your position in that range, your size is Medium.",
    speed = "Your base walking speed is 30 feet.",
    speed_val = "30ft",
    languages = "You can speak, read, and write Galactic Basic and Catharese",
    language_vals =["Galactic Basic", "Catharese"]

)
cerean = Specie(
    name = "Cerean",
    bio_and_appeaerance = "The Cereans’ enlarged skulls, extending above their foreheads, house complex binary brains, provided with sufficient blood by an extra heart in their heads. The binary structure of Cerean thinking helps them to ponder two sides of an issue at once. It also enables them to process information and solve problems rapidly and provides a highly advanced capacity for concentration and meditation. Because of their thoughtful nature, they tend to be calm, rational and analytical, preferring peaceful philosophies and a lifestyle which works in harmony with nature. Though the quick-thinking Cereans have equally quick reflexes, they are commonly not as well coordinated as humans.",
    society_and_culture = "Cereans developed a low-tech society on their homeworld and prefer to live in isolation from the wider galaxy. Preserving the natural beauty of Cerea, the planet is home to many Outsider Citadels where it is permissible to use offworld technology, though it could not be removed from the Citadel. Meditation is a core part of a Cerean’s daily rituals, with many employing specially-forged kasha crystals as a focusing tool. By focusing one’s thoughts while in contact with such crystals, distractions are eliminated, creating an exceptional meditation environment. Cerean Jedi sometimes incorporate these crystals into their lightsabers, providing great focus, even during intense physical combat.",
    names = "Cerean male first names are often hyphenated, while females are not. Surnames are familial. Male Names. Ji-Cheelia, Ki-Adi, Pick-toh, Sauli-Fanz, Female Names. Dreash, Kilniavy, Melm, Rharoth, Surnames. Codux, Emkom, Kyureft, Lonnik, Mundi",
    ability_score_increase = " Your Intelligence score increases by 2, and your Wisdom score increases by 1.",
    age = "Cereans reach adulthood in their late teens and live less than a century.",
    alignment = " Cereans’ altruistic nature causes them to tend toward the light side, though there are exceptions.",
    size = "Cereans typically stand between 6 and 7 feet tall and weigh about 150 lbs. Regardless of your position in that range, your size is Medium",
    speed = "Your base walking speed is 30 feet.",
    speed_val = "30ft",
    languages = "You can speak, read, and write Galactic Basic and Cerean. Cerean is characterized by its gravelly sounds.",
    language_vals =["Galactic Basic", "Cerean"]

)
chiss = Specie(
    name = "Chiss",
    bio_and_appeaerance = "The chiss are a near-human species distinguished by their blue skin and glowing red eyes. Genetic analysis indicate that they are an offshoot of humanity, and it is believed that moving underground led to a divergence between them and baseline Humans. Their blue skin, jet black hair and red eyes generally command attention; these features make them physically striking and instantly recognizable.",
    society_and_culture = "Chiss society is highly structured and ordered with the rule of law being enforced by a group of four affiliations known as the Ruling Families: the Csapla, Nuruodo, Inrokini and Sabosen. These are not biological family groupings but instead different branches of their government. Every chiss claims affiliation to one of the four families, as determined by both tradition and place of birth. The family names are more of a cultural holdover; the bloodlines had grown so co-meddled that any chiss could claim affiliation to any of the ruling families. In spite of the outward impression of calm and order that the chiss like to project to outsiders, there were evidently tensions within the Families; political assassinations are a real part of chiss political life for the Ruling Families.",
    names = "A chiss true-name has 3 parts, each separated by an apostrophe. The first part is their family name, the second part is their root name, and the third part is their occupation. Chiss rarely share their true-name with non-chiss, and usually go by their root name. Male and female names do not significantly deviate. Names. Crorcu’ecuk’unist, Dash’esoru’ishur, Jerd’ecer’lonii, Kisk’egauw’eqhi, Marag’aliphil’eduo, Pommo’icuote’nlerme, Vornu’wuzi’lerdim",
    ability_score_increase = "Your Intelligence score increases by 2, and your Charisma score increases by 1.",
    age = "Chiss reach adulthood in their late teens and live less than a century.",
    alignment = "Chiss’ tactical and selfish nature cause them to tend toward lawful dark side, though there are exceptions.",
    size = "Chiss typically stand between 5 and 6 feet tall and weigh about 160 lbs. Regardless of your position in that range, your size is Medium.",
    speed = "Your base walking speed is 30 feet.",
    speed_val = "30ft",
    languages = "You can speak, read, and write Galactic Basic and Cheunh. Cheunh is a complex language that is difficult for non-chiss to learn. Chiss take pride in this difficulty.",
    language_vals =["Galactic Basic", "Cheunh"]

)

db.session.add_all([bith, bothan, cathar, cerean, chiss])
db.session.commit()
#--------------------------------------------------------------

#-------------------Species Traits-----------------------------
#? Bith
detail_oriented = SpecieTraits(
    name = "Detail Oriented",
    details = "You are practiced at scouring for details. You have advantage on Intelligence (Investigation) checks within 5 feet."
)
keen_hearing_and_smell = SpecieTraits(
    name = "Keen Hearing and Smell",
    details = "You have advantage on Wisdom (Perception) checks that involve hearing or smell."
)
musician = SpecieTraits(
    name = "Musician",
    details = "You are proficient in one musical instrument of your choice."
)
programmer = SpecieTraits(
    name = "Programmer",
    details = "Whenever you make an Intelligence (Technology) check related to computers, you are considered to have expertise in the Technology skill."
)
#? Bothan
naturally_stealth = SpecieTraits(
    name = "Naturally Stealth",
    details = "You can attempt to hide even when you are obscured only by a creature that is your size or larger than you." 
)
nimble_escape = SpecieTraits(
    name = "Nimble Escape",
    details = "You can take the Disengage or Hide action as a bonus action on each of its turns." 
)
shrewd = SpecieTraits(
    name = "Shrewd",
    details = "You are proficient in the Insight and Deception skills" 
)
#? Cathar
cats_claws = SpecieTraits(
    name = "Cat's Claws",
    details = "You have a climbing speed of 20 feet. Additionally, your unarmed strikes deal 1d4 kinetic damage and have the finesse property"
)
cats_talent = SpecieTraits(
    name = "Cat's Talent",
    details = "You have proficiency in the Perception and Stealth skills."
)
darkvision = SpecieTraits(
    name = "Darkvision",
    details = "You have a cat’s keen senses, especially in the dark. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."
)
leonine_agility = SpecieTraits(
    name = "Leonine Agility",
    details = "Your reflexes and agility allow you to move with a burst of speed. When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can’t use it again until you move 0 feet on one of your turns."
)
#? Cerean
closed_mind = SpecieTraits(
    name = "Closed Mind",
    details = "You have advantage on Wisdom and Charisma saving throws against force powers."
)
intuitive_initative = SpecieTraits(
    name = "Intutitive Initiative",
    details = "You can choose to reroll Initiative checks, but you must use the new roll."
)
perceptive = SpecieTraits(
    name = "Perceptive",
    details = "You have proficiency in Perception."
)
strong_legged = SpecieTraits(
    name = "Strong-Legged",
    details = "When you make a long jump, you can cover a number of feet up to twice your Strength score. When you make a high jump, you can leap a number of feet up into the air equal to 3 + twice your Strength modifier."
)
trance = SpecieTraits(
    name = "Trance",
    details = "You only need 3 hours of sleep during a long rest to gain its benefits, instead of 6. Additionally, if your long rest would be interrupted, you only need to complete the long rest instead of restarting it to gain its benefits."
)
#? Chiss
tech_resistance = SpecieTraits(
    name = "Tech Resistance",
    details = "Growing up around technology leaves an impact on chiss. You have advantage on Dexterity and Intelligence saving throws against tech powers."
)
martial_proficiency = SpecieTraits(
    name = "Martial Proficiency",
    details = "You have proficiency with light and medium armor as well as the blaster pistol and sniper rifle."
)

db.session.add_all([detail_oriented, keen_hearing_and_smell, musician, programmer, naturally_stealth, nimble_escape, shrewd, cats_claws, cats_talent, darkvision, leonine_agility, closed_mind, intuitive_initative, perceptive, strong_legged, trance, tech_resistance, martial_proficiency])
db.session.commit()
#--------------------------------------------------------------

#---------------------Species to Traits------------------------
t1 = SpeciesToTraits(
    species_id = 1,
    trait_id = 1
)
t2 = SpeciesToTraits(
    species_id = 1,
    trait_id = 2
)
t3 = SpeciesToTraits(
    species_id = 1,
    trait_id = 3
)
t4 = SpeciesToTraits(
    species_id = 1,
    trait_id = 4
)
t5 = SpeciesToTraits(
    species_id = 2,
    trait_id = 5
)
t6 = SpeciesToTraits(
    species_id = 2,
    trait_id = 6
)
t7 = SpeciesToTraits(
    species_id = 2,
    trait_id = 7
)
t8 = SpeciesToTraits(
    species_id = 3,
    trait_id = 8
)
t9 = SpeciesToTraits(
    species_id = 3,
    trait_id = 9
)
t10 = SpeciesToTraits(
    species_id = 3,
    trait_id = 10
)
t11 = SpeciesToTraits(
    species_id = 3,
    trait_id = 11
)
t12 = SpeciesToTraits(
    species_id = 4,
    trait_id = 12
)
t13 = SpeciesToTraits(
    species_id = 4,
    trait_id = 13
)
t14 = SpeciesToTraits(
    species_id = 4,
    trait_id = 14
)
t15 = SpeciesToTraits(
    species_id = 4,
    trait_id = 15
)
t16 = SpeciesToTraits(
    species_id = 4,
    trait_id = 16
)
t17 = SpeciesToTraits(
    species_id = 5,
    trait_id = 17
)
t18 = SpeciesToTraits(
    species_id = 5,
    trait_id = 18
)
t10_1 = SpeciesToTraits(
    species_id = 5,
    trait_id = 10
)

db.session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t10_1])
db.session.commit()
#--------------------------------------------------------------

#-----------------------Backgrounds----------------------------
agent = Background(
    name = "Agent",
    intro = "Many organizations active in the galaxy aren’t bound by strictures of geography. These factions pursue their agendas without regard for political boundaries, and their members operate anywhere the organization deems necessary. These groups employ listeners, rumormongers, smugglers, mercenaries, cache-holders (people who guard caches of wealth or items for use by the faction’s operatives), haven keepers, and message drop minders, to name a few. At the core of every faction are those who don’t merely fulfill a small function for that organization, but who serve as its hands, head, and heart. As a prelude to your adventuring career (and in preparation for it), you served as an agent of a particular faction. You might have operated openly or secretly, depending on the faction and its goals, as well as how those goals mesh with your own. Becoming an adventurer doesn’t necessarily require you to relinquish membership in your faction (though you can choose to do so), and it might enhance your status in the faction.",
    skill_proficiencies = "Choose two from Deception, Investigation, Lore, and Persuasion",
    skill_vals = [2, "Deception", "Investigation", "Lore", "Persuasion"],
    languages = "Two of your choice",
    equipment = "Badge or emblem of your faction, a copy of a seminal faction text (or a code-book for a covert faction), a set of common clothes, and a pouch containing 150 cr",
    credits = 150,
    background_feature_name = "Safe Haven",
    background_feature_details = "As a faction agent, you have access to a secret network of supporters and operatives who can provide assistance on your adventures. You know a set of secret signs and passwords you can use to identify such operatives, who can provide you with access to a hidden safe house, free room and board, or assistance in finding information. These agents never risk their lives for you or risk revealing their true identities."
)
bounty_hunter = Background(
    name = "Bounty Hunter",
    intro = "Before you became an adventurer, your life was already full of conflict and excitement, because you made a living tracking down people for pay. Unlike some people who collect bounties, though, you aren’t a savage who follows quarry into or through the wilderness. You’re involved in a lucrative trade, in the place where you live, that routinely tests your skills and survival instincts. What’s more, you aren’t alone, as a bounty hunter in the wild would be: you routinely interact with both the criminal subculture and other bounty hunters, maintaining contacts in both areas to help you succeed. You might be a cunning thief-catcher, prowling the rooftops to catch one of the myriad burglars of the city. Perhaps you are someone who has your ear to the street, aware of the doings of street gangs. You might be a “velvet mask” bounty hunter, one who blends in with high society and noble circles in order to catch the criminals that prey on the rich, whether pickpockets or con artists. As a member of an adventuring party, you might find it more difficult to pursue a personal agenda that doesn’t fit with the group’s objectives - but on the other hand, you can take down much more formidable targets with the help of your companions.",
    skill_proficiencies = "Choose two from Deception, Insight, Persuasion, and Stealth",
    tool_proficiencies = "Your choice of demolitions kit, security kit, or slicer's kit",
    skill_vals = [2, "Deception", "Insight", "Persuasion", "Stealth"],
    languages = "One of your choice",
    equipment = "A set of clothes appropriate to your duties, a set of binders, and a pouch containing 200 cr",
    credits = 200,
    background_feature_name = "Ear to the Ground",
    background_feature_details = "You are in frequent contact with people in the segment of society that your chosen quarries move through. These people might be associated with the criminal underworld, the rough-and-tumble folk of the streets, or members of high society. This connection comes in the form of a contact in any city you visit, a person who provides information about the people and places of the local area."
)
criminal = Background(
    name = "Criminal",
    intro = "You are an experienced criminal with a history of breaking the law. You have spent a lot of time among other criminals and still have contacts within the criminal underworld. You’re far closer than most people to the world of murder, theft, and violence that pervades the underbelly of civilization, and you have survived up to this point by flouting the rules and regulations of society.",
    skill_proficiencies = "Choose two from Deception, Intimidation, Sleight of Hand, and Stealth",
    tool_proficiencies = "One type of gaming set, your choice of demolitions kit, security kit, or slicer's kit",
    skill_vals = [2, "Deception", "Intimidation", "Sleight of Hand", "Stealth"],
    equipment = " A set of common clothes with a hood, a gaming set (one of your choice), and a belt pouch containing 150 cr", 
    credits = 150,
    background_feature_name = "Criminal Contact",
    background_feature_details = "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."
)

db.session.add_all([agent, bounty_hunter, criminal])
db.session.commit()
#--------------------------------------------------------------

#--------------------------Feats-------------------------------
silver_tongued = Feat(
    name = "Silver-Tongued",
    details = "Increase your Charisma score by 1, to a maximum of 20. You gain proficiency in the Deception skill. If you are already proficient in it, you instead gain expertise in it. When you take the Attack action, you can replace one attack with an attempt to deceive one humanoid you can see within 30 feet of you that can see and hear you. Make a Charisma (Deception) check contested by the target’s Wisdom (Insight) check. If your check succeeds, your movement doesn’t provoke opportunity attacks from the target and your attack rolls against it have advantage; both benefits last until the end of your next turn or until you use this ability on a different target. If your check fails, the target can’t be deceived by you in this way for 1 hour."
)
investigator = Feat(
    name = "Investigator",
    details = "Increase your Intelligence score by 1, to a maximum of 20. You gain proficiency in the Investigation skill. If you are already proficient in it, you instead gain expertise in it. You can take the Search action as a bonus action."
)
empathic = Feat(
    name = "Empathic",
    details = "Increase your Wisdom score by 1, to a maximum of 20. You gain proficiency in the Insight skill. If you are already proficient in it, you instead gain expertise in it. You can use your action to try to get uncanny insight about one humanoid you can see within 30 feet of you. Make a Wisdom (Insight) check contested by the target’s Charisma (Deception) check. On a success, you have advantage on attack rolls and ability checks against the target until the end of your next turn."
)
threatening = Feat(
    name = "Threatening",
    details = "Increase your Charisma score by 1, to a maximum of 20. You gain proficiency in the Intimidation skill. If you are already proficient in it, you instead gain expertise in it. When you take the Attack action, you can replace one attack with an attempt to demoralize one humanoid you can see within 30 feet of you that can see and hear you. Make a Charisma (Intimidation) check contested by the target’s Wisdom (Insight) check. If your check succeeds, the target is frightened until the end of your next turn. If your check fails, the target can’t be frightened by you in this way for 1 hour."
)

db.session.add_all([silver_tongued, investigator, empathic, threatening])
db.session.commit()
#--------------------------------------------------------------

#----------------------Feat-to-Background----------------------
feat1 = FeatsBackround(
    background_id = 1,
    feat_id = 1
)
feat2 = FeatsBackround(
    background_id = 1,
    feat_id = 2
)
feat3 = FeatsBackround(
    background_id = 2,
    feat_id = 1
)
feat4 = FeatsBackround(
    background_id = 2,
    feat_id = 3
)
feat5 = FeatsBackround(
    background_id = 3,
    feat_id = 1
)
feat6 = FeatsBackround(
    background_id = 3,
    feat_id = 4
)

db.session.add_all([feat1, feat2, feat3, feat4, feat5, feat6])
db.session.commit()
#--------------------------------------------------------------

#---------------------Personality Traits-----------------------
person_trait1 = PersonalityTraits(
    details = "I idolize a particular hero of my faction, and constantly refer to that person's deeds and example."
)
person_trait2 = PersonalityTraits(
    details = "I always have a plan for what to do when things go wrong."
)
person_trait3 = PersonalityTraits(
    details = "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me."
)

db.session.add_all([person_trait1, person_trait2, person_trait3])
db.session.commit()
#--------------------------------------------------------------

#-----------------------Personality Background-----------------
pt1 = PersonalityBackground(
    background_id = 1,
    personality_trait_id = 1 
)
pt2 = PersonalityBackground(
    background_id = 2,
    personality_trait_id = 2
)
pt3 = PersonalityBackground(
    background_id = 3,
    personality_trait_id = 2
)
pt4 = PersonalityBackground(
    background_id = 3,
    personality_trait_id = 3 
)

db.session.add_all([pt1, pt2, pt3, pt4])
db.session.commit()
#--------------------------------------------------------------

#--------------------------Ideals------------------------------
honor = Ideals(
    name = "Honor",
    details = "Honor. I don't steal from others in the trade. (Lawful)"
)
freedom = Ideals(
    name = "Freedom",
    details = "	Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)"
)
tradition = Ideals(
    name = "Tradition",
    details = "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)"
)

db.session.add_all([honor, freedom, tradition])
db.session.commit()
#--------------------------------------------------------------

#--------------------------Ideals Backgrounds------------------
ib1 = IdealsBackgrounds(
    background_id = 1,
    ideal_id = 3
)
ib2 = IdealsBackgrounds(
    background_id = 2,
    ideal_id = 1
)
ib3 = IdealsBackgrounds(
    background_id = 3,
    ideal_id = 2
)

db.session.add_all([ib1, ib2, ib3])
db.session.commit()
#--------------------------------------------------------------

#-------------------------Bonds-------------------------------
bond1 = Bonds(
    details = "I would die to recover an artifact of my faction that was lost long ago."
)
bond2 = Bonds(
    details = "I'm trying to pay off an old debt I owe to a generous benefactor."
)

db.session.add_all([bond1, bond2])
db.session.commit()
#--------------------------------------------------------------

#--------------------Bonds Backgrounds-------------------------
bb1 = BondsBackgrounds(
    background_id = 1,
    bond_id = 1
)
bb2 = BondsBackgrounds(
    background_id = 2,
    bond_id = 2
)
bb3 = BondsBackgrounds(
    background_id = 3,
    bond_id = 2
)

db.session.add_all([bb1, bb2, bb3])
db.session.commit()
#--------------------------------------------------------------

#-------------------------Flaws--------------------------------
flaw1 = Flaws(
    details = "I judge others harshly, and myself even more severely."
)
flaw2 = Flaws(
    details = "When I see something valuable, I can't think about anything but how to steal it."
)

db.session.add_all([flaw1, flaw2])
db.session.commit()
#--------------------------------------------------------------

#---------------------Flaws Backgrounds------------------------
fb1 = FlawsBackgrounds(
    background_id = 1,
    flaw_id = 1
)
fb2 = FlawsBackgrounds(
    background_id = 2,
    flaw_id = 2
)
fb3 = FlawsBackgrounds(
    background_id = 3,
    flaw_id = 2
)

db.session.add_all([fb1, fb2, fb3])
db.session.commit
#--------------------------------------------------------------

#--------------------------Armor-------------------------------
combat_suit = Armor(
    name = "Combat Suit",
    type = "Light",
    cost = 100,
    weight = 10,
    armor_class = "11 + Dex modifier",
    details = "Combat suits are seen all over the galaxy, and can be found for sale by almost any merchant who dealt in weapons and armor. Many such suits are used by military organizations, such as the Galactic Republic’s military, as well as by mercenaries, criminals, bounty hunters and even some Jedi. The suit itself offers decent protection from most types of attacks while maintaining maximum flexibility and minimum weight. However this armor is only recommended for light skirmishes."
)
mesh_armor= Armor(
    name = "Mesh Armor",
    type = "Medium",
    cost = 500,
    weight = 20,
    armor_class = "13 + Dex modifier",
    details = "Providing solid protection for a minimal cost, mesh armor is considered excellent protection for entrenched troops or guards. However, this protection comes at a cost of mobility, limiting its uses by rapidly advancing infantry. Still, it provides more mobility than battle armor."
)
assault_armor = Armor(
    name = "Assault Armor",
    type = "Heavy",
    properties = ["Bulky", "Strength 15"],
    cost = 2000,
    weight = 60,
    armor_class = "17",
    stealth = "Disadvantage",
    details = "Assault armor improved on battle armor, with the benefit of micro-hydraulics that boost the efficacy of the operator. It offers better protection, but increased weight."
)
heavy_physical_shield  = Armor(
    name = "Heavy Physical Shield",
    type = "Shield",
    properties = ["Obtrusive", "Stregth 15"],
    cost = 500,
    weight = 36,
    armor_class = "+3"
)

db.session.add_all([combat_suit, mesh_armor, assault_armor, heavy_physical_shield])
db.session.commit()
#--------------------------------------------------------------

#----------------------Weapons---------------------------------
blaster_carbine = Weapon(
    name = "Blaster Carbine",
    type = "Simple Blaster",
    properties = ["Ammunition(range 60/240)", "Reload 16", "two-handed"],
    cost = 300,
    weight = 8,
    damage = "1d6 Energy"
)
assault_cannon = Weapon(
    name = "Assault Cannon",
    type = "Martial Blaster",
    properties = ["Ammunition (range 80/320)", "Burst 4", "Reload 8", "Strength 11", "Two-handed"],
    cost = 500,
    weight = 24,
    damage = "1d10 Energy"
)
lightclub = Weapon(
    name = "Lightclub",
    type = "Simple Lightweapon",
    properties = ["Luminous", "Two-handed"],
    cost = 150,
    weight = 5,
    damage = "1d10 Energy"
)
doublesaber = Weapon(
    name = "Doublesaber",
    type = "Martial Lightweapon",
    properties = ["Double(1d8 Energy)", "Finesse", "Luminous"],
    cost = 1400,
    weight = 4,
    damage = "1d8 Energy"
)
techaxe = Weapon(
    name = "Techaxe",
    type = "Simple Vibroweapon",
    properties = ["Light", "Thrown(range 20/60)"],
    cost = 75,
    weight = 2,
    damage = "1d6 Kinetic"
)
chakram = Weapon(
    name = "Chakram",
    type = "Martial Vibroweapon",
    properties = ["Finesse", "Returning", "Thrown(range 30/90)"],
    cost = 250,
    weight = 3,
    damage = "1d6 Kinetic"
)

db.session.add_all([blaster_carbine, assault_cannon, lightclub, doublesaber, techaxe, chakram])
db.session.commit()
#--------------------------------------------------------------

#---------------------Adventuring Gear-------------------------
power_cell = AdventureingGear(
    name = "Power Cell",
    category = "Ammunition",
    cost = 10,
    weight = 1.0,
    details = "Power cells fuel blaster weapons that deal energy or ion damage. Additionally, power cells are used to energize certain tools."
)
common_clothes = AdventureingGear(
    name = "Common Clothes",
    category = "Clothing",
    cost = 5,
    weight = 3.0,
)
commlink = AdventureingGear(
    name = "Commlink",
    category = "Communications",
    cost = 50,
    weight = 0.5,
    details = "Commlinks are standard handheld communication devices, fitted with microphones and receivers. Standard, personal commlinks have a range of up to 30 miles, but are reduced in dense, urban areas or areas of high level interference."
)
code_cylinder = AdventureingGear(
    name = "Code Cylinder",
    category = "Data Recording and Storage",
    cost = 20,
    weight = 0.5,
    details = "Code cylinders are security devices in the shape of short cylinders that contain coded information about their bearers and grant them access to secure areas."
)
fragmentation_grenade = AdventureingGear(
    name = "Fragmentaion Grenade",
    category = "Explosive",
    cost = 100,
    weight = 1.0,
    details = "Grenades can be set to detonate on impact or with a timer that causes them to explode on initiative count 20 (losing all initiative ties). As an action, you can throw a grenade at a point you can see within 30 feet + your Strength modifier x 5. Each creature within 10 feet must make a DC 14 Dexterity saving throw. A creature takes 2d10 kinetic damage on a failed save, or half as much as on a successful one."
)
chance_cubes = AdventureingGear(
    name = "Chance Cubes",
    category = "Gaming Set",
    cost = 1,
    weight = 0.0,
)
chefs_kit = AdventureingGear(
    name = "Chef's Kit",
    category = "Kit",
    cost = 500,
    weight = 8,
)
flight_suit = AdventureingGear(
    name = "Flight Suit",
    category = "Life Support",
    cost = 1000,
    weight = 5,
    details = "Flight suits, or jumpsuits, are a type of outfit worn by pilots. They are worn in conjunction with flight helmets. They come in a variety of different colors and provide life support, and protect from hostile environments."
)
medpac = AdventureingGear(
    name = "Medpac",
    category = "Medical",
    cost = 300,
    weight = 0.5,
    details = "A medpac is a quick-acting syringe filled with a concentrated dose of kolto. As an action, you can use this medpac to restore hit points to a beast or humanoid within 5 feet. The creature rolls one die equal to the size of their Hit Die and regains hit points equal to the amount rolled + their Constitution modifier (minimum of one hit point). If the creature has Hit Dice of different sizes, use whichever Hit Die size they have the most of."
)
bandfill = AdventureingGear(
    name = "Bandfill",
    category = "Musical Instrument",
    cost = 300,
    weight = 2,
)
backpack = AdventureingGear(
    name = "Backpack",
    category = "Storage",
    cost = 50,
    weight = 3,
    details = "A backpack stores 30 lb., not exceeding 1 cubic foot."
)
armormechs_implements = AdventureingGear(
    name = "Armormech's Implements",
    category = "Tool",
    cost = 200,
    weight = 8,
)
bedroll = AdventureingGear(
    name = "Bedroll",
    category = "Utility",
    cost = 10,
    weight = 7.0,
)
bipod = AdventureingGear(
    name = "Bipod",
    category = "Weapon or Armor Accessory",
    cost = 200,
    weight = 2.0,
    details = "A bipod is a device mounted to a two-handed blaster weapon to offer increased stability while prone. As an action, you can deploy or collapse the bipod. While deployed, you ignore the Strength requirement on ranged weapons with the strength property while you are prone, and your speed is reduced to 0. Additionally, while deployed and prone, you have a +10 bonus to ability checks and saving throws to avoid being disarmed of the weapon."
)

db.session.add_all([power_cell, common_clothes, commlink, code_cylinder, fragmentation_grenade, chance_cubes, chefs_kit, flight_suit, medpac, bandfill, backpack, armormechs_implements, bedroll, bipod])
db.session.commit()
#--------------------------------------------------------------
