from app import app
from models import SpeciesToTraits, db, Class, ClassFeatures, Archetype, FightingMastery, FightingStyles, LightsaberForms, TechPowers, ForcePowers, Specie, SpecieTraits, Background, Feat, PersonalityTraits, Ideals, Bonds, Flaws, Armor, Weapon, AdventureingGear, Condition, BerserkerInstincts, ForceEmpoweredCasting, Maneuver, GuardianAura, MonasticVows, OperativeExploits, ScholarDiscovery, ScoutRoutine, SentinelIdeals, FeatsBackround, PersonalityBackground, IdealsBackgrounds, BondsBackgrounds, FlawsBackgrounds


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

# -----------------Berserker Instincts------------------------
acklay_instinct = BerserkerInstincts(
    name = "Acklay's Instinct",
    details = "While raging, you have advantage on Constitution saving throws.",
    class_id = 1
)
bantha_instinct = BerserkerInstincts(
    name = "Bantha's Instinct",
    prerequisite = "7th level",
    details = "Your carrying capacity and the weight you can push, drag, or lift doubles. If it would already double, it instead triples. Additionally, you have advantage on Strength checks made to push, pull, lift, or break objects.",
    class_id = 1
)
blurrg_instinct = BerserkerInstincts(
    name = "Blurrg's Instinct",
    details = "Whether mounted or on foot, your travel pace is doubled, as is the travel pace of up to ten companions while they’re within 60 feet of you and you’re not incapacitated.",
    class_id = 1
)
boggdo_instinct = BerserkerInstincts(
    name = "Bofggdo's Instinct",
    prerequisite = "13 level",
    details = "While raging you have a flying speed equal to your current walking speed, though you fall if you end your turn in the air and nothing else is holding you aloft.",
    class_id = 1
)
chirodactyl_instinct = BerserkerInstincts(
    name = "Chirodactyl's Instinct",
    prerequisite = "7th level",
    details = "While raging, you have blindsight to a range of 30 feet, and you have advantage on Wisdom (Perception) checks that rely on sound, as long as you aren’t deafened.",
    class_id = 1
)
dewback_instinct = BerserkerInstincts(
    name = "Dewback's Instinct",
    details = "Choose three damage types other than true damage. While raging, you have resistance to the chosen damage types.",
    class_id = 1
)
fighter_instinct = BerserkerInstincts(
    name = "Fighter's Instinct",
    details = "You adopt a particular style of fighting as your specialty. Choose one of the Fighting Style options",
    class_id = 1
)
fyrnock_instinct = BerserkerInstincts(
    name = "Fyrnock's Instinct",
    details = "While raging, you can use your bonus action to leap up to 30 feet to an empty space you can see. When you land you deal kinetic damage equal to your Strength modifier to each creature within 5 feet of where you land. You can use this feature a number of times equal to your Constitution modifier (a minimum of once). You regain all expended uses when you complete a long rest.",
    class_id = 1
)
hawk_instinct = BerserkerInstincts(
    name = "Hawk's Instinct",
    prerequisite = "7th level",
    details = "You can see up to 1 mile away with no difficulty. You are able to discern even fine details as though looking at something no more than 100 feet away from you. Additionally, dim light doesn’t impose disadvantage on your Wisdom (Perception) checks.",
    class_id = 1
)
katarn_instinct = BerserkerInstincts(
    name = "Katarn's Instinct",
    details = "You gain a climbing speed equal to your movement speed.",
    class_id = 1
)
loth_cat_instinct = BerserkerInstincts(
    name = "Loth Cat's Instinct",
    details = "While you’re raging, other creatures have disadvantage on opportunity attack rolls against you, and you can take the Dash action as a bonus action on your turn",
    class_id = 1
)
predator_instinct = BerserkerInstincts(
    name = "Predator's Instinct",
    details = "Your speed increases by 10 feet.",
    class_id = 1
)
rancor_instinct = BerserkerInstincts(
    name = "Rancor's Instinct",
    prerequisite = "13th level",
    details = "While you’re raging any creature within 5 feet of you that’s hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can’t see or hear you or if it can’t be frightened.",
    class_id = 1
)
tactician_instinct = BerserkerInstincts(
    name = "Tactician's Instinct",
    details = "When you use your Reckless Attack feature, you can choose to not have advantage on your attack rolls this turn. If you do so, friendly creatures within 5 feet of a hostile creature that is within 5 feet of you have advantage on attack rolls against that creature.",
    class_id = 1
)
tracker_instinct = BerserkerInstincts(
    name = "Tracker's Instinct",
    prerequisite = "7th level",
    details = "You can track other creatures while traveling at a fast pace, and you can move stealthily while traveling at a normal pace.",
    class_id = 1
)
terentatek_instinct = BerserkerInstincts(
    name = "Terentatek's Instinct",
    prerequisite = "13th level",
    details = "When you are forced to make a saving throw against a force power, you can immediately use your reaction to move up to half your speed towards the source power’s caster. If you end this movement within 5 feet of the target, you can immediately make one melee weapon attack against the target as a part of that reaction.",
    class_id = 1
)
varactyl_instinct = BerserkerInstincts(
    name = "Varactyl's Instinct",
    prerequisite = "13th level",
    details = "While raging, you have advantage Dexterity checks, your attack rolls can’t suffer from disadvantage, and each slowed level only reduces your speed by 5 feet, unless it would reduce your speed to 0.",
    class_id = 1
)

db.session.add_all([acklay_instinct, bantha_instinct, blurrg_instinct, boggdo_instinct, chirodactyl_instinct, dewback_instinct, fighter_instinct, fyrnock_instinct, hawk_instinct, katarn_instinct, loth_cat_instinct, predator_instinct, rancor_instinct, tactician_instinct, tracker_instinct, terentatek_instinct, varactyl_instinct])
db.session.commit()
# ------------------------------------------------------------

#---------------Force-Empowered Casting-----------------------
careful_power = ForceEmpoweredCasting(
    name = "Careful Power",
    details = "When you cast a power that forces other creatures to make a saving throw, you can protect some of those creatures from the power’s full force. To do so, you spend 1 additional force point and choose a number of those creatures up to your Wisdom or Charisma modifier (your choice, minimum of one). A chosen creature automatically succeeds on its saving throw against the power.",
    class_id = 2
)
distant_power = ForceEmpoweredCasting(
    name = "Distant Power",
    details = "When you cast a power that has a range of 5 feet or greater, you can spend 1 additional force point to double the range of the power. Alternatively, when you cast a power that has a range of touch, you can spend 1 additional force point to make the range of the power 30 feet.",
    class_id = 2
)
extended_power = ForceEmpoweredCasting(
    name = "Extended Power",
    details = "When you cast a power that has a duration of 1 minute or longer, you can spend 1 additional force point to double its duration, to a maximum duration of 24 hours.",
    class_id = 2
)
heightened_power = ForceEmpoweredCasting(
    name = "Heightened Power",
    details = "When you cast a power that forces a creature to make a saving throw to resist its effects, you can spend 3 additional force points to give one target of the power disadvantage on its first saving throw made against the power.",
    class_id = 2
)
improved_power = ForceEmpoweredCasting(
    name = "Improved Power",
    details = "When you roll damage for a power, you can spend 1 additional force point to reroll a number of the damage dice up to your Wisdom or Charisma modifier (your choice, minimum of one). You must use the new rolls. You can use Improved Power even if you have already used a different Force-Empowered Casting option during the casting of the power.",
    class_id = 2
)
lingering_power = ForceEmpoweredCasting(
    name = "Lingering Power",
    details = "When you cast a power that requires concentration to maintain you can choose to spend 3 additional force points. If you do, when you lose concentration on the power, the power will not end until the end of your next turn.",
    class_id = 2
)
pinpoint_power = ForceEmpoweredCasting(
    name = "Pinpoint Power",
    details = "When you cast a power that allows you to force creatures in an area to make a saving throw you can instead spend 1 force point and make a ranged force attack against a single target that would be in the range. On a hit the target suffers the effects as though they failed their saving throw.",
    class_id = 2
)
quickened_power = ForceEmpoweredCasting(
    name = "Quckened Power",
    details = "When you cast a power that has a casting time of 1 action, you can spend 2 additional force points to change the casting time to 1 bonus action for this casting.",
    class_id = 2
)
refocused_power = ForceEmpoweredCasting(
    name = "Refocused Power",
    details = "When you are forced to make a Constitution saving throw to maintain concentration on a power you can use your reaction and spend 2 force points to automatically succeed on the saving throw. You can use Refocused Power even if you have already used a different Force-Empowered Casting option during the casting of the power.",
    class_id = 2
)
seeking_power = ForceEmpoweredCasting(
    name = "Seeking Power",
    details = "If you miss with a force power that calls for an attack roll, you can spend 2 force points to reroll the attack. You must use the new roll. You can use Seeking Power even if you have already used a different Force-Empowered Casting option during the casting of the power.",
    class_id = 2
)
twinned_power = ForceEmpoweredCasting(
    name = "Twinned Power",
    details = "When you cast a power that targets only one creature and doesn’t have a range of self, you can spend a number of additional force points equal to the power’s level to target a second creature in range with the same power (1 force point if the power is at-will).",
    class_id = 2
)

db.session.add_all([careful_power, distant_power, extended_power, heightened_power, improved_power, lingering_power, pinpoint_power, quickened_power, refocused_power, seeking_power, twinned_power])
db.session.commit()
#-------------------------------------------------------------

#------------------------Maneuver-----------------------------
#? Fighter
commander_strike = Maneuver(
    name = "Commander's Strike",
    details = "When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of your companions to strike. When you do so, choose a friendly creature who can see or hear you and expend one superiority die. That creature can immediately use its reaction to make one weapon attack, adding the superiority die to the attack’s damage roll.",
    class_id = 4
)
disarming_attack = Maneuver(
    name = "Disarming Atrack",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to disarm the target, forcing it to drop one item of your choice that it’s holding. You add the superiority die to the attack’s damage roll, and the target must make a Strength saving throw. On a failed save, it drops the object you choose. The object lands at its feet.",
    class_id = 4
)
distracting_strike = Maneuver(
    name = "Distracting Strike",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to distract the creature, giving your allies an opening. You add the superiority die to the attack’s damage roll. The next attack roll against the target by an attacker other than you has advantage if the attack is made before the start of your next turn.",
    class_id = 4
)
evasive_footwork = Maneuver(
    name = "Evasive Footwork",
    details = "When you move, you can expend one superiority die, rolling the die and adding the number rolled to your AC until you stop moving.",
    class_id = 4
)
feinting_attack = Maneuver(
    name = " Feinting Attack",
    details = "You can expend one superiority die and use a bonus action on your turn to feint, choosing one creature within 5 feet of you as your target. You have advantage on your next attack roll against that creature. If that attack hits, add the superiority die to the attack’s damage roll.",
    class_id = 4
)
goading_attack = Maneuver(
    name = "Goading Attack",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to goad the target into attacking you. You add the superiority die to the attack’s damage roll, and the target must make a Wisdom saving throw. On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn.",
    class_id = 4
)
lunging_attack = Maneuver(
    name = "Lunging Attack",
    details = "When you make a melee weapon attack on your turn, you can expend one superiority die to increase your reach for that attack by 5 feet. If you hit, you add the superiority die to the attack’s damage roll.",
    class_id = 4
)
maneuvering_attack = Maneuver(
    name = "Maneuvering Attack",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to maneuver one of your comrades into a more advantageous position. You add the superiority die to the attack’s damage roll, and you choose a friendly creature who can see or hear you.",
    class_id = 4
)
menacing_attack = Maneuver(
    name = "Menacing Attack",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to frighten the target. You add the superiority die to the attack’s damage roll, and the target must make a Wisdom saving throw. On a failed save, it is frightened of you until the end of your next turn.",
    class_id = 4
)
parry = Maneuver(
    name = "Parry",
    details = "When another creature damages you with a melee attack, you can use your reaction and expend one superiority die to reduce the damage by the number you roll on your superiority die + your Dexterity modifier.",
    class_id = 4
)
precision_attack = Maneuver(
    name = "Precision Attack",
    details = "When you make a weapon attack roll against a creature, you can expend one superiority die to add it to the roll. You can use this maneuver before or after making the attack roll, but before any effects of the attack are applied.",
    class_id = 4
)
pushing_attack = Maneuver(
    name = "Pushing Attack",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to drive the target back. You add the superiority die to the attack’s damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you push the target up to 15 feet away from you.",
    class_id = 4
)
rally = Maneuver(
    name = "Rally",
    details = "On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to the superiority die roll + your Charisma modifier.",
    class_id = 4
)
riposte = Maneuver(
    name = "Riposte",
    details = "When a creature misses you with a melee attack, you can use your reaction and expend one superiority die to make a melee weapon attack against the creature. If you hit, you add the superiority die to the attack’s damage roll.",
    class_id = 4
)
sweeping_attack = Maneuver(
    name = "Sweeping Attack",
    details = "When you hit a creature with a melee weapon attack, you can expend one superiority die to attempt to damage another creature with the same attack. Choose another creature within 5 feet of the original target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to the number you roll on your superiority die. The damage is of the same type dealt by the original attack.",
    class_id = 4
)
trip_attack = Maneuver(
    name = "Trip Attack",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to knock the target down. You add the superiority die to the attack’s damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you knock the target prone.",
    class_id = 4
)

#? Scholar 
administer_aid = Maneuver(
    name = "Administer Aid",
    details = "As an action, you can expend a superiority die to tend to a creature you can touch. The creature regains a number of hit points equal to the number rolled + your Intelligence modifier.",
    class_id = 8
)
assess_the_situation = Maneuver(
    name = "Assess the Situation",
    details = "You can expend one superiority die to make a Wisdom (Perception) or Intelligence (Investigation) check as a bonus action, adding the superiority die to the check.",
    class_id = 8
)
crippling_strike = Maneuver(
    name = "Crippling Strike",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to cripple the creature. You add the superiority die to the attack’s damage roll and the creature’s gains 1 slowed level until the end of their next turn.",
    class_id = 8
)
deliberate_movement = Maneuver(
    name = "Deliberate Movement",
    details = "You can expend one superiority die to take the Disengage action as a bonus action and ignore the effects of standard difficult terrain until the end of your turn.",
    class_id = 8
)
exploit_weakness = Maneuver(
    name = "Exploit Weakness",
    details = "When you hit a creature with a weapon attack, you can expend a superiority die and deal additional damage equal to the number rolled. This damage cannot be reduced in any way.",
    class_id = 8
)
goading_attack_scholar = Maneuver(
    name = "Goading Attack",
    details = "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to goad the target into attacking you. You add the superiority die to the attack’s damage roll, and the target must make a Wisdom saving throw. On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn.",
    class_id = 8
)
heads_up = Maneuver(
    name = "Heads Up",
    details = "When a friendly creature who can see or hear you makes a saving throw, you can use your reaction and expend a superiority die, adding the number rolled to the result of the saving throw. You can use this maneuver before or after making the saving throw, but before any effects of the saving throw are determined.",
    class_id = 8
)
measured_action = Maneuver(
    name = "Measured Action",
    details = "As a reaction when you make a roll for a contested skill check, you can expend a superiority die to add to the roll. You can use this maneuver before or after making the contested skill check roll, but before any effects of the contested skill check are determined.",
    class_id = 8
)
one_step_ahead = Maneuver(
    name = "One Step Ahead",
    details = "When you roll initiative and you are not surprised, you can expend a superiority die and add the number rolled to your initiative.",
    class_id = 8
)
targeted_strike = Maneuver(
    name = "Targeted Strike",
    details = "When an ally makes an attack against a creature, you can use your reaction to expend a superiority die. You add the superiority die to the attack roll, and the damage roll if it hits. You can use this maneuver before or after the attack roll, but before the GM determines whether or not the attack hits.",
    class_id = 8
)

db.session.add_all([commander_strike, disarming_attack, distracting_strike, evasive_footwork, feinting_attack, goading_attack, lunging_attack, maneuvering_attack, menacing_attack, parry, precision_attack, pushing_attack, rally, riposte, sweeping_attack, trip_attack, administer_aid, assess_the_situation, crippling_strike, deliberate_movement, exploit_weakness, goading_attack_scholar, heads_up, measured_action, one_step_ahead, targeted_strike])
db.session.commit()
#-------------------------------------------------------------

#---------------------Guardian Auras--------------------------
aura_of_conquest = GuardianAura(
    name = "Aura of Conquest",
    details = "The auras are presented in alphabetical order. If multiple guardians grant the same aura, affected creatures can only benefit from it once. You must be conscious to grant the benefits of your auras.",
    class_id = 5
)
aura_of_conviction = GuardianAura(
    name = "Aura of Conviction",
    details = "Whenever a creature who is frightened of you starts its turn within 5 feet of you, its speed is reduced to 0 and that creature takes psychic damage equal to half your guardian level.",
    class_id = 5
)
aura_of_hatred = GuardianAura(
    name = "Aura of Hatred",
    details = "You and friendly creatures within 5 feet of you gain a bonus to the first melee weapon damage rolls you make each round equal to your Charisma modifier (minimum of +1).",
    class_id = 5
)
aura_of_presence = GuardianAura(
    name = "Aura of Presence",
    details = "Whenever you or a friendly creature within 5 feet of you must make a saving throw, the creature gains a bonus to the saving throw equal to your Wisdom modifier (minimum of +1).",
    class_id = 5
)
aura_of_protection = GuardianAura(
    name = "Aura of Protection",
    details = "Whenever a creature within 5 feet of you takes damage, you can use your reaction to take that damage instead of that creature taking it. This feature doesn’t transfer any other effects that might accompany the damage, and this damage can’t be reduced in any way.",
    class_id = 5
)
aura_of_vigor = GuardianAura(
    name = "Aura of Vigor",
    details = "Whenever a friendly creature starts its turn within 5 feet of you, that creature gains temporary hit points equal to your Wisdom or Charisma modifier (your choice, minimum of one).",
    class_id = 5
)
aura_of_warding = GuardianAura(
    name = "Aura of Warding",
    details = "You and friendly creatures within 5 feet of you have resistance to damage from force powers.",
    class_id = 5
)

db.session.add_all([aura_of_conquest, aura_of_conviction, aura_of_hatred, aura_of_presence, aura_of_protection, aura_of_vigor, aura_of_warding])
db.session.commit()
#-------------------------------------------------------------

#----------------------Monastic Vows--------------------------
vow_of_deflection = MonasticVows(
    name = "Vow of Deflection",
    details = "You can use your reaction to divert a strike when you are dealt damage by a melee weapon attack. When you do so, the damage taken by the attack is reduced by 1d10 + your Dexterity modifier + your monk level.",
    class_id = 6
)
vow_of_the_devoted = MonasticVows(
    name = "Vos of the Devoted",
    details = "You gain a limited ability to manipulate the Force. Force Powers Known. You learn 2 force powers of your choice. You learn an additional power at 3rd, 5th, 7th, 9th, 11th, 13th, 15th, and 17th level. You may not learn a force power of a level higher than your Max Power Level, and you may learn a force power at the same time you learn its prerequisite. You may only learn universal powers in this way. Force Points. Rather than force points, powers you learn through this vow are cast using your focus points, at 1 focus point per power level. You may only cast universal powers in this way. Max Power Level. Many force powers can be overpowered, consuming more focus points to create a greater effect. You can overpower these abilities to a maximum level, which increases at higher levels. Your Max Power Level is 1st. It increases to 2nd at 7th level, 3rd at 13th level, and 4th at 17th level. You may only cast force powers at 4th-level once. You regain the ability to do so after a long rest. Forcecasting Ability. You use your focus ability whenever a power refers to your forcecasting ability. If a power you cast with focus points calls for a saving throw, you use your focus save DC. If a power you cast with focus points calls for an attack roll, you use your focus attack modifier.",
    class_id = 6
)
vow_of_fate = MonasticVows(
    name = "Vow of Fate",
    prerequisite = "7th level",
    details = "When you finish a short or long rest, roll a d20 and record the number rolled. Once before your next short or long rest, you can replace any attack roll, saving throw, or ability check made by you or a creature within 5 feet of you with this roll. You must choose to do so before the roll.",
    class_id = 6
)
vow_of_the_fighter = MonasticVows(
    name = "Vow of the Fighter",
    details = "You adopt a particular style of fighting as your specialty. Choose one of the fighting Style options",
    class_id = 6
)
vow_of_the_focused = MonasticVows(
    name = "Vow of the Focused",
    details = "You can substitute Strength, Constitution, or Intelligence (chosen when you take this vow) for Wisdom or Charisma for your monk class features, except for other vows.",
    class_id = 6
)
vow_of_fortitude = MonasticVows(
    name = "Vow of Fortitude",
    prerequisite = "7th level",
    details = "You can use your action or bonus action to end one effect on yourself that is causing you to be blinded or deafened.",
    class_id = 6
)
vow_of_freedom = MonasticVows(
    name = "Vow of Freedom",
    details = "You ignore unenhanced difficult terrain, and when you would use your action to break free of an effect that is grappling or restraining you, you can instead use your bonus action.",
    class_id = 6
)
vow_of_intuition = MonasticVows(
    name = "Vow of Intuition",
    details = "You can no longer have disadvantage on attack rolls against creatures within 10 feet of you due to not being able to see them.",
    class_id = 6
)
vow_of_the_limber = MonasticVows(
    name = "Vow of the limber",
    prerequisite = "7th level",
    details = "When you make your first unarmed strike on your turn, you can choose to spend 1 focus point. If you do so, your reach with your unarmed strikes increases by 5 feet until the end of your turn.",
    class_id = 6
)
vow_of_the_nemesis = MonasticVows(
    name = "Vow of the Nemesis",
    prerequisite = "13th level",
    details = "As a bonus action, you can choose one creature within 30 feet that you can see. The creature must make a Wisdom saving throw against your focus save DC. On a successful save, the creature becomes immune to this feature for 24 hours. On a failed save, for the next minute, the creature has disadvantage on attack rolls against creatures other than you, and it must make an additional Wisdom saving throw each time it attempts to move to a space that is more than 30 feet away from you; if it succeeds on this saving throw, this feature doesn’t restrict its movement for that turn. This feature ends early if you attack another creature, if you target another hostile creature with a power or class feature, if a friendly creature damages the target, if a friendly creature targets it with a power or class feature, or if you target another creature with this feature.",
    class_id = 6
)
vow_of_the_open_mind = MonasticVows(
    name = "Vow of the Open Mind",
    details = "You gain proficiency in a skill of your choice. Additionally, you can spend 1 focus point and 10 minutes meditating on a skill in which you are proficient. If you do so, when you make an ability check with the chosen skill, you can add your Wisdom or Charisma modifier to the check if it doesn’t already include that modifier. You can only have one instance of this feature active at a time.",
    class_id = 6
)
vow_of_precision = MonasticVows(
    name = "Vow of Precision",
    prerequisite = "13th level",
    details = "Your critical hit range with unarmed strikes increases by 1",
    class_id = 6
)
vow_of_requital = MonasticVows(
    name = "Vow of Requital",
    prerequisite = "13th level",
    details = "When you take the Dodge action and an attack made by a creature within 5 feet of you misses you before the start of your next turn, you can use your reaction to make one melee weapon attack with a monk weapon or unarmed strike against that creature.",
    class_id = 6
)
vow_of_restoration = MonasticVows(
    name = "Vow of Restoration",
    details = "When you would make an unarmed strike, you can spend 1 focus point to instead touch a willing creature within your reach. Roll your Martial Arts die. The target gains hit points equal to the amount rolled + your Wisdom or Charisma modifier (your choice, minimum of +1).",
    class_id = 6
)
vow_of_the_sentry = MonasticVows(
    name = "Vow of the Sentry",
    details = "You gain proficiency in light and medium armor. Additionally, you can now gain the benefits of your Martial Arts and Unarmored Movement features while wearing light or medium armor as long as you are not wielding a shield.",
    class_id = 6
)
vow_of_serenity = MonasticVows(
    name = "Vow of Serenity",
    details = "Your maximum focus increases by an amount equal to half your Wisdom or Charisma modifier (your choice, rounded up, minimum of +1).",
    class_id = 6
)
vow_of_spirit = MonasticVows(
    name = "Vow of Spirit",
    details = "You can use your choice of Wisdom or Charisma instead of Strength or Dexterity for the attack and damage rolls of your unarmed strikes and monk weapons. You must use the same modifier for both rolls.",
    class_id = 6
)
vow_of_the_versatile = MonasticVows(
    name = "Vow of the Versatile",
    details = "When you would make an unarmed strike as part of your Martial Arts bonus action attack or your Flurry of Blows, you can instead make a melee weapon attack with a monk weapon you are wielding.",
    class_id = 6
)

db.session.add_all([vow_of_deflection, vow_of_the_devoted, vow_of_fate, vow_of_the_fighter, vow_of_the_focused, vow_of_fortitude, vow_of_freedom, vow_of_intuition, vow_of_the_limber, vow_of_the_nemesis, vow_of_the_open_mind, vow_of_precision, vow_of_requital, vow_of_restoration, vow_of_the_sentry, vow_of_serenity, vow_of_spirit, vow_of_the_versatile])
db.session.commit()
#-------------------------------------------------------------

#---------------------Operative Exploits----------------------
commanders_exploit = OperativeExploits(
    name = "Commander's Exploit",
    details = "You gain proficiency in medium armor.",
    class_id = 7
)
explorers_exploit = OperativeExploits(
    name = "Explorer's Explot",
    details = "You can hold your breath twice as long as you are normally able to, and take half as much damage from fall damage.",
    class_id = 7
)
fates_exploit = OperativeExploits(
    name = "Fate's Exploit",
    prerequisite = "7th",
    details = "When you finish a short or long rest, roll a d20 and record the number rolled. Once before your next short or long rest, you can replace any attack roll, saving throw, or ability check made by you or a creature within 5 feet of you with this roll. You must choose to do so before the roll.",
    class_id = 7
)
fighters_exploit = OperativeExploits(
    name = "Fighter's Exploit",
    details = "You adopt a particular style of fighting as your specialty. Choose one of the fighting Style options",
    class_id = 7
)
freedoms_exploit = OperativeExploits(
    name = "Freedom's Exploit",
    details = "You ignore unenhanced difficult terrain, and when you would use your action to break free of an effect that is grappling or restraining you, you can instead use your bonus action.",
    class_id = 7
)
gurrillas_exploit = OperativeExploits(
    name = "Gurrilla's Exploit",
    details = "You only need 3 hours of sleep during a long rest to gain its benefits, instead of 6. Additionally, if your long rest would be interrupted, you only need to complete the long rest instead of restarting it to gain its benefits. Lastly, you have advantage on saving throws against exhaustion.",
    class_id = 7
)
learners_exploit = OperativeExploits(
    name = "Learner's Exploit",
    details = "You gain proficiency in a skill and a tool, or two tools. You can select this exploit multiple times, each time choosing a new skill and a tool, or two new tools.",
    class_id = 7
)
mentors_exploit = OperativeExploits(
    name = "Mentor's Exploit",
    prerequisite = "13th",
    details = "Once per turn, whenever both you and a friendly creature within 60 feet that can see and hear you both have to make a saving throw to resist the same effect, you can choose to have disadvantage on the save. If you do so, the friendly creature gains advantage on the save. You can use this feature before or after you both make the saving throw, but you must do so before the GM says whether the save succeeds or fails.",
    class_id = 7
)
skills_exploit = OperativeExploits(
    name = "",
    details = "You learn an exploit that enhances your ability to apply your knowledge to combat situations. You can take this exploit multiple times. When you take the Attack action, you can use one of your skill exploits granted by this feature. You can use these features a combined number of times equal to your Intelligence modifier (a minimum of once). You regain any expended uses when you finish a long rest. Choose from the following. You must be proficient in the skill in order to take that skill’s exploit. Aim (Stealth). You attempt to line up a strike against a creature you can see that you are hidden from. Make a Dexterity (Stealth) check contested by the target’s Wisdom (Perception) check. If your check succeeds, you gain a +10 bonus to the first attack roll you make against the target before the end of your next turn. If your check fails, you are no longer hidden from the target. Angle (Perception). You attempt to predict the behavior of a humanoid you can see within 30 feet. Make a Wisdom (Perception) check contested by the target’s Dexterity (Sleight of Hand) check. If your check succeeds, the first attack roll the target makes before the start of your next turn has disadvantage, and the first saving throw the creature makes before the start of your next turn has disadvantage. If your check fails, you can’t use this feature on this target again for 1 hour. Battle Cry (Intimidation). You attempt to demoralize one humanoid you can see within 30 feet of you that can see and hear you. Make a Charisma (Intimidation) check contested by the target’s Wisdom (Insight) check. If your check succeeds, the target is frightened until the end of your next turn. If the target was already frightened of you, it must immediately drop whatever it is holding. On its next turn, if it is still frightened of you, it must take the Dash action and move away from you by the safest available route on its turn, unless there is nowhere to move. If your check fails, you can’t use this feature on this target again for 1 hour. Charm (Persuasion). You attempt to convince one humanoid you can see within 30 feet that can hear and understand you. Make a Charisma (Persuasion) check contested by the target’s Wisdom (Insight) check. If you have dealt damage to the creature in the last hour, it has advantage on the check. If your check succeeds, the target is charmed by you until the start of your next turn, and it has disadvantage on the first attack roll it makes against a creature before the end of its next turn. If your check fails, you can’t use this feature on this target again for 1 hour. Confuse Beast (Animal Handling). You attempt to confuse one beast on the battlefield. Make a Wisdom (Animal Handling) check contested by the target’s Wisdom (Insight) check. If your check succeeds, the beast cannot take actions or reactions until the end of your next turn. If your check fails, you can’t use this feature on this target again for 1 hour. Distract (Performance). You attempt to distract one beast or humanoid you can see within 30 feet of you that can see and hear you. Make a Charisma (Performance) check contested by the target’s Wisdom (Insight) check. If your check succeeds, the next attack roll made against the target before the start of its next turn has advantage. If your check fails, you can’t use this feature on this target again for 1 hour. Emulate Predator (Nature). You attempt to emulate the sounds of a natural predator of a beast or plant you can see within 30 feet. Make an Intelligence (Nature) check contested by the target’s Wisdom (Insight) check. If your check succeeds, the target must take the Dash action and move away from you by the safest available route on its turn, unless there is nowhere to move. If your check fails, you can’t use this feature on this target again for 1 hour. Feint (Deception). You attempt to divert the attention of a target you can see within 30 feet. Make a Charisma (Deception) check contested by the target’s Wisdom (Insight) check. If your check succeeds, the first attack roll made against the target before the start of your next turn by someone other than you has advantage, and the target has disadvantage on the first saving throw they make against an effect caused by a creature other than you before the start of your next turn. If your check fails, the target can’t be deceived by you in this way for 1 hour. Hacktivate (Technology). You attempt to determine the weaknesses in a droid you can see within 30 feet. Make an Intelligence (Technology) check contested by the target’s Intelligence (Technology) check. If your check succeeds, you have advantage on the next attack roll you make against the target before the end of your turn, and if you hit, you deal additional damage equal to your Intelligence modifier. If your check fails, you can’t use this feature on this target again for 1 hour. Instruct (Investigation). You attempt to find a weakness in your target. Make an Intelligence (Investigation) check contested by the target’s Charisma (Deception) check. If your check succeeds, if a friendly creature makes an attack roll against the target and they can see and hear you, you can use your reaction to grant them advantage on the roll. If you do so, and they hit, they deal additional damage equal to your bonus to Investigation checks. This damage is the same type as the attack’s damage. If your check fails, you can’t use this feature on this target again for 1 hour. Intuit (Insight). You attempt to determine the motivations of one humanoid you can see within 30 feet. Make a Wisdom (Insight) check contested by the target’s Charisma (Deception) check. If your check succeeds, the target can’t have advantage on ability checks, attack rolls, or saving throws against you until the end of your next turn. If your check fails, the target instead can’t have disadvantage on ability checks, attack rolls, or saving throws against you until the end of your next turn. Tumble (Acrobatics). You attempt to make a quick tumble, immediately moving 10 feet. If you begin or end this movement within a creature’s reach, make a Dexterity (Acrobatics) check contested by it’s Strength (Athletics) or Dexterity (Acrobatics) check (the target chooses the ability to use). If your check succeeds, this movement does not provoke opportunity attacks from it, and you have advantage on the first attack roll you make against it before the end of your turn. If your check fails, you immediately fall prone. Pocket Sand (Sleight of Hand). You attempt to blind one beast or humanoid you can see within 15 feet of you. Make a Dexterity (Sleight of Hand) check contested by the target’s Wisdom (Perception) check. If your check succeeds, the target is blinded until the end of your turn. If your check fails, you can’t use this feature on this target again for 1 hour. Precision Strike (Medicine). You attempt to strike a pressure point in one humanoid within your reach. Make a Wisdom (Medicine) check contested by the target’s Strength (Athletics) or Dexterity (Acrobatics) check (the target chooses the ability to use). If your check succeeds, they are incapacitated until the end of their next turn. If your check fails, you can’t use this feature on this target again for 1 hour. Snare (Survival). You attempt to cause a creature within 30 feet of you to stumble. Make a Wisdom (Survival) check contested by the target’s Wisdom (Perception) check. If your check succeeds, and the target moves towards you before the start of your next turn, it gains 1 slowed level, and you can use your reaction to cause it to fall prone. If your check fails, you can’t use this feature on this target again for 1 hour. Spin (Piloting). You attempt to confound a piloted construct you can see within 30 feet. Make an Intelligence (Piloting) check contested by the target’s Intelligence (Piloting) check. If your check succeeds, the target has disadvantage on attack rolls against you, and you have advantage on Dexterity saving throws against the target, until the start of your next turn. If your check fails, the target instead has advantage on attack rolls against you, and you have disadvantage on Dexterity saving throws against the target, until the start of your next turn. Study (Lore). You attempt to anticipate your target’s action. Make an Intelligence (Lore) check contested by the target’s Charisma (Deception) check. If your check succeeds, you have advantage on the first ability check, attack roll or saving throw you make against that creature before the end of your next turn. Alternatively, before the end of your next turn, you can use your reaction to grant disadvantage on the first ability check, attack roll, or saving throw the target makes against you. If your check fails, you instead have disadvantage on the first ability check, attack roll or saving throw you make against that creature before the end of your next turn. Wrestle (Athletics). You attempt to grab and pin a creature within 5 feet of you with at least one free hand. The target must be no more than one size larger than you. Make a Strength (Athletics) check contested by the target’s Strength (Athletics) or Dexterity (Acrobatics) check (the target chooses the ability to use). If your check succeeds, the target is both grappled and restrained by you. If the target stops being grappled, it also stops being restrained. If your check fails, you can’t use this feature on this target again for 1 hour.",
    class_id = 7
)
technologists_exploit = OperativeExploits(
    name = "Technologist's Exploit",
    details = "You learn and can cast one 1st-level tech power once per long rest. Your techcasting ability is Intelligence. You require use of a wristpad for this power. You can select this exploit multiple times. Each time you do so, you must choose a different power.",
    class_id = 7
)
weaponmasters_exploit = OperativeExploits(
    name = "Weaponmaster's Exploit",
    details = "You gain proficiency in three blasters or vibroweapons that lack the heavy and strength properties. You can select this exploit multiple times. Each time you do so, you must choose different weapons.",
    class_id = 7
)

db.session.add_all([commanders_exploit, explorers_exploit, fates_exploit, fighters_exploit, freedoms_exploit, gurrillas_exploit, learners_exploit, mentors_exploit, skills_exploit, technologists_exploit, weaponmasters_exploit])
db.session.commit()
#-------------------------------------------------------------

#---------------------Scholar Discoveries---------------------
academic_memory = ScholarDiscovery(
    name = "Academic Memory",
    details = "You can recall anything you have read in the past month that you understand. This includes but is not limited to books, maps, signs, and lists.",
    class_id = 8
)
adaptive = ScholarDiscovery(
    name = "Adaptive",
    prerequisite = "15th",
    details = "When the target of your Critical Analysis feature is reduced to 0 hit points, you can use your reaction to change the target of your analysis to another creature within range.",
    class_id = 8
)
ambassador = ScholarDiscovery(
    name = "Ambassador",
    details = "You learn three additional languages of your choice. You may choose this discovery multiple times.",
    class_id = 8
)
clever_application = ScholarDiscovery(
    name = "Clever Applications",
    details = "You gain proficiency with improvised weapons, and they gain the finesse property for you. Additionally, when you make an attack with an improvised weapon, it deals 1d6 damage. You can use your Sage Advice feature to give friendly creatures improvised weapon proficiency if they don’t already have it, following the same rules of that feature as if it were a skill or tool. The friendly creatures retain this proficiency for the entire duration instead.",
    class_id = 8
)
mental_prowess = ScholarDiscovery(
    name = "Mental Prowess",
    details = "When you make a Strength (Athletics) or Dexterity (Acrobatics) check to grapple a creature or break out of a grapple, net, and other restraining equipment, you can use your Intelligence modifier instead of Strength or Dexterity.",
    class_id = 8
)
hardened_mind = ScholarDiscovery(
    name = "Hardened Mind",
    prerequisite = "9th",
    details = "You have advantage on saving throws against illusions and on Intelligence checks to discern them from reality. You also gain resistance to psychic damage.",
    class_id = 8
)
lifelong_learning = ScholarDiscovery(
    name = "Lifelong Learning",
    details = "You gain proficiency in a skill and a tool, or two tools. You can select this discovery multiple times, each time choosing a new skill and a tool, or two new tools.",
    class_id = 8
)
lingering_advice = ScholarDiscovery(
    name = "Lingering Advice",
    prerequisite = "5th",
    details = "When you use your Sage Advice feature, the targeted creatures retain the benefit from your instruction for the full duration.",
    class_id = 8
)
masters_advice = ScholarDiscovery(
    name = "Master's Advice",
    details = "When you use your Sage Advice feature, the first time each targeted creature makes the chosen skill check, they gain an additional bonus to the roll equal to your Intelligence modifier.",
    class_id = 8
)
perfect_maneuver = ScholarDiscovery(
    name = "Perfect Maneuver",
    prerequisite = "15th",
    details = "When you roll a 1 on a superiority die, you can reroll the die and must use the new roll.",
    class_id = 8
)
quick_analysis = ScholarDiscovery(
    name = "Quick Analysis",
    prerequisite = "9th",
    details = "When you roll initiative and aren’t surprised, you can use your reaction to use your Critical Analysis feature.",
    class_id = 8
)
rancors_discipline = ScholarDiscovery(
    name = "Rancor's Discipline",
    details = "You can substitute Wisdom or Charisma (chosen when you study this discipline) for Intelligence for your scholar class features, except for other discoveries.",
    class_id = 8
)
reliable_sources = ScholarDiscovery(
    name = "Reliable Sources",
    prerequisite = "9th",
    details = "When you make an Intelligence (Lore) or Intelligence (Nature) skill check that lets you add your proficiency bonus, you can treat a d20 roll of 9 or lower as a 10.",
    class_id = 8
)
resolute = ScholarDiscovery(
    name = "Resolute",
    details = "When you make a saving throw to resist charm and fear effects, you may add your Intelligence modifier to the roll.",
    class_id = 8
)
runnin_on_fumes = ScholarDiscovery(
    name = "Running on Fumes",
    details = "You only need 3 hours of sleep during a long rest to gain its benefits, instead of 6. Additionally, if your long rest would be interrupted, you only need to complete the long rest instead of restarting it to gain its benefits. Lastly, you have advantage on saving throws against exhaustion.",
    class_id = 8
)
survival_expert = ScholarDiscovery(
    name = "Survival Expert",
    details = "When you make a Survival skill check, you may use your Intelligence modifier instead of your Wisdom modifier. Additionally, you have advantage on saving throws against poison.",
    class_id = 8
)
targeted_analysis = ScholarDiscovery(
    name = "targeted Analysis",
    prerequisite = "5th",
    details = "Your attack rolls against the target of your Critical Analysis feature cannot suffer from disadvantage.",
    class_id = 8
)
tech_amateur = ScholarDiscovery(
    name = "Tech Amateur",
    details = "You learn and can cast one 1st-level tech power once per long rest. Your techcasting ability is Intelligence. You require use of a wristpad for this power. You can select this discovery multiple times. Each time you do so, you must choose a different power.",
    class_id = 8
)
universal_language = ScholarDiscovery(
    name = "Universal Language",
    details = "You can communicate simple ideas with any creature with an Intelligence score of 6 or higher through basic expressions and gestures.",
    class_id = 8
)

db.session.add_all([academic_memory, adaptive, ambassador, clever_application, mental_prowess, hardened_mind, lifelong_learning, lingering_advice, masters_advice, perfect_maneuver, quick_analysis, rancors_discipline, reliable_sources, resolute, runnin_on_fumes, survival_expert, targeted_analysis, tech_amateur, universal_language])
db.session.commit()
#-------------------------------------------------------------

#---------------------Scout Routines--------------------------
adaptability_routine = ScoutRoutine(
    name = "Adaptability Routine",
    details = "At the start of each of your turns, you can choose an ability score with a saving throw in which you are not proficient. Until the start of your next turn, you add half your proficiency bonus, rounded down, to saving throws you make with the chosen ability. Alternatively, you can choose to extend this benefit to friendly creatures within 5 feet of you, except for you.",
    class_id = 9
)
mavens_routine = ScoutRoutine(
    name = "Maven's Routine",
    details = "At the start of each of your turns, you can choose to gain resistance to damage from tech powers until the start of your next turn. Alternatively, you can choose to extend this benefit to friendly creatures within 5 feet of you, except for you.",
    class_id = 9
)
mesmers_routine = ScoutRoutine(
    name = "Mesmer's Routine",
    details = "At the start of each of your turns, you can choose to have advantage on saving throws against effects that would incapacitate you or put you to sleep until the start of your next turn. Alternatively, you can choose to extend this benefit to friendly creatures within 5 feet of you, except for you",
    class_id = 9
)
nomads_routine = ScoutRoutine(
    name = "Nomad's Routine",
    details = "At the start of each of your turns, you can choose to gain advantage on Constitution saving throws to avoid exhaustion from unenhanced sources, as well as being naturally adapted to both hot and cold climates. Alternatively, you can choose to extend this benefit to friendly creatures within 5 feet of you, except for you.",
    class_id = 9
)
responders_routine = ScoutRoutine(
    name = "Responder's routine",
    details = "When you roll initiative, you can choose to add your proficiency bonus to the initiative roll and have advantage on attack rolls against creatures that have not yet acted. Alternatively, you can choose to allow each creature within 5 feet of you, including you, to add half your proficiency bonus to the initiative roll and have advantage on the first attack roll they make against a creature that has not yet acted.",
    class_id = 9
)
sharpshooters_routine = ScoutRoutine(
    name = "Sharpshooter's Routine",
    details = "At the start of each of your turns, you can choose to gain a bonus to the first weapon attack roll you make before the start of your next turn equal to your Intelligence modifier. Alternatively, you can choose to allow each creature within 5 feet of you, including you, to add half your Intelligence modifier to the first weapon attack roll they make before the start of your next turn.",
    class_id = 9
)
striders_routine = ScoutRoutine(
    name = "Strider's Routine",
    details = "At the start of each of your turns, you can choose to have each slowed level only reduce your speed by 5 feet, unless it would reduce your speed to 0 until the start of your next turn. Alternatively, you can choose to extend this benefit to friendly creatures within 5 feet of you, except for you.",
    class_id = 9
)
wardens_routine = ScoutRoutine(
    name = "Warden's Routine",
    details = "At the start of each of your turns, you can choose to gain a climbing and swimming speed equal to your walking speed. Alternatively, you can choose to extend this benefit to friendly creatures within 5 feet of you, except for you.",
    class_id = 9
)

db.session.add_all([adaptability_routine, mavens_routine, mesmers_routine, nomads_routine, responders_routine, sharpshooters_routine, striders_routine, wardens_routine])
db.session.commit()
#-------------------------------------------------------------

#-----------------------Sentinel Ideals-----------------------
ideal_of_the_agile = SentinelIdeals(
    name = "Ideal of the Agile",
    details = "You gain a swimming speed and a climbing speed equal to your walking speed. When you make a long jump, you can cover a number of feet up to twice your Wisdom or Charisma score (your choice). When you make a high jump, you can leap a number of feet up into the air equal to 3 + twice your Wisdom or Charisma modifier (your choice). Additionally, as a bonus action, you can manifest this ideal in a brief surge of energy. For the next minute, opportunity attacks against you are made with disadvantage.",
    class_id = 10
)
ideal_of_the_artisan = SentinelIdeals(
    name = "Ideal of the Artisan",
    details = "Choose one of your skill or tool proficiencies. When you make an ability check with the chosen skill or tool, you can add half your Wisdom or Charisma modifier (your choice, minimum of one) to any check you make that doesn’t already include that modifier. Additionally, as an action, you can manifest this ideal in a brief surge of energy. For the next 10 minutes, the bonus increases to your Wisdom or Charisma modifier, and you can choose a second skill or tool to extend this feature to.",
    class_id = 10
)
ideal_of_the_contender = SentinelIdeals(
    name = "Ideal of the Contender",
    details = "You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes, and your unarmed strike damage increases by one step (from 1 to d4, d4 to d6, or d6 to d8). Additionally, as a bonus action, you can manifest this ideal in a brief surge of energy. For the next minute, your unarmed strikes count as enhanced for the purpose of overcoming resistance and immunity to unenhanced attacks and damage, and you can use your Wisdom or Charisma modifier (your choice) instead of Strength for checks made to grapple a target or escape a grapple.",
    class_id = 10
)
ideal_of_the_fighter = SentinelIdeals(
    name = "ideal of the Fighter",
    details = "You adopt a particular style of fighting as your specialty. Choose one of the fighting style options. Additionally, as a bonus action, you can manifest this ideal in a brief surge of energy. For the next minute, you know the fighting mastery that corresponds with the fighting style you chose with this feature. If you already know that fighting mastery, you instead learn another of your choice for the duration.",
    class_id = 10
)
ideal_of_the_hunter = SentinelIdeals(
    name = "Ideal of the Hunter",
    details = "You gain darkvision out to a range of 60 feet. If you already have darkvision, this ideal increases its range by 30 feet. Additionally, as a bonus action, you can manifest this ideal in a brief surge of energy. For the next minute, you can see normally in enhanced darkness, and you gain blindsight to 10 feet.",
    class_id = 10
)
ideal_of_the_steadfast = SentinelIdeals(
    name = "Ideal of the Steadfast",
    details = "When you would make a melee weapon attack roll, you can instead force the target to make a Dexterity saving throw (DC = 8 + your bonus to attacks with the weapon). If you would have advantage on your attack roll, the creature instead has disadvantage on their saving throw, and if you would have disadvantage on your attack roll, the creature instead has advantage on their saving throw. On a failed save, the target takes normal weapon damage and is subjected to any additional effects that would occur on a hit. Additionally, as a bonus action, you can manifest this ideal in a brief surge of energy. For the next minute, when a creature succeeds on the saving throw, they take half the normal weapon damage, and when a creature rolls a 1 on the saving throw, they treat the damage as if you had rolled the maximum.",
    class_id = 10
)
ideal_of_the_titan = SentinelIdeals(
    name = "Ideal of the titan",
    details = "You gain proficiency in medium armor. Additionally, as a bonus action, you can manifest this ideal in a brief surge of energy. For the next minute, you have advantage on ability checks and attack rolls that would forcefully move another creature, and the distance they would be moved increases by 5 feet.",
    class_id = 10
)
ideal_of_the_tranquil = SentinelIdeals(
    name = "Ideal of the Tranquil",
    details = "When you finish a short or long rest, you gain a number of temporary force points equal to half your Wisdom or Charisma modifier (rounded up, your choice, minimum of one). When you would spend a force point while you have temporary force points, the temporary force points are spent first. All temporary force points are lost at the end of your next short or long rest. Additionally, as an action, you can manifest this ideal in a brief surge of energy. You regain a number of force points equal to half your Wisdom or Charisma modifier (rounded up, your choice, minimum of one).",
    class_id = 10
)
ideal_of_the_vigorous = SentinelIdeals(
    name = "Ideal of the Vigorous",
    details = "When you roll a Hit Die to regain hit points, you may use your Wisdom or Charisma modifier in place of your Constitution modifier when determining the number of hit points you regain. Additionally, as an action, you can manifest this ideal in a brief surge of energy. You gain a number of temporary hit points equal to half your sentinel level (rounded down) + your Wisdom or Charisma modifier (your choice, minimum of one).",
    class_id = 10
)

db.session.add_all([ideal_of_the_agile, ideal_of_the_artisan, ideal_of_the_contender, ideal_of_the_fighter, ideal_of_the_hunter, ideal_of_the_steadfast, ideal_of_the_titan, ideal_of_the_tranquil, ideal_of_the_vigorous])
db.session.commit()
#-------------------------------------------------------------

#--------------------Class Archetypes-------------------------
ballistic_approach = Archetype(
    name = "Ballistic Approach",
    caster_type = "None",
    features = {
        "1": {
            "name": "Firestorm",
            "levels": ["3rd"],
            "details": "You gain proficiency in martial blasters with the burst or rapid property. Additionally, you’ve learned to use ranged weapons with untold fury. While wielding a blaster with which you are proficient, you gain the following benefits: When making a ranged weapon attack while within 30 feet of your target, you use your choice of Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls. When you use a blaster as an improvised weapon, you are considered proficient with it."
        },
        "2": {
            "name": "Explosive",
            "levels": ["3rd", "9th"],
            "details": "While raging, you gain the following benefits: When you roll a 1 or 2 on a damage die for an attack made with a blaster weapon, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. You add your rage damage to damage rolls from ranged weapon attacks using Strength. You may only apply your rage damage to one target when you use the burst property. At 9th level, when a creature rolls a 1 on a saving throw against your burst or rapid property, you can add your Brutal Critical dice to the damage."
        },
        "3": {
            "name": "Rampage",
            "levels": ["6th"],
            "details": "While raging, when you deal damage with a blaster with which you are proficient, and you added your Strength modifier to the damage roll, you can use a bonus action to move up to half your speed towards your target. You must end this movement closer to your target than you started. If you end this movement within 5 feet of your target, you can make one melee weapon attack with your blaster as a part of this bonus action. Additionally, when a creature rolls a 1 on a saving throw against your burst or rapid property, you can apply your Brutal Critical dice to the roll against that creature."
        },
        "4": {
            "name": "Down, Not Out",
            "levels": ["10th"],
            "details": "When you are hit with an attack by a creature within 30 feet of you, you can use your reaction to make a single attack against that creature with a blaster with which you are proficient."
        },
        "5": {
            "name": "Brawn",
            "levels": ["14th"],
            "details": "When you use the burst property of a blaster with which are you proficient, you can apply your rage damage bonus to every target that takes damage, instead of just one. Additionally, when a creature fails the saving throw against your burst or rapid property, it is knocked prone."
        }
    },
    class_id = 1
)
marauder_approach = Archetype(
    name = "Marauder Approach",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Forcecasting",
            "levels": ["3rd"],
            "details": "You have derived powers from your primal connection to the Force. You learn 4 force powers of your choice, and you learn more at higher levels. You may not learn a force power of a level higher than your Max Power Level, and you may learn a force power at the same time you learn its prerequisite. You have a number of force points equal to your berserker level + your Wisdom or Charisma modifier (your choice). You use these force points to cast force powers. You regain all expended force points when you finish a long rest. Many force powers can be overpowered, consuming more force points to create a greater effect. You can overpower these abilities to a maximum level, which increases at higher levels. You may only cast force powers at 4th-level once. You regain the ability to do so after a long rest. Your forcecasting ability varies based on the alignment of the powers you cast. You use Wisdom for light side powers, Charisma for dark side powers, and Wisdom or Charisma for universal powers (your choice). You use this ability score modifier whenever a power refers to your forcecasting ability. Additionally, you use this ability score modifier when setting the saving throw DC for a force power you cast and when making an attack roll with one. Force save DC = 8 + your proficiency bonus + your forcecasting ability modifier. Force attack modifier = your proficiency bonus + your forcecasting ability modifier." 
        },
        "2": {
            "name": "Furious Force",
            "levels": ["3rd"],
            "details": "You can cast force powers while raging as long as the power’s casting time is no more than 1 action, the power does not require concentration, and you are not wearing heavy armor or wielding a medium or heavy shield. While raging, you add your rage damage to damage rolls from force powers you cast that require a force attack or saving throw. If a force power damages more than one target, you may only apply your rage damage to one of them. Casting force powers during rage counts as attacking for the purposes of maintaining rage, and you can use your Reckless Attack feature to gain advantage when casting a force power that requires a force attack."
        },
        "3": {
            "name": "Reckless Power",
            "levels": ["6th"],
            "details": "Weapons and the force are equally an extension of your rage. While you are raging and you use your action to cast a force power, you can make a single melee weapon attack as a bonus action."
        }, 
        "4": {
            "name": "Powerful Pressence",
            "levels": ["10th"],
            "details": "As a bonus action, you unleash a battle cry infused with force energy. Choose up to ten other creatures of within 60 feet of you that can hear you. Friendly creatures have advantage on attack rolls and saving throws until the start of your next turn, and hostile creatures have disadvantage on attack rolls and saving throws until the end of your next turn. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        }, 
        "5": {
            "name": "Force Storm",
            "levels": ["14th"],
            "details": "You can expel the might of your rage all at once to unleash a devastating storm of force energy. As an action, you can end your rage early, forcing each creature within 15 feet of you to make a Dexterity saving throw against your universal force save DC. On a failed save, a creature takes 1d12 force damage for each round you’ve spent in rage, or half as much on a successful one."
        },
        "marauder_table": {
            "3": {
                "force powers known": "4",
                "force points": "3",
                "max power level": "1st"
            },
            "4": {
                "force powers known": "6",
                "force points": "4",
                "max power level": "1st"
            },
            "5": {
                "force powers known": "7",
                "force points": "5",
                "max power level": "1st"
            },
            "6": {
                "force powers known": "8",
                "force points": "6",
                "max power level": "1st"
            },
            "7": {
                "force powers known": "10",
                "force points": "7",
                "max power level": "2nd"
            },
            "8": {
                "force powers known": "11",
                "force points": "8",
                "max power level": "2nd"
            },
            "9": {
                "force powers known": "12",
                "force points": "9",
                "max power level": "2nd"
            },
            "10": {
                "force powers known": "13",
                "force points": "10",
                "max power level": "2nd"
            },
            "11": {
                "force powers known": "14",
                "force points": "11",
                "max power level": "2nd"
            },
            "12": {
                "force powers known": "15",
                "force points": "12",
                "max power level": "2nd"
            },
            "13": {
                "force powers known": "17",
                "force points": "13",
                "max power level": "3rd"
            },
            "14": {
                "force powers known": "18",
                "force points": "14",
                "max power level": "3rd"
            },
            "15": {
                "force powers known": "19",
                "force points": "15",
                "max power level": "3rd"
            },
            "16": {
                "force powers known": "20",
                "force points": "16",
                "max power level": "3rd"
            },
            "17": {
                "force powers known": "22",
                "force points": "17",
                "max power level": "4th"
            },
            "18": {
                "force powers known": "23",
                "force points": "18",
                "max power level": "4th"
            },
            "19": {
                "force powers known": "24",
                "force points": "19",
                "max power level": "4th"
            },
            "20": {
                "force powers known": "25",
                "force points": "20",
                "max power level": "4th"
            }
        }
    },
    class_id = 1
)
precision_approach = Archetype(
    name = "Precision Approach",
    caster_type = "None",
    features = {
        "1": {
            "name": "Careful Steps",
            "levels": ["3rd"],
            "details": "You gain skills that represent your precise movement. You gain proficiency in your choice of Acrobatics or Stealth. While raging, you have advantage on checks you make with the chosen skill."
        },
         "2": {
            "name": "Focused Rage",
            "levels": ["3rd"],
            "details": "You hone your rage to a razor sharp focus. While raging, when you make a melee weapon attack using Dexterity, you add your rage damage to the damage roll. Additionally, you can use your Reckless Attack feature to give you advantage on melee weapon attacks using Dexterity during your turn."
        },
        "3": {
            "name": "Battle Anticapation",
            "levels": ["6th"],
            "details": "While raging, your critical hit range with melee weapon attacks using Dexterity increases by 1."
        },
        "4": {
            "name": "Improved Danger Sense",
            "levels": ["10th"],
            "details": "While raging, when you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage against effects that you can see, such as traps and powers, you are treated as proficient in the save, and you instead take no damage if you succeed on a saving throw, and only half damage if you fail."
        },
        "5": {
            "name": "Calm within the Storm",
            "levels": ["14th"],
            "details": "The precision with which you act during your rage causes you to become a storm of reactive lethality. When you use your Reckless Attack feature, you can make a number of opportunity attacks equal to your proficiency bonus without using your reaction, and when a creature within 5 feet of you misses you with an attack, you can use your reaction to make a melee weapon attack using Dexterity against that creature. You can only take one reaction per turn."
        }
    },
    class_id = 1
)
warchief_approach = Archetype(
    name = "Warchief Approach",
    caster_type = "None",
    features = {
        "1": {
            "name": "Savage Diplomat",
            "levels": ["3rd"],
            "details": "Your path necessitates that you build relationships with others, for the betterment of your tribe or yourself. You gain proficiency in one of the following skills of your choice: Persuasion or Intimidation. You can choose to learn one language in place of the skill proficiency."
        },
        "2": {
            "name": "Commanding Rage",
            "levels": ["3rd"],
            "details": "You become more aware of your allies, and their intent when fighting at your side. While you are raging, when an ally within 10 feet of you makes an attack roll against an enemy, you can use your reaction to grant advantage to that attack and add your rage damage bonus to the damage roll, if the attack hits. You can use this feature a number of times equal to your proficiency bonus, as shown in the berserker table. You regain all expended uses when you complete a short or long rest."
        },
        "3": {
            "name": "Inspiring Presence",
            "levels": ["6th"],
            "details": "Your mere presence on the battlefield rallies your allies. When you rage, choose up to 3 allies that you can see within 30 feet of you. Each creature gains temporary hit points equal to half your berserker level (rounded down) + your Charisma modifier (minimum of one)."
        }, 
        "4": {
            "name": "Raid Planning",
            "levels": ["10th"],
            "details": "You learn to flare up your allies’ drive for combat, urging them to follow you into the fray. During a long rest, you tell sagas, sing battle songs, and give inspiring speeches. At the end of the long rest choose up to 5 creatures that can hear and understand you (which can include yourself) to add your Charisma modifier (minimum of one) to their next initiative roll, and a 10 foot bonus to their speed on their first turn of combat."
        },
        "5": {
            "name": "War Chant",
            "levels": ["14th"],
            "details": "You have memorized the litanies, songs, and chants of your people and their dedication to war. When you enter a rage on your turn, you can enter a commanding rage for one minute. When you do so, during this turn and at the start of each of your turns, you have a number of special reactions equal to your proficiency bonus you can only use for your Commanding Rage feature. When you use Commanding Rage with these special reactions, they do not count against your uses of that feature. You can only use one reaction per turn. Additionally, during this rage, when an enemy within 10 feet of you makes an attack roll against an ally, you can use your reaction to reduce the attack by an amount equal to your Charisma modifier. Once you’ve used this feature, you must complete a long rest before you can use it again."
        }
    },
    class_id = 1
)
way_of_balance = Archetype(
    name = "Way of Balance",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Force Barrier",
            "levels": ["3rd"],
            "details": "You can weave the Force around yourself for protection. When you cast a universal power of 1st level or higher, you can simultaneously manipulate the Force to create a barrier on yourself that lasts until you finish a long rest. The barrier has hit points equal to twice your consular level + your Wisdom or Charisma modifier (your choice). Your barrier can never have hit points greater than twice your consular level + your Wisdom or Charisma modifier (your choice). Whenever you take damage, the barrier takes the damage instead. If this damage reduces the barrier to 0 hit points, you take any remaining damage. While the barrier has 0 hit points, it can’t absorb damage, but its power remains. Whenever you cast a universal power of 1st level or higher, the barrier regains a number of hit points equal to twice the level of the power. Once you create the barrier, you can’t create it again until you finish a long rest."
        },
        "2": {
            "name": "Projected Barrier",
            "levels": ["6th"],
            "details": "When a creature that you can see within 30 feet of you takes damage, you can use your reaction to cause your Force Barrier to absorb that damage. If this damage reduces the barrier to 0 hit points, the warded creature takes any remaining damage."
        },
        "3": {
            "name": "At-Will Barrier",
            "levels": ["10th"],
            "details": "Your at-will universal powers grant a small boost to your Force Barrier. When you cast an at-will universal power, the barrier regains 1 hit point. You can’t restore your barrier above half its maximum hit points in this way."
        },
        "4": {
            "name": "Improved Suppression",
            "levels": ["14th"],
            "details": "At 14th level, when you cast a force power that requires you to make an ability check as a part of casting that power, such as sever force or force suppression, you add your proficiency bonus to that ability check."
        },
        "5": {
            "name": "Force Resistance",
            "levels": ["18th"],
            "details": "Starting at 18th level, you have advantage on saving throws against force powers. Additionally, you have resistance against the damage of force powers."
        },
    },
    class_id = 2
)
way_of_lightning = Archetype(
    name = "Way of Lightning",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Shocking Affinity",
            "levels": ["3rd"],
            "details": "When you cast a force power that deals lightning damage, you can use Wisdom or Charisma as your forcecasting ability for it. Additionally, when you cast a damage-dealing force power that requires a force attack or saving throw, you can cause that power to instead deal lightning damage. If the power would call for a saving throw other than Dexterity, it instead calls for a Dexterity saving throw. If you hit with the power, or the target fails the power’s saving throw, affected creatures become shocked until the start of your next turn. You can use this feature a number of times equal to your Wisdom or Charisma modifier (your choice, a minimum of once). You regain all expended uses when you finish a short or long rest."
        },
        "2": {
            "name": "Potent Lightning",
            "levels": ["6th"],
            "details": "You add your governing ability modifier (minimum of +1) to any damage you deal with force powers that deal lightning damage that don’t already include that modifier."
        }, 
        "3": {
            "name": "",
            "levels": ["10th"],
            "details": "When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. On a failed save, the creature takes 1d10 plus your consular level lightning damage, is pushed back 10 feet, and becomes shocked until the end of their next turn. On a successful save, the creature takes half as much damage and isn’t moved or shocked. You can use this feature a number of times equal to your Wisdom or Charisma modifier (your choice, a minimum of once). You regain all expended uses when you finish a long rest."
        },
        "4": {
            "name": "Electric Attunement",
            "levels": ["14th"],
            "details": "You gain resistance to lightning damage, and force powers you cast ignore resistance to lightning damage."
        },
        "5": {
            "name": "You can increase the power of your simpler lightning force powers. When you cast a force power of 1st through 6th level that deals lightning damage, you can deal maximum damage with that power. You can use this feature with no adverse effects a number of times equal to your Wisdom or Charisma modifier (your choice, a minimum of once). If you use this feature beyond this before you finish a long rest, you take 2d12 true damage for each level of the power, immediately after you cast it. Each time you use this feature again before finishing a long rest, the damage increases by 1d12.",
            "levels": ["18th"],
            "details": "Unlimited Power"
        },
    },
    class_id = 2
)
way_of_suggestion = Archetype(
    name = "Way of Suggestion",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Subtle Control",
            "levels": ["3rd"],
            "details": "You can befuddle a creature’s mind with nothing but a gesture. As an action, you can cause a creature you can see within 30 feet to make a Wisdom saving throw against your universal force save DC. On a failed save, you can force the creature to believe or forget a single aspect of a conversation, observation or encounter it had that you were present for in the past 10 minutes. Whether the creature succeeds or fails their saving throw, you can’t use this feature on them again until you finish a long rest. Additionally, creatures who attempt to detect your use of the Force have disadvantage on ability checks to do so, and if a creature has the sense force or force sight power active, they must succeed on a universal forcecasting ability check against your universal force save DC in order to notice your usage of the Force, your alignment within the Force, or how strong your connection to the Force is."
        },
        "2": {
            "name": "Out of Mind",
            "levels": ["6th"],
            "details": "You can erase yourself from a single creature’s sight momentarily. As a bonus action, choose a creature within 60 feet of you that you are aware of. That creature must make a Wisdom saving throw against your universal force save DC. On a failed save, you become invisible to that creature for 1 minute, or until you deal damage to it. Once you’ve used this feature, you can’t use it again until you finish a short or long rest."
        },  
        "3": {
            "name": "Delicate Potency",
            "levels": ["10th"],
            "details": "Your mind-affecting powers are particularly potent. When you cast one of cloud mind, dominate mind, mass coerce mind, and dominate monster, you can choose to treat the power as if cast at your Max Power Level. You can use this feature a number of times equal to your Wisdom or Charisma modifier (your choice, a minimum of once). You regain all expended uses when you finish a long rest."
        },
        "4": {
            "name": "Delayed Effect",
            "levels": ["18th"],
            "details": "When you cast a force power, you can delay the effects of the force power for up to a number of rounds equal to half your consular level. If you do so, the power immediately takes effect at the start of your turn, after the specified number of rounds have passed. Once you’ve used this feature, you can’t use it again until you complete a long rest."
        },
        "5": {
            "name": "",
            "levels": [""],
            "details": "You’ve learned how to weave the Force around you in a cloak of your choice. As an action, you can focus the Force for 10 minutes. For the duration, you gain your choice of one of the following effects. You can use each feature once. You regain all expended uses when you complete a long rest. Cloak of Fright: Each creature of your choice that is within 60 feet must succeed on a Wisdom saving throw against your universal force save DC or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. Cloak of Invisibility: You and everything you are wearing or carrying become invisible to creatures of your choice. If you damage a creature or affect it with a force power, it can make a Wisdom saving throw against your universal force save DC. On a success, you are no longer invisible to that creature. Cloak of Memory: Creatures that see you or any allies within 30 feet of you during this time cannot recall your physical appearances, your mannerisms, or any other identifying features. Creatures that interact with you must make a Wisdom saving throw against your universal force save DC once the interaction ends. You can choose to exclude a creature from this effect. On a failed save, the creature forgets all details of the interaction, rationalizing any of its outcomes."
        },
    },
    class_id = 2
)
way_of_the_sage = Archetype(
    name = "Way of the Sage",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Disciple of Life",
            "levels": ["3rd"],
            "details": "When you cast a force power that restores hit points, you can use Wisdom or Charisma as your forcecasting ability for it. Additionally, whenever you use a force power of 1st level or higher to restore hit points to a creature, the creature regains extra hit points equal to 2 + the power’s level."
        },
        "2": {
            "name": "Preserve Life",
            "levels": ["6th"],
            "details": "As an action, you can channel the Force and evoke healing energy that restores a number of hit points equal to five times your consular level. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half its hit point maximum. This feature has no effect on droids or constructs. You can use this feature a number of times equal to your Wisdom or Charisma modifier (your choice, a minimum of once). You regain all expended uses when you finish a long rest."
        }, 
        "3": {
            "name": "Blessed Healer",
            "levels": ["10th"],
            "details": "The healing powers you cast on others heal you as well. When you cast a force power that restores hit points to a creature other than you, you regain hit points equal to 2 + the power’s level."
        },
        "4": {
            "name": "Blessed by the Force",
            "levels": ["14th"],
            "details": "You gain the ability to overcome grievous injuries. As a bonus action when you have fewer than half your hit points remaining, you can regain a number of hit points equal to half your hit point maximum. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        },
        "5": {
            "name": "Supreme Healing",
            "levels": ["18th"],
            "details": "When you would normally roll one or more dice to restore hit points with a power, you instead use the highest number possible for each die. For instance, instead of restoring 2d6 hit points to a creature, you restore 12."
        },
    },
    class_id = 2
)
armormech_engineering = Archetype(
    name = "Armormech Engineering",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Bonus Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in armormech’s implements, medium armor, and heavy armor. Additionally, when you engage in crafting with armormech’s implements, the rate at which you craft doubles."
        },
        "2": {
            "name": "Modified Armor",
            "levels": ["3rd"],
            "details": "You learn to modify one unenhanced suit of armor or shield utilizing your armormech knowledge. Over the course of a long rest, you can modify one suit of armor or a shield. You must have the armor or shield and armormech’s implements in order to perform this modification. Your modified armor or shield is enhanced, requires attunement, can only be used by you, and counts as a tech focus for your tech powers while you are attuned to it. Your modified armor has 4 modification slots, and it gains more at higher levels, as shown in the Modification Slots column of the engineer table. For each modification installed in excess of your proficiency bonus, your tech point maximum is reduced by 1. Over the course of a long rest, you can install, replace, or remove a number of modifications up to your Intelligence modifier (minimum of one). Some modification effects require saving throws. When you use such an effect from this class, the DC equals your tech save DC. At 9th level, you can maintain both a modified suit of armor and shield. Each modified item has modification slots as shown in the Modification Slots column of the engineer table."
        }, 
        "3": {
            "name": "Damage Absorption",
            "levels": ["3rd"],
            "details": "When you take damage, you can use your reaction and expend one use of your Potent Aptitude to absorb some of that damage. When you do so, the damage you take from the attack is reduced by the amount rolled on the die + your Intelligence modifier (minimum of one). You must be wearing your modified armor or wielding your modified shield to gain this benefit."
        },
        "4": {
            "name": "Extra Attack",
            "levels": ["6th"],
            "details": "You can attack twice, instead of once, whenever you take the Attack action on your turn. You must be wearing your modified armor or wielding your modified shield to gain this benefit."
        },
        "5": {
            "name": "Armormech's Celerity",
            "levels": ["14th"],
            "details": "When you take the Attack action or use your action to a cast a tech power of 1st-level or higher, you can make one weapon attack as a bonus action. You can use this feature a number of times equal to your Intelligence modifier (a minimum of once). You regain all expended uses when you complete a long rest."
        },
        "6": {
            "name": "Suit Reliability",
            "levels": ["18th"],
            "details": "Your suit is like a second skin. Whenever you make an ability check or saving throw that uses Strength, Dexterity,or Constitution, you can treat a d20 roll of 9 or lower as a 10. You must be wearing your modified armor or wielding your modified shield to gain this benefit."
        },
        "Modifications": {
            "Absorption Shield": {
                "prerequisite": "Physical Shield",
                "details": "You modify your physical shield to block incoming damage. As a bonus action you can activate this ability and gain temporary hit points equal to 1d4 + Intelligence modifier, which last for one hour. You can use this feature a number of times equal to your Intelligence modifier (a minimum of once). You regain any expended uses when you finish a long rest."
            },
            "Accelerated Movement": {
                 "prerequisite": "Armor",
                 "details": "You reduce the weight of your modified armor’s bulk and increase the power to joints. If the armor has a Strength requirement, you ignore it. The modified armor’s weight is reduced by 15 lbs. While wearing your modified armor your speed increases by 10 feet. This applies to all movement speeds you have while wearing your armor."
            },
            "Adapable Armor": {
                 "prerequisite": "Armor",
                 "details": "You integrate deployable hooks and fins into your armor, augmenting its mobility. While wearing your modified armor, you gain a climbing speed equal to your walking speed, and you can move up, down, and across vertical surfaces and upside down along ceilings, while leaving your hands free. Additionally, you gain a swim speed equal to your walking speed."
            },
            "Advanced Power Fist": {
                 "prerequisite": "11th level, Prototype Power Fist",
                 "details": "You further modify your modified armor’s gauntlet with increased reinforcement and weight. Your modified armor’s unarmed strike deals 1d8 kinetic damage. Additionally, your critical hit range with your unarmed strikes increases by 1."
            },
            "Artificially Intelligent": {
                 "prerequisite": "9th level, Armor",
                 "details": "You install an artificial intelligence into your modified armor. While wearing your modified armor, when you make an ability check, your armor’s artificial intelligence can take the Help action. You can use this feature a number of times equal to your Intelligence modifier (a minimum of once). You regain all expended uses when you complete a long rest."
            },
            "Bonded Plates": {
                 "prerequisite": "5th level",
                 "details": "You gain a +1 bonus to AC against melee attacks. This bonus increases to +2 at 9th level and +3 at 13th level."
            },
            "Collapsible Suit": {
                 "prerequisite": "5th level, Armor",
                 "details": "Your modified armor can collapse into a case for easy storage. When transformed this way the armor is indistinguishable from a normal case and weighs one-third its normal weight. As an action you can don or doff the armor, allowing it to transform as needed."
            },
            "Darkvision Visor": {
                 "prerequisite": "Armor",
                 "details": "While wearing your modified armor, you have darkvision to a range of 60 feet. If you already have darkvision, this modification increases its range by 30 feet."
            },
            "Enhanced Endurance": {
                 "prerequisite": "Armor",
                 "details": "When you are reduced to 0 hit points while wearing your modified armor but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest."
            },
            "Electrshock Shield": {
                 "prerequisite": "Shield Generator",
                 "details": "You install electroshockers in your shield generator. Whenever an enemy misses you with a melee attack, you can use your reaction to do 1d4 + your Intelligence modifier lightning damage to the attacker."
            },
            "Flight": {
                 "prerequisite": "9th level, Armor",
                 "details": "You integrate a propulsion system into your modified armor. While wearing your modified armor you have an enhanced flying speed of 30 feet."
            },
            "Grappling Hook": {
                 "prerequisite": "Armor",
                 "details": "Your modified armor gains an integrated grappling harpoon set into your gauntlet. With this harpoon, you can make a ranged weapon attack with a range of 30/60. On a hit, it deals 1d6 kinetic damage. This attack can target a surface, object, or creature. A creature struck by this attack is impaled by the harpoon. As an action, a creature can attempt to remove the harpoon. Removing the harpoon requires a Strength check. While the harpoon is stuck in the target, you are connected to the target by a 60 foot cable. While the harpoon is deployed, you can use your bonus action to activate the reel, pulling yourself to the location if the target is larger than you. A creature or object your size or smaller is pulled to you. Alternatively, you can opt to release the cable (no action required). Once you’ve used this feature, you can’t use it again until you recover and reinsert the harpoon as an action."
            },
            "Heavy Suit": {
                 "prerequisite": "5th level, Armor",
                 "details": "You enhance your suit, making it difficult to move. As a bonus action, you can anchor your feet to the ground. While anchored, your speed is 0, you have advantage on Strength checks and Strength saving throws, and your carrying capacity and the weight you can push, drag, or lift doubles. If it would already double, it instead triples."
            },
            "Infiltration Suit": {
                 "prerequisite": "Armor",
                 "details": "You install a cloaking device in your modified armor. This device has 2 charges. As an action you can use 1 charge to cast infiltrate targeting yourself. The cloaking device regains all expended charges after a long rest."
            },
            "Magnetized Shield": {
                 "prerequisite": "Physical Shield",
                 "details": "You modify your physical shield such that when a melee weapon attack misses you by an amount less than or equal to your bonus to AC from your shield, the attacking creature must make a Strength check against your tech save DC. On a failed save, the creature’s weapon adheres to the shield. As an action, a creature can repeat this check. On a success, the weapon is freed."
            },
            "Overload Shield": {
                 "prerequisite": "Shield Generator",
                 "details": "You modify your shield generator to overload. As an action you can overload your shield. Each Large or smaller creature within 5 feet of you must make a Dexterity or Strength saving throw (their choice) against your tech save DC. On a failed save, they are pushed back 5 feet and knocked prone. You can use this feature a number of times equal to your Intelligence modifier (a minimum of once). You regain any expended uses when you finish a long rest."
            },
            "Power Fist": {
                 "prerequisite": "Armor",
                 "details": "You modify your modified armor gauntlet with increased reinforcement and weight. Your modified armor’s unarmed strike deals 1d4 kinetic damage. Additionally, when you take the Attack action and make an unarmed attack, you can make an additional unarmed attack as a bonus action"
            },
            "Prototype Power Fist": {
                 "prerequisite": "5th level, Power Fist",
                 "details": "ou further modify your modified armor gauntlet with increased reinforcement and weight. Your modified armor’s unarmed strike deals 1d6 kinetic damage and has the following property. If you or your target move at least 10 feet in a straight line immediately before making an unarmed attack, the first unarmed attack you make deals additional damage equal to your Intelligence modifier."
            },
            "Reinforced Underlay": {
                 "prerequisite": "5th level",
                 "details": "You gain a +1 bonus to AC against ranged attacks. This bonus increases to +2 at 9th level and +3 at 13th level."
            },
            "Resistance": {
                 "prerequisite": "Armor",
                 "details": "You tune your modified armor against certain forms of damage. Choose acid, cold, fire, ion, lightning, or sonic damage. While wearing your modified armor you have resistance to that type of damage. You can select this modification multiple times. Each time you do so, you must choose a different damage type."
            },
            "Sealed Suit": {
                 "prerequisite": "5th level, Armor",
                 "details": "As a bonus action you can hermetically seal your modified armor, giving you an air supply for up to 1 hour and making you immune to poison (but not curing you of existing poisoned conditions). Your armor regains 1 minute of air for every minute that you are not submerged and the armor is not sealed. Additionally, while you are wearing your modified armor you are considered adapted to cold and hot climates as well as high altitude"
            },
            "Sentinet Armor": {
                 "prerequisite": "13th level, Artifically Intelligent",
                 "details": "Your artificial intelligence has learned to control the suit without you being in it. It is now a valid target of the tracker droid interface tech power. While your armor is acting independently, it uses your ability scores, saving throws, and skills, and it has hit points equal to your engineer level. If reduced to 0 hit points, it falls directly to the ground, and it can not be equipped again until you finish a long rest."
            },
            "Shield Amplifier": {
                 "prerequisite": "Shield Generator",
                 "details": "You modify your shield generator to project outward. As a bonus action you can amplify your shield until the start of your next turn. Each creature within 5 feet of you gains a bonus to AC equal to your shield’s bonus. You can use this feature a number of times equal to your Intelligence modifier (a minimum of once). You regain any expended uses when you finish a long rest."
            },
            "Shield Anchor": {
                 "prerequisite": "Physical Shield",
                 "details": "You modify your shield to be used as a portable source of cover. As an action, you can anchor or recover the shield. While anchored, you gain no benefit from a shield, and it does not require the use of a hand. Instead, while anchored, a light shield provides one-quarter cover, a medium shield provides half cover, and a large shield provides three-quarters cover."
            },
            "Tech Blast": {
                 "prerequisite": "Armor",
                 "details": "You modify your modified armor gauntlet with a blaster weapon with which you are proficient. The weapon uses your Intelligence modifier for its attack and damage rolls, and deals 1d8 energy damage on a hit. It has a normal range of 30 feet and a long range of 120 feet."
            },
            "Weapon Integration Armoring": {
                 "prerequisite": "Armor",
                 "details": "You can integrate a single weapon that weighs no more than 8 lb. into your armor. While integrated, that weapon gains the hidden property. Additionally, you have advantage on Strength saving throws to avoid being disarmed."
            }
        }
    },
    class_id = 3
)
armstech_engineering = Archetype(
    name = "ArmsTech Engineering",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Bonus Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in armstech’s implements, medium armor, martial blasters, and martial vibroweapons. Additionally, when you engage in crafting with armstech’s implements, the rate at which you craft doubles."
        },
        "2": {
            "name": "Modified Weaponry",
            "levels": ["3rd"],
            "details": "You learn to modify one unenhanced weapon with which you are proficient utilizing your armstech experience. Over the course of a long rest, you can modify the weapon. You must have the weapon and armstech’s implements in order to perform this modification. Your modified weapon is enhanced, requires attunement, can only be used by you, and counts as a tech focus for your tech powers while you are attuned to it. Your modified weapon has 4 modification slots, and it gains more at higher levels, as shown in the Modification Slots column of the engineer table. For each modification installed in excess of your proficiency bonus, your tech point maximum is reduced by 1. Over the course of a long rest, you can install, replace, or remove a number of modifications up to your Intelligence modifier (minimum of one). Some modification effects require saving throws. When you use such an effect from this class, the DC equals your tech save DC. At 9th level, you can maintain two modified weapons. Each modified weapon has modification slots as shown in the Modification Slots column of the engineer table."
        },  
        "3": {
            "name": "Close Call",
            "levels": ["3rd"],
            "details": "Lastly at 3rd level, when you make an attack roll with your modified weapon and miss, you can expend one use of your Potent Aptitude to attempt to turn that miss into a hit. Roll the die and add it to the attack roll."
        },
        "4": {
            "name": "Armstech's Strike",
            "levels": ["6th"],
            "details": "Once per round, when you deal damage to a creature with your modified weapon, you can increase the damage by 1d6. The damage is of the same type as the weapon’s damage. The damage increases to 2d6 at 11th level and 3d6 at 17th level."
        },
        "5": {
            "name": "Targeting Matrix",
            "levels": ["14th"],
            "details": "When you cast a tech power that allows you to force creatures in an area to make a saving throw, you can instead make an attack roll with your modified weapon against a single target that would be in the range of the power. On a hit, the target suffers the effects as though they failed their saving throw. If the power would affect more than one creature, it instead affects only one. You can use this feature a number of times equal to your Intelligence modifier (a minimum of once). You regain any expended uses when you finish a long rest."
        },
        "6": {
            "name": "Armstech's Salvo",
            "levels": ["18th"],
            "details": "When you use your Targeting Matrix feature, and the tech power would affect more than one creature, you can instead attack each affected creature that would be in the range of the power. Make a separate attack roll for each target. On a hit, each target suffers the effects as though they failed their saving throw."
        },
        "Modifications": {
            "Accuracy Focus": {
                "prerequisite": "5th level, Blaster",
                "details": "You gain a +1 bonus to attack rolls made with this weapon. This bonus increases to +2 at 9th level and +3 at 13th level."
            },
            "Amplifying Barrel": {
                "prerequisite": "5th level, Blaster",
                "details": "You gain a +1 bonus to damage rolls made with this weapon. This bonus increases to +2 at 9th level and +3 at 13th level."
            },
            "Bayonet": {
                "prerequisite": "Blaster",
                "details": "You affix a short blade to the barrel of your modified blaster weapon, allowing you to make a melee weapon attack with it. The blade is a melee weapon with the finesse property that you are proficient with, and deals 1d6 kinetic damage."
            },
            "Burst Core": {
                "prerequisite": "Blaster",
                "details": "Your weapon gains the burst property, with a burst number equal to its reload number."
            },
            "Booming Strikes": {
                "prerequisite": "5th level",
                "details": "You pack extra power into your modified weapon. Once per turn, when you hit with the weapon, you can deal an additional 1d6 damage. If you do so, the weapon makes a loud boom which can be heard 100 feet away. If you are hidden, Intelligence (Investigation) and Wisdom (Perception) checks made to locate you that rely on sound have advantage."
            },
            "Celerity Oscillator": {
                "details": "Once per turn, when you deal damage with your modified weapon, your walking speed increases by 10 feet until the start of your next turn, and the damaged creature can’t make opportunity attacks against you for the rest of your turn."
            },
            "Collapsible Frame": {
                "prerequisite": "Vibroweapon",
                "details": "You install an expandable hilt on your modified weapon. Your modified weapon gains the reach property."
            },
            "Compensation Oscillator": {
                "prerequisite": "Vibroweapon with the dexterity property",
                "details": "You install a compensation oscillator in your modified vibroweapon, removing the dexterity property from it."
            },
            "Contoured Grip": {
                "prerequisite": "5th level, Vibroweapon",
                "details": "You gain a +1 bonus to attack rolls made with this weapon. This bonus increases to +2 at 9th level and +3 at 13th level."
            },
            "Expanded Magazine": {
                "prerequisite": "Blaster",
                "details": "You gain a +1 bonus to attack rolls made with this weapon. This bonus increases to +2 at 9th level and +3 at 13th level."
            },
            
            "Flashlight": {
                "details": "You affix a targeted light to your weapon. As a bonus action, you can toggle the light on or off. While on, your weapon sheds bright light in a 60-foot cone."
            },
            "Harpoon Reel": {
                "details": "You install a secondary firemode that launches a harpoon attached to a tightly coiled cord. With this harpoon, you can make a ranged weapon attack with a range of 30/60. On a hit, it deals 1d6 kinetic damage. This attack can target a surface, object, or creature. A creature struck by this attack is impaled by the harpoon. As an action, a creature can attempt to remove the harpoon. Removing the harpoon requires a Strength check. While the harpoon is stuck in the target, you are connected to the target by a 60 foot cable. While connected in this manner, you can use your bonus action to activate the reel, pulling yourself to the location if the target is your size or larger. A creature or object smaller than you is pulled to you. Alternatively, you can opt to release the cable (no action required). Once you’ve used this feature, you can’t use it again until you recover and reinsert the harpoon as an action."
            },
            "Imbue Weapon": {
                "prerequisite": "9th level",
                "details": "You modify your weapon to carry a charge. Over the course of a short rest, you can cast an at-will tech power, channeling it into your weapon. The next time you hit with your weapon, the stored power is released. If the power would require an attack roll, make a tech attack roll. If the power would require a saving throw, the target must make the saving throw as normal. On a hit, or a failure, the target suffers the power’s normal effects."
            },
            "Improved Burst Core": {
                "prerequisite": "9th level, Burst Core",
                "details": "Your weapon’s burst number is reduced to half its reload number."
            },
            "Integrated Magazine": {
                "prerequisite": "Expanded Magazine",
                "details": "Your modified weapon can be more efficiently reloaded. You can reload your modified weapon twice without using an action. You can’t use this feature again until you reload the weapon with an action."
            },
            "Jagged Oscillator": {
                "prerequisite": "Vibroweapon",
                "details": "When you critically hit with the weapon, you deal an additional 1d8 kinetic damage."
            },
            "Keen Oscillator": {
                "prerequisite": "5th level, Jagged Oscillator",
                "details": "Your weapon’s critical hit range increases by 1."
            },
            "Neutronium Edge": {
                "prerequisite": "5th level, Vibroweapon",
                "details": "You gain a +1 bonus to damage rolls made with this weapon. This bonus increases to +2 at 9th level and +3 at 13th level."
            },
            "Overcharge Weapon": {
                "prerequisite": "11th level, Booming Strikes",
                "details": "You gain the ability to channel your tech power to enhance your weapon’s damage. You can expend one tech slot to deal additional damage to the target. The extra damage is 1d6 for a 1st-level tech slot, plus 1d6 for each slot level higher than 1st, to a maximum of 5d6. The damage is the same type as the weapon damage. If you also use your Booming Strikes with an attack, you add this damage to the extra damage of your Booming Strikes."
            },
            "Power Loop": {
                "prerequisite": "9th level",
                "details": "When you hit with the weapon, you can choose channel the energy generated, gaining temporary hit points equal to half the damage dealt."
            },
            "Recoil Dampener": {
                "prerequisite": "Blaster with the strength property",
                "details": "You install a recoil dampener in your modified blaster, removing the strength property from it."
            },
            "Returning Weapon Guard": {
                "prerequisite": "Vibroweapon",
                "details": "You install a retractible chain in your modified vibroweapon. If the weapon does not already have the thrown property, it gains it with a range of 20/60. Additionally, it gains the returning property."
            },
            "Screening Weapon": {
                "details": "You modify your modified weapon with a sound dampening module. When you make a weapon attack with your weapon while hidden, Investigation and Perception checks made to locate you that rely on sound have disadvantage."
            },
            "Shock Absorber": {
                "details": "You add a reclamation device to your modified weapon to gather energy from the surroundings when it is present. While wielding your modified weapon, you can cast the absorb energy tech power and the power’s extra damage applies to both melee and ranged weapon attacks."
            },
            "Siege Weapon": {
                "details": "You modify your weapon to be more effective against barriers. Your weapon deals double damage against structures."
            },
            "Shocking Harpoon": {
                "prerequisite": "9th level, Harpoon Reel",
                "details": "After hitting a creature with the harpoon fire mode, you can use the connection to deliver an at-will tech power. As a bonus action, you can cast an at-will tech power at the target with a range of touch. If the power requires an attack roll, you have advantage. If the target requires a saving throw, the target has disadvantage. Once you’ve used this feature, you can’t use it again until you recover the harpoon."
            },
            "Shocking Oscillator": {
                "prerequisite": "9th level, Vibroweapon",
                "details": "When you hit with the weapon, you can create an electronic burst. Each creature in a 15-foot cone centered on the creature you hit must make a Dexterity saving throw against your tech save DC, taking 1d8 lightning damage on a failed save or half as much on a successful one. Once you’ve used this feature, you must complete a long rest before you can use it again."
            },
            "Snap Fire": {
                "prerequisite": "9th level, Blaster",
                "details": "You modify your modified blaster weapon for quick shots. You can use your reaction to take a opportunity attack with your modified weapon if an enemy comes within 10 feet of you. You have disadvantage on this attack."
            },
            "Staggering Oscillator": {
                "prerequisite": "Vibroweapon",
                "details": "When you hit with the weapon, you can force the target to make a Strength saving throw. On a failed save, the creature is pushed back 10 feet and knocked prone. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
            },
            "Tracker": {
                "prerequisite": "5th level",
                "details": "You add a tracking mechanism to your modified weapon. The tracker has 3 charges. As an action you can use 1 charge to cast target lock. As an action you can use 2 charges to cast detect invisibility. The tracker regains all expended charges after a long rest."
            },
            "Truelight": {
                "prerequisite": "11th level, Flashlight",
                "details": "When toggled on, your flashlight now automatically dispels illusions and can detect invisibility, as with truesight."
            },
            "Venomous Oscillator": {
                "prerequisite": "9th level, Vibroweapon",
                "details": "As a bonus action, you can coat your weapon in a thin layer of poison for 1 minute. The next time you hit with the weapon, the creature must make a Constitution saving throw against your tech save DC. On a failed save, a creature takes 1d10 poison damage and becomes poisoned for 1 minute. Once you’ve used this feature, you must complete a long rest before you can use it again."
            }
        }
    },
    class_id = 3
)
gadgeteer_engineering = Archetype(
    name = "Gadgeteer Engineering",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Bouns Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in gadgeteer’s implements. Additionally, when you engage in crafting with gadgeteer’s implements, the rate at which you craft doubles."
        },
        "2": {
            "name": "Gadgeteer Harness",
            "levels": ["3rd"],
            "details": "You learn to create and modify adventuring gear utilizing your gadgeteer experience. Over the course of a long rest, you can create your modified gadgeteer harness. You must have gadgeteer’s implements in order to perform this modification. Your gadgeteer harness is enhanced, requires attunement, can only be used by you, and counts as a tech focus for your tech powers while you are attuned to it. Your gadgeteer harness has 4 modification slots to which you can affix gadgets, and it gains more at higher levels, as shown in the Modification Slots column of the engineer table. For each modification installed in excess of your proficiency bonus, your tech point maximum is reduced by 1. Over the course of a long rest, you can install, replace, or remove a number of modifications up to your Intelligence modifier (minimum of one). Some modification effects require saving throws. When you use such an effect from this class, the DC equals your tech save DC."
        }, 
        "3": {
            "name": "Projected Barrier",
            "levels": ["3rd"],
            "details": "As a bonus action while wearing your gadgeteer harness, you can expend a use of your Potent Aptitude to project a barrier on a friendly creature you can see within 30 feet. A creature can only have one barrier active at a time. Environmental Barrier: You project an environmental barrier that lasts until the end of your next short or long rest. The barrier has a number of hit points equal to the amount rolled on your Potent Aptitude die + your engineer level. Whenever a creature with this barrier takes damage (one of acid, cold, fire, force, lightning, necrotic, poison, psychic, or sonic, chosen by you when you activate the effect), the barrier takes the damage instead. If this damage reduces the barrier to 0 hit points, the creature take any remaining damage. Physical Barrier: You project a physical barrier that lasts until the end of your next short or long rest. The barrier has a number of hit points equal to the amount rolled on your Potent Aptitude die + half your engineer level (rounded down). Whenever a creature with this barrier takes damage (one of energy, ion, or kinetic, chosen by you when you activate the effect), the barrier takes the damage instead. If this damage reduces the barrier to 0 hit points, the creature take any remaining damage."
        },
        "4": {
            "name": "Versatile Direction",
            "levels": ["6th"],
            "details": "You can take a second bonus action on each of your turns. You can use this feature a number of times equal to your Intelligence modifier (a minimum of once). You regain all expended uses when you finish a long rest."
        },
        "5": {
            "name": "Reinforced Barriers",
            "levels": ["14th"],
            "details": "When you cast a tech power while you have a barrier active, you can restore hit points to the barrier, provided it is within 30 feet of you. You restore a number of hit points equal to twice the power’s level, or 1 hit point for an at-will power. This can’t increase a barrier’s hit points above its initial hit points. If you have multiple barriers active, you can divide these hit points between them as you see fit."
        },
        "6": {
            "name": "Adaptive Barrier",
            "levels": ["18th"],
            "details": "When a creature who has one of your barriers within 30 feet of you that you can see takes damage, and that damage is of a type that could be affected by that barrier, you can use your reaction to grant them resistance to the triggering damage. If that damage is the same type as the barrier’s chosen damage, you instead grant them immunity. Whether resistance or immunity, the barrier immediately drops to 0 hit points."
        },
        "Contraptions": {
            "Advanced Grounding System": {
                "prerequisite": "13th level, Prototype Grounding System",
                "details": "While wearing your gadgeteer harness you have immunity to lightning damage."
            },
            "Auto-Injection Regenerator": {
                "prerequisite": "5th level",
                "details": "You install a special kolto injector into your gadgeteer harness that can inject you with kolto in response to pain. When you take damage, you can use your reaction and expend a Hit Die to regain health as long as the damage would not reduce your hit points to 0"
            },
            "Autothrusters": {
                "prerequisite": "Jet Pack",
                "details": "You can take the Dash and Disengage actions as a bonus action while your jet pack is active."
            },
            "Climbing Gloves": {
                "details": "You craft a set of gloves with a powerful assisted grip. While wearing these gloves, you have a climbing speed of 20 feet, and you have advantage on Strength saving throws and Strength (Athletics) checks that involve climbing."
            },
            "Darkvision Goggles": {
                "details": "You craft a set of gloves with a powerful assisted grip. While wearing these gloves, you have a climbing speed of 20 feet, and you have advantage on Strength saving throws and Strength (Athletics) checks that involve climbing."
            },
            "Extneded Tank": {
                "prerequisite": "5th level, Jet Pack",
                "details": "Your jet pack now lasts up to 10 minutes when activated."
            },
            "Flame Vents": {
                "prerequisite": "9th level, Jet Pack",
                "details": "You learn the flame sweep tech power and can cast it at first level without using tech points. Once you have used this ability, you cannot use it again until you finish a short or long rest. Additionally, while your jet pack is active, you can cast flame sweep using your bonus action instead of your action."
            },
            "Grounding System": {
                "details": "While wearing your gadgeteer harness you are immune to the shocked condition."
            },
            "Integrated Targeter": {
                "prerequisite": "5th level",
                "details": "While using your harness as a tech focus, you gain a +1 bonus to your tech save DC. This bonus increases to +2 at 9th level and +3 at 13th level."
            },
            "Intelligence Core Override": {
                "prerequisite": "9th level",
                "details": "You can cast the override interface tech power at 5th level without spending tech points. Once you’ve used this feature, you must complete a long rest before you can use it again."
            },
            "Jet Pack": {
                "details": "You integrate a jet pack into your gadgeteer harness to grant you temporary, limited flight. Activating or deactivating the jets requires a bonus action and, while active, you have a flying speed of 30 feet. The jet pack last for 1 minute before deactivating. Once the jets have been activated, they can’t be activated again until you finish a short or long rest. Your jet pack’s speed increases to 40 feet at 5th level, 50 feet at 9th level, 60 feet at 13th level, 70 feet at 17th level, and 80 feet at 20th level."
            },
            "Mechanical Arm": {
                "details": "You create a mechanical arm which mounts to your shoulder, which you can use independently. You can only gain the benefit of items held by two of your arms at any given time. You can choose this modification twice."
            },
            "Mimicker": {
                "prerequisite": "9th level",
                "details": "You create a device that attaches to your gadgeteer harness. Your mimicker casts a shadow that makes you appear to be standing in a place near your actual location, causing any creature to have disadvantage on attack rolls against you. If you take damage, the property ceases to function for 1 minute. Your mimicker is suppressed while you are incapacitated, restrained, or otherwise unable to move."
            },
            "Miniaturized Hydraulics": {
                "details": "Your gadgeteer harness can store 20 pounds of equipment without adding to your encumbrance."
            },
            "Oil Spill": {
                "details": "As an action, you can cast the oil slick tech power without expending tech points. When you cast the power in this way, the oil will remain in place for the full duration of the power. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
            },
            "Powered Grappling Hook": {
                "prerequisite":"9th level, Wrist-Mounted Grappling Hook",
                "details": "While your wrist-mounted grappling hook is deployed, when you cast a tech power with a range of touch, your hook can deliver the power as if it had cast it."
            },
            "Prototype Grounding System": {
                "prerequisite": "9th level, Grounding System",
                "details": "While wearing your gadgeteer harness you have resistance to lightning damage."
            },
            "Quick Start Engine": {
                "prerequisite": "5th level, Jet Pack",
                "details": "You can now activate your Jet Pack as an object interaction rather than as a bonus action."
            },
            "Recycled Adrenals": {
                "details": "You can augment a single adrenal to regain its charge. This adrenal can only be used by you, and it can only affect you. Once you’ve used this adrenal, you can’t use it again until you finish a short or long rest."
            },
            "Recycled Explosives": {
                "details": "You can augment a single explosive to regain its charge. This explosive can only be used by you, and it uses your tech save DC instead of its own, unless its own DC would be higher. Once you’ve used this explosive, you can’t use it again until you finish a short or long rest."
            },
            "Recycled Stimpacs": {
                "details": "You can augment a single stimpac to regain its charge. This stimpac can only be used by you, and it can only affect you. Once you’ve used this stimpac, you can’t use it again until you finish a short or long rest."
            },
            "Sentry Turrent": {
                "details": "You learn how to craft small sentry turrets shaped like globes that can adhere to any surface. As an action or bonus action (your choice), you can throw a sentry to a point you can see within range (30 feet + your Strength modifier x 5). At the end of each of your turns, a deployed sentry automatically targets a hostile creature within 10 feet of it. If multiple targets are available, one is chosen at random. The target must make a Dexterity saving throw. On a failed save, it takes 1d4 energy damage and gains 1 slowed level until the end of your next turn. If a creature would be targeted by more than one of these sentries, it only makes this saving throw once, taking an additional d4 damage for each sentry beyond the first. The sentries have 1 hit point, an armor class of 10, and can be repaired over the course of a long rest. Each sentry lasts for 1 minute before deactivating. You can maintain a number of sentries equal to your Intelligence modifier. Once a sentry has been activated, it can’t be activated again until you finish a short or long rest."
            },
            "Shocking Hook": {
                "prerequisite": "9th level, Wrist-Mounted Grappling Hook",
                "details": "After hitting a creature with your grappling hook, you can use the connection to deliver an at-will tech power. As a bonus action, you can cast an at-will tech power at the target with a range of touch. If the power requires an attack roll, you have advantage. If the target requires a saving throw, the target has disadvantage. Once you’ve used this feature, you can’t use it again until you recover the hook."
            },
            "Stealth Field Generator": {
                "prerequisite": "9th level",
                "details": "You create an augmented belt that functions as a portable, personal cloaking device. Activating or deactivating the generator requires a bonus action and, while active, you have advantage on Dexterity (Stealth) ability checks that rely on sight. The generator lasts for 1 minute. This effect ends early if you make an attack or cast a force- or tech- power. Once the belt has been activated, it can’t be activated again until you finish a short or long rest."
            },
            "Shocking Barrier": {
                "prerequisite": "5th level",
                "details": "You enhanced your barriers. Whenever a creature with one of your barriers active takes damage from a creature within 5 feet of it, the damaged creature can roll your Potent Aptitude die, dealing the result of the die as lightning damage to the creature that damaged it."
            },
            "Truesight Goggles": {
                "prerequisite": "11th level, Darkvision Goggles",
                "details": "You modify your goggles with a toggle allowing you to briefly gain enhanced sight. As a bonus action, you can activate the truesight feature of your goggles. When toggled on, for the next minute your goggles now automatically dispel illusions and can detect invisibility, as with truesight. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
            },
            "Weapon Integration": {
                "details": "You can integrate a single weapon that weighs no more than 8 lb. into your gadgeteer harness. While integrated, that weapon gains the hidden and fixed properties."
            },
            "Wrist-mounted Grappling Hook": {
                "details": "You craft a wrist-mounted grappling hook weapon attached to a tightly coiled cord. With this contraption, you can make a ranged weapon attack with a range of 30/60. On a hit, it deals 1d4 kinetic damage. This attack can target a surface, object, or creature. A creature struck by this attack is impaled by the hook. As an action, a creature can attempt to remove the hook. Removing the hook requires a Strength check. While the hook is stuck in the target, you are connected to the target by a 60 foot cable. While the hook is deployed, you can use your bonus action to activate the reel, pulling yourself to the location if the target is your size or larger. A creature or object smaller than you is pulled to you. Alternatively, you can opt to release the cable (no action required). Once you’ve used this feature, you can’t use it again until you recover and reinsert the hook as an action."
            }
        }
    },
    class_id = 3
)
unstable_engineering = Archetype(
    name = "Unstable Engineering",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Bonus Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in your choice of artisan’s implements. Additionally, when you engage in crafting with tinker’s implements, the rate at which you craft doubles."
        },
        "2": {
            "name": "Modified Tinkercannon",
            "levels": ["3rd", "9th", "17th"],
            "details": "You learn to enhance your tinker’s implements with unstable science, modifying them into a harness with a cannon. Over the course of a long rest, you can modify your tinker’s implements to create a tinkercannon. You must have tinker’s implements in order to perform this modification. Whenever you cast a tech power of 1st level or higher while wielding your tinkercannon, you risk unexpected complications. Your GM can have you roll a d20. If you roll a 1, roll on the Unstable Engineering Surge table to create a random effect. Additionally, your tinkercannon come equipped with four overrides, and they gain more at higher levels, as shown in the Modification Slots column of the engineer table. Each time you trigger an Unstable Engineering Surge, you can use an override to reroll the percentile dice. You must use the new result, you can only do this once per surge, and each time you do so in excess of your proficiency bonus (resetting on a long rest) your maximum tech points is reduced by 1 until you complete a long rest. You regain all expended overrides when you complete a long rest."
        }, 
        "3": {
            "name": "Unstable Volley",
            "levels": ["3rd", "9th", "17th"],
            "details": "While wielding your tinkercannon, as a bonus action you can expend one use of your Potent Aptitude to launch a volley of unstable energy at a surface located within 30 feet of you that you can see. This energy adheres to the surface for 1 minute, after which it erupts. As a part of this bonus action, or as a bonus action on a following turn, you can cause the energy to erupt early. Each creature within 5 feet of it must make a Dexterity saving throw against your tech save DC. A creature takes 1d6 lightning damage on a failed save, or half as much on a successful one. The range at which you can launch your volley increases to 60 feet at 9th level, and 120 feet at 17th level. This damage increases when you reach certain levels in this class, increasing to 2d6 at 5th level, 3d6 at 11th level, and 4d6 at 17th level."
        },
        "4": {
            "name": "Creative Destruction",
            "levels": ["6th level"],
            "details": "You can add your governing ability modifier (minimum of +1) to any damage you deal with tech powers and class features that don’t already include that modifier. If the tech power or class feature would damage multiple creatures, you can only deal this additional damage to one of them. If you choose to deal this additional damage, your GM can have you roll on the Unstable Engineering Surge table."
        },
        "5": {
            "name": "Experimental Overrides",
            "levels": ["14th level"],
            "details": "You gain a modicum of control over your surges. Whenever you roll on the Unstable Engineering Surge table and use one of your overrides, you can choose either total."
        },
        "6": {
            "name": "Engineering Bombardment",
            "levels": ["18th level"],
            "details": "The harmful energies of your tech powers and class features intensify. When you roll damage for a tech power or class feature and roll the highest number possible on any of the dice, you can roll it again and use both results. You can only use this ability once per tech power or class feature."
        },
        "Unstable Engineering Surge": {
            "details": "Roll a d100",
            "01-02": {
                "details": "Roll on this table at the start of each of your turns for 1 minute, ignoring this result on subsequent rolls."
            },
            "03-04": {
                "details": "For the next minute, you can see any invisible creature if you have line of sight to it."
            },
            "05-06": {
                "details": "A DRK-1 tracker droid appears with 5 feet of you, then disappears 1 minute later."
            },
            "07-08": {
                "details": "You cast explosion at 3rd-level centered on yourself without expending tech points."
            },
            "09-10": {
                "details": "You cast homing rockets at 5th-level without expending tech points."
            },
            "11-12": {
                "details": "Roll a d10. Your height changes by a number of inches equal to the roll: if odd, you shrink; if even, you grow."
            },
            "13-14": {
                "details": "You fall asleep standing for 1 minute or until you take damage."
            },
            "15-16": {
                "details": "For the next minute, you regain 5 hit points at the start of each of your turns"
            },
            "17-18": {
                "details": "You grow a long beard made of feathers that remains until you sneeze."
            },
            "19-20": {
                "details": "You cast oil slick centered on yourself without expending tech points."
            },
            "21-22": {
                "details": "Creatures have disadvantage on the first saving throw they make against you in the next minute."
            },
            "23-24": {
                "details": "Your skin turns a vibrant shade of blue. Any effect that ends a curse ends this."
            },
            "25-26": {
                "details": "You grow an extra eye, granting advantage on Wisdom (Perception) checks that rely on sight for 1 minute."
            },
            "27-28": {
                "details": "For the next minute, all your tech powers with a casting time of 1 action have a casting time of 1 bonus action"
            },
            "29-30": {
                "details": "You teleport up to 60 feet to an unoccupied space of your choice that you can see."
            },
            "31-32": {
                "details": "You take 2d10 lightning damage and are shocked for 1 minute"
            },
            "33-34": {
                "details": "Maximize the damage of the next damaging tech power you cast within the next minute."
            },
            "35-36": {
                "details": "Roll a d10. Your age changes by a number of years equal to the roll: if odd, younger; if even, older."
            },
            "37-38": {
                "details": "You start running uncontrollably for 1 minute, moving your entire speed each turn"
            },
            "39-40": {
                "details": "You regain 2d10 hit points."
            },
            "41-42": {
                "details": "Each creature within 30 feet of you is subjected to the gleaming outline tech power for 1 minute."
            },
            "43-44": {
                "details": "For the next minute, you can teleport up to 20 feet as a bonus action on each of your turns."
            },
            "45-46": {
                "details": "You are blinded and deafened for 1 minute."
            },
            "47-48": {
                "details": "You have disadvantage on the first ability check, attack roll, or saving throw you make each turn for 1 minute"
            },
            "49-50": {
                "details": "You can’t speak for the next minute. Whenever you try, pink bubbles float out of your mouth."
            },
            "51-52": {
                "details": "	A shimmering energy barrier grants you a +2 bonus to AC for 1 minute."
            },
            "53-54": {
                "details": "You are immune to being intoxicated by alcohol for the next 5d6 days."
            },
            "55-56": {
                "details": "Your hair falls out but grows back within 24 hours. If you don’t have hair, you instead grow it for 24 hours."
            },
            "57-58": {
                "details": "For 1 minute, any flammable object not worn or carried you touch bursts into flame."
            },
            "59-60": {
                "details": "You regain tech points equal to your Intelligence modifier (minimum of one)."
            },
            "61-62": {
                "details": "For the next minute, you shout whenever you speak."
            },
            "63-64": {
                "details": "You cast smoke cloud centered on yourself without expending tech points."
            },
            "65-66": {
                "details": "Up to three creatures you choose within 30 feet of you take 4d10 lightning damage"
            },
            "67-68": {
                "details": "You are frightened by the nearest creature until the end of your next turn."
            },
            "69-70": {
                "details": "Each creature within 30 feet of you becomes invisible for 1 minute, or until it attacks or casts a power."
            },
            "71-72": {
                "details": "You gain resistance to all damage for the next minute."
            },
            "73-74": {
                "details": "A random creature within 60 feet of you becomes poisoned for 1d4 hours."
            },
            "75-76": {
                "details": "You emit bright light in a 30-foot radius for 1 minute."
            },
            "77-78": {
                "details": "Each creature within 30 feet of you except you gains the benefits of mirror image for 1 minute."
            },
            "79-80": {
                "details": "Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute"
            },
            "81-82": {
                "details": "You can take one additional action immediately."
            },
            "83-84": {
                "details": "Each creature within 30 feet of you takes 1d10 necrotic damage and you gain hit points equal to the damage."
            },
            "85-86": {
                "details": "You cast mirror image without expending tech points."
            },
            "87-88": {
                "details": "You are frozen in carbonite and paralyzed for 1 minute or until you take damage"
            },
            "89-90": {
                "details": "You turn invisible and can’t make sound for 1 minute, or until you attack or cast a power."
            },
            "91-92": {
                "details": "If you die within the next minute, you immediately come back to life as if by the defibrillate power."
            },
            "93-94": {
                "details": "Your size increases by one size category for the next minute."
            },
            "95-96": {
                "details": "You and all creatures within 30 feet of you gain vulnerability to energy damage for the next minute."
            },
            "97-98": {
                "details": "You are surrounded by faint, ethereal music for the next minute."
            },
            "99-100": {
                "details": "You regain half your expended tech points."
            }
        }

    },
    class_id = 3
)
assault_specialist = Archetype(
    name = "Assault Specialist",
    caster_type = "None",
    features = {
        "1": {
            "name": "Brute Force",
            "levels": ["3rd", "5th", "9th", "13th", "17th"],
            "details": "Once per turn, when you deal damage with a weapon, you can deal an additional 1d4 damage of the same type as the weapon’s damage. If this damage would affect multiple creatures, you can only apply this damage bonus to one of them. This damage increases to 1d6 at 5th level, 1d8 at 9th level, 1d10 at 13th level, and 1d12 at 17th level."
        },
        "2": {
            "name": "Remarkable Athlete",
            "levels": ["3rd"],
            "details": "You can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn’t already use your proficiency bonus."
        },
        "3": {
            "name": "Brutish Durability",
            "levels": ["7th"],
            "details": "Once per round, roll 1d6 and add the die to your saving throw total. If applying this bonus to a death saving throw increases the total to 20 or higher, you gain the benefits of rolling a 20 on the d20. You can choose to use this feature before or after you make a saving throw, but you must decide before the GM says whether the save succeeds or fails."
        },
        "4": {
            "name": "Additional Fight Style",
            "levels": ["10th"],
            "details": "You can choose a second fighting style option."
        },
        "5": {
            "name": "Devastating Critical",
            "levels": ["15th"],
            "details": "When you score a critical hit with a weapon attack, you gain a bonus to that weapon’s damage roll equal to your fighter level."
        },
        "6": {
            "name": "Survivor",
            "levels": ["18th"],
            "details": "You attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half your hit points left. You don’t gain this benefit if you have 0 hit points."
        } 
    },
    class_id = 4
)
heavy_weapons_specialist = Archetype(
    name = "Heavy Weapon Specialist",
    caster_type = "None",
    features = {
        "1": {
            "name": "Rock Steady",
            "levels": ["3rd"],
            "details": "You have learned to use the heft of your weapon to root yourself in place. At the end of each of your turns, if you move less than half your speed while wielding a weapon with the heavy or strength properties, you have advantage on saving throws to avoid being restrained, moved, or knocked prone. This advantage lasts until the end of your next turn."
        },
         "2": {
            "name": "My little friend says hello there",
            "levels": ["3rd"],
            "details": "You know how to use the sheer size of your weapon to strike fear in those around you. You can add your Strength modifier to any Charisma (Intimidation) check you make while wielding a weapon with the heavy or strength properties that doesn’t already include that modifier."
        },   
         "3": {
            "name": "Maximum Output",
            "levels": ["7th"],
            "details": "When you take the Attack action while wielding a weapon with the heavy or strength properties, you can forgo one or more attacks. If you do so, the first time you deal damage with the weapon before the start of your next turn, you deal additional damage of the same type as the weapon’s damage. If this instance would deal damage to multiple creatures, you can only apply this additional damage to one of them. For each attack you forgo, you deal additional damage equal to 1d12 + half your fighter level (rounded down). If you miss with the first attack roll you make before the end of your next turn, or one target succeeds on the saving throw against your weapon’s burst or rapid property, you instead deal normal weapon damage."
        }, 
         "4": {
            "name": "Straight Through",
            "levels": ["10th"],
            "details": "When you score a critical hit on your turn while wielding a weapon with the heavy or strength properties, you can make one weapon attack against a creature within 5 feet of the target using your reaction."
        }, 
         "5": {
            "name": "Overwhelm",
            "levels": ["15th"],
            "details": "When you use your Second Wind while wielding a weapon with the heavy or strength properties, if you hit with the first attack roll you make, or if one creatures fails the saving throw against your weapon’s burst or rapid property, before the end of your next turn, you treat the hit as a critical hit. If you miss with the first attack roll you make before the end of your next turn, or one target succeeds on the saving throw against your weapon’s burst or rapid property, you instead deal normal weapon damage."
        }, 
         "6": {
            "name": "Pure Performance",
            "levels": ["18th"],
            "details": "At 18th level, attack rolls you make while wielding a weapon with the heavy or strength properties can’t suffer from disadvantage."
        }
    },
    class_id = 4
)
shield_specialist = Archetype(
    name = "Shield Specialist",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Techcasting",
            "levels": ["3rd"],
            "details": "You have derived powers from schematics with the aid of your wristpad. You learn 3 tech powers of your choice, and you learn more at higher levels, as shown in the Tech Powers Known column of the Shield Specialist Techcasting table. You may not learn a tech power of a level higher than your Max Power Level. You have a number of tech points equal to half your fighter level (rounded up), as shown in the Tech Points column of the Shield Specialist Techcasting table, + your Intelligence modifier. You use these tech points to cast tech powers. You regain all expended tech points when you finish a short or long rest. Many tech powers can be overcharged, consuming more tech points to create a greater effect. You can overcharge these powers to a maximum level, which increases at higher levels, as shown in the Max Power Level column of the Shield Specialist Techcasting table. You may only cast tech powers at 4th-level once. You regain the ability to do so after a long rest. Intelligence is your techcasting ability for your tech powers. You use your Intelligence whenever a power refers to your techcasting ability. Additionally, you use your Intelligence modifier when setting the saving throw DC for a tech power you cast and when making an attack roll with one. Tech save DC = 8 + your proficiency bonus + your Intelligence modifier. You use a wristpad as a tech focus for your tech powers."
        },
        "2": {
            "name": "Stay in Formation",
            "levels": ["3rd"],
            "details": "You can take the Guard action as a bonus action on your turn."
        },
        "3": {
            "name": "Rallying Cry",
            "levels": ["7th"],
            "details": "When you use your Second Wind feature, you can choose up to three creatures within 60 feet of you that are allied with you. Each one regains hit points equal to your fighter level, provided that the creature can see or hear you."
        },
        "4": {
            "name": "Inspiring Surge",
            "levels": ["10th"],
            "details": "When you use your Action Surge feature, you can choose one creature within 60 feet of you that is allied with you. That creature can make one melee or ranged weapon attack with its reaction, provided that it can see or hear you."
        },
        "5": {
            "name": "Bulwark",
            "levels": ["15th"],
            "details": "You can extend the benefit of your Indomitable feature to an ally. When you decide to use Indomitable to reroll an Intelligence, a Wisdom, or a Charisma saving throw and you aren’t incapacitated, you can choose one ally within 60 feet of you that also failed its saving throw against the same effect. If that creature can see or hear you, it can reroll its saving throw and must use the new roll."
        },
        "6": {
            "name": "greater Inspiring Surge",
            "levels": ["18th"],
            "details": "You can choose two allies within 60 feet of you, rather than one, when you using your Inspiring Surge feature."
        },
        "Techcasting Table": {
            "3": {
                "Tech Powers Known": "3",
                "Tech Points": "2",
                "Max Power Level": "1st"
            },
            "4": {
                "Tech Powers Known": "4",
                "Tech Points": "2",
                "Max Power Level": "1st"
            },
            "5": {
                "Tech Powers Known": "5",
                "Tech Points": "3",
                "Max Power Level": "1st"
            },
            "6": {
                "Tech Powers Known": "6",
                "Tech Points": "3",
                "Max Power Level": "1st"
            },
            "7": {
                "Tech Powers Known": "7",
                "Tech Points": "4",
                "Max Power Level": "2nd"
            },
            "8": {
                "Tech Powers Known": "8",
                "Tech Points": "4",
                "Max Power Level": "2nd"
            },
            "9": {
                "Tech Powers Known": "9",
                "Tech Points": "5",
                "Max Power Level": "2nd"
            },
            "10": {
                "Tech Powers Known": "10",
                "Tech Points": "5",
                "Max Power Level": "2nd"
            },
            "11": {
                "Tech Powers Known": "11",
                "Tech Points": "6",
                "Max Power Level": "2nd"
            },
            "12": {
                "Tech Powers Known": "12",
                "Tech Points": "6",
                "Max Power Level": "2nd"
            },
            "13": {
                "Tech Powers Known": "13",
                "Tech Points": "7",
                "Max Power Level": "3rd"
            },
            "14": {
                "Tech Powers Known": "14",
                "Tech Points": "7",
                "Max Power Level": "3rd"
            },
            "15": {
                "Tech Powers Known": "15",
                "Tech Points": "8",
                "Max Power Level": "3rd"
            },
            "16": {
                "Tech Powers Known": "16",
                "Tech Points": "8",
                "Max Power Level": "3rd"
            },
            "17": {
                "Tech Powers Known": "17",
                "Tech Points": "9",
                "Max Power Level": "4th"
            },
            "18": {
                "Tech Powers Known": "18",
                "Tech Points": "9",
                "Max Power Level": "4th"
            },
            "19": {
                "Tech Powers Known": "19",
                "Tech Points": "10",
                "Max Power Level": "4th"
            },
            "20": {
                "Tech Powers Known": "20",
                "Tech Points": "10",
                "Max Power Level": "4th"
            }
        }
    },
    class_id = 4
)
tactical_specialist = Archetype(
    name = "tactical Specialist",
    caster_type = "None",
    features = {
        "1": {
            "name": "Bonus Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in your choice of artisan’s implements."
        },
        "2": {
            "name": "Improved Comabat Superiority",
            "levels": ["3rd"],
            "details": "Your tactical skill in combat improves, granting bonuses to your Combat Superiority. You know four maneuvers of your choice, instead of two, and you earn more at higher levels, as shown in the Maneuvers Known column of the Tactical Specialist Combat Superiority table. You have four superiority dice, instead of two, and you earn more at higher levels, as shown in the Superiority Dice column of the Tactical Specialist Combat Superiority table."
        },
        "3": {
            "name": "Signature Maneuver",
            "levels": ["3rd"],
            "details": "You choose a maneuver you know from this class as your signature maneuver. Whenever you use that maneuver, you can use it without expending a Superiority Dice. You may only use this feature once per round."
        },
        "4": {
            "name": "Know your Enemy",
            "levels": ["7th"],
            "details": "If you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The GM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice: Strength score, Dexterity score, Constitution score, Armor Class, Current hit points, Total class levels (if any), Fighter class levels (if any)"
        },
        "5": {
            "name": "Greater Signature Maneuver",
            "levels": ["10th"],
            "details": "You can choose a second signature maneuver."
        },
        "6": {
            "name": "Relentless",
            "levels": ["15th"],
            "details": "When you roll initiative and have no Superiority Dice remaining, you regain 1 Superiority Die."
        },
        "7": {
            "name": "Maneuver Mastery",
            "levels": ["18th"],
            "details": "Once per round, when you would roll a Superiority Die, you can instead choose the maximum."
        },
        "Tactical Specialist Table": {
            "3": {
                'Superiority Dice': "4",
                "Maneuvers Known": "4"
            },
            "4": {
                'Superiority Dice': "4",
                "Maneuvers Known": "4"
            },
            "5": {
                'Superiority Dice': "4",
                "Maneuvers Known": "4"
            },
            "6": {
                'Superiority Dice': "4",
                "Maneuvers Known": "4"
            },
            "7": {
                'Superiority Dice': "6",
                "Maneuvers Known": "6"
            },
            "8": {
                'Superiority Dice': "6",
                "Maneuvers Known": "6"
            },
            "9": {
                'Superiority Dice': "6",
                "Maneuvers Known": "6"
            },
            "10": {
                'Superiority Dice': "6",
                "Maneuvers Known": "6"
            },
            "11": {
                'Superiority Dice': "8",
                "Maneuvers Known": "8"
            },
            "12": {
                'Superiority Dice': "8",
                "Maneuvers Known": "8"
            },
            "13": {
                'Superiority Dice': "8",
                "Maneuvers Known": "8"
            },
            "14": {
                'Superiority Dice': "8",
                "Maneuvers Known": "8"
            },
            "15": {
                'Superiority Dice': "10",
                "Maneuvers Known": "10"
            },
            "16": {
                'Superiority Dice': "10",
                "Maneuvers Known": "10"
            },
            "17": {
                'Superiority Dice': "10",
                "Maneuvers Known": "10"
            },
            "18": {
                'Superiority Dice': "10",
                "Maneuvers Known": "10"
            },
            "19": {
                'Superiority Dice': "10",
                "Maneuvers Known": "10"
            },
            "20": {
                'Superiority Dice': "10",
                "Maneuvers Known": "10"
            }
            
        }
    },
    class_id = 4
)
makashi_form = Archetype(
    name = "Makashi Form",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Form Basics",
            "levels": ["3rd"],
            "details": "You gain the Makashi lightsaber form, detailed in Chapter 6. If you already know this form, you can instead choose another lightsaber form."
        },
        "2": {
            "name": "The Way of the Ysalamiri",
            "levels": ["3rd"],
            "details": "As a bonus action, you can enter an offensive stance for one minute. While in this stance, you add your Wisdom or Charisma modifier (your choice) to the first melee weapon attack and damage rolls you make each turn. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        },
        "3": {
            "name": "Channel the Force",
            "levels": ["3rd"],
            "details": "You gain the following Channel the Force option. Makashi Riposte: When another creature damages you with a melee attack, you can expend a use of your Channel the Force and use your reaction to attempt to deflect the attack. When you do so, the damage you take from the attack is reduced by 1d10 + your Dexterity modifier + your guardian level. If you reduce the damage to 0, you can immediately make a single melee weapon attack against that creature as a part of the reaction."
        },
        "4": {
            "name": "Shatterpoint",
            "levels": ["7th"],
            "details": "If you spend at least 1 minute observing or interacting with another creature outside combat, you can use your connection to the Force to sense their strengths and weaknesses, and learn certain information about its capabilities compared to your own. The GM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice: Strength score, Dexterity score, Wisdom score, Charisma score, Armor Class, Current hit points, Total class levels (if any), Total Forcecaster levels (if any)"
        },
        "5": {
            "name": "Glancing Blow",
            "levels": ["15th"],
            "details": "When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack’s damage against you."
        },
        "6": {
            "name": "Master of Contention",
            "levels": ["20th"],
            "details": "You are a duelist of the highest caliber. Your Dexterity and Wisdom or Charisma scores (your choice) increase by 2. Your maximum for those scores increases by 2. Additionally, you can use your action to gain the following benefits for 1 minute: You have resistance to kinetic and energy damage, and you ignore resistance to kinetic and energy damage. All melee attacks have disadvantage against you. Your melee weapon attacks inflict an additional damage die. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        }  
    },
    class_id = 5
)
niman_form = Archetype(
    name = "Niman Form",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Form Basics",
            "levels": ["3rd"],
            "details": "You gain the Niman lightsaber form, detailed in Chapter 6. If you already know this form, you can instead choose another lightsaber form."
        },
        "2": {
            "name": "The Way of the Rancor",
            "levels": ["3rd"],
            "details": "As a bonus action, you can enter a balanced stance for one minute. As a part of this bonus action, and as a bonus action on each of your turns, when you use your action to cast a force power, you can make one melee weapon attack. Additionally, for the duration, you can use Wisdom or Charisma instead of Strength or Dexterity for the attack and damage rolls of your melee weapon attacks. You must use the same modifier for both rolls. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        },  
        "3": {
            "name": "Channel the Force",
            "levels": ["3rd"],
            "details": "You gain the following Channel the Force option. Telekinetic Slash: When you deal damage with an at-will force power that requires a force attack or a saving throw, you can expend a use of your Channel the Force and expend force points to deal additional damage to the target, which is the same type as the power’s damage. The additional damage is 1d8 for each point spent in this way. You can’t deal more additional damage than the amount shown in the Focused Strikes column of the guardian table."
        }, 
        "4": {
            "name": "Enlightenment",
            "levels": ["7th"],
            "details": "You can add half your Wisdom or Charisma modifier (your choice, rounded down, minimum of one) to any saving throw you make that doesn’t already include that modifier."
        }, 
        "5": {
            "name": "Redirect",
            "levels": ["15th"],
            "details": "When you would be affected by a weapon or force power that requires a Dexterity saving throw or attack roll and would affect only you, you can use your reaction to redirect that power to another target within 30 feet. If the weapon or power required a melee or ranged attack, make a melee or ranged force attack against the new target, as appropriate. If it required a Dexterity saving throw, the new target must make a Dexterity saving throw against your universal force save DC. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
        }, 
        "6": {
            "name": "Master of Moderation",
            "levels": ["20th"],
            "details": "The Force flows in perfect concert with your weapon attacks. Your Dexterity and Wisdom or Charisma scores (your choice) increase by 2. Your maximum for these scores increases by 2. Additionally, you can use your action to gain the following benefits for 1 minute: You have resistance to kinetic and energy damage from unenhanced weapons. You have advantage on saving throws against force powers. Additionally, you have resistance against the damage of force powers. When you use your action to cast an at-will force power that targets only one creature, you can target an additional creature within 5 feet of the original target and within the power’s range. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        }
    },
    class_id = 5
)
shien_djem_so_form = Archetype(
    name = "Shien/Djem So Form",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Bonus Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in heavy armor."
        }, 
        "2": {
            "name": "Form Basics",
            "levels": ["3rd"],
            "details": "You gain your choice of the Shien or Djem So lightsaber form, detailed in Chapter 6. If you already know the chosen form, you can instead choose another lightsaber form."
        }, 
        "3": {
            "name": "The Way of the Krayt Dragon",
            "levels": ["3rd"],
            "details": "As a bonus action, you can take a threatening stance for one minute. While in this stance, the first time you hit with a melee weapon attack using Strength each turn, you can attempt to damage another creature within 5 feet of the original target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to your Strength modifier. The damage is of the same type dealt by the original attack. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        },
        "4": {
            "name": "Channel the Force",
            "levels": ["3rd"],
            "details": "You gain one of the following Channel the Force options. Choose Blade Barrier for Shien or Falling Avalanche for Djem So. Blade Barrier: On your turn, when you deal melee weapon damage that includes your Strength modifier, you can forgo your Strength modifier to the damage roll, expend a use of your Channel the Force (no action required), and reduce your speed by half. If you do so, energy and kinetic damage you take from weapons before the end of your next turn is reduced by an amount equal to your Strength modifier. You can not use this feature if you have moved more than half your speed this turn. Falling Avalanche: On your turn, you can expend a use of your Channel the Force (no action required) and reduce your speed by half to gain advantage on the next ability check or attack roll you make using Strength before the end of your next turn. You can not use this feature if you have moved more than half your speed this turn."
        },
        "5": {
            "name": "Determination",
            "levels": ["7th"],
            "details": "You gain one of the following features. Choose Aggressive Negotiations for Shien or Reliable Vigor for Djem So. Aggressive Negotiations: You gain proficiency in Intimidation or Persuasion. Additionally, while you are wielding a weapon with which you are proficient, you can’t have disadvantage on Charisma (Intimidation) and Charisma (Persuasion) checks, and if the target would make a contested check, they can’t have advantage on it. Reliable Vigor: If your total for a Strength check or saving throw is less than your guardian level, you can use your guardian level in place of the total."
        },
        "6": {
            "name": "Presence",
            "levels": ["15th"],
            "details": "You gain one of the following features. Choose Precise Reflection for Shien or Brutal Strikes for Djem So. Precise Reflection: When you hit with an attack made by the saber reflect power, you can expend force points to deal additional damage to the target, which is the same type as the weapon’s damage. The additional damage is 1d8 for each point spent in this way. You can’t deal more additional damage than the amount shown in the Focused Strikes column of the guardian table. Brutal Strikes: The Force flowing through you grants you incredible strength. When you roll a 1 or 2 on a Force-Empowered Strikes or Improved Force-Empowered Strikes damage die, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. Additionally, when you spend force points to use your Force-Empowered Strikes feature, you gain temporary hit points equal to twice the number of points spent"
        },
        "7": {
            "name": "Master of Preseverance",
            "levels": ["20th"],
            "details": "Your might overwhelms even the most implacable of foes. Your Strength and Constitution scores increase by 2. Your maximum for these scores increases by 2. Additionally, you can use your action to gain the following benefits for 1 minute: You have resistance to kinetic and energy damage from unenhanced weapons. Once per turn, when you hit with a melee weapon attack using Strength, you can use your Force-Empowered Strikes feature at 1st-level without expending force points. You gain temporary hit points equal to the extra damage dealt. When a creature within 5 feet of you makes an attack roll against you, you can use your reaction to make a single weapon attack with advantage against that creature. If the attack hits, you impose disadvantage on the triggering attack roll. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        }
    },
    class_id = 5
)
soresu_form = Archetype(
    name = "Soresu Form",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Bonus Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in heavy armor."
        },
        "2": {
            "name": "Form Basics",
            "levels": ["3rd"],
            "details": "You gain the Soresu lightsaber form, detailed in Chapter 6. If you already know this form, you can instead choose another lightsaber form."
        },  
        "3": {
            "name": "The Way of the Mynock",
            "levels": ["3rd"],
            "details": "As a bonus action, you can enter a defensive stance for one minute. As a part of this bonus action, and as a bonus action on each of your turns, you can cast the saber ward power. When you do so, you have a number of special reactions equal to your proficiency bonus that you can only use to cast the saber reflect force power. You can only take one reaction per turn. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        },
        "4": {
            "name": "Channel the Force",
            "levels": ["3rd"],
            "details": "You gain the following Channel the Force option. Advancing Defender: When you cast the saber reflect power, you can expend a use of your Channel the Force to move up to 10 feet as a part of that same reaction. This movement does not provoke opportunity attacks."
        },
        "5": {
            "name": "Circle of Shelter",
            "levels": ["7th"],
            "details": "You learn to fend off strikes directed at you or other creatures nearby. If you or a creature you can see within 5 feet of you is hit by an attack, you can use your reaction to ward the creature if you’re wielding a melee weapon or a shield. Roll 1d8 and add the number rolled to the target’s AC against that attack. If the attack still hits, the target has resistance against the attack’s damage. You can use this feature a number of times equal to your Constitution modifier (a minimum of once), and you regain all expended uses when you finish a long rest."
        },
        "6": {
            "name": "Stand Aginst the Tide",
            "levels": ["15th"],
            "details": "When a hostile creature misses you with a melee attack, you can use your reaction to force that creature to repeat the same attack against another creature (other than itself) of your choice."
        },
        "7": {
            "name": "Master of Resilience",
            "levels": ["20th"],
            "details": "Your presence on the field of battle is an inspiration to your allies. Your Constitution and Wisdom or Charisma scores (your choice) increase by 2. Your maximum for those scores increases by 2. Additionally, you can use your action to gain the following benefits for 1 minute: You have resistance to kinetic and energy damage from unenhanced weapons. When you use the saber reflect force power, you can make a single melee attack on an enemy within 5ft of you as a part of that same reaction. You have advantage on Dexterity saving throws, as do your allies within 30 feet of you. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        } 
    },
    class_id = 5
)
crimson_order = Archetype(
    name = "Crimson Order",
    caster_type = "None",
    features = {
        "1": {
            "name": "Crimson Armaments",
            "levels": ["3rd"],
            "details": "You gain proficiency in light and medium armor. If you are already proficient in light and medium armor, you instead gain proficiency in heavy armor. Additionally, you can now gain the benefits of your Martial Arts and Unarmored Movement features while wearing armor as long as you are not wielding a shield. Additionally, you’ve learned to adapt to new weaponry. Over the course of an hour, which can be performed during a short rest, you can perform a kata with a weapon of your choice. You gain proficiency in that weapon if you do not already have proficiency, and it becomes a monk weapon for you. You can only adapt to one weapon at a time, and if you attempt to adapt to another weapon you immediately lose your proficiency with the chosen weapon."
        },
        "2": {
            "name": "Crimson Squall",
            "levels": ["6th", "11th", "17th"],
            "details": "You’ve learned to enhance your kata. As a bonus action while wielding a monk weapon, you can expend 1 focus point to cause the area within 5 feet of you to become difficult terrain for 1 minute. This area travels with you, and creatures within the area can not make opportunity attacks. At 11th level, the range of this area increases to 15 feet, and at 17th level, the range of this area increases to 30 feet."
        },
        "3": {
            "name": "Vigilant Sentinel",
            "levels": ["11th"],
            "details": "When you attempt to perceive your surroundings on your turn, you can opt to not move on that turn. If you avoid moving, you gain a +10 bonus to your Wisdom (Perception) checks until the start of your next turn. You lose this benefit if you move or fall prone, either voluntarily or because of some external effect."
        },
        "4": {
            "name": "Sovereign Protector",
            "levels": ["17th"],
            "details": "Your mastery of focus has allowed you to unlock your fullest potential in combat. As a bonus action, you can gain the following effects for 1 minute. Your speed is doubled. Your AC increases by 2. You have advantage on Dexterity saving throws. You gain an additional action of each of your turns. This action can be used only to take the Attack (one weapon attack only), Dash, Disengage, Hide, or Use an Object action. This effect ends early if you are incapacitated or die. Once you’ve used this feature, you can’t use it again until you finish a long rest."
        }
        
    },
    class_id = 6
)
echani_order = Archetype(
    name = "Echani Order",
    caster_type = "None",
    features = {
        "1": {
            "name": "Echani Weapons",
            "levels": ["3rd"],
            "details": "Your special martial arts training leads you to master the use of certain weapons. You gain the following benefits. Choose two types of weapons to be your Echani weapons: one vibroweapon and one blaster. Each of these weapons can be any simple or martial weapon that lacks the special property. You gain proficiency with these weapons if you don’t already have it. Weapons of the chosen types are monk weapons for you. Many of this order’s features work only with your Echani weapons. When you reach 6th, 11th, and 17th level in this class, you can choose another type of weapon to be an Echani weapon for you, following the criteria above. Agile Parry: If you make an unarmed strike as part of the Attack action on your turn and are holding an Echani weapon, you can use it to defend yourself if it is a melee weapon. You gain a +2 bonus to AC until the start of your next turn, while the weapon is in your hand and you aren’t incapacitated. Echani's Shot: You can use a bonus action on your turn to make your ranged attacks with an Echani weapon more deadly. When you do so, any target you hit with a ranged attack using an Echani weapon takes an extra 1d4 damage of the weapon’s type. You retain this benefit until the end of the current turn."
        },
        "2": {
            "name": "One with the Blade",
            "levels": ["6th"],
            "details": "You extend your focus into your Echani weapons, granting you the following benefits. Enhanced Echani Weapons: Your attacks with your Echani weapons count as enhanced for the purpose of overcoming resistance and immunity to unenhanced attacks and damage. Deft Strike: When you hit a target with an Echani weapon, you can spend 1 focus point to cause the weapon to deal extra damage to the target equal to your Martial Arts die. You can use this feature only once on each of your turns."
        },  
        "3": {
            "name": "Sharpen the Blade",
            "levels": ["11th"],
            "details": "You gain the ability to augment your weapons further with your focus. As a bonus action, you can expend up to 3 focus points to grant one Echani weapon you touch a bonus to attack and damage rolls when you attack with it. The bonus equals the number of points you spent. This bonus lasts for 1 minute or until you use this feature again. This feature has no effect on an enhanced weapon that already has a bonus to attack and damage rolls."
        },
        "4": {
            "name": "unerring Accuracy",
            "levels": ["17th"],
            "details": "Your mastery of weapons grants you extraordinary accuracy. If you miss with an attack roll using a monk weapon on your turn, you can reroll it. You can use this feature only once on each of your turns."
        }
    },
    class_id = 6
)
matukai_order = Archetype(
    name = "Matukai Order",
    caster_type = "None",
    features = {
        "1": {
            "name": "Force-Empowered Strikes",
            "levels": ["3rd"],
            "details": "You learn to channel the Force into your unarmed strikes and monk weapons, further enhancing your melee strikes. When you hit a creature with an unarmed strike or melee weapon attack with a monk weapon, you can spend 1 focus point to force the creature to make a Strength saving throw. On a failed save, it takes 2d6 force damage and is pushed up to 15 feet away from you. On a successful save, the creature only takes half as much damage and isn’t pushed."
        }, 
        "2": {
            "name": "Instinctive Leap",
            "levels": ["6th"],
            "details": "When a hostile creatures moves to within 5 feet of you, you can use your reaction to disengage and leap up to half your speed. If you end this movement in the air, you immediately fall to the ground."
        }, 
        "3": {
            "name": "Absorb Damage",
            "levels": ["11th"],
            "details": "You learn to channel the Force into your skin and bones, greatly enhancing your durability. You can use a bonus action to channel the Force throughout your body. Until the start of your next turn, you have resistance to kinetic and energy damage. You can use this feature a number of times equal to your Wisdom or Charisma modifier (your choice, a minimum of once). You regain all expended uses when you finish a long rest."
        },
        "4": {
            "name": "Control the Field",
            "levels": ["17th"],
            "details": "Whenever you use your Instinctive Leap feature, you can leap your entire movement speed instead of only half. Additionally, when you land, you can make an unarmed strike with advantage against a creature within 5 feet of you as part of the same reaction. On a hit, this attack deals an additional 2d6 force damage."
        }
    },
    class_id = 6
)
nightsister_order = Archetype(
    name = "Nightsister Order",
    caster_type = "None",
    features = {
        "1": {
            "name": "Ichor Lightning",
            "levels": ["3rd"],
            "details": "You gain a new attack option that you can use with the Attack action. This special attack is a ranged focus attack with a range of 30 feet. You are proficient with it, and you add your focus ability modifier to its attack and damage rolls. Its damage is necrotic, and it uses your Martial Arts die for its damage die. When you would make an unarmed strike as part of your Martial Arts bonus action attack or your Flurry of Blows, you can replace the attack with this one. When you reduce a creature to 0 hit points with this attack, you gain temporary hit points equal to your Wisdom or Charisma modifier + your monk level (your choice, minimum of one)."
        },
        "2": {
            "name": "Dark Magick",
            "levels": ["6th"],
            "details": "You can use your action to force each creature within 30 feet of you that can see you to make a Wisdom saving throw against your focus save DC or be charmed or frightened (your choice) of you until the end of your next turn."
        },  
        "3": {
            "name": "Mastery of Death",
            "levels": ["11th"],
            "details": "When you are reduced to 0 hit points, you can expend 1 focus point (no action required) to have 1 hit point instead."
        },
        "4": {
            "name": "Spirit Blade Assault",
            "levels": ["17th"],
            "details": "As an action, you conjure a blade of spirit energy and strike one creature within 5 feet of you with it, expending 1 to 10 focus points. The target must make a Constitution saving throw. On a failed save, it takes 2d10 necrotic damage per focus point spent, or half as much on a successful one."
        }  
    },
    class_id = 6
)
acquisitions_practice = Archetype(
    name = "Acquisitions Practice",
    caster_type = "None",
    features = {
        "1": {
            "name": "Fast and Agile",
            "levels": ["3rd"],
            "details": "You can use the bonus action granted by your Cunning Action to make a Dexterity (Sleight of Hand) check, use your demolitions kit or security kit to disarm a trap or open a lock, or take the Use an Object action. Additionally, climbing no longer costs you extra movement, and you gain the ability to move in flying leaps with incredible speed, precision, and power. When you move, instead of using your walking speed, you may take two short movements by flying. Each movement is at half your speed, and you must end each one on a solid object, a surface, or on the ground. If you do not, you fall and your movement ends. If you Dash, your bonus movement is applied to your normal speed, not this movement."
        },
        "2": {
            "name": "Deft Hands",
            "levels": ["3rd"],
            "details": "You learn a number of techniques to distract and confuse your opponents. When you deal Sneak Attack damage, you may choose to forgo two of your Sneak Attack dice to perform a deft hand maneuver. Some of your deft hand maneuvers require your target to make a saving throw to resist the deft hand maneuver’s effects. The saving throw DC is as follows: Deft Hands save DC = 8 + your proficiency bonus + your Dexterity modifier. Hinder: You attempt to distract your target in order to hinder their movement. The target must make a Constitution saving throw. On a failed save, it gains 1 slowed level until the end of its next turn and it makes the first Dexterity saving throw before the end of its next turn with disadvantage. Pilfer: ou attempt to pick your target’s pockets. The target must make a Wisdom saving throw. On a failed save, you have advantage on the first Dexterity (Sleight of Hand) check you make against the target before the end of your next turn. Tumble: You attempt to nimbly roll away. You immediately move 10 feet in a direction of your choice, and the target must make a Dexterity saving throw. On a failed save, this movement does not provoke opportunity attacks from the creature."
        },
        "3": {
            "name": "Supreme Sneak",
            "levels": ["9th"],
            "details": "You have advantage on a Dexterity (Stealth) check if you move no more than half your speed on the same turn. Additionally, as long as you aren’t incapacitated, you no longer take damage from falling less than 100 feet, and have resistance to falling damage."
        },
        "4": {
            "name": "Aerial Agility",
            "levels": ["13th"],
            "details": "Your agility in the air grants you the following benefits: When you move, you can instead take 3 short movements by flying. Whenever you end your flying movement and you are within 5 feet of a climbable surface, you can grab onto that surface as though you were climbing upon it."
        },
        "5": {
            "name": "thief's Reflexes",
            "levels": ["17th"],
            "details": "You can take two turns during the first round of any combat. You take your first turn at your normal initiative and your second turn at your initiative minus 10. You can’t use this feature when you are surprised. Additionally, you learn to utilize the momentum of your fall to make deadly vertical strikes. Whenever you fall at least 50 feet and land within 5 feet of an enemy creature you can use your reaction to make one weapon attack against that creature. If the attack is a Sneak Attack, you can deal three additional weapon dice worth of damage and the creature must make a Dexterity saving throw or be knocked prone."
        }
    },
    class_id = 7
)
beguiler_practice = Archetype(
    name = "Beguiler Practice",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Forcecasting",
            "levels": ["3rd"],
            "details": "You have derived powers from your emotional connection to the Force. You learn 4 force powers of your choice, and you learn more at higher levels, as shown in the Force Powers Known column of the Beguiler Practice Forcecasting table. You may not learn a force power of a level higher than your Max Power Level, and you may learn a force power at the same time you learn its prerequisite. You have a number of force points equal to your operative level, as shown in the Force Points column of the Beguiler Practice Forcecasting table, + your Wisdom or Charisma modifier (your choice). You use these force points to cast force powers. You regain all expended force points when you finish a long rest. Many force powers can be overpowered, consuming more force points to create a greater effect. You can overpower these abilities to a maximum level, which increases at higher levels, as shown in the Max Power Level column of the Beguiler Practice Forcecasting table. You may only cast force powers at 4th-level once. You regain the ability to do so after a long rest. Your forcecasting ability varies based on the alignment of the powers you cast. You use your Wisdom for light side powers, Charisma for dark side powers, and Wisdom or Charisma for universal powers (your choice). You use this ability score modifier whenever a power refers to your forcecasting ability. Additionally, you use this ability score modifier when setting the saving throw DC for a force power you cast and when making an attack roll with one. Force save DC = 8 + your proficiency bonus + your forcecasting ability modifier. Force attack modifier = your proficiency bonus + your forcecasting ability modifier"
        },  
        "2": {
            "name": "Facinating Display",
            "levels": ["3rd"],
            "details": "You can spend 1 minute attemping to distract and enthrall those around you. Choose a number of humanoids within 60 feet of you who watched your display for the duration, up to a number equal to your Charisma modifier (minimum of one). Each target must succeed on a Wisdom saving throw (DC = 8 + your proficiency bonus + your Charisma modifier) or be charmed by you. While charmed in this way, the target idolizes you, speaking glowingly of you to anyone who talks to it. Additionally, it hinders anyone who opposes you, although it avoids violence unless it was already inclined to fight on your behalf. This effect ends on a target after 1 hour, if it takes any damage, if you attack it, or if it witnesses you attacking or damaging any of its allies. If a target succeeds on this saving throw, the target has no hint you tried to charm it. Once you’ve used this feature, you must complete a long rest before you can use it again."
        },
        "3": {
            "name": "Mesmerizing presence",
            "levels": ["9th"],
            "details": "You have advantage on attack rolls against creatures charmed by you."
        },
        "4": {
            "name": "Enthralling Vigor",
            "levels": ["13th"],
            "details": "Whenever a creature fails a Wisdom or Charisma saving throw against a force power or class feature you use, you can gain temporary hit points equal to half your operative level (rounded down) + your Charisma modifier (minimum of one). You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain all expended uses when you finish a short or long rest."
        },
        "5": {
            "name": "Distracting Countenance",
            "levels": ["17th"],
            "details": "As a bonus action, you can mask yourself with the Force for 1 minute or until you are incapacitated. For the duration, whenever any creature tries to attack you for the first time on a turn, the attacker must make a Charisma saving throw (DC = 8 + your proficiency bonus + your Charisma modifier). On a failed save, it can’t attack you on this turn, and it must choose a new target for its attack or the attack is wasted. On a successful save, it can attack you on this turn, but it has disadvantage on any saving throw it makes against your powers on your next turn. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
        },
        "Beguiler Practice Table": {
            "3": {
                "Force Powers Known": "4",
                'Force Points': "3",
                "Max Power Level": "1st"
            },
            "4": {
                "Force Powers Known": "6",
                'Force Points': "4",
                "Max Power Level": "1st"
            },
            "5": {
                "Force Powers Known": "7",
                'Force Points': "5",
                "Max Power Level": "1st"
            },
            "6": {
                "Force Powers Known": "8",
                'Force Points': "6",
                "Max Power Level": "1st"
            },
            "7": {
                "Force Powers Known": "10",
                'Force Points': "7",
                "Max Power Level": "2nd"
            },
            "8": {
                "Force Powers Known": "11",
                'Force Points': "8",
                "Max Power Level": "2nd"
            },
            "9": {
                "Force Powers Known": "12",
                'Force Points': "9",
                "Max Power Level": "2nd"
            },
            "10": {
                "Force Powers Known": "13",
                'Force Points': "10",
                "Max Power Level": "2nd"
            },
            "11": {
                "Force Powers Known": "14",
                'Force Points': "11",
                "Max Power Level": "2nd"
            },
            "12": {
                "Force Powers Known": "15",
                'Force Points': "12",
                "Max Power Level": "2nd"
            },
            "13": {
                "Force Powers Known": "17",
                'Force Points': "13",
                "Max Power Level": "3rd"
            },
            "14": {
                "Force Powers Known": "18",
                'Force Points': "14",
                "Max Power Level": "3rd"
            },
            "15": {
                "Force Powers Known": "19",
                'Force Points': "15",
                "Max Power Level": "3rd"
            },
            "16": {
                "Force Powers Known": "20",
                'Force Points': "16",
                "Max Power Level": "3rd"
            },
            "17": {
                "Force Powers Known": "22",
                'Force Points': "17",
                "Max Power Level": "4th"
            },
            "18": {
                "Force Powers Known": "23",
                'Force Points': "18",
                "Max Power Level": "4th"
            },
            "19": {
                "Force Powers Known": "24",
                'Force Points': "19",
                "Max Power Level": "4th"
            },
            "20": {
                "Force Powers Known": "25",
                'Force Points': "20",
                "Max Power Level": "4th"
            }
        }
    },
    class_id = 7
)
gunslinger_practice = Archetype(
    name = "Gunslinger Practice",
    caster_type = "None",
    features = {
        "1": {
            "name": "Dive for Cover",
            "levels": ["3rd"],
            "details": "You learn to quickly move into cover when under fire. Once per round, when you are the target of a ranged attack, or you are subjected to an effect that allows you to make a Dexterity saving throw, and there is cover within 10 feet of you, you can move up to 10 feet (no action required). You must end this movement in cover. You can use this feature a number of times equal to your Dexterity modifier (a minimum of once). You regain all expended uses when you complete a long rest."
        },
        "2": {
            "name": "trick Shooter",
            "levels": ["3rd"],
            "details": "You learn a number of trick shots you can use to debilitate enemies and impress allies. When you deal Sneak Attack damage to a creature, you may choose to forgo two of your Sneak Attack dice to make the attack a trick shot. Some of your trick shots require your target to make a saving throw to resist the trick shot’s effects. The saving throw DC is calculated as follows: Trick Shot save DC = 8 + your proficiency bonus + your Dexterity modifier. Blinding Shot: You attempt to blind the target. The target must make a Constitution saving throw or be blinded until the end of your next turn. Brutal Shot: You attempt to knock the target prone. The target must make a Strength saving throw or be knocked prone. Hampering Shot: You attempt to hobble the enemy’s movement. The target must make a Dexterity saving throw. If it fails, it gains 1 slowed level and it has disadvantage on Dexterity saving throws until the end of its next turn."
        }, 
        "3": {
            "name": "Spinning Flourish",
            "levels": ["9th"],
            "details": "You can flourish your weapon in an intimidating or charming manner. As an action, you can cause one creature within 60 feet to make a Wisdom saving throw (DC = 8 + your proficiency bonus + your Dexterity modifier). On a failed save, the target is charmed or frightened by you (your choice) until the end of your next turn."
        }, 
        "4": {
            "name": "Ricochet Shot",
            "levels": ["13th"],
            "details": "You learn how to work all the angles. Once per turn, when you take the Attack action and miss with a ranged weapon attack, you can repeat the attack against a different target within 10 feet of the original target (no action required)."
        },
        "5": {
            "name": "Quickraw",
            "levels": ["17th"],
            "details": "You learn to perform miracles with just a blaster and some nerve. On your first turn in combat, if you aren’t surprised, you can use your action to attack creatures that have not yet acted. Choose up to six such creatures that you can see, making a ranged weapon attack against each. On a hit, you deal normal weapon damage and can apply a single trick shot to each attack made this way. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
        }  
    },
    class_id = 7
)
sharpshooter_practice = Archetype(
    name = "Sharpshooter Practice",
    caster_type = "None",
    features = {
        "1": {
            "name": "Assume the Position",
            "levels": ["3rd"],
            "details": "You don’t need advantage on your attack roll to use your Sneak Attack if your target is greater than 30 feet from you and no enemies are within 5 feet of you. Additionally, standing up from prone now only costs 5 feet of movement. Additionally, you gain proficiency with two martial blasters of your choice."
        },
        "": {
            "name": "Placed Shots",
            "levels": ["3rd"],
            "details": "You perfect the art of placing distant shots for maximum effectiveness in debilitating and controlling your enemies. When you deal Sneak Attack damage to a creature, you may choose to forgo two of your Sneak Attack dice to make the attack a placed shot. Some of your placed shots require your target to make a saving throw to resist the placed shot’s effects. The saving throw DC is calculated as follows: Placed Shot save DC = 8 + your proficiency bonus + your Dexterity modifier. Disarming Shot: You attempt to disarm a creature with your attack. The target must succeed on a Strength saving throw or be forced to drop one item of your choice that it’s holding. The object lands at its feet. Penetrating Shot: You attempt to damage another target with the same attack. Choose a second target within 15 feet of and directly behind your initial target. If the original attack roll would hit the second target, it takes two dice worth of Sneak Attack damage. The damage is of the same type dealt by the original attack. Suppressive Shot: You attempt to pin the target to its location. The target must succeed on a Wisdom saving throw or be frightened of you until the end of its next turn."
        },  
        "3": {
            "name": "Head Shot",
            "levels": ["9th"],
            "details": "You are at your deadliest when your enemies are unaware of the danger they are in. You have advantage on attack rolls against any creature that hasn’t taken a turn in combat yet. Additionally, any hit you score against a creature that is surprised is a critical hit."
        },
        "4": {
            "name": "Distracting Shot",
            "levels": ["13th"],
            "details": "You are able to defend your compatriots from afar. When a friendly creature you can see within your weapon’s normal range is the target of a ranged attack, or forced to make a saving throw, and the source of the effect is within your weapon’s normal range, you can use your reaction to make a ranged weapon attack against the source. On a hit, instead of dealing damage, the target of your attack has disadvantage on the attack roll against your ally, or your ally has advantage on the saving throw to resist the effect."
        },
        "5": {
            "name": "Double Tap",
            "levels": ["17th"],
            "details": "You’ve learned to capitalize when you have the advantage. When you take the Attack action and make an attack with advantage, you can choose to forgo the advantage. If you do, you can make an additional attack against the target or another creature within 5 feet of it (no action required). Both attacks can benefit from your Sneak Attack damage, instead of only one."
        } 
    },
    class_id = 7
)
doctor_pursuit = Archetype(
    name = "Doctor Pursuit",
    caster_type = "None",
    features = {
        "1": {
            "name": "Medical Practitioner",
            "levels": ["3rd"],
            "details": "You gain proficiency with biochemist’s kits and your choice of the Medicine or Nature skills. Additionally, you can’t have disadvantage on checks you make with them."
        },
        "2": {
            "name": "Remote Healer",
            "levels": ["3rd"],
            "details": "You have learned to deploy medicine from a range. When you use a maneuver targeting an ally that is the target of your Critical Analysis feature, that maneuver’s range becomes 30 feet."
        },  
        "3": {
            "name": "Additional Maneuvers",
            "levels": ["3rd"],
            "details": "You gain access to new maneuvers which reflect the progress of your studies into the medical arts. Whenever you learn a new maneuver, you can choose from any of the following as well. The maneuvers are listed in alphabetical order.",
            "maneuvers": {
                "Adrenaline Hit": {
                    "details": "You can use an action and expend one superiority die to inject a creature with regenerative medication that temporarily enhances their agility. When you do so, a creature you can touch regains hit points equal to the superiority die roll. Additionally, until the start of your next turn, when that creature would take damage, the amount is reduced by an amount equal to your maneuver modifier."
                },
                "Emergency Prescription": {
                    "details": "As an action, you can expend one superiority die and touch a creature. That creature regains hit points equal to result of the die + your maneuver modifier, and when that creature makes their first ability check, attack roll, or saving throw before the start of your next turn they roll the superiority die and add it to the roll."
                },
                "Enhancement Injection": {
                    "details": "As an action, you can expend one superiority die to inject a creature you can touch with enhancements, granting them temporary hit points equal to the superiority die roll + your maneuver modifier, which last for 1 minute. Additionally, when the target makes a Strength or Constitution check or saving throw while it has these temporary hit points, it gains a bonus equal to your maneuver modifier."
                },
                "Neuroblock": {
                    "details": "When you make an attack roll, you can expend a superiority die and add it to the attack roll. On a hit, the creature’s next attack has disadvantage and it cannot regain hit points until the start of your next turn."
                },
                "Reassure": {
                    "details": "As an action, you can expend a superiority die and call out to a creature within 60 feet that can see or hear you that is charmed, frightened, or stunned. When you do so, that creature immediately makes another saving throw, adding the amount rolled to the save."
                },
                "Remove Toxins": {
                    "details": "As an action, you can expend a superiority die to purge the toxins from a creature you can touch. The target regains hit points equal to the number rolled and, if it is poisoned or diseased, you neutralize the poison or disease. If more than one poison or disease afflicts the target, you neutralize one poison or disease that you know is present, or you neutralize one at random."
                },
                "Smelling Salts": {
                    "details": "As a bonus action, you can expend a superiority die to heal a creature you can touch by a number of hit points equal to the number rolled."
                },
                "Transfusion": {
                    "details": "Once per turn when you hit a creature with a finesse melee weapon, you can expend a superiority to give you or an ally that is within 5 feet of the creature a transfusion. Add the superiority dice to the damage you deal. You or your ally gain hit points equivalent to the damage you deal to the creature. You can be the creature hit with the attack as long as there is an ally with 5 feet of you, in which you can let it hit without rolling an attack and must choose an ally to heal with the transfusion."
                },
                "Weak Point strike": {
                    "details": "When you hit a creature with a weapon attack, you can expend a superiority die to temporarily daze the creature. Add the number rolled to the damage of the weapon attack and the creature must succeed on a Constitution saving throw or be stunned until the end of its next turn."
                }
            }
        },
        "4": {
            "name": "Field Surgeon",
            "levels": ["6th", "11th"],
            "details": "Whenever you expend superiority dice to restore hit points or grant temporary hit points to a creature, you can roll an additional die d6 and add it to the roll. This die increases to d8 at 9th level, d10 at 13th level, and d12 at 17th level. Additionally, whenever you expend superiority dice to restore hit points or grant temporary hit points to a creature, if the creature is the target of your Critical Analysis, you can instead choose the maximum on both dice. Once you’ve used this feature, you must finish a short or long rest before you can use it again. Starting at 11th level, you can use it twice before a rest, but only once on the same turn."
        },
        "5": {
            "name": "Resuscitate",
            "levels": ["9th"],
            "details": "Through your medical studies you have learned to delay seemingly inevitable death. As a bonus action, you can stabilize a creature you can touch that has 0 hit points. Additionally, as an action, you can tend to a creature you can touch that has died since the end of your last turn. The creature immediately regains 1 hit point and stabilizes. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
        },
        "6": {
            "name": "Panacea",
            "levels": ["17th"],
            "details": "You’ve developed the formula to concoct a cure-all miracle solution: a panacea. Over the course of 10 minutes, you can expend rare medical supplies worth 1,000 cr to create your panacea in a simple syringe. The panacea retains its potency for 24 hours. As a bonus action, a creature can use the panacea. Alternatively, as an action, they can administer it to another creature within 5 feet. The target has its exhaustion level reduced by one and regains all of its hit points. If the target is diseased, poisoned, paralyzed, or stunned, the condition ends. Once you create a panacea, you can’t create another until you finish a long rest."
        },
        "1": {
            "name": "Doctor Discoveries",
            "details": "When you select this pursuit, you gain access to new discoveries which reflect the progress of your studies into the medical arts. Whenever you learn a new discovery, you can choose from any of the following as well. The discoveries are listed in alphabetical order.",
            "Discoveries": {
                "Advanced Remote Healer": {
                    "prerequisite": "11th",
                    "details": "The range of your Remote Healer feature increases to 60 feet."
                },
                "Experimental Treatments": {
                    "details": "Your medication and treatments are known to be untested and unstable. Immediately after you use a maneuver that causes a creature to regain hit points or gain temporary hit points, you can choose to roll on the Side Effects table to the right. The condition or effect lasts until the creature completes a long rest, or you use this feature again. You can use this feature a number of times equal to your proficiency bonus, as shown in the scholar table. You regain all expended uses when you finish a short or long rest."
                },
                "From the Brink": {
                    "prerequisite": "7th",
                    "details": "If the target of your Critical Analysis feature would be reduced to 0 hp, you may use your reaction and end your Critical Analysis feature to have them be reduced to 1 hp instead. Once a creature has benefited from this feature, they must complete a long rest before they can do so again."
                },
                "Health Advisor": {
                    "details": "Whenever a creature that is a target of your Critical Analysis feature begins their turn, you can use your reaction to give them temporary hit points equal to one-fourth your scholar level (rounded down) + your proficiency bonus, as shown in the scholar table, which last until the start of their next turn."
                },
                "Patient Protector": {
                    "prerequisite": "5th",
                    "details": "You can treat creatures within 5 feet of the target of your Critical Analysis feature as if they were also targets of your Critical Analysis"
                },
                "Surgical Precision": {
                    "prerequisite": "5th",
                    "details": "When you hit a creature that is the target of your Critical Analysis feature with a weapon attack, it takes additional damage equal to your Dexterity modifier."
                },
                "tend the Wounded": {
                    "details": "If you or any friendly creatures you can touch regain hit points by spending one or more Hit Dice at the end of a short rest, each of those creatures regain 1d4 extra hit points. This die increases when you reach certain levels in this class: 1d6 at 5th level, 1d8 at 9th level, 1d10 at 13th level, and to 1d12 at 17th level."
                },
                'Side Effects': {
                    "details": "Roll a d20",
                    "1": {
                        "details": "The creature turns out to be allergic to this specific treatment. Every ability score is reduced by 1."
                    },
                    "2": {
                        "details": "The creature starts sneezing uncontrollably. Any attack rolls with a die roll value of 19 results in a miss due to a poorly timed sneeze."
                    },
                    "3": {
                        "details": "The creature’s legs become swollen. The creature gains 1 slowed level."
                    },
                    "4": {
                        "details": "The creature becomes one size larger or smaller."
                    },
                    "5": {
                        "details": "The skin at their joints turns into a wooden material, giving them a bonus of +2 to AC."
                    },
                    "6": {
                        "details": "The creature’s body starts producing powerful stomach acid in high amounts. The creature can use an action to spew stomach acid in a 15 feet cone. The DC for this saving throw equals 8 + your proficiency bonus + your Constitution modifier. A creature takes 2d6 acid damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 5th level, 4d6 at 11th level, and 5d6 at 17th level."
                    },
                    "7": {
                        "details": "The creature becomes mute and has uncontrollable gas. They have disadvantage on Dexterity (Stealth) checks that rely on smell."
                    },
                    "8": {
                        "details": "The creature’s eyes glows bright red. The creature also gains darkvision, but if they already have darkvision they get a light headache instead."
                    },
                    "9": {
                        "details": "The creature gains advantage on perception checks based on hearing, but everything seems uncomfortably loud to them. They gain vulnerability to sonic damage."
                    },
                    "10": {
                        "details": "The treatment slows down their brain function, reducing their Intelligence by 4."
                    },
                    "11": {
                        "details": "The creature’s skin turns dark purple. If they are already purple, they turn bright pink instead."
                    },
                    "12": {
                        "details": "The creature becomes covered in sickly, green pustules. When the creature is hit by a melee attack, the attacker takes 1d4 poison damage."
                    },
                    "13": {
                        "details": "The creature’s skin starts to seriously bloat up from internal pressure build-up, and a strong impact may cause it to explode. Whenever the creature takes damage, the creature has to pass a concentration check or the creature takes kinetic damage equal to half their maximum hit points. Other creatures within 10 feet of the explosion also take a fourth of the damage. Once this explosion occurs, their skin becomes very soft."
                    },
                    "14": {
                        "details": "The creature rapidly grows body hair all over, including the face, until they resemble a wookiee. If they are already a wookiee, the reverse effect occurs; all hair immediately falls off, leaving the skin bare."
                    },
                    "15": {
                        "details": "The creature’s body temperature fluctuates to extremes. They gain resistance to cold and fire damage."
                    },
                    "16": {
                        "details": "The creature becomes ravenous. Every hour they haven’t eaten a meal they gain a level of exhaustion."
                    },
                    "17": {
                        "details": "The creature believes they are the chosen one."
                    },
                    "18": {
                        "details": "	The creature has a difficult time resting. The amount they heal from Hit Dice is now halved"
                    },
                    "19": {
                        "details": "The creature’s movement speed is increased by 15 feet, and opportunity attacks on them have disadvantage."
                    },
                    "20": {
                        "details": "	The creature gains 10d10 hit points, and they feel happy and carefree."
                    }
                }
            }
        },
    },
    class_id = 8
)
gambler_pursuit = Archetype(
    name = "Gambler pursuit",
    caster_type = "None",
    features = {
        "1": {
            "name": "Gambler's Aptitude",
            "levels": ["3rd"],
            "details": "You gain proficiency with your choice of gaming set and your choice of the Insight, Deception, Persuasion, or Sleight of Hand skills. Additionally, you can’t have disadvantage on checks you make with them."
        },
        "2": {
            "name": "Risk Versus Reward",
            "levels": ["3rd", "9th", "13th", "17th"],
            "details": "When you make your first attack on your turn against the target of your Critical Analysis feature, you can decide to gamble by rolling a d6. On a roll of 4 or higher, you have advantage on attack rolls against that creature until the start of your next turn. On a roll of 3 or lower, that creature instead has advantage on attack rolls against you until the start of your next turn. This die increases to d8 at 9th level, d10 at 13th level, and d12 at 17th level."
        },  
        "3": {
            "name": "Additional Maneuvers",
            "levels": ["3rd"],
            "details": "You gain access to new maneuvers which reflect your deep understanding of chance. Whenever you learn a new maneuver, you can choose from any of the following as well. The maneuvers are listed in alphabetical order.",
            "maneuvers": {
                "All In": {
                    "details": "When you make an attack roll, and the result is less than 20, you can expend a superiority die and roll it, adding it to the roll. If the resulting sum is 20 or 23, the attack is considered a critical hit."
                },
                "Blind Luck": {
                    "details": "When you fail an ability check, you can expend a superiority die. If the result of your ability check plus the superiority die is within a range equal to half your proficiency bonus (rounded down) above or below the check’s DC, you pass the check instead."
                },
                "Double Bluff": {
                    "details": "If on the same round of combat that you have missed a weapon attack, an enemy also misses you with a weapon attack, you can expend a superiority die and make a single weapon attack, adding the results of your superiority die to both the attack and damage rolls."
                },
                "The idiot's Array": {
                    "details": "When a creature hits you with a weapon attack roll, you can expend a superiority die and roll it. On a roll of 4 or higher, you take minimum damage on the damage roll and subtract the value of the superiority die. On a roll of 3 or lower, you instead take the maximum."
                },
                "Played their hand": {
                    "details": "When a creature hits you with an opportunity attack while within 5 feet of you, you can use your reaction and expend a superiority die to impose disadvantage on the attack roll. If the attack misses, you can make a Dexterity (Sleight of Hand) check contested by the attacker’s Strength (Athletics) or Dexterity (Acrobatics) check (their choice) as a part of this reaction. On a success, the target drops the weapon it made the attack with. If you are within 5 feet of the target, and you have a free hand, you can catch the item. Otherwise, the object lands at its feet."
                },
                "Pure Sabacc": {
                    "details": "When you score a critical hit with a weapon attack, you can expend a superiority die and roll it. On a roll of 4 or higher, you deal maximum damage on the weapon’s damage roll, including the superiority die. On a roll of 3 or lower, you instead deal the minimum."
                },
                "Raise the Stakes": {
                    "details": "When the target of your Critical Analysis feature makes an attack roll against you, you can use your reaction to expend a superiority die. Roll the die and subtract the result from the enemy’s attack roll, but add the result to their damage roll on a hit."
                },
                "Take a Chance": {
                    "details": "Before making an attack roll, you can expend a superiority die. On a miss, you lose that superiority die and do not benefit from it in any way. On a hit, you can choose two other maneuvers that you know, and subject the target to both maneuvers, without expending additional superiority dice."
                },
                "Tiebreaker": {
                    "details": "When you roll a superiority die as a part of a maneuver you learned from this class, you can expend another superiority die and use the total of both dice."
                }
            }
        },
        "4": {
            "name": "Lucky Number 7",
            "levels": ["6th"],
            "details": "Whenever you roll a 7 on an attack roll against the target of your Critical Analysis feature, the attack automatically hits and you regain a superiority die. You can not have more superiority dice than the amount shown in the Superiority Dice column of the scholar table. When attacking with advantage or disadvantage, this effect applies if either roll is a 7. If both rolls are a 7, the attack is a critical hit."
        },
        "5": {
            "name": "Tell me the Odds",
            "levels": ["9th", "13th", "17th"],
            "details": "If the target of your Critical Analysis hits you with a weapon attack roll, you can use your reaction to roll a d8. On a 4 or higher, you impose disadvantage on the roll. If the target already had disadvantage, they must instead reroll one of the dice once (your choice). This die increases to d10 at 13th level and d12 at 17th level."
        },
        "6": {
            "name": "Borrowed Luck",
            "levels": ["17th"],
            "details": "You have gained the ability to unnaturally alter luck in your favor. Once per round, after an attack roll, saving throw, or ability check is rolled by you or a creature that you can see, you can replace the number on the d20 with a 7. Note the number on the d20 of the roll that you replaced. That number becomes your borrowed luck roll. While you have a borrowed luck roll, you can expend it and replace any ability check, attack roll, or saving throw made by you or a creature that you can see with the value of the borrowed luck roll. You can only have one borrowed luck roll at a time, and you lose any unused borrowed luck rolls when you complete a short or long rest."
        },
        "7": {
            "name": "Gambler Discoveries",
            "details": "When you select this pursuit, you gain access to new discoveries which reflect your deep understanding of chance. Whenever you learn a new discovery, you can choose from any of the following as well. The discoveries are listed in alphabetical order.",
            "discoveries": {
                "Ace up your sleeve": {
                    "details": "Whenever you make a Dexterity (Sleight of Hand) or Charisma (Deception) check, you can expend a superiority die, adding the result to your total for the check."
                },
                "Against the house": {
                    "details": "Whenever you would make a Charisma (Persuasion) check involving haggling, you can instead challenge the target to a game of chance. If they accept your offer, you can make an ability check with an available gaming set. If you win the challenge, you automatically succeed on the Charisma (Persuasion) check."
                },
                "Ante Up": {
                    "details": "When you roll initiative, are not surprised, and end up first in the initiative order, you can take one additional action on top of your regular action and a possible bonus action during your first turn in combat."
                },
                "Calculated Bluff": {
                    "details": "When you make an ability check using your Charisma, you can choose to instead make the check using your Intelligence or Wisdom modifier (your choice)."
                },
                "Cold Read": {
                    "prerequisite": "5th",
                    "details": "As an action, you may make a Wisdom (Insight) check contested by a target’s Charisma (Deception) check. On a success, you know the next action the target intends to take, so long as the situation does not change dramatically."
                },
                "Feeling the Pressure": {
                    "prerequisite": "13th",
                    "details": "Whenever you roll a 4 or higher on your Risk Versus Reward feature, the target of your Critical Analysis feature also has disadvantage on attack rolls made against you until the start of your next turn."
                },
                "The Magic Number": {
                    "prerequisite": "7th",
                    "details": "Whenever you roll a 7 on an ability check or saving throw, you can reroll the ability check or saving throw with advantage."
                }
            }
        }
    },
    class_id = 8
)
politician_pursuit = Archetype(
    name = "Politician Pursuit",
    caster_type = "None",
    features = {
         "1": {
            "name": "Silver Tonge",
            "levels": ["3rd"],
            "details": "You learn your choice of two languages and your choice of Charisma skill. Additionally, you can’t have disadvantage on checks you make with it."
        },
        "2": {
            "name": "Motivating Diplomat",
            "levels": ["3rd"],
            "details": "When you are the target of your Critical Analysis feature, you and all allies within 10 feet of you gain a bonus to their AC equal to half your Critical Analysis modifier (rounded down)."
        },   
        "3": {
            "name": "additional Maneuvers",
            "levels": ["3rd"],
            "details": "You gain access to new maneuvers which reflect the progress of your studies into the political world. Whenever you learn a new maneuver, you can choose from any of the following as well. The maneuvers are listed in alphabetical order.",
            "maneuvers": {
                "Call to Arms": {
                    "details": "If you are surprised at the start of combat and aren’t incapacitated, you can expend one superiority die to act normally. Additionally, on your first turn in combat, as a bonus action you can make a call to arms. When you do so, a number of creatures equal to the amount rolled on the superiority die that you choose within 30 feet who can see or hear you may act normally on their first turn."
                },
                "Call the Guards": {
                    "details": "When a creature makes an attack roll against you, you can use your reaction and expend a superiority die and command a willing ally within 5 feet of that creature to use their reaction to intercede. The creature is then forced to make an attack on the ally instead. If the attack misses, the ally can immediately make a weapon attack against that creature as a part of that same reaction. Roll the superiority die, and add the result to the ally’s attack roll."
                },
                "Charge": {
                    "details": "As a bonus action on your turn, you can expend one superiority die to spurn your allies to move. Until the start of your next turn, creatures you choose within 10 feet of you who can see or hear you can move an additional distance equal to 5 times the superiority die rolled on their turn and ignore unenhanced difficult terrain."
                },
                "Encourging Speech": {
                    "details": "You can expend a superiority die to give an encouraging speech, spending the next minute rallying your allies. You grant a number of creature up to your maneuver modifier temporary hit points equal to the amount rolled on the superiority die + your proficiency bonus, as shown in the scholar table."
                },
                "incite": {
                    "details": "On your turn, you can use an action and expend one superiority die to bolster the resolve of one of an ally. When you do so, choose an ally who can see or hear you within 30 feet of you. The ally can add your maneuver modifier to every damage roll they make until the start of your next turn."
                },
                "Overwhelming Presence": {
                    "details": "As an action, you can make a Charisma (Persuasion) or Charisma (Intimidation) skill check and expend one superiority die to attempt to charm or frighten a humanoid creature who can see or hear you within 60 feet. Add the superiority die to the roll. The target makes a contested Wisdom (Insight) check. If your check succeeds, the target is charmed by you if you used Persuasion, or frightened of you if you used Intimidation, until the end of your next turn."
                },
                "Self-Preservation": {
                    "details": "As a reaction when you make a saving throw against an effect you can see, you can expend a superiority die and add the result. You can use this maneuver before or after making the saving throw, but before any effects of the saving throw are det-ermined."
                },
                "Steady the Nerves": {
                    "details": "As an action, you can expend one superiority die to strengthen your allies’ defences. Roll a superiority die. Until the end of your next turn, you and all allies within 5 feet of you when you use this action has a bonus to any saving throws they make equal to amount rolled."
                },
                "tyrannical Strike": {
                    "details": "When you hit a creature with a weapon attack, you can expend one superiority die and use your reaction to issue a one-word command to a creature who can see or hear you. You add the superiority die to the attack’s damage roll, and the target must succeed on a Wisdom saving throw. On a failed save, the target must follow the command on its next turn. The target automatically succeeds if it is immune to charm, it doesn’t understand your language, or if your command is directly harmful to it."
                }
            }
        }, 
        "4": {
            "name": "Force of Personality",
            "levels": ["6th"],
            "details": "As an action, you suggest a course of activity (limited to a sentence or two) to influence a creature you can see within range that can hear and understand you. Creatures that can’t be charmed are immune to this effect. The suggestion must be worded in such a manner as to make the course of action sound reasonable. Asking the creature to stab itself, throw itself onto a spear, immolate itself, or do some other obviously harmful act ends the effect. The target must make a Wisdom saving throw against your maneuver save DC. On a failed save, the target is charmed by you, and it pursues the course of action you described to the best of its ability. The suggested course of action can continue for up to 24 hours. If the suggested activity can be completed in a shorter time, the effect ends when the subject finishes what it was asked to do. You can also specify conditions that will trigger a special activity during the duration. For example, you might suggest that an officer givers her gun to the first smuggler she meets. If the condition isn’t met before the effect ends, the activity isn’t performed. If you or any of your companions damage the target, the effect ends. You can use this feature a number of times equal to your proficiency bonus, as shown in the scholar table. You regain all expended uses when you finish a long rest."
        }, 
        "5": {
            "name": "Reassemble",
            "levels": ["9th"],
            "details": "You may use to a bonus action to call your allies towards you. When you do so, choose a number of creatures that you can see within 60 feet of you equal to your Critical Analysis modifier (minimum of one). They can use their reaction to immediately move a number of feet equal to their speed. This movement does not provoke opportunity attacks, and they must end this movement closer to you than they started. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
        }, 
        "6": {
            "name": "Beguiling Presence",
            "levels": ["17th"],
            "details": "Humanoids within 60 feet are particularly susceptible to your presence. Humanoids within range have disadvantage on saving throws against any charm or fear effects that originate from you."
        }, 
        "7": {
            "name": "Politician Discoveries",
            "details": "When you select this pursuit, you gain access to new discoveries which reflect the progress of your studies into the political world. Whenever you learn a new discovery, you can choose from any of the following as well. The discoveries are listed in alphabetical order.",
            "discoveries": {
                "Charming Feint": {
                    "details": "Allies within range of your Motivating Diplomat feature also gain a bonus to their damage rolls equal to half your Intelligence, Wisdom, or Charisma modifier (rounded down, chosen when you learn this discovery)."
                },
                "Demanding Leader": {
                    "prerequisite": "5th",
                    "details": "The range of each of your maneuvers increases by 10 feet. If the range is touch, it becomes 10 feet."
                },
                "Dominating Presence": {
                    "prerequisite": "15th",
                    "details": "As a bonus action, you can call out to a humanoid who can understand you that is charmed by you or frightened of you to direct their next action. The target must succeed a Wisdom saving throw against your maneuver save DC. On a failed save, until the end of your next turn, the creature takes only the actions you choose, and doesn’t do anything that you don’t allow it to do. During this time you can use your reaction to force the creature to use its reaction. Once you’ve used this feature, you must complete a short or long rest before you can use it again."
                },
                "Influencer": {
                    "prerequisite": "5th",
                    "details": "The range on the your Motivating Diplomat feature is increased to 15 feet."
                },
                "Reliable Words": {
                    "prerequisite": "9th",
                    "details": "When you make a Deception, Intimidation, or Persuasion skill check, you may treat any roll 9 or lower as if you had rolled a 10."
                },
                "Social Oppertunist": {
                    "details": "You can add half your proficiency bonus (rounded down) to any Charisma check you make that doesn’t already include your proficiency bonus."
                },
                "Tyrant's Ferocity": {
                    "details": "You have advantage on any attack against a creature that is charmed by you or frightened of you."
                }
            }
        }
    },  
    class_id = 8
)
tactician_pursuit = Archetype(
    name = "Tactician Pursuit",
    caster_type = "None",
    features = {
       "1": {
            "name": "Battle Display",
            "levels": ["3rd"],
            "details": "You gain proficiency in martial blasters and martial vibroweapons"
        },
        "2": {
            "name": "Tactical Mastery",
            "levels": ["3rd"],
            "details": "You learn to better command your allies to victory from afar. Your Critical Analysis range is increased to 90 feet."
        },
        "3": {
            "name": "Additional Maneuvers",
            "levels": ["3rd"],
            "details": "You gain access to new maneuvers which reflect your mastery in the field of combat. Whenever you learn a new maneuver, you can choose from any of the following as well. The maneuvers are listed in alphabetical order.",
            "maneuvers": {
                "Bolster": {
                    "details": "On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equals to the superiority die roll + maneuver modifier."
                },
                "Commander's Strike": {
                    "details": "When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of your companions to strike. When you do so, choose a friendly creature within 60 feet who can see or hear you and expend one superiority die. That creature can immediately use its reaction to make one weapon attack, adding your superiority die to the attack’s damage roll."
                },
                "Disarming Attack": {
                    "details": "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to disarm the target, forcing it to drop one item of your choice that it’s holding. You add the superiority die to the attack’s damage roll, and the target must make a Strength saving throw. On a failed save, it drops the object you choose. The object lands at its feet."
                },
                "Distracting Strike": {
                    "details": "When you hit a creature with a weapon attack, you can expend one superiority die to distract the creature, giving your allies an opening. You add the superiority die to the attack’s damage roll. The next attack roll against the target by an attacker other than you has advantage if the attack is made before the start of your next turn."
                },
                "Maneuvering Attack": {
                    "details": "When you hit a creature with a weapon attack, you can expend one superiority die to maneuver one of your allies into a more advantageous position. You add the superiority die to the attack’s damage roll, and you choose a friendly creature who can see or hear you. That creature can use its reaction to move up to half its speed without provoking opportunity attacks from the target of your attack."
                },
                "Pushing Attack": {
                    "details": "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to drive the target back. You add the superiority die to the attack’s damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you push the target up to 15 feet away from you."
                },
                "Riposte": {
                    "details": "When a creature misses you with a melee attack, you can use your reaction and expend one superiority die to make a melee weapon attack against the creature. If you hit, you add the superiority die to the attack’s damage roll."
                },
                "Scholar's parry": {
                    "details": "When a creature damages you with a weapon attack, you can use your reaction and expend one superiority die to reduce the damage by the number you roll on your superiority die + your maneuver modifier."
                },
                "Targeted Attack": {
                    "details": "When you make a weapon attack roll, you can expend one superiority die to add it to the roll. You can use this maneuver before or after making the attack roll, but before any effects of the attack are applied."
                },
                "Trip Attack": {
                    "details": "When you hit a creature with a weapon attack, you can expend one superiority die to attempt to knock the target down. You add the superiority die to the attack’s damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you knock the target prone."
                }
            }
        },
        "4": {
            "name": "Fire as One",
            "levels": ["6th"],
            "details": "You can focus your target down with the help with an ally. Once per round, whenever the creature that is the target of your Critical Analysis feature is attacked by someone other than you, you can use your reaction to make one weapon attack against them."
        },
        "5": {
            "name": "Battlefield Survey",
            "levels": ["9th"],
            "details": "You become a master at leading your allies around in a battlefield you have studied. When you spend 10 minutes observing an area that is within 120 feet from you, or by using a detailed map, select a number of creatures up to your Critical Analysis modifier. You and those selected allies ignore unenhanced difficult terrain, and have advantage on Dexterity (Stealth) checks in that area."
        },
        "6": {
            "name": "All-Out Attack",
            "levels": ["17th"],
            "details": "You can use your action to initiate an all-out attack. Choose a number of allies up to your Critical Analysis modifier within 60 feet who can see or hear you. The chosen allies may then immediately use their reaction to make one weapon attack against a target of your choice. You may choose the target for each attack separately. Once you use this feature, you cannot use it again until you finish a short or long rest."
        },
        "7": {
            "name": "Tactician Discoveries",
            "details": "When you select this pursuit, you gain access to new discoveries which reflect your mastery in the field of combat. Whenever you learn a new discovery, you can choose from any of the following as well. The discoveries are listed in alphabetical order.",
            "discoveries": {
                "Commander's Armor": {
                    "prerequisite": "5th",
                    "details": "You gain proficiency in medium armor."
                },
                "Contingency Plan": {
                    "prerequisite": "9th",
                    "details": "When the target of your Critical Analysis feature scores a critical hit, you can use your reaction and expend a superiority die to treat the attack as a normal hit instead."
                },
                "Fighting Style": {
                    "details": "You adopt a particular style of fighting as your specialty. Choose one of the fighting style options"
                },
                "Firing Command": {
                    "details": "As a bonus action, you can take the Help action. Additionally, when you take the Help action, it has a range of 30 feet."
                },
                "Observant Leader": {
                    "details": "You have advantage Wisdom (Perception) checks that rely on sight."
                },
                "Studied Commander": {
                    "details": "When you make an Intelligence (Lore) or Intelligence (Technology) check related to battles, tactics, or weaponry, you may expend a superiority die and add it to the roll."
                },
                "Tactical Retreat": {
                    "details": "When you take the Dash action, opportunity attacks made against you are made at disadvantage."
                },
                "Unbound Commander": {
                    "prerequisite": "12th",
                    "details": "You learn to command your allies to victory from afar. Your Critical Analysis range is increased to 120 feet"
                },
            }
        },
    },
    class_id = 8
)
bulwark_technique = Archetype(
    name = "Bulwark Technique",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Bonus Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in heavy armor."
        },
        "2": {
            "name": "Personal Barrier",
            "levels": ["3rd"],
            "details": "You gain access to a powerful personal barrier. Whenever you complete a short or long rest, you create a barrier on yourself that lasts until you finish a short or long rest. That barrier has hit points equal to twice your scout level + your Intelligence modifier. Your barrier can never have hit points greater than twice your scout level + your Intelligence modifier. Whenever you take damage, the barrier takes the damage instead. If this damage reduces the barrier to 0 hit points, you take any remaining damage. While the barrier has 0 hit points, it can’t absorb damage, but its power remains. Whenever you cast a tech power of 1st level or higher, your barrier regains hit points equal to the number of tech points spent. Additionally, for as long as your barrier has hit points, you gain the following benefits: You are considered proficient in Constitution saving throws for the purpose of maintaining concentration on tech powers. Hostile creatures that hit you with melee attacks take energy damage equal to your Intelligence modifier (minimum of 1)"
        },  
        "3": {
            "name": "Mark of the Bulwark",
            "levels": ["3rd"],
            "details": "When the target of your Ranger’s Quarry feature makes a melee attack against a friendly creature within 5 feet of you, you can use your reaction to force the attack to target you instead. If the attack hits, and your Personal Barrier has hit points, the attacking creature takes bonus damage equal to your Ranger’s Quarry Damage Die."
        },
        "4": {
            "name": "Projected Barrier",
            "levels": ["7th", "11th", "17th"],
            "details": "You’ve learned how to manipulate your barrier to create new effects. As an action, you can spend three of your barrier’s hit points to create a unique effect. You have three such effects: Projected Sphere, Projected Maelstrom, and Projected Wave. When you use your Projected Barrier, you choose which effect to create. Some Projected Barrier Effects require saving throws. When you use such an effect from this class, the DC equals your tech save DC. If your barrier’s hit points are reduced to 0, any Projected Barrier features immediately end. Projected Sphere: You create a protective spherical barrier in a 5-foot-radius sphere a point you can see within 30 feet that lasts until the start of your next turn. Creatures within the barrier have three-quarters cover from attacks originating from outside the barrier. You can maintain the barrier by spending an additional barrier hit point at the start of each of your turns (no action required). Projected Maelstorm: You create an unstable energy maelstrom in a 5-foot cube at a point you can see within 30 feet that lasts until the start of your next turn. A creature takes 4d4 energy damage when it enters the area for the first time on a turn or starts its turn there. You can maintain the barrier by spending an additional barrier hit point at the start of each of your turns (no action required). This feature’s damage increases by 1d4 when you reach 11th level (5d4) and 17th level (6d4). Projected Wave: You create a wave of barrier energy in a 15-foot cone. Each creature within the cone must make a Dexterity saving throw. On a failed save, a creature takes 2d6 energy damage and is pushed back to the edge of the cone. On a success, they take half damage and aren’t pushed. This feature’s damage increases by 1d6 when you reach 11th level (3d6) and 17th level (4d6)."
        },
        "5": {
            "name": "Regenerative Shielding",
            "levels": ["11th"],
            "details": "When a hostile creature forces you to make a saving throw and you succeed, your personal barrier regains hit points equal to your Intelligence modifier."
        },
        "6": {
            "name": "Adaptive Barrier",
            "levels": ["15th"],
            "details": "When your personal barrier takes damage, you can have it gain resistance to subsequent damage of that type until the start of your next turn (no action required). If it takes damage of more than one type simultaneously, you can choose which type it gains resistance to. Your barrier can only have resistance to one type of damage at a time."
        }
    },
    class_id = 9
)
hunter_technique = Archetype(
    name = "Hunter Technique",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Hunter's Prey",
            "levels": ["3rd"],
            "details": "You gain one of the following features of your choice. Colossus Slayer: Your tenacity can wear down the most potent foes. When you hit a creature with a weapon attack, the creature takes an extra 1d8 damage if it’s below its hit point maximum. You can deal this extra damage only once per turn, and this damage is the same type as the weapon’s damage. Giant Killer: When a Large or larger creature within 5 feet of you hits or misses you with an attack, you can use your reaction to attack that creature immediately after its attack, provided that you can see the creature. Horde Breaker: Once on each of your turns when you make a weapon attack, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target and within range of your weapon, no action required."
        },
        "2": {
            "name": "Mark of the Hunter",
            "levels": ["3rd"],
            "details": "When you use your Ranger’s Quarry feature, the first time you make a tech or weapon attack against the target of your Ranger’s Quarry each turn, roll your Ranger’s Quarry die and add it to the roll."
        },  
        "3": {
            "name": "Defensive Tactics",
            "levels": ["7th"],
            "details": "You gain one of the following features of your choice. Escape the Horde: Opportunity attacks against you are made with disadvantage. Multiattack Defense: When a creature hits you with an attack, you gain a +4 bonus to AC against all subsequent attacks made by that creature for the rest of the turn. Steel Will: You have advantage on saving throws against being frightened."
        },
        "4": {
            "name": "Multiattack",
            "levels": ["11th"],
            "details": "You gain one of the following features of your choice. Volley: You can use your action to make a ranged attack against any number of creatures within 10 feet of a point you can see within your weapon’s range. You must have ammunition for each target, as normal, and you make a separate attack roll for each target. Whirlwind Attack: You can use your action to make melee attacks against any number of creatures within 5 feet of you, with a separate attack roll for each target."
        },
        "5": {
            "name": "Superior Hunter's Defense",
            "levels": ["15th"],
            "details": "You gain one of the following features of your choice. Evasion: When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on a saving throw, and only half damage if you fail. Stand Against the Tide: When a hostile creature misses you with a melee attack, you can use your reaction to force that creature to repeat the same attack against another creature (other than itself) of your choice. Uncanny Dodge: When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack’s damage against you."
        }
    },
    class_id = 9
)
slayer_technique = Archetype(
    name = "Slayer's Technique",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Bonus Proficiencies",
            "levels": ["3rd"],
            "details": "You gain proficiency in heavy armor."
        }, 
        "2": {
            "name": "Slayer's Pride",
            "levels": ["3rd"],
            "details": "You have advantage on saving throws against being frightened."
        },  
        "3": {
            "name": "Mark of the Slayer",
            "levels": ["3rd"],
            "details": "You immediately learn if the target of your Ranger’s Quarry feature has any damage immunities, resistances, or vulnerabilities and what they are. Additionally, the first time you hit the target of your Ranger’s Quarry feature with a weapon attack each turn, it takes extra damage equal to your Ranger’s Quarry Damage Die. The damage is of the same type as the weapon’s damage."
        }, 
        "4": {
            "name": "Supernatural Defense",
            "levels": ["7th"],
            "details": "Whenever the target of your Ranger’s Quarry forces you to make a saving throw, or whenever you make an ability check to escape that targets grapple, you can use your reaction and roll your Ranger’s Quarry Damage Die, adding it to the roll."
        }, 
        "5": {
            "name": "Nemesis",
            "levels": ["11th"],
            "details": "When you score a critical hit or reduce a creature to 0 hit points on your turn, you can use your bonus action to force one creature of your choice that you can see within 30 feet of you to make a Wisdom saving throw against your tech save DC. On a failed save, a creature becomes frightened of you for 1 minute. At the end of each of the creature’s turns it repeats this saving throw, ending the effect on a success."
        }, 
        "6": {
            "name": "Slayer's Counter",
            "levels": ["15th"],
            "details": "If the target of your Ranger’s Quarry feature forces you to make a saving throw, you can use your reaction to make one weapon attack against it. You make this attack immediately before making the saving throw. If your attack hits, you automatically succeed on the saving throw, in addition to the attack’s normal effects."
        }
    },
    class_id = 9
)
stalker_technique = Archetype(
    name = "Stalker Technique",
    caster_type = "Tech",
    features = {
        "1": {
            "name": "Accomplished Ambusher",
            "levels": ["3rd"],
            "details": "When you take the Attack action against a creature that is surprised, you can make one additional attack against that creature as a part of that action."
        },
        "2": {
            "name": "Mark of the Stalker",
            "levels": ["3rd"],
            "details": "While you are hidden from the target of your Ranger’s Quarry feature, the first attack roll you make each round against that creature does not automatically reveal your presence to that creature. Make a Dexterity (Stealth) check contested by your target’s Wisdom (Perception) check. On a success, you remain hidden. If you are less than 30 feet from your target, the Dexterity (Stealth) check is made with disadvantage."
        },   
        "3": {
            "name": "Concealment",
            "levels": ["7th"],
            "details": "You’ve become adept at evading creatures that rely on darkvision. While in darkness, you are invisible to any creature that relies on darkvision to see you in that darkness. Additionally, when you hit a creature with a ranged weapon attack while hidden, you can force that creature to make a Dexterity saving throw against your tech save DC. On a failed save, the creature’s speed is reduced to 0 until the end of your next turn. You can use this feature a number of times equal to your Intelligence modifier (minimum of one). You regain all expended uses when you finish a short or long rest."
        }, 
        "4": {
            "name": "Stalker's Fury",
            "levels": ["11th"],
            "details": "If you have advantage on a weapon attack against a target on your turn, you can forgo that advantage to immediately make an additional weapon attack against the same target as a bonus action."
        }, 
        "5": {
            "name": "Stalker's Dodge",
            "levels": ["15th"],
            "details": "Whenever a creature attacks you and does not have advantage, you can use your reaction to impose disadvantage on the creature’s attack roll against you. You can use this feature before or after the attack roll is made, but it must be used before the outcome of the roll is determined."
        }
    },
    class_id = 9
)
path_of_aggression = Archetype(
    name = "Path of Aggression",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Voltaic Slash",
            "levels": ["3rd"],
            "details": "Starting when you choose this calling at 3rd level, you learn the lightning charge force power, which does not count against your total powers known. Additionally, you can use Wisdom or Charisma as your forcecasting ability for it, and you can use all three Force-Empowered Self options when you cast it as your action and hit the target. Finally, when you deal lightning damage with the lightning charge force power, you deal additional lightning damage equal to half your Wisdom or Charisma modifier (your choice, minimum of one) if it doesn’t already include that modifier."
        },
        "2": {
            "name": "Thunderous Momentum",
            "levels": ["3rd"],
            "details": "Your stride becomes nigh unbreakable. You are immune to the shocked condition, and each slowed level only reduces your speed by 5 feet, unless it would reduce your speed to 0."
        },  
        "3": {
            "name": "Entropic Rush",
            "levels": ["7th"],
            "details": "You’ve learned to move with speed and precision, discharging your lightning in a massive burst. When you move at least half your speed before casting lightning charge, you make the attack roll with advantage. Additionally, on a hit, the lightning can leap a second time, to a third creature within range or back to the first creature."
        },
        "4": {
            "name": "Living Current",
            "levels": ["13th"],
            "details": "You’ve learned to channel the damage done to you to enhance your strikes. The first time you deal damage on your turn, if you took damage since the start of your last turn, you can deal additional lightning damage equal to your Kinetic Combat die + half the amount of damage taken (rounded down). You can use this feature a number of times equal to your Wisdom or Charisma modifier (your choice, a minimum of once). You regain all expended uses when you finish a short or long rest."
        },
        "5": {
            "name": "Retaliatory Strike",
            "levels": ["18th"],
            "details": "When a creature hits you with an attack while within 5 feet of you, you can use your reaction to cast the lightning charge force power, targeting them."
        }
    },
    class_id = 10
)
path_of_focus = Archetype(
    name = "Path of Focus",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Focused Burst",
            "levels": ["3rd"],
            "details": "You learn the burst force power, which does not count against your total powers known. Additionally, you can use all three Force-Empowered Self options when you cast it as your action. If more than one creature would be affected, and you use your Double Strike feature, only one creature takes the additional damage. Finally, you add your Wisdom or Charisma modifier (your choice, minimum of +1) to damage rolls with it, and creatures that succeed on their saving throw take half damage, instead of none."
        },
        "2": {
            "name": "Blade Dance",
            "levels": ["3rd"],
            "details": "When you deal damage to a creature within 5 feet of you, you can move up to 10 feet without provoking opportunity attacks."
        },    
        "3": {
            "name": "Blade Storm",
            "levels": ["7th"],
            "details": "Your bursts become even more overwhelming. Once on your turn, when a creature takes damage from you twice, you can immediately make one additional attack against that creature (no action required). This attack uses your Kinetic Combat die instead of the weapon’s damage die."
        },  
        "4": {
            "name": "Focused Flow",
            "levels": ["13th"],
            "details": "Whenever you use a Force-Empowered Self feature, you may instead expend no force points and roll a d4 in place of your Kinetic Combat die."
        },  
        "5": {
            "name": "Master Strike",
            "levels": ["18th"],
            "details": "At 18th level, your bursts can overpower even the fiercest of foes. Once on your turn, when a creature takes damage from you three times, you can force it to make a Constitution saving throw against your universal force save DC. On a failed save, it becomes stunned until the end of its next turn."
        }
    },
    class_id = 10
)
path_of_shadows = Archetype(
    name = "Path of Shadow",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Dead Silence",
            "levels": ["3rd"],
            "details": "You learn the psychic charge force power, which does not count against your total powers known. Additionally, you can use Wisdom or Charisma as your forcecasting ability for it, and you can use all three Force-Empowered Self options when you cast it as your action and hit the target. Finally, when you hit a creature with the psychic charge force power and the target tries to speak, it takes additional damage equal to your Wisdom or Charisma modifier (your choice, minimum of +1), and its voice does not produce sound until the end of your next turn."
        },
        "2": {
            "name": "Cloak of Shadows",
            "levels": ["3rd"],
            "details": "You can take the Hide action as a bonus action on your turn. Additionally, you can try to hide when you are lightly obscured from the creature from which you are hiding."
        },
        "3": {
            "name": "Shadow Strike",
            "levels": ["7th"],
            "details": "You learn to strike from the shadows. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the roll."
        },
        "4": {
            "name": "Shadow Step",
            "levels": ["13th"],
            "details": "You gain the ability to step from one shadow into another. While you are in dim light or darkness, as a bonus action you can teleport up to 60 feet to an unoccupied space you can see that is also in dim light or darkness. You then have advantage on the first melee attack you make before the end of the turn."
        },
        "5": {
            "name": "Shadow's Wrath",
            "levels": ["18th"],
            "details": "Your training has taught you advanced techniques while you maneuver in the shadows. While you are hidden from your target, the first attack roll you make each round does not automatically reveal your presence. Make a Dexterity (Stealth) check against your target’s Wisdom (Perception) check. On a success, you remain hidden. If you are also invisible, you remain invisible."
        }  
    },
    class_id = 10
)
path_of_the_forceblade = Archetype(
    name = "Path of the Forceblade",
    caster_type = "Force",
    features = {
        "1": {
            "name": "Phasethrow",
            "levels": ["3rd"],
            "details": "You learn the saber throw force power, which does not count against your total powers known. Additionally, you no longer have disadvantage on the attack roll with it if you are within 5 feet of a hostile creature, and you can use all three Force-Empowered Self options when you cast it as your action and hit a target. Finally, when you hit a creature within with the saber throw force power, you deal additional damage equal to half your Wisdom or Charisma modifier (your choice, rounded up, minimum of +1) if it doesn’t already include that modifier."
        },
        "2": {
            "name": "Forceblade Bond",
            "levels": ["3rd"],
            "details": "You learn how to bond with a light- or vibro-weapon through the Force, making it part of you. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond, gaining the following benefits: You can’t be disarmed of that weapon while you are conscious. If the weapon is within 60 feet of you and you can see it, you can summon that weapon as a bonus action on your turn, causing it to travel instantly to you. If you have a free hand, you catch the weapon. Otherwise, it lands at your feet. You can use Wisdom or Charisma instead of Strength or Dexterity for the attack and damage rolls. You can have two weapons bonded to you in this way at a time, and you can summon both of them to you with the same bonus action."
        },  
        "3": {
            "name": "Twin Saber Throw",
            "levels": ["7th"],
            "details": "When you cast saber throw while wielding your forceblade, you can attack the same target multiple times. Additionally, when you deal damage to a creature within 30 feet of you with your forceblade, you can use your bonus action to teleport to within 5 feet of that creature and make a melee weapon attack against that creature. This attack uses your Kinetic Combat die instead of your weapon’s damage die. You can use this feature a number of times equal to your Wisdom or Charisma modifier (a minimum of once). You regain all expended uses when you complete a long rest."
        },  
        "4": {
            "name": "Disruptive Throw",
            "levels": ["13th"],
            "details": "When you are the target of a ranged attack, and the source is within range of your saber throw force power, you can use your reaction to throw your forceblade at the source of the attack. Make a ranged force attack. On a hit, this attack deals damage using your Kinetic Combat die instead of the weapon’s damage die and you impose disadvantage on the triggering attack roll."
        },  
        "5": {
            "name": "Forceblade Mastery",
            "levels": ["18th"],
            "details": "You’ve mastered controlling your forceblade with your mind, using it to keep your enemies at bay. As an action, you can telekinetically control your forceblade and have it strike any number of creatures within 10 feet of you, spending 1 force point per target. Each target must make a Dexterity saving throw (DC = 8 + your bonus to weapon attack rolls with that weapon). On a failed save, it takes damage using your Kinetic Combat die + half your sentinel level (rounded down), is pushed back 10 feet and knocked prone."
        }  
    },
    class_id = 10
)

db.session.add_all([ballistic_approach, marauder_approach, precision_approach, warchief_approach, way_of_balance, way_of_lightning, way_of_suggestion, way_of_the_sage, armormech_engineering, armstech_engineering, gadgeteer_engineering, unstable_engineering, assault_specialist, heavy_weapons_specialist, shield_specialist, tactical_specialist, makashi_form, niman_form, shien_djem_so_form, soresu_form, crimson_order, echani_order, matukai_order, nightsister_order, acquisitions_practice, beguiler_practice, gunslinger_practice, sharpshooter_practice, doctor_pursuit, gambler_pursuit, politician_pursuit, tactician_pursuit, bulwark_technique, hunter_technique, slayer_technique, stalker_technique, path_of_aggression, path_of_focus, path_of_shadows, path_of_the_forceblade])
db.session.commit()
#--------------------------------------------------------------

#--------------------Fighting Styles---------------------------
akimbo = FightingStyles(
    name = "Akimbo Style",
    description = "You are skilled at fighting with two blasters. While you are wielding separate weapons in each hand with which you are proficient, you gain the following benefits: When you engage in Two-Weapon Fighting, you can add your ability modifier to the damage roll of your Two-Weapon Fighting attack as long as it doesn’t already include that modifier. Reloading a weapon no longer requires a free hand."
)
berserker_style = FightingStyles(
    name = "Berserker Style",
    description = "You are skilled at returning pain to those who deliver it. You gain the following benefits: When you hit with a melee weapon attack using Strength, you deal additional damage equal to your Strength modifier if that creature dealt damage to you since the start of your last turn. When you choose to let an attack that would miss you hit you instead, the creature rolls the damage as normal instead of choosing the maximum."
)
brawler = FightingStyles(
    name = "Brawler Style",
    description = "You are skilled at using your weight to your advantage. You gain the following benefits: You are proficient with improvised weapons. Your damage die for your unarmed strikes and natural weapons increases by one step (from 1 to d4, d4 to d6, or d6 to d8). When you take the Attack action and attempt to grapple, shove, or trip a creature, or make an attack against a creature with an unarmed strike or a weapon wielded in one hand on your turn, you can use your bonus action to make an unarmed strike, grapple, shove, or trip against the same creature."
)
covert = FightingStyles(
    name = "Covert Style",
    description = "You are skilled at fighting from unseen angles. You gain the following benefits: You can take the Hide action as a bonus action. If you could already take the Hide action as a bonus action, you can instead take it as a reaction on your turn. Creatures you’ve dealt damage to since the start of your last turn have disadvantage on Wisdom (Perception) checks made to find you."
)
defense = FightingStyles(
    name = "Defense Style",
    description = "You are skilled at the art of defending yourself. While you are wearing medium or heavy armor with which you are proficient, you gain the following benefits: You can use your bonus action to mark a target within 30 feet that you can see until the end of your next turn. When you do so, damage dealt to you by the target is reduced by an amount equal to half your Strength or Constitution modifier (your choice, rounded up, minimum of 1) while marked. You can only have one creature marked in this way at a time. You have advantage on Strength checks and Strength saving throws to avoid being moved."
)
disruption = FightingStyles(
    name = "Disruption Style",
    description = "Choose one from force- or tech-casting. You are skilled at fighting and interfering with casters of the chosen type. You gain the following benefits: When you force a creature to make a Constitution saving throw to maintain concentration on your turn, and they succeed on the save, you can use your bonus action to force them to reroll the save. They must use the new roll. Once per round, when a hostile creature attempts to cast a power while within 5 feet of you, they must first make a Constitution saving throw as if to maintain concentration (DC = 10 + the power’s level). On a failure, the power isn’t cast and any points are wasted."
)
dual_wield = FightingStyles(
    name = "Dual Wield Style",
    description = "You are skilled at fighting with two weapons. While you are wielding separate weapons in each hand with which you are proficient, you gain the following benefits: When you engage in Two-Weapon Fighting, you can add your ability modifier to the damage roll of your Two-Weapon Fighting attack as long as it doesn’t already include that modifier. When you make an opportunity attack, you can attack with both of your weapons."
)

db.session.add_all([akimbo, berserker_style, brawler, covert, defense, disruption, dual_wield])
db.session.commit()
#--------------------------------------------------------------

#--------------------Fighting Masteries------------------------
akimbo_mastery = FightingMastery(
    name = "Akimbo Mastery",
    description = "You’ve mastered fighting with two blasters, unleashing a volley of shots. While you are wielding separate weapons in each hand with which you are proficient, you gain the following benefits: When you roll the maximum on a weapon damage die against a creature, that creature suffers a -1 penalty on the first attack roll it makes before the start of your next turn. You can engage in Two-Weapon Fighting even when the weapons you are wielding lack the light property. You can reload two weapons when you would normally only be able to reload one. When you take the Attack action, you can choose to attack swiftly at the expense of accuracy. Your weapon attack is made without the aid of your proficiency bonus, but you can use your reaction to attack with a different weapon that you’re holding in the other hand, also without your proficiency bonus. If you would make more than one attack when you take the Attack action, only one attack is made without your proficiency bonus."
)
berserker_mastery = FightingMastery(
    name = "Berserker Mastery",
    description = "You’ve mastered returning pain to those who deliver it, becoming a scourge on the battlefield. You gain the following benefits: When a creature within 5 feet of you deals damage to you with a weapon or unarmed strike, you can use your reaction to make a melee weapon attack or unarmed strike against that creature. On a hit, you deal additional damage equal to your proficiency bonus. When a creature scores a critical hit against you, you have advantage on the first attack you make against that creature before the end of your next turn. If you would already have advantage, you can instead reroll one of the dice once. You have advantage on saving throws that would force you to act against your will, be frightened, or prevent you from attacking a creature."
)
brawler_mastery = FightingMastery(
    name = "Brawler Mastery",
    description = "You’ve mastered using your weight to your advantage, easily wrangling targets around. You gain the following benefits: Your improvised weapons use a d6 for damage and gain the versatile (2d4) property. Your damage die for your unarmed strikes and natural weapons increases by one step (from 1 to d4, d4 to d6, or d6 to d8). Your speed isn’t halved by carrying a grappled creature who is the same size category as you or smaller. Once on each of your turns, when you hit a creature with an unarmed strike or a weapon wielded in one hand on your turn, you can make an additional unarmed strike against the same target without the aid of your proficiency bonus (no action required)."
)
covert_mastery = FightingMastery(
    name = "Covert Mastery",
    description = "You’ve mastered fighting from unseen angles, gaining an advantage over your foes. You gain the following benefits: You can try to hide when you are lightly obscured from the creature from which you are hiding. Dim light doesn’t impose disadvantage on your Wisdom (Perception) checks that rely on sight. When you are hidden from a creature and miss it with an unarmed strike or weapon attack, making the attack doesn’t automatically reveal your position. Once per turn, when you deal damage to a creature with an unarmed strike or weapon attack while hidden from it, you deal additional damage equal to your proficiency bonus."
)

db.session.add_all([akimbo_mastery, berserker_mastery, brawler_mastery, covert_mastery])
db.session.commit()
#--------------------------------------------------------------

#-------------------Lightsaber Forms---------------------------
aqinos = LightsaberForms(
    name = "Aqinos Form",
    prerequisite = "The ability to cast tech powers",
    description = "As a part of the bonus action to adopt this form, if you cast a tech power of 1st level or higher, but no higher than half your Max Power Level (rounded up), as your action you can make one melee weapon attack."
)
ataru = LightsaberForms(
    name = "Ataru Form",
    description = "As a part of the bonus action to adopt this form, you can leap up to 15 feet to an unoccupied space you can see."
)
bakuuni_hand = LightsaberForms(
    name = "Bakuuni Hand Form",
    description = "As a part of the bonus action to adopt this form, if you took the Attack action and would be able to use your bonus action to make an unarmed strike, you can do so as a part of this bonus action. Until the start of your next turn, when a creature enters your reach or moves while within your reach, you can use your reaction to attempt to shove the creature. On a success, you shove the target 10 feet away from you, instead of only 5."
)
djem_so = LightsaberForms(
    name = "Djem So Form",
    description = "Before the end of your next turn, you can add half your Wisdom or Charisma modifier (your choice, rounded down, minimum of +1) to one ability check or attack roll you make using Strength."
)

db.session.add_all([aqinos, ataru, bakuuni_hand, djem_so])
db.session.commit()
#--------------------------------------------------------------

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
#? 2nd level
acid_dart = TechPowers(
    name = "Acid Dart",
    level = 2,
    casting_period = "1 action",
    range = "90 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "A shimmering green dart streaks toward a target within range and bursts in a spray of acid. Make a ranged tech attack against the target. On a hit, the target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its next turn. On a miss, the dart splashes the target with acid for half as much of the initial damage and no damage at the end of its next turn. Overcharge Tech. When you cast this power using a tech slot of 3rd level or higher, the damage (both initial and later) increases by 1d4 for each slot level above 2nd."
)
#? 3rd level
autonomous_servant = TechPowers(
    name = "Autonomous Servant",
    level = 3,
    casting_period = "1 minute",
    range = "Touch",
    duration = "Or until the end of your next short or long rest; whichever happens first",
    concentration = "-",
    description = "You touch one Tiny, unenhanced object that isn’t attached to another object or a surface and isn’t being carried by another creature. The target animates and gains little arms and legs, becoming a creature under your control until the power ends or the creature drops to 0 hit points. See the stat block for its statistics. As a bonus action, you can nonverbally command the creature if it is within 120 feet of you. (If you control multiple creatures with this power, you can command any or all of them at the same time, issuing the same command to each one.) You decide what action the creature will take and where it will move during its next turn, or you can issue a simple, general command, such as to fetch a code cylinder, stand watch, or stack some small objects. If you issue no commands, the servant does nothing other than defend itself against hostile creatures. Once given an order, the servant continues to follow that order until its task is complete. When the creature drops to 0 hit points, it reverts to its original form, and any remaining damage carries over to that form. The creature is considered a valid target for the tracker droid interface power. Overcharge Tech. When you cast this power using a tech slot of 4th level or higher, you can animate two additional objects for each slot level above 3rd."
)
#? 4th level
ballistic_shield = TechPowers(
    name = "Ballistic Shield",
    level = 4,
    casting_period = "1 action",
    range = "Self",
    duration = "Up to 1 hour",
    concentration = "Cencentration",
    description = "A flickering blue shield surrounds your body. Until the power ends, you have resistance to kinetic, energy, and ion damage."
)
#? 5th level
cryogenic_spray = TechPowers(
    name = "Cryogenic Spray",
    level = 5,
    casting_period = "1 action",
    range = "Self",
    duration = "Instantaneous",
    concentration = "-",
    description = "A blast of cold air erupts from you. Each creature in a 60-foot cone must make a Constitution saving throw. On a failed save, a creature takes 8d8 cold damage, and gains 1 slowed level until the start of your next turn. On a successful save, a creature takes half as much damage and isn’t slowed. A creature killed by this power becomes frozen in carbonite. Overcharge Tech. When you cast this power using a tech slot of 6th level or higher, the damage increases by 1d8 for each slot level above 5th."
)
#? 6th level
carbon_fog = TechPowers(
    name = "Carbon Fog",
    level = 6,
    casting_period = "1 action",
    range = "120 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    description = "You create a cloud of icy fog in a 20-foot-radius sphere centered on a point you can see. The sphere extends around corners, and its area is heavily obscured. The fog is semi-solid, and its area is considered difficult terrain. Each creature that enters the power’s area for the first time on a turn or starts its turn there takes 4d6 cold damage and gains 1 slowed level until the end of its turn. The fog lasts for the duration of the power or until it’s dispersed by a wind of moderate or greater speed (at least 10 mph)."
)
#? 7th level
cage = TechPowers(
    name = "Cage",
    level = 7,
    casting_period = "1 action",
    range = "100 feet",
    duration = "1 hour",
    concentration = "-",
    description = "An immobile, invisible, cube-shaped prison composed of energy springs into existence around an area you choose within range. The prison can be a cage or a solid box as you choose. A prison in the shape of a cage can be up to 20 feet on a side and is made from 1/2-inch diameter bars spaced 1/2 inch apart. A prison in the shape of a box can be up to 10 feet on a side, creating a solid barrier that prevents any matter from passing through it and blocking any powers cast into or out of the area. When you cast the power, any creature that is completely inside the cage’s area is trapped. Creatures only partially within the area, or those too large to fit inside the area, are pushed away from the center of the area until they are completely outside the area. A creature inside the cage can’t leave it by unenhanced means. If the creature tries to teleport to leave the cage, it must first make a Charisma saving throw. On a success, the creature can use that power to exit the cage. On a failure, the creature can’t exit the cage and wastes the use of the power or effect."
)
#? 8th level
stun_dart = TechPowers(
    name = "Stun Dart",
    level = 8,
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    description = "You emit a tiny crippling dart at a target within range. If the target has 150 hit points or fewer, it is stunned. Otherwise, the power has no effect. The stunned target must make a Constitution saving throw at the end of each of its turns. On a successful save, this stunning effect ends."
)
#? 9th level
carbonite_explosion = TechPowers(
    name = "Carbonite Explosion",
    level = 9,
    casting_period = "1 action",
    range = "250 feet",
    duration = "Instaneous",
    concentration = "-",
    description = "You generate an explosion of cryogenic energy in a 60-foot-radius sphere centered on a point you can see within range. Each creature in the affected area must make a Constitution saving throw. On a failed save, the creature takes 8d6 + 20 cold damage and is restrained for 1 minute as it is encased in carbonite. On a successful save, the creature takes half damage and is restrained until the end of its next turn. As an action, a restrained creature can make a Strength check against your tech save DC, ending this effect on itself on a success. A creature reduced to 0 hit points by this power dies instantly, as its body shatters into frozen chunks."
)

db.session.add_all([acid_splash, absorb_energy, acid_dart, autonomous_servant, ballistic_shield, cryogenic_spray, carbon_fog, cage, stun_dart, carbonite_explosion])
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
#? 2nd level
affliction = ForcePowers(
    name = "Affliction", 
    level = 2,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "30 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "Slow",
    description = "Choose a creature that you can see within range. That creature must make a Constitution saving throw. On a failed save, the target gains 1 slowed level, it takes a -2 penalty to AC and Dexterity saving throws, and it can’t use reactions. On its turn, it can use either an action or a bonus action, not both. Regardless of the creature’s abilities or items, it can’t make more than one melee or ranged attack during its turn. If the creature attempts to cast a power with a casting time of 1 action, roll a d20. On an 11 or higher, the power doesn’t take effect until the creature’s next turn, and the creature must use its action on that turn to complete the power. If it can’t, the power is wasted. The creatures makes another Constitution saving throw at the end of its turn. On a successful save, the effect ends."
)
#? 3rd level
aura_of_vigor_power = ForcePowers(
    name = "Aura of Vigor", 
    level = 3,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Self (30-foot radius)",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "Valor",
    description = "Envigorating energy radiates from you in a 30-foot radius. Until the power ends, the aura moves with you, centered on you. Each nonhostile creature in the aura (including you) deals an extra 1d4 damage with weapon attacks."
)
#? 4th level
arua_of_purity = ForcePowers(
    name = "Aura of Purity", 
    level = 4,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "Self (30-foot radius)",
    duration = "Up to 10 minutes",
    concentration = "Concentration",
    prerequisite = "Restoration",
    description = "Purifying energy radiates from you in a 30-foot radius. Until the power ends, the aura moves with you, centered on you. Each nonhostile creature in the aura (including you) can’t become diseased, has resistance to poison damage, and has advantage on saving throws against effects that cause any of the following conditions: blinded, charmed, deafened, frightened, paralyzed, poisoned, and stunned."
)
#? 5th level
control_pain = ForcePowers(
    name = "Control Pain", 
    level = 5,
    force_alignment = "Universal",
    casting_period = "1 action",
    range = "Self",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "Force Body",
    description = "You use the Force to push your body beyond its normal limits. You can’t die from damage or from failed death saving throws while this power is in effect, but the effort taxes you. If you have 0 hit points while you are under the effect of this power, you do not fall unconscious, and continue acting and fighting normally. While you remain at 0 hit points, you must make a death saving throw at the start of each of your turns. Each time you fail a death saving throw, you suffer a cumulative -1 penalty to attack rolls, ability checks, and saving throws (including death saving throws). This penalty lasts until you regain hit points. Successful death saving throws have no effect, but a natural 20 restores 1 hit point as usual. If you have 0 hit points when this power ends, you die instantly."
)
#? 6th level
crush = ForcePowers(
    name = "Crush", 
    level = 6,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "60 feet",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "Choke",
    description = "You make a crushing gesture at a creature within range. The target must make a Constitution saving throw. On a failed save target takes 10d8 force damage and is paralyzed until the end of your next turn. On a successful save, the target takes half as much damage and is not paralyzed. You can use a bonus action while the target is paralyzed to move the target up to 10 feet in any direction. Force Potency. When you cast this power using a force slot of 7th level or higher, the damage increases by 1d8 for each slot level above 6th."
)
#? 7th level
destroy_droid = ForcePowers(
    name = "Destroy Droid", 
    level = 7,
    force_alignment = "Light",
    casting_period = "1 action",
    range = "120 feet (30-foot cube)",
    duration = "Up tp 1 minute",
    concentration = "Concentration",
    prerequisite = "Disable Droid",
    description = "Choose a point that you can see within range. Each droid or construct must succeed on a Constitution saving throw or be paralyzed for the duration. At the beginning of each of its turns, an affected target takes energy damage equal to twice your forcecasting ability modifier and then repeats this saving throw. On a success, the power ends on the target."
)
#? 8th level
death_field = ForcePowers(
    name = "Death Field", 
    level = 8,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "90 feet (30-foot cube)",
    duration = "Instantaneous",
    concentration = "-",
    prerequisite = "Siphon Life",
    description = "You draw the life force from every creature in a 30-foot cube centered on a point you choose within range. Each creature in that area must make a Constitution saving throw. A creature takes 10d8 necrotic damage on a failed save, or half as much damage on a successful one. If you reduce a hostile creature to 0, you gain temporary hit points equal to half the damage dealt. This power has no effect on droids or constructs."
)
#? 9th level
force_storm = ForcePowers(
    name = "Force Storm", 
    level = 9,
    force_alignment = "Dark",
    casting_period = "1 action",
    range = "150 feet",
    duration = "Up to 1 minute",
    concentration = "Concentration",
    prerequisite = "Force Lightning Cone",
    description = "A crackling storm of lightning with a diameter of 60 feet and a height of 120 feet appears in a location you choose within range. Whenever a creature enters the storm or starts its turn there, it must make a Dexterity saving throw. On a failed save, it takes 30d6 lightning damage or half as much as a successful one. The power damages objects in the area and ignites flammable objects that aren’t being worn or carried."
)

db.session.add_all([affect_mind, armor_of_abeloth, aura_of_vigor_power, arua_of_purity, control_pain, crush, destroy_droid, death_field, force_storm])
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

#-----------------------Conditions-----------------------------
blinded = Condition(
    name = "",
    details = ""
)
#--------------------------------------------------------------
