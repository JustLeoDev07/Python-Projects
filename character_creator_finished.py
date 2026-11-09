import random
import math

def roll_dice(sides):
    return random.randint(1, sides)
#For a dice roll, use roll_dice(6) or whatever number you need, d6 = roll_dice(6)  etc etc


print('''
===============================
THE ADVENTURER'S GUILD 
=============================== 
''')
print('Welcome, Adventurer! Here you will start your quest into the many realms you may encounter, but my first question... is your name!')
character_name = input("Enter your character's name: ")
print(f"Nice to meet you, {character_name}!")
print("The next thing you need to do is tell me what race you are?")


racial_feature_descriptions = {
    "Darkvision": "You can see in dim light within 60 feet as though it were bright light, and in darkness as though it were dim light. You cannot distinguish colours in darkness.",

    "Fey Ancestry": "You have advantage on saving throws against being charmed, and magic cannot put you to sleep.",

    "Trance": "You meditate deeply for 4 hours instead of sleeping. You gain the same benefit that a human does from 8 hours of sleep.",

    "Keen Senses": "You have proficiency in the Perception skill.",

    "Dwarven Resilience": "You have advantage on saving throws against poison and resistance to poison damage.",

    "Dwarven Combat Training": "You have proficiency with battleaxes, handaxes, light hammers and warhammers.",

    "Tool Proficiency": "You gain proficiency with your chosen type of artisan's tools.",

    "Stonecunning": "When making a History check related to the origin of stonework, you are considered proficient and add double your proficiency bonus instead of your normal proficiency bonus.",

    "Dwarven Speed": "Your speed is not reduced by wearing heavy armour.",

    "Hellish Resistance": "You have resistance to fire damage.",

    "Infernal Legacy": "You gain racial spells as you increase in level, using Charisma as your spellcasting ability.",

    "Draconic Ancestry": "Your draconic ancestry determines the damage type associated with your breath weapon and damage resistance.",

    "Breath Weapon": "You can use your action to exhale destructive energy determined by your draconic ancestry.",

    "Damage Ressistance": "You have resistance to the damage type associated with your draconic ancestry."
}


class_feature_descriptions = {
    # FIGHTER
    "Fighting Style": "You specialise in a particular style of combat.",
    "Second Wind": "On your turn, you can use a bonus action to regain 1d10 + your Fighter level hit points. Recharges after a short or long rest.",
    "Action Surge": "On your turn, you can take one additional action. Recharges after a short or long rest.",
    "Action Surge (2 Uses)": "You can use Action Surge twice between rests, but only once on the same turn.",
    "Martial Archetype": "You gain features from your chosen Fighter subclass.",
    "Indomitable (1 Use)": "You can reroll a failed saving throw once per long rest. You must use the new result.",
    "Indomitable (2 Uses)": "You can reroll failed saving throws twice per long rest, using each new result.",
    "Indomitable (3 Uses)": "You can reroll failed saving throws three times per long rest, using each new result.",

    # WIZARD
    "Spellcasting": "You can cast spells using your class's spellcasting ability.",
    "Arcane Recovery": "Once per day, after a short rest, you can recover expended spell slots with a combined level up to half your Wizard level, rounded up. None can be level 6 or higher.",
    "Arcane Tradition": "You gain features from your chosen Wizard school of magic.",
    "Spell Mastery": "Choose a 1st-level and a 2nd-level Wizard spell from your spellbook. You can cast them at their lowest levels without spending spell slots when prepared.",
    "Signature Spells": "Choose two 3rd-level Wizard spells. They are always prepared, and you can cast each once at 3rd level without expending a spell slot per short or long rest.",

    # ROGUE
    "Expertise": "Your proficiency bonus is doubled for ability checks using your selected skill or tool proficiencies.",
    "Sneak Attack": "Once per turn, you can deal extra damage with a finesse or ranged weapon when you meet the Sneak Attack conditions.",
    "Thieves' Cant": "You know the secret language and signs used by thieves to communicate hidden messages.",
    "Cunning Action": "You can use a bonus action to Dash, Disengage or Hide.",
    "Roguish Archetype": "You gain features from your chosen Rogue subclass.",
    "Uncanny Dodge": "When an attacker you can see hits you, you can use your reaction to halve the attack's damage.",
    "Evasion": "When an effect allows a Dexterity saving throw for half damage, you take no damage on a success and half on a failure.",
    "Reliable Talent": "For ability checks that include your proficiency bonus, a d20 roll of 9 or lower counts as 10.",
    "Blindsense": "You know the location of hidden or invisible creatures within 10 feet of you, provided you can hear.",
    "Slippery Mind": "You gain proficiency in Wisdom saving throws.",
    "Elusive": "Attack rolls against you cannot have advantage while you are not incapacitated.",
    "Stroke of Luck": "Once per short or long rest, you can turn a missed attack into a hit or treat a failed ability check's d20 roll as 20.",

    # CLERIC
    "Divine Domain": "You gain features and additional spells from your chosen Cleric domain.",
    "Channel Divinity (1 Use)": "You can channel divine energy once between short or long rests.",
    "Channel Divinity (2 Uses)": "You can channel divine energy twice between short or long rests.",
    "Channel Divinity (3 Uses)": "You can channel divine energy three times between short or long rests.",
    "Turn Undead": "As an action, present your holy symbol to force nearby undead to make a Wisdom saving throw or become turned.",
    "Divine Intervention": "You can request assistance from your deity. Your chance of success is based on your Cleric level.",
    "Divine Intervention Improvement": "Your Divine Intervention succeeds automatically at level 20.",
    "Destroy Undead (CR 1/2)": "When an undead creature of challenge rating 1/2 or lower fails its saving throw against your Turn Undead feature, it is instantly destroyed.",
    "Destroy Undead (CR 1)": "When an undead creature of challenge rating 1 or lower fails its saving throw against your Turn Undead feature, it is instantly destroyed.",
    "Destroy Undead (CR 2)": "When an undead creature of challenge rating 2 or lower fails its saving throw against your Turn Undead feature, it is instantly destroyed.",
    "Destroy Undead (CR 3)": "When an undead creature of challenge rating 3 or lower fails its saving throw against your Turn Undead feature, it is instantly destroyed.",
    "Destroy Undead (CR 4)": "When an undead creature of challenge rating 4 or lower fails its saving throw against your Turn Undead feature, it is instantly destroyed.",

    # BARBARIAN
    "Rage": "You can enter a rage as a bonus action, gaining benefits to Strength checks, Strength saving throws, melee damage and damage resistance, subject to Rage restrictions.",
    "Unarmoured Defense": "While not wearing armour, your AC equals 10 + your Dexterity modifier + your Constitution modifier. You can still use a shield.",
    "Reckless Attack": "On your first attack of your turn, you can gain advantage on Strength-based melee weapon attacks, but attacks against you gain advantage until your next turn.",
    "Danger Sense": "You have advantage on Dexterity saving throws against effects you can see, provided you are not blinded, deafened or incapacitated.",
    "Primal Path": "You gain features from your chosen Barbarian subclass.",
    "Extra Attack": "You can attack twice when you take the Attack action.",
    "Fast Movement": "Your walking speed increases by 10 feet while you are not wearing heavy armour.",
    "Feral Instinct": "You have advantage on initiative rolls and can act normally when surprised if you enter a rage first.",
    "Relentless Rage": "While raging, you can attempt a Constitution saving throw to remain at 1 hit point when damage would reduce you to 0.",
    "Persistent Rage": "Your rage ends early only if you fall unconscious or choose to end it.",
    "Indomitable Might": "When a Strength check total is lower than your Strength score, you can use your Strength score instead.",
    "Primal Champion": "Your Strength and Constitution scores each increase by 4, and their maximums become 24.",
    "Brutal Critical (1 Die)": "You can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack.",
    "Brutal Critical (2 Dice)": "You can roll two additional weapon damage dice when determining the extra damage for a critical hit with a melee attack.",
    "Brutal Critical (3 Dice)": "You can roll three additional weapon damage dice when determining the extra damage for a critical hit with a melee attack.",

    #SHARED FEATURES
    "Ability Score Improvement": "You can increase your ability scores according to your class's Ability Score Improvement rules.",
    "Extra Attack (2 Attacks)": "You can attack twice when taking the Attack action.",
    "Extra Attack (3 Attacks)": "You can attack three times when taking the Attack action.",
    "Extra Attack (4 Attacks)": "You can attack four times when taking the Attack action.",
    "Martial Archetype Feature": "You gain an additional feature from your chosen Fighter subclass.",
    "Arcane Tradition Feature": "You gain an additional feature from your chosen Wizard subclass.",
    "Roguish Archetype Feature": "You gain an additional feature from your chosen Rogue subclass.",
    "Divine Domain Feature": "You gain an additional feature from your chosen Cleric domain.",
    "Primal Path Feature": "You gain an additional feature from your chosen Barbarian path."
}


subclass_feature_descriptions = {

    # FIGHTER - CHAMPION
    "Improved Critical": "Your weapon attacks score a critical hit on a roll of 19 or 20.",

    "Remarkable Athlete": "Add half your proficiency bonus, rounded up, to Strength, Dexterity and Constitution checks that do not already include your proficiency bonus. Your running long jump distance also increases.",

    "Additional Fighting Style": "You can choose an additional Fighting Style.",

    "Superior Critical": "Your weapon attacks score a critical hit on a roll of 18, 19 or 20.",

    "Survivor": "At the start of each turn, if you have no more than half your hit points remaining but at least 1 hit point, you regain 5 + your Constitution modifier hit points.",

    # FIGHTER - BATTLE MASTER
    "Combat Superiority": "You learn combat manoeuvres powered by superiority dice. These manoeuvres can enhance your attacks and combat abilities. Expended superiority dice return after a short or long rest.",

    "Student of War": "You gain proficiency with one type of artisan's tools.",

    "Know Your Enemy": "After observing or interacting with a creature outside combat for at least 1 minute, you can learn how certain characteristics compare to your own.",

    "Improved Combat Superiority (d10)": "Your superiority dice become d10s.",

    "Relentless": "When you roll initiative and have no superiority dice remaining, you regain one superiority die.",

    "Improved Combat Superiority (d12)": "Your superiority dice become d12s.",

    # FIGHTER - ELDRITCH KNIGHT
    # ROGUE - ARCANE TRICKSTER

    "Spellcasting": "You gain limited Wizard spellcasting using Intelligence. Your available cantrips, known spells and spell slots depend on your subclass and level.",

    "Weapon Bond": "You can magically bond with up to two weapons. A bonded weapon cannot normally be disarmed from you, and you can summon it to your hand as a bonus action while on the same plane.",

    "War Magic": "When you use your action to cast a cantrip, you can make one weapon attack as a bonus action.",

    "Eldritch Strike": "When you hit a creature with a weapon attack, it has disadvantage on its next saving throw against a spell you cast before the end of your next turn.",

    "Arcane Charge": "When you use Action Surge, you can teleport up to 30 feet to an unoccupied space you can see.",

    "Improved War Magic": "When you use your action to cast a spell, you can make one weapon attack as a bonus action.",

    # WIZARD - SCHOOL OF ABJURATION

    "Abjuration Savant": "The gold and time required to copy an abjuration spell into your spellbook are halved.",

    "Arcane Ward": "Casting an abjuration spell of level 1 or higher can create or restore a magical ward that absorbs damage for you.",

    "Projected Ward": "You can use your reaction to have your Arcane Ward absorb damage dealt to a creature within 30 feet.",

    "Improved Abjuration": "You add your proficiency bonus to ability checks made as part of casting an abjuration spell, such as Counterspell or Dispel Magic.",

    "Spell Resistance": "You have advantage on saving throws against spells and resistance to damage from spells.",

    # WIZARD - SCHOOL OF CONJURATION

    "Conjuration Savant": "The gold and time required to copy a conjuration spell into your spellbook are halved.",

    "Minor Conjuration": "You can use your action to conjure a small, nonmagical object into your hand or onto the ground nearby.",

    "Benign Transposition": "You can use your action to teleport up to 30 feet to a space you can see, or swap places with a willing creature.",

    "Focused Conjuration": "Taking damage cannot break your concentration on a conjuration spell.",

    "Durable Summons": "Creatures you summon or create with conjuration spells gain 30 temporary hit points.",


    # WIZARD - SCHOOL OF DIVINATION

    "Divination Savant": "The gold and time required to copy a divination spell into your spellbook are halved.",

    "Portent": "After a long rest, roll two d20s and record their results. You can replace certain attack rolls, saving throws or ability checks with these recorded rolls.",

    "Expert Divination": "When you cast a divination spell of level 2 or higher using a spell slot, you can regain an expended lower-level spell slot, up to level 5.",

    "The Third Eye": "You can use your action to gain a special sense, such as darkvision, seeing invisible creatures, reading languages or seeing into the Ethereal Plane.",

    "Greater Portent": "You roll three d20s for Portent instead of two.",


    # WIZARD - SCHOOL OF ENCHANTMENT

    "Enchantment Savant": "The gold and time required to copy an enchantment spell into your spellbook are halved.",

    "Hypnotic Gaze": "You can use your action to charm and incapacitate a creature within 5 feet if it fails a Wisdom saving throw, maintaining the effect with subsequent actions.",

    "Instinctive Charm": "When a nearby creature attacks you, you can use your reaction to try to redirect its attack to another creature.",

    "Split Enchantment": "When you cast an eligible enchantment spell targeting one creature, you can target a second creature.",

    "Alter Memories": "Creatures charmed by your enchantment spells can be made unaware of being charmed. You can also attempt to erase some memories of the time spent charmed.",

    # WIZARD - SCHOOL OF EVOCATION

    "Evocation Savant": "The gold and time required to copy an evocation spell into your spellbook are halved.",

    "Sculpt Spells": "When casting an evocation spell that affects other creatures you can see, you can protect selected creatures from the spell's harmful effects.",

    "Potent Cantrip": "Creatures that succeed on saving throws against your damaging cantrips still take half damage, but suffer no additional effects.",

    "Empowered Evocation": "You add your Intelligence modifier to one damage roll of a Wizard evocation spell you cast.",

    "Overchannel": "You can maximise the damage of a Wizard spell of levels 1 to 5 that deals damage. Repeated uses before a long rest cause necrotic damage to you.",


    # WIZARD - SCHOOL OF ILLUSION

    "Illusion Savant": "The gold and time required to copy an illusion spell into your spellbook are halved.",

    "Improved Minor Illusion": "You learn Minor Illusion if you do not already know it, and can create both sound and an image with a single casting.",

    "Malleable Illusions": "While an illusion spell you cast is active, you can use your action to change its nature within the spell's normal limits.",

    "Illusory Self": "When a creature attacks you, you can use your reaction to create an illusory duplicate that causes the attack to miss. Recharges after a short or long rest.",

    "Illusory Reality": "You can temporarily make one nonmagical, inanimate object from an illusion spell real. It cannot directly harm anyone.",


    # WIZARD - SCHOOL OF NECROMANCY

    "Necromancy Savant": "The gold and time required to copy a necromancy spell into your spellbook are halved.",

    "Grim Harvest": "Once per turn, when you kill a creature with a spell of level 1 or higher, you regain hit points based on the spell's level.",

    "Undead Thralls": "You gain Animate Dead if you do not already know it. Undead you create with necromancy spells gain extra hit points and damage.",

    "Inured to Undeath": "You gain resistance to necrotic damage, your hit point maximum cannot be reduced, and you have become accustomed to undead energies.",

    "Command Undead": "You can attempt to take control of an undead creature you can see. Intelligent undead may resist or escape your control.",


    # WIZARD - SCHOOL OF TRANSMUTATION

    "Transmutation Savant": "The gold and time required to copy a transmutation spell into your spellbook are halved.",

    "Minor Alchemy": "You can temporarily transform certain nonmagical materials into other materials of similar form.",

    "Transmuter's Stone": "You create a magical stone that grants its bearer a chosen benefit, such as darkvision, increased speed, Constitution saving throw proficiency or resistance to a damage type.",

    "Shapechanger": "You can cast Polymorph on yourself without expending a spell slot once per short or long rest, transforming into a beast of challenge rating 1 or lower.",

    "Master Transmuter": "You can consume your Transmuter's Stone to produce a powerful effect, such as restoring life, removing an affliction or changing an object into another material.",


    # ROGUE - THIEF

    "Fast Hands": "You can use Cunning Action to make certain Dexterity (Sleight of Hand) checks, disarm traps, open locks or use objects as a bonus action.",

    "Second-Story Work": "Climbing no longer costs extra movement, and your running jump distance increases based on your Dexterity modifier.",

    "Supreme Sneak": "You have advantage on Dexterity (Stealth) checks when you move no more than half your speed on the same turn.",

    "Use Magic Device": "You can ignore class, race and level requirements when using magic items.",

    "Thief's Reflexes": "You can take two turns during the first round of combat, acting at your normal initiative and again at initiative minus 10.",


    # ROGUE - ASSASSIN

    "Bonus Proficiencies": "You gain additional proficiencies determined by your subclass, such as disguise kits, poisoner's kits, weapons or armour.",

    "Assassinate": "You have advantage on attack rolls against creatures that have not yet taken a turn in combat. Hits against surprised creatures are critical hits.",

    "Infiltration Expertise": "You can spend time and money creating a false identity, including an established history and documents.",

    "Impostor": "You can imitate another person's speech, writing and behaviour after studying them.",

    "Death Strike": "When you hit a surprised creature, it must make a Constitution saving throw or take double the attack's damage.",


    # ROGUE - ARCANE TRICKSTER

    "Mage Hand Legerdemain": "Your Mage Hand becomes invisible and can perform additional tasks such as manipulating objects, picking locks and using thieves' tools.",

    "Magical Ambush": "When you are hidden from a creature as you cast a spell, that creature has disadvantage on saving throws against the spell that turn.",

    "Versatile Trickster": "You can use your Mage Hand to distract a creature, gaining advantage on attack rolls against it as a bonus action.",

    "Spell Thief": "When a creature casts a spell targeting you or including you in its area, you can use your reaction to attempt to steal knowledge of that spell.",


     # CLERIC - KNOWLEDGE DOMAIN

    "Blessings of Knowledge": "You learn two additional languages and gain proficiency and expertise in two chosen knowledge skills.",

    "Channel Divinity: Knowledge of the Ages": "You can use Channel Divinity to gain temporary proficiency with a chosen skill or tool.",

    "Channel Divinity: Read Thoughts": "You can use Channel Divinity to read a creature's surface thoughts and potentially cast Suggestion on it.",

    "Potent Spellcasting": "You add your Wisdom modifier to the damage dealt by your Cleric cantrips.",

    "Visions of the Past": "You can meditate with an object or in a location to receive visions of past events connected to it.",


    # CLERIC - LIFE DOMAIN

    "Bonus Proficiency": "You gain a bonus proficiency determined by your chosen domain, such as heavy armour.",

    "Disciple of Life": "Your healing spells of level 1 or higher restore additional hit points equal to 2 + the spell's level.",

    "Channel Divinity: Preserve Life": "You can use Channel Divinity to restore a pool of hit points equal to five times your Cleric level, divided among nearby creatures.",

    "Blessed Healer": "When you cast a spell of level 1 or higher that restores hit points to another creature, you also regain hit points.",

    "Divine Strike (1d8)": "Once on each of your turns when you hit with a weapon attack, you deal an additional 1d8 damage of the type granted by your domain.",

    "Supreme Healing": "When rolling dice to restore hit points with a healing spell, you use the maximum possible result for each die.",


    # CLERIC - LIGHT DOMAIN

    "Bonus Cantrip": "You learn the Light cantrip if you do not already know it.",

    "Warding Flare": "You can use your reaction to impose disadvantage on an attack roll made against you by a creature you can see nearby.",

    "Channel Divinity: Radiance of the Dawn": "You can use Channel Divinity to dispel magical darkness and damage hostile creatures with radiant energy.",

    "Improved Flare": "You can also use Warding Flare to protect another creature within 30 feet.",

    "Corona of Light": "You can create an aura of sunlight that imposes disadvantage on saving throws against spells dealing fire or radiant damage.",


    # CLERIC - NATURE DOMAIN
    "Acolyte of Nature": "You learn one Druid cantrip and gain proficiency in a chosen nature-related skill.",

    "Channel Divinity: Charm Animals and Plants": "You can use Channel Divinity to charm nearby beasts and plant creatures.",

    "Dampen Elements": "When a creature nearby takes certain elemental damage, you can use your reaction to grant resistance against that damage.",

    "Master of Nature": "You can command beasts and plant creatures affected by your Charm Animals and Plants feature.",


    # CLERIC - TEMPEST DOMAIN

    "Wrath of the Storm": "When a creature within 5 feet hits you, you can use your reaction to deal lightning or thunder damage to it.",

    "Channel Divinity: Destructive Wrath": "You can use Channel Divinity to deal maximum damage instead of rolling when you deal lightning or thunder damage.",

    "Thunderbolt Strike": "When you deal lightning damage to a Large or smaller creature, you can push it up to 10 feet away.",

    "Stormborn": "You gain a flying speed equal to your walking speed while you are not underground or indoors.",


    # CLERIC - TRICKERY DOMAIN

    "Blessing of the Trickster": "You can grant another creature advantage on Dexterity (Stealth) checks for up to 1 hour.",

    "Channel Divinity: Invoke Duplicity": "You can create an illusory duplicate of yourself that you can move and use as the origin point for casting certain spells.",

    "Channel Divinity: Cloak of Shadows": "You can use Channel Divinity to become invisible until the end of your next turn.",

    "Improved Duplicity": "You can create up to four illusory duplicates with Invoke Duplicity.",



    # CLERIC - WAR DOMAIN
    "War Priest": "When you take the Attack action, you can make one weapon attack as a bonus action a limited number of times per long rest.",

    "Channel Divinity: Guided Strike": "You can use Channel Divinity to gain a +10 bonus to an attack roll.",

    "Channel Divinity: War God's Blessing": "You can use your reaction and Channel Divinity to grant another creature a +10 bonus to an attack roll.",

    "Avatar of Battle": "You have resistance to bludgeoning, piercing and slashing damage from nonmagical weapons.",



    # BARBARIAN - PATH OF THE BERSERKER

    "Frenzy": "When you enter a rage, you can choose to frenzy, allowing an additional melee weapon attack as a bonus action on subsequent turns. You gain one level of exhaustion when the rage ends.",

    "Mindless Rage": "You cannot be charmed or frightened while raging. Existing charm or fear effects are suspended during your rage.",

    "Intimidating Presence": "You can use your action to frighten a creature within 30 feet if it fails a Wisdom saving throw.",

    "Retaliation": "When a creature within 5 feet damages you, you can use your reaction to make a melee weapon attack against it.",



    # BARBARIAN - PATH OF THE TOTEM WARRIOR
    "Spirit Seeker": "You can cast Beast Sense and Speak with Animals as rituals.",

    "Totem Spirit": "You gain a special benefit while raging based on your chosen totem animal: Bear, Eagle or Wolf.",

    "Aspect of the Beast": "You gain an exploration or utility benefit based on your chosen totem animal.",

    "Spirit Walker": "You can cast Commune with Nature as a ritual to seek guidance from nature spirits.",

    "Totemic Attunement": "You gain an additional combat benefit while raging based on your chosen totem animal."
}


subrace_feature_descriptions = {
    "Elf Weapon Training": "You have proficiency with longswords, shortswords, shortbows and longbows.",

    "Cantrip": "You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it.",

    "Extra Language": "You can speak, read and write one additional language of your choice.",

    "Fleet of Foot": "Your base walking speed increases to 35 feet.",

    "Mask Of The Wild": "You can attempt to hide when only lightly obscured by natural phenomena such as foliage, heavy rain, falling snow or mist.",

    "Superior Darkvision": "Your darkvision extends to a range of 120 feet.",

    "Sunlight Sensitivity": "You have disadvantage on attack rolls and Wisdom (Perception) checks relying on sight when you or what you are trying to perceive is in direct sunlight.",

    "Drow Magic": "You know the Dancing Lights cantrip. At level 3, you can cast Faerie Fire once per long rest. At level 5, you can cast Darkness once per long rest. Charisma is your spellcasting ability for these spells.",

    "Drow Weapon Training": "You have proficiency with rapiers, shortswords and hand crossbows.",

    "Dwarven Toughness": "Your hit point maximum increases by 1, and increases by 1 again whenever you gain a level.",

    "Dwarven Armour Training": "You have proficiency with light armour and medium armour."
}


all_skill_options = [
    "Acrobatics", "Animal Handling", "Arcana",
    "Athletics", "Deception", "History",
    "Insight", "Intimidation", "Investigation",
    "Medicine", "Nature", "Perception",
    "Performance", "Persuasion", "Religion",
    "Sleight of Hand", "Stealth", "Survival"
]

cantrip_lists = {
    "Wizard": [
        "Acid Splash",
        "Blade Ward",
        "Chill Touch",
        "Dancing Lights",
        "Fire Bolt",
        "Friends",
        "Light",
        "Mage Hand",
        "Mending",
        "Message",
        "Minor Illusion",
        "Poison Spray",
        "Prestidigitation",
        "Ray of Frost",
        "Shocking Grasp",
        "True Strike"
    ],

    "Cleric": [
        "Guidance",
        "Light",
        "Mending",
        "Resistance",
        "Sacred Flame",
        "Spare the Dying",
        "Thaumaturgy"
    ],
    "Druid": [
        "Druidcraft",
        "Guidance",
        "Mending",
        "Poison Spray",
        "Produce Flame",
        "Resistance",
        "Shillelagh",
        "Thorn Whip"
    ]
}

spell_details = {'Acid Splash': {'level': 0,
                 'classes': ['Wizard'],
                 'description': 'Throws acid at one or two nearby creatures, dealing acid damage '
                                'on failed Dexterity saves.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': ''},
 'Aid': {'level': 2,
         'classes': ['Cleric'],
         'description': 'Raises the current and maximum hit points of up to three creatures for '
                        'eight hours.',
         'conditions_inflicted': [],
         'conditions_granted': [],
         'concentration': False,
         'ritual': False,
         'notable_requirements': ''},
 'Alarm': {'level': 1,
           'classes': ['Wizard'],
           'description': 'Wards an entrance or small area and alerts you when an unapproved '
                          'creature enters.',
           'conditions_inflicted': [],
           'conditions_granted': [],
           'concentration': False,
           'ritual': True,
           'notable_requirements': ''},
 'Alter Self': {'level': 2,
                'classes': ['Wizard'],
                'description': 'Temporarily changes your body to gain aquatic adaptations, altered '
                               'appearance, or natural weapons.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': True,
                'ritual': False,
                'notable_requirements': ''},
 'Animate Dead': {'level': 3,
                  'classes': ['Wizard', 'Cleric'],
                  'description': 'Raises a skeleton or zombie from remains and lets you command it '
                                 'for a limited period.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': ''},
 'Animate Objects': {'level': 5,
                     'classes': ['Wizard'],
                     'description': 'Animates unattended objects into temporary creatures you can '
                                    'command.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''},
 'Antimagic Field': {'level': 8,
                     'classes': ['Wizard', 'Cleric'],
                     'description': 'Creates an aura suppressing spells, magical items, and other '
                                    'magical effects.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''},
 'Antipathy/Sympathy': {'level': 8,
                        'classes': ['Wizard'],
                        'description': 'Places an aura that repels or attracts a chosen kind of '
                                       'intelligent creature.',
                        'conditions_inflicted': ['Frightened'],
                        'conditions_granted': [],
                        'concentration': False,
                        'ritual': False,
                        'notable_requirements': ''},
'Arcane Eye': {'level': 4,
                'classes': ['Wizard'],
                'description': 'Creates an invisible floating eye you can move to observe distant '
                               'places.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': True,
                'ritual': False,
                'notable_requirements': ''},
 'Arcane Gate': {'level': 6,
                 'classes': ['Wizard'],
                 'description': 'Creates two linked portals allowing travel between their '
                                'locations.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': True,
                 'ritual': False,
                 'notable_requirements': ''},
 'Arcane Lock': {'level': 2,
                 'classes': ['Wizard'],
                 'description': 'Magically secures a door, chest, or other closed entry against '
                                'opening.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': 'Requires gold dust worth at least 25 gp, consumed.'},
 'Astral Projection': {'level': 9,
                       'classes': ['Wizard', 'Cleric'],
                       'description': 'Projects your astral forms into the Astral Plane while '
                                      'physical bodies remain behind.',
                       'conditions_inflicted': [],
                       'conditions_granted': [],
                       'concentration': False,
                       'ritual': False,
                       'notable_requirements': 'Requires a jacinth worth 1,000 gp and a silver bar '
                                               'worth 100 gp per creature, consumed.'},
'Augury': {'level': 2,
            'classes': ['Cleric'],
            'description': 'Uses omens to predict whether a proposed action is likely to bring '
                           'good or bad results.',
            'conditions_inflicted': [],
            'conditions_granted': [],
            'concentration': False,
            'ritual': True,
            'notable_requirements': 'Requires specially marked divination tokens worth at least 25 '
                                    'gp.'},
 'Bane': {'level': 1,
          'classes': ['Cleric'],
          'description': 'Up to three targets subtract a d4 from attacks and saving throws after '
                         'failed Charisma saves.',
          'conditions_inflicted': [],
          'conditions_granted': [],
          'concentration': True,
          'ritual': False,
          'notable_requirements': ''},
 'Banishment': {'level': 4,
                'classes': ['Wizard', 'Cleric'],
                'description': 'Sends a creature to a harmless demiplane or back to its native '
                               'plane after a failed Charisma save.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': True,
                'ritual': False,
                'notable_requirements': ''},
 'Beacon of Hope': {'level': 3,
                    'classes': ['Cleric'],
                    'description': 'Gives allies advantage on Wisdom and death saves and maximises '
                                   'healing received.',
                    'conditions_inflicted': [],
                    'conditions_granted': [],
                    'concentration': True,
                    'ritual': False,
                    'notable_requirements': ''},
 'Bestow Curse': {'level': 3,
                  'classes': ['Wizard', 'Cleric'],
                  'description': 'Places a harmful curse on a creature that fails a Wisdom save.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': True,
                  'ritual': False,
                  'notable_requirements': ''},
"Bigby's Hand": {'level': 5,
                  'classes': ['Wizard'],
                  'description': 'Summons a giant force hand that can strike, push, grapple, or '
                                 'protect.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': True,
                  'ritual': False,
                  'notable_requirements': ''},
 'Blade Barrier': {'level': 6,
                   'classes': ['Cleric'],
                   'description': 'Creates a wall of whirling blades that damages creatures '
                                  'passing through it.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': True,
                   'ritual': False,
                   'notable_requirements': ''},
 'Blade Ward': {'level': 0,
                'classes': ['Wizard'],
                'description': 'Briefly grants resistance to weapon-attack bludgeoning, piercing, '
                               'and slashing damage.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': False,
                'ritual': False,
                'notable_requirements': ''},
 'Bless': {'level': 1,
           'classes': ['Cleric'],
           'description': 'Up to three allies add a d4 to attack rolls and saving throws.',
           'conditions_inflicted': [],
           'conditions_granted': [],
           'concentration': True,
           'ritual': False,
           'notable_requirements': ''},
 'Blight': {'level': 4,
            'classes': ['Wizard'],
            'description': 'Drains moisture from a creature, dealing heavy necrotic damage, '
                           'especially to plants.',
            'conditions_inflicted': [],
            'conditions_granted': [],
            'concentration': False,
            'ritual': False,
            'notable_requirements': ''},
'Blindness/Deafness': {'level': 2,
                        'classes': ['Wizard', 'Cleric'],
                        'description': 'A Constitution save may blind or deafen a creature without '
                                       'concentration.',
                        'conditions_inflicted': ['Blinded', 'Deafened'],
                        'conditions_granted': [],
                        'concentration': False,
                        'ritual': False,
                        'notable_requirements': ''},
 'Blink': {'level': 3,
           'classes': ['Wizard'],
           'description': 'May shift you into the Ethereal Plane at the end of each turn, avoiding '
                          'some attacks.',
           'conditions_inflicted': [],
           'conditions_granted': [],
           'concentration': False,
           'ritual': False,
           'notable_requirements': ''},
 'Blur': {'level': 2,
          'classes': ['Wizard'],
          'description': 'Makes your outline waver, imposing disadvantage on many attacks against '
                         'you.',
          'conditions_inflicted': [],
          'conditions_granted': [],
          'concentration': True,
          'ritual': False,
          'notable_requirements': ''},
 'Burning Hands': {'level': 1,
                   'classes': ['Wizard'],
                   'description': 'A fan of flame damages creatures in a short cone; Dexterity '
                                  'saves reduce the damage.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': False,
                   'ritual': False,
                   'notable_requirements': ''},
 'Calm Emotions': {'level': 2,
                   'classes': ['Cleric'],
                   'description': 'Suppresses charm or fear effects, or temporarily calms hostile '
                                  'humanoids.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': True,
                   'ritual': False,
                   'notable_requirements': ''},
 'Chain Lightning': {'level': 6,
                     'classes': ['Wizard'],
                     'description': 'Sends lightning through an initial target and several '
                                    'additional creatures.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''},
 'Charm Person': {'level': 1,
 'classes': ['Wizard'],
 'description': 'Makes a humanoid regard you as a friendly acquaintance if it '
 'fails a Wisdom save.',
 'conditions_inflicted': ['Charmed'],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': ''},
 'Chill Touch': {'level': 0,
                 'classes': ['Wizard'],
                 'description': 'A spectral hand deals necrotic damage and prevents healing '
                                'briefly; undead are further hindered.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': ''},
 'Chromatic Orb': {'level': 1,
                   'classes': ['Wizard'],
                   'description': 'Hurls an elemental orb using a ranged spell attack; you choose '
                                  'the damage type.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': False,
                   'ritual': False,
                   'notable_requirements': 'Requires a diamond worth at least 50 gp (not '
                                           'consumed).'},
 'Circle of Death': {'level': 6,
                     'classes': ['Wizard'],
                     'description': 'Releases a large burst of necrotic energy, damaging creatures '
                                    'in its radius.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''},
 'Clairvoyance': {'level': 3,
                  'classes': ['Wizard', 'Cleric'],
                  'description': 'Creates an invisible sensor for remote sight or hearing at a '
                                 'chosen location.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': True,
                  'ritual': False,
                  'notable_requirements': ''},
 'Clone': {'level': 8,
           'classes': ['Wizard'],
           'description': 'Creates an inert duplicate body that can receive your soul after death.',
           'conditions_inflicted': [],
           'conditions_granted': [],
           'concentration': False,
           'ritual': False,
           'notable_requirements': 'Requires a diamond worth at least 1,000 gp, consumed, and a '
                                   'costly vessel.'},
 'Cloud of Daggers': {'level': 2,
                      'classes': ['Wizard'],
                      'description': 'Creates a small area of spinning blades that damages '
                                     'creatures entering or starting there.',
                      'conditions_inflicted': [],
                      'conditions_granted': [],
                      'concentration': True,
                      'ritual': False,
                      'notable_requirements': ''},
'Cloudkill': {'level': 5,
               'classes': ['Wizard'],
               'description': 'Creates a moving cloud of toxic gas that damages creatures caught '
                              'inside.',
               'conditions_inflicted': [],
               'conditions_granted': [],
               'concentration': True,
               'ritual': False,
               'notable_requirements': ''},
 'Color Spray': {'level': 1,
                 'classes': ['Wizard'],
                 'description': 'A burst of coloured light blinds creatures according to their '
                                'current hit points.',
                 'conditions_inflicted': ['Blinded'],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': ''},
 'Command': {'level': 1,
             'classes': ['Cleric'],
             'description': 'Forces a creature that fails a Wisdom save to obey a brief command on '
                            'its next turn.',
             'conditions_inflicted': ['Prone'],
             'conditions_granted': [],
             'concentration': False,
             'ritual': False,
             'notable_requirements': ''},
 'Commune': {'level': 5,
             'classes': ['Cleric'],
             'description': 'Asks a deity or divine agent up to three yes-or-no questions.',
             'conditions_inflicted': [],
             'conditions_granted': [],
             'concentration': False,
             'ritual': True,
             'notable_requirements': ''},
 'Comprehend Languages': {'level': 1,
          'classes': ['Wizard'],
          'description': 'Lets you understand the literal meaning of spoken and '
                         'written languages.',
          'conditions_inflicted': [],
          'conditions_granted': [],
          'concentration': False,
          'ritual': True,
          'notable_requirements': ''},
 'Cone of Cold': {'level': 5,
                  'classes': ['Wizard'],
                  'description': 'Unleashes a broad cone of cold damage, with a Constitution save '
                                 'for half.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': ''},
 'Confusion': {'level': 4,
               'classes': ['Wizard'],
               'description': "Scrambles affected creatures' behaviour, causing unpredictable "
                              'actions and lost turns.',
               'conditions_inflicted': [],
               'conditions_granted': [],
               'concentration': True,
               'ritual': False,
               'notable_requirements': ''},
 'Conjure Celestial': {'level': 7,
                       'classes': ['Cleric'],
                       'description': 'Summons a celestial creature to assist you for the '
                                      'duration.',
                       'conditions_inflicted': [],
                       'conditions_granted': [],
                       'concentration': True,
                       'ritual': False,
                       'notable_requirements': ''},
 'Conjure Elemental': {'level': 5,
                       'classes': ['Wizard'],
                       'description': 'Summons an elemental that obeys you while you maintain '
                                      'control.',
                       'conditions_inflicted': [],
                       'conditions_granted': [],
                       'concentration': True,
                       'ritual': False,
                       'notable_requirements': ''},
 'Conjure Minor Elementals': {'level': 4,
                              'classes': ['Wizard'],
                              'description': 'Summons one or more minor elemental creatures that '
                                             'follow your commands.',
                              'conditions_inflicted': [],
                              'conditions_granted': [],
                              'concentration': True,
                              'ritual': False,
                              'notable_requirements': ''},
 'Contact Other Plane': {'level': 5,
                         'classes': ['Wizard'],
                         'description': 'Asks questions of an extraplanar entity, risking '
                                        'temporary mental harm.',
                         'conditions_inflicted': [],
                         'conditions_granted': [],
                         'concentration': False,
                         'ritual': True,
                         'notable_requirements': ''},
 'Contagion': {'level': 5,
               'classes': ['Cleric'],
               'description': 'Infects a touched creature with a debilitating magical disease '
                              'after a successful spell attack.',
               'conditions_inflicted': ['Poisoned'],
               'conditions_granted': [],
               'concentration': False,
               'ritual': False,
               'notable_requirements': ''},
 'Contingency': {'level': 6,
                 'classes': ['Wizard'],
                 'description': 'Stores a lower-level spell to activate automatically when a '
                                'specified condition occurs.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': 'Requires a statuette of yourself worth at least 1,500 gp '
                                         '(not consumed).'},
 'Continual Flame': {'level': 2,
                     'classes': ['Wizard', 'Cleric'],
                     'description': 'Creates a long-lasting magical flame that gives light without '
                                    'heat.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires ruby dust worth at least 50 gp, consumed.'},
 'Control Water': {'level': 4,
                   'classes': ['Wizard', 'Cleric'],
                   'description': 'Changes the behaviour of a large body of water, including '
                                  'flooding and parting it.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': True,
                   'ritual': False,
                   'notable_requirements': ''},
 'Control Weather': {'level': 8,
                     'classes': ['Wizard', 'Cleric'],
                     'description': 'Gradually changes local precipitation, temperature, and wind '
                                    'conditions.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''},
 'Counterspell': {'level': 3,
                  'classes': ['Wizard'],
                  'description': "Interrupts another creature's spellcasting, sometimes requiring "
                                 'an ability check.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': ''},
 'Create Food and Water': {'level': 3,
                           'classes': ['Cleric'],
                           'description': 'Produces enough basic food and water to sustain several '
                                          'creatures.',
                           'conditions_inflicted': [],
                           'conditions_granted': [],
                           'concentration': False,
                           'ritual': False,
                           'notable_requirements': ''},
 'Create Undead': {'level': 6,
                   'classes': ['Wizard', 'Cleric'],
                   'description': 'Animates corpses as more powerful undead servants, depending on '
                                  'slot level.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': False,
                   'ritual': False,
                   'notable_requirements': 'Requires a black onyx stone worth at least 150 gp for '
                                           'each corpse.'},
 'Create or Destroy Water': {'level': 1,
                             'classes': ['Cleric'],
                             'description': 'Creates clean water or destroys water within the '
                                            "spell's limits.",
                             'conditions_inflicted': [],
                             'conditions_granted': [],
                             'concentration': False,
                             'ritual': False,
                             'notable_requirements': ''},
 'Creation': {'level': 5,
              'classes': ['Wizard'],
              'description': 'Forms a temporary nonliving object from shadowy material, with '
                             'duration depending on substance.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': False,
              'ritual': False,
              'notable_requirements': ''},
 'Crown of Madness': {'level': 2,
                      'classes': ['Wizard'],
                      'description': 'Charms a humanoid and can compel it to attack a nearby '
                                     'creature.',
                      'conditions_inflicted': ['Charmed'],
                      'conditions_granted': [],
                      'concentration': True,
                      'ritual': False,
                      'notable_requirements': ''},
 'Cure Wounds': {'level': 1,
                 'classes': ['Cleric'],
                 'description': 'Restores hit points to a creature you touch; ineffective on '
                                'undead or constructs.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': ''},
 'Dancing Lights': {'level': 0,
                    'classes': ['Wizard'],
                    'description': 'Creates several small lights you can move while concentrating.',
                    'conditions_inflicted': [],
                    'conditions_granted': [],
                    'concentration': True,
                    'ritual': False,
                    'notable_requirements': ''},

                 'Hellish Rebuke': {
                     'level': 1,
                     'classes': ['Warlock'],
                     'description': (
                         'As a reaction when damaged by a creature you can see '
                         'within 60 feet, flames engulf that creature. It makes '
                         'a Dexterity saving throw, taking 2d10 fire damage on '
                         'a failed save, or half as much on a success. '
                         'Damage increases by 1d10 per spell slot level above 1st.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': (
                         'Reaction when damaged by a visible creature within 60 feet. '
                         'Tieflings cast this spell at 2nd level once per long rest '
                         'starting at character level 3.'
                     )
                 },

                 'Darkness': {'level': 2,
              'classes': ['Wizard'],
              'description': 'Creates magical darkness that ordinary darkvision cannot see '
                             'through.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': True,
              'ritual': False,
              'notable_requirements': ''},
'Detect Evil and Good': {'level': 1,
                          'classes': ['Cleric'],
                          'description': 'Senses certain supernatural creature types and '
                                         'consecrated or desecrated places nearby.',
                          'conditions_inflicted': [],
                          'conditions_granted': [],
                          'concentration': True,
                          'ritual': False,
                          'notable_requirements': ''},
'Detect Magic': {'level': 1,
                 'classes': ['Wizard', 'Cleric'],
                 'description': 'Reveals nearby magic and, with an action, its school when '
                                'visible.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': True,
                 'ritual': True,
                 'notable_requirements': ''},
'Detect Poison and Disease': {'level': 1,
                              'classes': ['Cleric'],
                              'description': 'Senses nearby poisons, poisonous creatures, and '
                                             'diseases.',
                              'conditions_inflicted': [],
                              'conditions_granted': [],
                              'concentration': True,
                              'ritual': True,
                              'notable_requirements': ''},
'Detect Thoughts': {'level': 2,
                    'classes': ['Wizard'],
                    'description': 'Reads surface thoughts and can probe deeper, potentially '
                                   'alerting the subject.',
                    'conditions_inflicted': [],
                    'conditions_granted': [],
                    'concentration': True,
                    'ritual': False,
                    'notable_requirements': ''},
'Dimension Door': {'level': 4,
                   'classes': ['Wizard'],
                   'description': 'Teleports you and optionally one willing companion to a '
                                  'destination within range.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': False,
                   'ritual': False,
                   'notable_requirements': ''},
'Disguise Self': {'level': 1,
                  'classes': ['Wizard'],
                  'description': 'Changes your apparent appearance without physically altering '
                                 'your body.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': ''},
'Disintegrate': {'level': 6,
                 'classes': ['Wizard'],
                 'description': 'Fires a ray that deals immense force damage and can reduce a '
                                'slain target to dust.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': ''},
'Dispel Evil and Good': {'level': 5,
                         'classes': ['Cleric'],
                         'description': 'Protects you from supernatural creatures and can break '
                                        'possession or send one away.',
                         'conditions_inflicted': [],
                         'conditions_granted': [],
                         'concentration': True,
                         'ritual': False,
                         'notable_requirements': ''},
'Dispel Magic': {'level': 3,
                 'classes': ['Wizard', 'Cleric'],
                 'description': 'Ends spells affecting a target, with checks for sufficiently '
                                'high-level effects.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': ''},
'Divination': {'level': 4,
               'classes': ['Cleric'],
               'description': 'Offers a truthful but possibly cryptic omen about a specific '
                              'near-future event.',
               'conditions_inflicted': [],
               'conditions_granted': [],
               'concentration': False,
               'ritual': True,
               'notable_requirements': 'Requires a sacrificial offering worth at least 25 gp, '
                                       'consumed.'},
'Divine Word': {'level': 7,
                'classes': ['Cleric'],
                'description': 'Speaks a divine utterance that can deafen, blind, stun, or kill '
                               'weakened enemies.',
                'conditions_inflicted': ['Deafened', 'Blinded', 'Stunned'],
                'conditions_granted': [],
                'concentration': False,
                'ritual': False,
                'notable_requirements': ''},
'Dominate Monster': {'level': 8,
                     'classes': ['Wizard'],
                     'description': 'Charms a creature and allows you to command or control its '
                                    'actions.',
                     'conditions_inflicted': ['Charmed'],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''},
'Dominate Person': {'level': 5,
                    'classes': ['Wizard'],
                    'description': 'Charms a humanoid and gives you powerful control over its '
                                   'actions.',
                    'conditions_inflicted': ['Charmed'],
                    'conditions_granted': [],
                    'concentration': True,
                    'ritual': False,
                    'notable_requirements': ''},
"Drawmij's Instant Summons": {'level': 6,
                              'classes': ['Wizard'],
                              'description': 'Marks an object so you can later summon it using a '
                                             'specially prepared sapphire.',
                              'conditions_inflicted': [],
                              'conditions_granted': [],
                              'concentration': False,
                              'ritual': True,
                              'notable_requirements': ''},
'Dream': {'level': 5,
          'classes': ['Wizard'],
          'description': "Enters a sleeping creature's dreams to communicate or inflict a "
                         'nightmare.',
          'conditions_inflicted': [],
          'conditions_granted': [],
          'concentration': False,
          'ritual': False,
          'notable_requirements': ''},
'Earthquake': {'level': 8,
               'classes': ['Cleric'],
               'description': 'Shakes a large area, creating fissures, collapsing structures, and '
                              'knocking creatures down.',
               'conditions_inflicted': ['Prone'],
               'conditions_granted': [],
               'concentration': True,
               'ritual': False,
               'notable_requirements': ''},
'Fire Bolt': {'level': 0,
               'classes': ['Wizard'],
               'description': 'A ranged spell attack deals fire damage and may ignite unattended '
                              'flammable objects.',
               'conditions_inflicted': [],
               'conditions_granted': [],
               'concentration': False,
               'ritual': False,
               'notable_requirements': ''},
'Fire Shield': {'level': 4,
                'classes': ['Wizard'],
                'description': 'Surrounds you with a fiery or icy aura that resists one damage '
                               'type and punishes melee attackers.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': False,
                'ritual': False,
                'notable_requirements': ''},
'Fire Storm': {'level': 7,
               'classes': ['Cleric'],
               'description': 'Creates multiple fiery areas that damage creatures and objects.',
               'conditions_inflicted': [],
               'conditions_granted': [],
               'concentration': False,
               'ritual': False,
               'notable_requirements': ''},
'Fireball': {'level': 3,
             'classes': ['Wizard'],
             'description': 'Explodes in a wide area, dealing fire damage with a Dexterity save '
                            'for half.',
             'conditions_inflicted': [],
             'conditions_granted': [],
             'concentration': False,
             'ritual': False,
             'notable_requirements': ''},
'Flame Strike': {'level': 5,
                 'classes': ['Cleric'],
                 'description': 'Calls down divine fire and radiant energy in a vertical column.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': ''},
'Flaming Sphere': {'level': 2,
                   'classes': ['Wizard'],
                   'description': 'Creates a movable fiery sphere that burns creatures near it.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': True,
                   'ritual': False,
                   'notable_requirements': ''},
'Flesh to Stone': {'level': 6,
                   'classes': ['Wizard'],
                   'description': 'Gradually transforms a creature into stone, restraining it '
                                  'before possible petrification.',
                   'conditions_inflicted': ['Restrained', 'Petrified'],
                   'conditions_granted': [],
                   'concentration': True,
                   'ritual': False,
                   'notable_requirements': ''},
'Fly': {'level': 3,
        'classes': ['Wizard'],
        'description': 'Grants a creature a flying speed for the duration.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': ''},
'Fog Cloud': {'level': 1,
              'classes': ['Wizard'],
              'description': 'Creates a heavily obscuring bank of fog that can spread with '
                             'stronger slots.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': True,
              'ritual': False,
              'notable_requirements': ''},
'Forbiddance': {'level': 6,
                'classes': ['Cleric'],
                'description': 'Wards a large area against planar travel and harms selected '
                               'supernatural creatures.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': False,
                'ritual': True,
                'notable_requirements': 'Requires materials worth at least 1,000 gp; consumed if '
                                        'made permanent by repeated casting.'},
'Forcecage': {'level': 7,
              'classes': ['Wizard'],
              'description': 'Creates a cage or box of force that traps creatures without '
                             'concentration.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': False,
              'ritual': False,
              'notable_requirements': ''},
'Foresight': {'level': 9,
              'classes': ['Wizard'],
              'description': 'Grants a creature powerful awareness, improving attacks, checks, '
                             'saves, and defence.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': False,
              'ritual': False,
              'notable_requirements': ''},
'Freedom of Movement': {'level': 4,
                        'classes': ['Cleric'],
                        'description': 'Protects a creature from magical movement restrictions '
                                       'and helps escape grapples or restraints.',
                        'conditions_inflicted': [],
                        'conditions_granted': [],
                        'concentration': False,
                        'ritual': False,
                        'notable_requirements': ''},
'Friends': {'level': 0,
            'classes': ['Wizard'],
            'description': 'Briefly grants advantage on Charisma checks against a nonhostile '
                           'creature, which notices afterwards.',
            'conditions_inflicted': [],
            'conditions_granted': [],
            'concentration': True,
            'ritual': False,
            'notable_requirements': ''},
'Gaseous Form': {'level': 3,
                 'classes': ['Wizard'],
                 'description': 'Transforms a willing creature into a cloudlike form able to pass '
                                'through small openings.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': True,
                 'ritual': False,
                 'notable_requirements': ''},
'Gate': {'level': 9,
         'classes': ['Wizard', 'Cleric'],
         'description': 'Opens a portal to another plane and can call a named creature through '
                        'it.',
         'conditions_inflicted': [],
         'conditions_granted': [],
         'concentration': True,
         'ritual': False,
         'notable_requirements': 'Requires a diamond worth at least 5,000 gp.'},
'Geas': {'level': 5,
         'classes': ['Wizard', 'Cleric'],
         'description': 'Places a long-lasting magical command on a creature, harming it for '
                        'disobedience.',
         'conditions_inflicted': ['Charmed'],
         'conditions_granted': [],
         'concentration': False,
         'ritual': False,
         'notable_requirements': ''},
'Gentle Repose': {'level': 2,
                  'classes': ['Wizard', 'Cleric'],
                  'description': 'Preserves a corpse and delays its eligibility window for '
                                 'certain resurrection spells.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': True,
                  'notable_requirements': ''},
'Globe of Invulnerability': {'level': 6,
                             'classes': ['Wizard'],
                             'description': 'Creates a protective sphere that blocks spells of '
                                            'lower levels from outside.',
                             'conditions_inflicted': [],
                             'conditions_granted': [],
                             'concentration': True,
                             'ritual': False,
                             'notable_requirements': ''},
'Glyph of Warding': {'level': 3,
                     'classes': ['Wizard', 'Cleric'],
                     'description': 'Sets a magical trap that triggers an explosive effect or '
                                    'stored spell.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires incense and powdered diamond worth at '
                                             'least 200 gp, consumed.'},
'Grease': {'level': 1,
           'classes': ['Wizard'],
           'description': 'Coats an area in slippery grease, potentially knocking creatures down.',
           'conditions_inflicted': ['Prone'],
           'conditions_granted': [],
           'concentration': False,
           'ritual': False,
           'notable_requirements': ''},
'Greater Invisibility': {'level': 4,
                         'classes': ['Wizard'],
                         'description': 'Keeps a creature invisible even when it attacks or casts '
                                        'spells.',
                         'conditions_inflicted': [],
                         'conditions_granted': ['Invisible'],
                         'concentration': True,
                         'ritual': False,
                         'notable_requirements': ''},
'Greater Restoration': {'level': 5,
                        'classes': ['Cleric'],
                        'description': 'Removes a major debilitating effect, including some '
                                       'curses, exhaustion, or ability reductions.',
                        'conditions_inflicted': [],
                        'conditions_granted': [],
                        'concentration': False,
                        'ritual': False,
                        'notable_requirements': 'Requires diamond dust worth at least 100 gp, '
                                                'consumed.'},
'Guardian of Faith': {'level': 4,
                       'classes': ['Cleric'],
                       'description': 'Summons a stationary guardian that deals radiant damage to '
                                      'approaching enemies.',
                       'conditions_inflicted': [],
                       'conditions_granted': [],
                       'concentration': False,
                       'ritual': False,
                       'notable_requirements': ''},
 'Guards and Wards': {'level': 6,
                      'classes': ['Wizard'],
                      'description': 'Fills a building with magical barriers, illusions, and other '
                                     'defences.',
                      'conditions_inflicted': [],
                      'conditions_granted': [],
                      'concentration': False,
                      'ritual': False,
                      'notable_requirements': ''},
 'Guidance': {'level': 0,
              'classes': ['Cleric'],
              'description': 'Adds a d4 to one ability check made by a willing creature while you '
                             'concentrate.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': True,
              'ritual': False,
              'notable_requirements': ''},
 'Guiding Bolt': {'level': 1,
                  'classes': ['Cleric'],
                  'description': 'A radiant ranged spell attack damages a target and grants '
                                 'advantage on the next attack against it.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': ''},
 'Gust of Wind': {'level': 2,
                  'classes': ['Wizard'],
                  'description': 'Produces a strong line of wind that pushes creatures and '
                                 'disperses vapours.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': True,
                  'ritual': False,
                  'notable_requirements': ''},
 'Hallow': {'level': 5,
            'classes': ['Cleric'],
            'description': 'Consecrates or desecrates an area, warding against selected creature '
                           'types and effects.',
            'conditions_inflicted': [],
            'conditions_granted': [],
            'concentration': False,
            'ritual': False,
            'notable_requirements': 'Requires herbs, oils, and incense worth at least 1,000 gp, '
                                    'consumed.'},
 'Hallucinatory Terrain': {'level': 4,
                           'classes': ['Wizard'],
                           'description': 'Makes natural terrain appear, sound, and smell like '
                                          'another type of natural terrain.',
                           'conditions_inflicted': [],
                           'conditions_granted': [],
                           'concentration': False,
                           'ritual': False,
                           'notable_requirements': ''},
 'Harm': {'level': 6,
          'classes': ['Cleric'],
          'description': "Deals necrotic damage and temporarily reduces a target's maximum hit "
                         'points.',
          'conditions_inflicted': [],
          'conditions_granted': [],
          'concentration': False,
          'ritual': False,
          'notable_requirements': ''},
 'Haste': {'level': 3,
           'classes': ['Wizard'],
           'description': 'Grants extra speed, AC, Dexterity-save advantage, and a limited extra '
                          'action.',
           'conditions_inflicted': [],
           'conditions_granted': [],
           'concentration': True,
           'ritual': False,
           'notable_requirements': ''},
'Heal': {'level': 6,
          'classes': ['Cleric'],
          'description': 'Restores a large amount of hit points and cures certain ailments.',
          'conditions_inflicted': [],
          'conditions_granted': [],
          'concentration': False,
          'ritual': False,
          'notable_requirements': ''},
 'Healing Word': {'level': 1,
                  'classes': ['Cleric'],
                  'description': 'Restores hit points at range using a bonus action.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': ''},
 "Heroes' Feast": {'level': 6,
                   'classes': ['Cleric'],
                   'description': 'Provides a magical feast granting hit points, poison and fear '
                                  'protection, and other benefits.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': False,
                   'ritual': False,
                   'notable_requirements': 'Requires a gem-encrusted bowl worth at least 1,000 gp, '
                                           'consumed.'},
 'Hold Monster': {'level': 5,
                  'classes': ['Wizard'],
                  'description': 'Paralyses a creature that fails a Wisdom save, except undead.',
                  'conditions_inflicted': ['Paralyzed'],
                  'conditions_granted': [],
                  'concentration': True,
                  'ritual': False,
                  'notable_requirements': ''},
 'Hold Person': {'level': 2,
                 'classes': ['Wizard', 'Cleric'],
                 'description': 'Paralyses a humanoid that fails a Wisdom save, with further saves '
                                'to escape.',
                 'conditions_inflicted': ['Paralyzed'],
                 'conditions_granted': [],
                 'concentration': True,
                 'ritual': False,
                 'notable_requirements': ''},
 'Holy Aura': {'level': 8,
               'classes': ['Cleric'],
               'description': 'Surrounds allies with divine radiance, granting defences and '
                              'potentially blinding attackers.',
               'conditions_inflicted': ['Blinded'],
               'conditions_granted': [],
               'concentration': True,
               'ritual': False,
               'notable_requirements': ''},
 'Hypnotic Pattern': {'level': 3,
                      'classes': ['Wizard'],
                      'description': 'A colourful illusion can charm and incapacitate creatures '
                                     'until disrupted.',
                      'conditions_inflicted': ['Charmed', 'Incapacitated'],
                      'conditions_granted': [],
                      'concentration': True,
                      'ritual': False,
                      'notable_requirements': ''},
 'Ice Storm': {'level': 4,
               'classes': ['Wizard'],
               'description': 'Pelts an area with hail and ice, causing bludgeoning and cold '
                              'damage and difficult terrain.',
               'conditions_inflicted': [],
               'conditions_granted': [],
               'concentration': False,
               'ritual': False,
               'notable_requirements': ''},
 'Identify': {'level': 1,
              'classes': ['Wizard'],
              'description': "Reveals an item's magical properties or spells affecting a creature "
                             'or object.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': False,
              'ritual': True,
              'notable_requirements': 'Requires a pearl worth at least 100 gp (not consumed).'},
'Illusory Script': {'level': 1,
                     'classes': ['Wizard'],
                     'description': 'Conceals written information behind an illusion readable by '
                                    'chosen creatures.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': True,
                     'notable_requirements': ''},
 'Imprisonment': {'level': 9,
                  'classes': ['Wizard'],
                  'description': 'Traps a creature in a magical prison chosen from several '
                                 'long-lasting forms.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': 'Requires a special component worth at least 500 gp per '
                                          'Hit Die of the target.'},
 'Incendiary Cloud': {'level': 8,
                      'classes': ['Wizard'],
                      'description': 'Creates a moving cloud of fire that damages creatures within '
                                     'it.',
                      'conditions_inflicted': [],
                      'conditions_granted': [],
                      'concentration': True,
                      'ritual': False,
                      'notable_requirements': ''},
 'Inflict Wounds': {'level': 1,
                    'classes': ['Cleric'],
                    'description': 'A melee spell attack deals substantial necrotic damage.',
                    'conditions_inflicted': [],
                    'conditions_granted': [],
                    'concentration': False,
                    'ritual': False,
                    'notable_requirements': ''},
 'Insect Plague': {'level': 5,
                   'classes': ['Cleric'],
                   'description': 'Summons biting insects that damage creatures and heavily '
                                  'obscure an area.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': True,
                   'ritual': False,
                   'notable_requirements': ''},
 'Invisibility': {'level': 2,
                  'classes': ['Wizard'],
                  'description': 'Makes a creature and carried gear invisible until the effect '
                                 'ends or it attacks or casts a spell.',
                  'conditions_inflicted': [],
                  'conditions_granted': ['Invisible'],
                  'concentration': True,
                  'ritual': False,
                  'notable_requirements': ''},
 'Jump': {'level': 1,
          'classes': ['Wizard'],
          'description': "Triples a creature's jumping distance for a short time.",
          'conditions_inflicted': [],
          'conditions_granted': [],
          'concentration': False,
          'ritual': False,
          'notable_requirements': ''},
 'Knock': {'level': 2,
           'classes': ['Wizard'],
           'description': 'Opens or unlocks a secured object, making a loud sound.',
           'conditions_inflicted': [],
           'conditions_granted': [],
           'concentration': False,
           'ritual': False,
           'notable_requirements': ''},
 'Legend Lore': {'level': 5,
                 'classes': ['Wizard', 'Cleric'],
                 'description': 'Reveals significant information about a legendary person, place, '
                                'or object.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': 'Requires costly incense and ivory strips; some materials '
                                         'are consumed.'},
 "Leomund's Secret Chest": {'level': 4,
                            'classes': ['Wizard'],
                            'description': 'Hides a specially prepared chest in the Ethereal Plane '
                                           'until recalled.',
                            'conditions_inflicted': [],
                            'conditions_granted': [],
                            'concentration': False,
                            'ritual': False,
                            'notable_requirements': 'Requires a costly crafted chest (at least '
                                                    '5,000 gp) and miniature replica (at least 50 '
                                                    'gp).'},
"Leomund's Tiny Hut": {'level': 3,
                        'classes': ['Wizard'],
                        'description': 'Creates a protective dome that shelters designated '
                                       'creatures from outside intrusion.',
                        'conditions_inflicted': [],
                        'conditions_granted': [],
                        'concentration': False,
                        'ritual': True,
                        'notable_requirements': ''},
 'Lesser Restoration': {'level': 2,
                        'classes': ['Cleric'],
                        'description': 'Ends one disease or one of several conditions affecting a '
                                       'creature.',
                        'conditions_inflicted': [],
                        'conditions_granted': [],
                        'concentration': False,
                        'ritual': False,
                        'notable_requirements': ''},
 'Levitate': {'level': 2,
              'classes': ['Wizard'],
              'description': 'Raises a creature or object vertically, potentially suspending an '
                             'unwilling target.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': True,
              'ritual': False,
              'notable_requirements': ''},
 'Light': {'level': 0,
           'classes': ['Wizard', 'Cleric'],
           'description': 'Makes an object glow, illuminating its surroundings.',
           'conditions_inflicted': [],
           'conditions_granted': [],
           'concentration': False,
           'ritual': False,
           'notable_requirements': ''},
 'Lightning Bolt': {'level': 3,
                    'classes': ['Wizard'],
                    'description': 'A straight line of lightning deals damage with a Dexterity '
                                   'save for half.',
                    'conditions_inflicted': [],
                    'conditions_granted': [],
                    'concentration': False,
                    'ritual': False,
                    'notable_requirements': ''},
 'Locate Creature': {'level': 4,
                     'classes': ['Wizard', 'Cleric'],
                     'description': 'Senses the direction of a familiar creature within range, '
                                    'subject to barriers.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''},
 'Locate Object': {'level': 2,
                   'classes': ['Wizard', 'Cleric'],
                   'description': 'Senses the direction of a familiar object within range.',
                   'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': True,
                   'ritual': False,
                   'notable_requirements': ''},
 'Longstrider': {'level': 1,
                 'classes': ['Wizard'],
                 'description': "Increases a creature's movement speed without requiring "
                                'concentration.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
                 'ritual': False,
                 'notable_requirements': ''},
 'Mage Armor': {'level': 1,
                'classes': ['Wizard'],
                'description': 'Sets the base AC of an unarmoured target to 13 plus Dexterity '
                               'modifier.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': False,
                'ritual': False,
                'notable_requirements': ''},
'Magic Circle': {'level': 3,
                 'classes': ['Wizard', 'Cleric'],
'description': 'Creates a ward against certain supernatural creature types and '
               'restricts their movement.',
'conditions_inflicted': [],
'conditions_granted': [],
'concentration': False,
'ritual': False,
'notable_requirements': 'Requires holy water or powdered silver and iron worth '
                        'at least 100 gp, consumed.'},
'Magic Jar': {'level': 6,
              'classes': ['Wizard'],
              'description': 'Transfers your soul into a container, allowing possession of '
                             'another humanoid body.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': False,
              'ritual': False,
              'notable_requirements': 'Requires a gem, crystal, reliquary, or similar container '
                                      'worth at least 500 gp.'},
'Magic Missile': {'level': 1,
                  'classes': ['Wizard'],
                  'description': 'Creates force darts that automatically hit visible targets '
                                 'unless blocked by special defences.',
                  'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
                  'ritual': False,
                  'notable_requirements': ''},
'Magic Mouth': {'level': 2,
                'classes': ['Wizard'],
                'description': 'Places a spoken message on an object that plays when a chosen '
                               'trigger occurs.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': False,
                'ritual': True,
                'notable_requirements': ''},
'Magic Weapon': {'level': 2,
                 'classes': ['Wizard'],
                 'description': 'Temporarily makes a nonmagical weapon magical with a bonus to '
                                'attack and damage.',
                 'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': True,
                 'ritual': False,
                 'notable_requirements': ''},
'Major Image': {'level': 3,
                'classes': ['Wizard'],
                'description': 'Creates a sensory illusion with sight, sound, smell, and '
                               'temperature.',
                'conditions_inflicted': [],
                'conditions_granted': [],
                'concentration': True,
                'ritual': False,
                'notable_requirements': ''},
'Mass Cure Wounds': {'level': 5,
                     'classes': ['Cleric'],
                     'description': 'Restores hit points to multiple creatures within an area.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''},
'Mass Heal': {'level': 9,
              'classes': ['Cleric'],
              'description': 'Distributes a huge pool of healing among creatures and cures '
                             'certain conditions.',
              'conditions_inflicted': [],
              'conditions_granted': [],
              'concentration': False,
              'ritual': False,
              'notable_requirements': ''},
'Mass Healing Word': {'level': 3,
                      'classes': ['Cleric'],
                      'description': 'Heals multiple creatures at range as a bonus action.',
                      'conditions_inflicted': [],
                      'conditions_granted': [],
                      'concentration': False,
                      'ritual': False,
                      'notable_requirements': ''},
'Mass Suggestion': {'level': 6,
                    'classes': ['Wizard'],
                    'description': 'Influences multiple creatures to follow a plausible course of '
                                   'action for an extended time.',
                    'conditions_inflicted': [],
                    'conditions_granted': [],
                    'concentration': False,
                    'ritual': False,
                    'notable_requirements': ''},
'Maze': {'level': 8,
         'classes': ['Wizard'],
         'description': 'Banishes a creature into an extradimensional labyrinth it must escape.',
         'conditions_inflicted': [],
         'conditions_granted': [],
         'concentration': True,
         'ritual': False,
         'notable_requirements': ''},
'Meld into Stone': {'level': 3,
                    'classes': ['Cleric'],
                    'description': 'Allows you to merge into a large stone object for shelter.',
                    'conditions_inflicted': [],
                    'conditions_granted': [],
                    'concentration': False,
                    'ritual': True,
                    'notable_requirements': ''},
"Melf's Acid Arrow": {'level': 2,
                      'classes': ['Wizard'],
                      'description': 'An acid projectile deals damage on a hit or partial damage '
                                     'on a miss, with lingering acid.',
                      'conditions_inflicted': [],
                      'conditions_granted': [],
                      'concentration': False,
                      'ritual': False,
                      'notable_requirements': ''},
'Mending': {'level': 0,
            'classes': ['Wizard', 'Cleric'],
            'description': 'Repairs a small break or tear in an object after a minute of casting.',
            'conditions_inflicted': [],
            'conditions_granted': [],
            'concentration': False,
            'ritual': False,
            'notable_requirements': ''},
'Mage Hand': {
    'level': 0,
    'classes': ['Wizard'],
    'description': (
        'Creates a spectral hand that can manipulate objects '
        'within 30 feet. The hand cannot attack, activate '
        'magic items, or carry more than 10 pounds.'
    ),
    'conditions_inflicted': [],
    'conditions_granted': [],
    'concentration': False,
    'ritual': False,
    'notable_requirements': ''
},
'Message': {'level': 0,
            'classes': ['Wizard'],
            'description': 'Whispers a message to a distant creature, which can whisper a reply.',
    'conditions_inflicted': [],
            'conditions_granted': [],
            'concentration': False,
    'ritual': False,
            'notable_requirements': ''},
'Meteor Swarm': {'level': 9,
                 'classes': ['Wizard'],
                 'description': 'Strikes several enormous areas with devastating fire and bludgeoning damage.',
    'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
    'ritual': False,
                 'notable_requirements': ''},
'Mind Blank': {'level': 8,
               'classes': ['Wizard'],
               'description': 'Shields a creature against psychic damage, mind reading, and certain magical influences.',
    'conditions_inflicted': [],
               'conditions_granted': [],
               'concentration': False,
    'ritual': False,
               'notable_requirements': ''},
'Minor Illusion': {'level': 0,
                   'classes': ['Wizard'],
                   'description': 'Creates a simple sound or image to distract or mislead observers.',
    'conditions_inflicted': [],
                   'conditions_granted': [],
                   'concentration': False,
    'ritual': False,
                   'notable_requirements': ''},
'Mirage Arcane': {'level': 7,
                  'classes': ['Wizard'],
                  'description': 'Transforms the apparent and tactile qualities of a large landscape.',
    'conditions_inflicted': [],
                  'conditions_granted': [],
                  'concentration': False,
    'ritual': False,
                  'notable_requirements': ''},
'Mirror Image': {'level': 2,
                 'classes': ['Wizard'],
                 'description': 'Creates illusory duplicates that can intercept incoming attacks.',
    'conditions_inflicted': [],
                 'conditions_granted': [],
                 'concentration': False,
    'ritual': False,
                 'notable_requirements': ''},
'Mislead': {'level': 5,
            'classes': ['Wizard'],
            'description': 'Makes you invisible while an illusory duplicate appears and can be controlled.',
    'conditions_inflicted': [],
            'conditions_granted': ['Invisible'],
            'concentration': True,
    'ritual': False, 'notable_requirements': ''},
'Misty Step': {
    'level': 2,
    'classes': ['Wizard'],
    'description': 'Teleports you a short distance to an unoccupied space you can see.',
    'conditions_inflicted': [],
    'conditions_granted': [],
    'concentration': False,
    'ritual': False,
    'notable_requirements': '',
},

'Modify Memory': {
    'level': 5,
    'classes': ['Wizard'],
    'description': (
        "Changes a creature's recollection of a recent event after a failed Wisdom "
        'save.'
    ),
    'conditions_inflicted': ['Charmed', 'Incapacitated'],
    'conditions_granted': [],
    'concentration': True,
    'ritual': False,
    'notable_requirements': '',
},
                 "Mordenkainen's Faithful Hound": {
                     'level': 4,
                     'classes': ['Wizard'],
                     'description': 'Creates an invisible watchdog that detects and attacks nearby intruders.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 "Mordenkainen's Magnificent Mansion": {
                     'level': 7,
                     'classes': ['Wizard'],
                     'description': 'Creates a secure extradimensional mansion with servants and provisions.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 "Mordenkainen's Private Sanctum": {
                     'level': 4,
                     'classes': ['Wizard'],
                     'description': (
                         'Wards an area against sound, vision, teleportation, and divination as '
                         'configured.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 "Mordenkainen's Sword": {
                     'level': 7,
                     'classes': ['Wizard'],
                     'description': 'Summons a floating sword of force that attacks creatures you designate.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': 'Requires a miniature platinum sword worth at least 250 gp.',
                 },

                 'Move Earth': {
                     'level': 6,
                     'classes': ['Wizard'],
                     'description': 'Gradually reshapes an area of natural earth, soil, sand, or clay.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Nondetection': {
                     'level': 3,
                     'classes': ['Wizard'],
                     'description': (
                         'Conceals a creature or object from divination magic and magical scrying '
                         'sensors.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires diamond dust worth at least 25 gp, consumed.',
                 },

                 "Nystul's Magic Aura": {
                     'level': 2,
                     'classes': ['Wizard'],
                     'description': (
                         "Disguises a target's magical aura or apparent creature type against "
                         'divination.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 "Otiluke's Freezing Sphere": {
                     'level': 6,
                     'classes': ['Wizard'],
                     'description': 'Creates a large freezing blast that can also freeze water.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 "Otiluke's Resilient Sphere": {
                     'level': 4,
                     'classes': ['Wizard'],
                     'description': 'Traps a creature or object inside a nearly indestructible force sphere.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 "Otto's Irresistible Dance": {
                     'level': 6,
                     'classes': ['Wizard'],
                     'description': (
                         'Forces a creature to dance, hindering movement and making it vulnerable to '
                         'attacks.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Passwall': {
                     'level': 5,
                     'classes': ['Wizard'],
                     'description': 'Opens a temporary passage through a suitable solid surface.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Phantasmal Force': {
                     'level': 2,
                     'classes': ['Wizard'],
                     'description': (
                         "Creates a convincing illusion in one creature's mind that can cause psychic "
                         'damage.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Phantasmal Killer': {
                     'level': 4,
                     'classes': ['Wizard'],
                     'description': (
                         "Conjures a creature's deepest fear, potentially frightening it and causing "
                         'psychic damage.'
                     ),
                     'conditions_inflicted': ['Frightened'],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Phantom Steed': {
                     'level': 3,
                     'classes': ['Wizard'],
                     'description': 'Conjures a fast, horse-like mount for travel.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': True,
                     'notable_requirements': '',
                 },

                 'Planar Ally': {
                     'level': 6,
                     'classes': ['Cleric'],
                     'description': (
                         'Requests assistance from a celestial, elemental, or fiend sent by a higher '
                         'power.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Planar Binding': {
                     'level': 5,
                     'classes': ['Wizard', 'Cleric'],
                     'description': (
                         'Attempts to bind a celestial, elemental, fey, or fiend into service for a '
                         'duration.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires a jewel worth at least 1,000 gp, consumed.',
                 },

                 'Plane Shift': {
                     'level': 7,
                     'classes': ['Wizard', 'Cleric'],
                     'description': (
                         'Transports creatures to another plane or attempts to banish an unwilling '
                         'target.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires a forked metal rod worth at least 250 gp, attuned to a plane.',
                 },

                 'Poison Spray': {
                     'level': 0,
                     'classes': ['Wizard'],
                     'description': 'Releases poisonous gas that deals damage on a failed Constitution save.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Polymorph': {
                     'level': 4,
                     'classes': ['Wizard'],
                     'description': (
                         'Transforms a creature into a beast, replacing its game statistics while '
                         'transformed.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Power Word Kill': {
                     'level': 9,
                     'classes': ['Wizard'],
                     'description': (
                         'Instantly kills a creature below a hit-point threshold without a saving '
                         'throw.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Power Word Stun': {
                     'level': 8,
                     'classes': ['Wizard'],
                     'description': 'Stuns a creature below a hit-point threshold until it succeeds on a save.',
                     'conditions_inflicted': ['Stunned'],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Prayer of Healing': {
                     'level': 2,
                     'classes': ['Cleric'],
                     'description': (
                         'Heals several creatures after a longer casting time; unsuitable for quick '
                         'combat healing.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Prestidigitation': {
                     'level': 0,
                     'classes': ['Wizard'],
                     'description': (
                         'Performs minor magical tricks, such as cleaning, warming, or creating '
                         'sensory effects.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Prismatic Spray': {
                     'level': 7,
                     'classes': ['Wizard'],
                     'description': 'Fires coloured rays with unpredictable elemental or other powerful effects.',
                     'conditions_inflicted': ['Blinded'],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Prismatic Wall': {
                     'level': 9,
                     'classes': ['Wizard'],
                     'description': (
                         'Creates a multilayered wall of dangerous coloured magic that can blind '
                         'nearby viewers.'
                     ),
                     'conditions_inflicted': ['Blinded'],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Programmed Illusion': {
                     'level': 6,
                     'classes': ['Wizard'],
                     'description': 'Creates a complex illusion that activates when a chosen trigger occurs.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Project Image': {
                     'level': 7,
                     'classes': ['Wizard'],
                     'description': (
                         'Creates an illusory duplicate you can see and hear through at great '
                         'distance.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Protection from Energy': {
                     'level': 3,
                     'classes': ['Wizard', 'Cleric'],
                     'description': 'Gives a creature resistance to one chosen elemental damage type.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Protection from Evil and Good': {
                     'level': 1,
                     'classes': ['Wizard', 'Cleric'],
                     'description': (
                         'Protects against several supernatural creature types, hindering their '
                         'attacks and certain effects.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Protection from Poison': {
                     'level': 2,
                     'classes': ['Cleric'],
                     'description': 'Neutralises one poison and protects a creature against poison effects.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Purify Food and Drink': {
                     'level': 1,
                     'classes': ['Cleric'],
                     'description': 'Removes poison and disease from nonmagical food and drink.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': True,
                     'notable_requirements': '',
                 },

                 'Raise Dead': {
                     'level': 5,
                     'classes': ['Cleric'],
                     'description': (
                         'Returns a creature dead for no more than ten days to life, with '
                         'restrictions and costly diamonds.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires a diamond worth at least 500 gp, consumed.',
                 },

                 "Rary's Telepathic Bond": {
                     'level': 5,
                     'classes': ['Wizard'],
                     'description': (
                         'Links willing creatures telepathically across great distances while on the '
                         'same plane.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': True,
                     'notable_requirements': '',
                 },

                 'Ray of Enfeeblement': {
                     'level': 2,
                     'classes': ['Wizard'],
                     'description': "Weakens a target's Strength-based weapon attacks while concentration lasts.",
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Ray of Frost': {
                     'level': 0,
                     'classes': ['Wizard'],
                     'description': 'A ranged spell attack deals cold damage and briefly slows a target.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Ray of Sickness': {
                     'level': 1,
                     'classes': ['Wizard'],
                     'description': 'A ranged spell attack deals poison damage and may poison the target.',
                     'conditions_inflicted': ['Poisoned'],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Regenerate': {
                     'level': 7,
                     'classes': ['Cleric'],
                     'description': 'Restores hit points over time and can regrow lost body parts.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Remove Curse': {
                     'level': 3,
                     'classes': ['Wizard', 'Cleric'],
                     'description': 'Ends curses on a creature or object, subject to special item rules.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Resistance': {
                     'level': 0,
                     'classes': ['Cleric'],
                     'description': (
                         'Adds a d4 to one saving throw made by a willing creature while you '
                         'concentrate.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Resurrection': {
                     'level': 7,
                     'classes': ['Cleric'],
                     'description': (
                         'Returns a creature dead for up to a century to life, subject to important '
                         'restrictions.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires a diamond worth at least 1,000 gp, consumed.',
                 },

                 'Reverse Gravity': {
                     'level': 7,
                     'classes': ['Wizard'],
                     'description': 'Reverses gravity in a large area, sending creatures and objects upward.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Revivify': {
                     'level': 3,
                     'classes': ['Cleric'],
                     'description': (
                         'Returns a creature that died within the last minute to life, using costly '
                         'diamonds.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires diamonds worth at least 300 gp, consumed.',
                 },

                 'Rope Trick': {
                     'level': 2,
                     'classes': ['Wizard'],
                     'description': 'Creates a small extradimensional refuge accessed by climbing a rope.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Sacred Flame': {
                     'level': 0,
                     'classes': ['Cleric'],
                     'description': (
                         'Radiant energy damages a creature that fails a Dexterity save, ignoring '
                         'cover bonuses.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Sanctuary': {
                     'level': 1,
                     'classes': ['Cleric'],
                     'description': (
                         'Protects a creature by forcing attackers to make Wisdom saves before '
                         'targeting it.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Scorching Ray': {
                     'level': 2,
                     'classes': ['Wizard'],
                     'description': 'Fires multiple rays of fire, each requiring its own spell attack.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Scrying': {
                     'level': 5,
                     'classes': ['Wizard', 'Cleric'],
                     'description': (
                         'Creates a remote sensor to watch and hear a target that fails a Wisdom '
                         'save.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': 'Requires a focus worth at least 1,000 gp (not consumed).',
                 },

                 'See Invisibility': {
                     'level': 2,
                     'classes': ['Wizard'],
                     'description': (
                         'Lets you see invisible creatures and objects and perceive into the Ethereal '
                         'Plane.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Seeming': {
                     'level': 5,
                     'classes': ['Wizard'],
                     'description': 'Disguises the appearance of multiple creatures for several hours.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Sending': {
                     'level': 3,
                     'classes': ['Wizard', 'Cleric'],
                     'description': (
                         'Delivers a short message across any distance and may receive an immediate '
                         'reply.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Sequester': {
                     'level': 7,
                     'classes': ['Wizard'],
                     'description': (
                         'Hides a creature or object from detection and suspends a willing creature '
                         'in time.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires gem dust worth at least 5,000 gp, consumed.',
                 },

                 'Shapechange': {
                     'level': 9,
                     'classes': ['Wizard'],
                     'description': (
                         'Lets you assume different creature forms while retaining key mental '
                         'abilities.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Shatter': {
                     'level': 2,
                     'classes': ['Wizard'],
                     'description': 'A loud burst deals thunder damage in an area and harms vulnerable objects.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Shield': {
                     'level': 1,
                     'classes': ['Wizard'],
                     'description': 'A reaction grants +5 AC until your next turn and blocks Magic Missile.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Shield of Faith': {
                     'level': 1,
                     'classes': ['Cleric'],
                     'description': 'Gives a creature +2 AC while you maintain concentration.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Shocking Grasp': {
                     'level': 0,
                     'classes': ['Wizard'],
                     'description': (
                         'A melee spell attack deals lightning damage and prevents the target taking '
                         'reactions briefly.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Silence': {
                     'level': 2,
                     'classes': ['Cleric'],
                     'description': (
                         'Creates an area without sound, preventing spells requiring verbal '
                         'components there.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': True,
                     'notable_requirements': '',
                 },

                 'Silent Image': {
                     'level': 1,
                     'classes': ['Wizard'],
                     'description': 'Creates a visual illusion that can move within its allowed area.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Simulacrum': {
                     'level': 7,
                     'classes': ['Wizard'],
                     'description': (
                         "Creates a duplicate of a beast or humanoid with many of the original's "
                         'abilities.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': (
                         'Requires powdered ruby worth at least 1,500 gp, consumed, plus other '
                         'materials.'
                     ),
                 },

                 'Sleep': {
                     'level': 1,
                     'classes': ['Wizard'],
                     'description': (
                         'Puts creatures with sufficiently low combined hit points into magical '
                         'sleep.'
                     ),
                     'conditions_inflicted': ['Unconscious'],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Sleet Storm': {
                     'level': 3,
                     'classes': ['Wizard'],
                     'description': (
                         'Creates freezing precipitation that obscures an area and may knock '
                         'creatures down.'
                     ),
                     'conditions_inflicted': ['Prone'],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Slow': {
                     'level': 3,
                     'classes': ['Wizard'],
                     'description': "Hampers creatures' movement, AC, reactions, attacks, and spellcasting.",
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': '',
                 },

                 'Spare the Dying': {
                     'level': 0,
                     'classes': ['Cleric'],
                     'description': (
                         'Stabilises a living creature at zero hit points without restoring hit '
                         'points.'
                     ),
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': '',
                 },
 'Speak with Dead': {
        'level': 3,
        'classes': ['Cleric'],
        'description': 'Allows a corpse with a mouth to answer a limited number of questions.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Spider Climb': {
        'level': 2,
        'classes': ['Wizard'],
        'description': 'Allows movement on walls and ceilings while leaving hands free.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Spirit Guardians': {
        'level': 3,
        'classes': ['Cleric'],
        'description': (
            'Creates a moving aura of spirits that damages selected creatures and slows '
            'them.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Spiritual Weapon': {
        'level': 2,
        'classes': ['Cleric'],
        'description': (
            'Summons a floating weapon that attacks using your bonus action without '
            'concentration.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Stinking Cloud': {
        'level': 3,
        'classes': ['Wizard'],
        'description': (
            "Fills an area with nauseating vapour that can waste affected creatures' "
            'actions.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Stone Shape': {
        'level': 4,
        'classes': ['Wizard', 'Cleric'],
        'description': 'Reshapes a volume of stone into a chosen form, including simple openings.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Stoneskin': {
        'level': 4,
        'classes': ['Wizard'],
        'description': 'Gives resistance to nonmagical bludgeoning, piercing, and slashing damage.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': 'Requires diamond dust worth at least 100 gp, consumed.',
    },

    'Suggestion': {
        'level': 2,
        'classes': ['Wizard'],
        'description': (
            'Magically persuades a creature that fails a Wisdom save to follow a '
            'reasonable-sounding course.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Sunbeam': {
        'level': 6,
        'classes': ['Wizard'],
        'description': 'Projects a repeated beam of radiant light that can blind creatures.',
        'conditions_inflicted': ['Blinded'],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Sunburst': {
        'level': 8,
        'classes': ['Wizard'],
        'description': 'Creates an intense radiant flash that damages and may blind creatures.',
        'conditions_inflicted': ['Blinded'],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Symbol': {
        'level': 7,
        'classes': ['Wizard', 'Cleric'],
        'description': (
            'Sets a powerful magical trap with effects such as fear, sleep, pain, or '
            'stunning.'
        ),
        'conditions_inflicted': ['Frightened', 'Stunned', 'Unconscious', 'Incapacitated'],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': 'Requires costly materials worth at least 1,000 gp, consumed.',
    },

    "Tasha's Hideous Laughter": {
        'level': 1,
        'classes': ['Wizard'],
        'description': 'A Wisdom save may leave a creature laughing, prone, and unable to act.',
        'conditions_inflicted': ['Prone', 'Incapacitated'],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Telekinesis': {
        'level': 5,
        'classes': ['Wizard'],
        'description': 'Moves or manipulates creatures and objects through sustained magical force.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Telepathy': {
        'level': 8,
        'classes': ['Wizard'],
        'description': (
            'Establishes a long-distance mental link allowing communication across '
            'language barriers.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Teleport': {
        'level': 7,
        'classes': ['Wizard'],
        'description': (
            'Instantly transports you and companions to a destination, with risk '
            'depending on familiarity.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Teleportation Circle': {
        'level': 5,
        'classes': ['Wizard'],
        'description': 'Creates a temporary portal to a known permanent teleportation circle.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': 'Requires 50 gp of rare chalks and inks, consumed.',
    },

    "Tenser's Floating Disk": {
        'level': 1,
        'classes': ['Wizard'],
        'description': 'Creates a hovering platform that follows you and carries equipment.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': True,
        'notable_requirements': '',
    },

    'Thaumaturgy': {
        'level': 0,
        'classes': ['Cleric'],
        'description': (
            'Creates minor divine signs, such as booming voice, trembling ground, or '
            'changing flame colour.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Thunderwave': {
        'level': 1,
        'classes': ['Wizard'],
        'description': 'A thunderous burst damages and pushes creatures away from you.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Time Stop': {
        'level': 9,
        'classes': ['Wizard'],
        'description': 'Grants several extra turns while other creatures appear frozen in time.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Tongues': {
        'level': 3,
        'classes': ['Wizard', 'Cleric'],
        'description': (
            'Allows a creature to understand spoken languages and be understood by '
            'listeners.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'True Polymorph': {
        'level': 9,
        'classes': ['Wizard'],
        'description': (
            'Transforms a creature or object into another creature or object, '
            'potentially permanently.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'True Resurrection': {
        'level': 9,
        'classes': ['Cleric'],
        'description': (
            'Restores a long-dead creature to life, even without its original body in '
            'some cases.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': 'Requires diamonds worth at least 25,000 gp, consumed.',
    },

    'True Seeing': {
        'level': 6,
        'classes': ['Wizard', 'Cleric'],
        'description': (
            'Grants truesight to perceive illusions, invisibility, and the Ethereal '
            'Plane.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': 'Requires an ointment for the eyes worth at least 25 gp, consumed.',
    },

    'True Strike': {
        'level': 0,
        'classes': ['Wizard'],
        'description': (
            'Helps you aim at a target, granting advantage on your first attack against '
            'it next turn.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Unseen Servant': {
        'level': 1,
        'classes': ['Wizard'],
        'description': 'Creates an invisible, mindless force to perform simple tasks.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': True,
        'notable_requirements': '',
    },

    'Vampiric Touch': {
        'level': 3,
        'classes': ['Wizard'],
        'description': (
            'A melee spell attack deals necrotic damage and restores some of your hit '
            'points.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Wall of Fire': {
        'level': 4,
        'classes': ['Wizard'],
        'description': (
            'Creates a burning wall that damages creatures on one chosen side or passing '
            'through it.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Wall of Force': {
        'level': 5,
        'classes': ['Wizard'],
        'description': 'Forms an invisible barrier that blocks physical passage and resists damage.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Wall of Ice': {
        'level': 6,
        'classes': ['Wizard'],
        'description': (
            'Raises a wall of ice that damages creatures and leaves freezing mist when '
            'broken.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Wall of Stone': {
        'level': 5,
        'classes': ['Wizard'],
        'description': (
            'Raises a stone barrier that can become permanent if concentration lasts '
            'long enough.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Warding Bond': {
        'level': 2,
        'classes': ['Cleric'],
        'description': 'Gives an ally defensive bonuses while you share damage it receives.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Water Breathing': {
        'level': 3,
        'classes': ['Wizard'],
        'description': 'Lets several willing creatures breathe underwater for a day.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': True,
        'notable_requirements': '',
    },

    'Water Walk': {
        'level': 3,
        'classes': ['Cleric'],
        'description': 'Allows several willing creatures to walk on liquid surfaces.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': True,
        'notable_requirements': '',
    },

    'Web': {
        'level': 2,
        'classes': ['Wizard'],
        'description': 'Fills an area with sticky webs that can restrain creatures and be burned.',
        'conditions_inflicted': ['Restrained'],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Weird': {
        'level': 9,
        'classes': ['Wizard'],
        'description': (
            'Creates terrifying illusions that can frighten targets and repeatedly harm '
            'them.'
        ),
        'conditions_inflicted': ['Frightened'],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Wish': {
        'level': 9,
        'classes': ['Wizard'],
        'description': (
            'Duplicates many lower-level spells or attempts a greater reality-altering '
            'effect at a cost.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Witch Bolt': {
        'level': 1,
        'classes': ['Wizard'],
        'description': (
            'A lightning attack connects you to a target, allowing repeat damage while '
            'the link lasts.'
        ),
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': True,
        'ritual': False,
        'notable_requirements': '',
    },

    'Word of Recall': {
        'level': 6,
        'classes': ['Cleric'],
        'description': 'Teleports you and willing companions to a previously designated sanctuary.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

    'Zone of Truth': {
        'level': 2,
        'classes': ['Cleric'],
        'description': 'Creatures that fail Charisma saves cannot deliberately lie within the zone.',
        'conditions_inflicted': [],
        'conditions_granted': [],
        'concentration': False,
        'ritual': False,
        'notable_requirements': '',
    },

                 # Missing Druid cantrips
                 'Druidcraft': {
                     'level': 0,
                     'classes': ['Druid'],
                     'description': 'Creates minor nature effects, such as predicting weather, making flowers bloom, or lighting small flames.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Produce Flame': {
                     'level': 0,
                     'classes': ['Druid'],
                     'description': 'Creates a flame in your hand that sheds light or can be hurled to deal fire damage.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Shillelagh': {
                     'level': 0,
                     'classes': ['Druid'],
                     'description': 'Empowers a club or quarterstaff so attacks can use Wisdom and deal magical bludgeoning damage.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': 'Requires a club or quarterstaff.'
                 },
                 'Thorn Whip': {
                     'level': 0,
                     'classes': ['Druid'],
                     'description': 'Makes a thorny vine attack a creature at range, dealing piercing damage and possibly pulling it closer.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },

                 # Missing Cleric domain-spell metadata
                 'Animal Friendship': {
                     'level': 1,
                     'classes': ['Bard', 'Druid', 'Ranger'],
                     'description': 'Charms a beast with Intelligence 3 or lower that fails a Wisdom saving throw.',
                     'conditions_inflicted': ['Charmed'],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Barkskin': {
                     'level': 2,
                     'classes': ['Druid', 'Ranger'],
                     'description': 'Makes a willing creature’s AC at least 16 for the duration.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Call Lightning': {
                     'level': 3,
                     'classes': ['Druid'],
                     'description': 'Creates a storm cloud from which you repeatedly call down damaging lightning bolts.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 "Crusader's Mantle": {
                     'level': 3,
                     'classes': ['Paladin'],
                     'description': 'Creates an aura that adds radiant damage to friendly creatures’ weapon attacks.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Daylight': {
                     'level': 3,
                     'classes': ['Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer'],
                     'description': 'Creates a large sphere of bright light that can dispel some magical darkness.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Death Ward': {
                     'level': 4,
                     'classes': ['Cleric', 'Paladin'],
                     'description': 'Protects a creature once from dropping to zero hit points or an instant-death effect.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Destructive Wave': {
                     'level': 5,
                     'classes': ['Paladin'],
                     'description': 'Unleashes thunder and radiant or necrotic damage around you, potentially knocking enemies prone.',
                     'conditions_inflicted': ['Prone'],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Divine Favor': {
                     'level': 1,
                     'classes': ['Paladin'],
                     'description': 'Makes your weapon attacks deal extra radiant damage while you concentrate.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Dominate Beast': {
                     'level': 4,
                     'classes': ['Druid', 'Sorcerer'],
                     'description': 'Charms a beast and lets you direct its actions if it fails a Wisdom saving throw.',
                     'conditions_inflicted': ['Charmed'],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Faerie Fire': {
                     'level': 1,
                     'classes': ['Bard', 'Druid'],
                     'description': 'Outlines creatures and objects in light, helping attackers hit affected targets.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Grasping Vine': {
                     'level': 4,
                     'classes': ['Druid', 'Ranger'],
                     'description': 'Summons a vine that can pull a creature closer if it fails a Dexterity saving throw.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Pass without Trace': {
                     'level': 2,
                     'classes': ['Druid', 'Ranger'],
                     'description': 'Grants nearby allies a +10 bonus to Dexterity (Stealth) checks and prevents ordinary tracking.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Plant Growth': {
                     'level': 3,
                     'classes': ['Bard', 'Druid', 'Ranger'],
                     'description': 'Causes plants to overgrow an area and impede movement, or enrich crops over a longer casting.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Speak with Animals': {
                     'level': 1,
                     'classes': ['Bard', 'Druid', 'Ranger'],
                     'description': 'Lets you understand and communicate verbally with beasts for a short time.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': True,
                     'notable_requirements': ''
                 },
                 'Spike Growth': {
                     'level': 2,
                     'classes': ['Druid', 'Ranger'],
                     'description': 'Creates hidden spikes over an area that damage creatures moving through it.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Tree Stride': {
                     'level': 5,
                     'classes': ['Druid', 'Ranger'],
                     'description': 'Allows travel between nearby living trees of the same kind while concentrating.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 'Wind Wall': {
                     'level': 3,
                     'classes': ['Druid', 'Ranger'],
                     'description': 'Creates a wall of strong wind that pushes vapours away and blocks many projectiles.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },
                 # Missing Wizard spells

                 'Darkvision': {
                     'level': 2,
                     'classes': ['Druid', 'Ranger', 'Sorcerer', 'Wizard'],
                     'description': 'Grants a willing creature darkvision out to 60 feet for 8 hours.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },

                 'Enlarge/Reduce': {
                     'level': 2,
                     'classes': ['Sorcerer', 'Wizard'],
                     'description': 'Makes a creature or object grow or shrink, affecting its size, weight, and abilities.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },

                 'Expeditious Retreat': {
                     'level': 1,
                     'classes': ['Sorcerer', 'Warlock', 'Wizard'],
                     'description': 'Allows you to take the Dash action as a bonus action while concentrating.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },

                 'False Life': {
                     'level': 1,
                     'classes': ['Sorcerer', 'Wizard'],
                     'description': 'Bolsters yourself with necromantic energy, granting 1d4 + 4 temporary hit points.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },

                 'Fear': {
                     'level': 3,
                     'classes': ['Bard', 'Sorcerer', 'Warlock', 'Wizard'],
                     'description': 'Projects a terrifying illusion that frightens creatures, causing them to drop held items and flee.',
                     'conditions_inflicted': ['Frightened'],
                     'conditions_granted': [],
                     'concentration': True,
                     'ritual': False,
                     'notable_requirements': ''
                 },

                 'Feather Fall': {
                     'level': 1,
                     'classes': ['Bard', 'Sorcerer', 'Wizard'],
                     'description': 'Slows the descent of up to five falling creatures, potentially preventing falling damage.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': False,
                     'notable_requirements': ''
                 },

                 'Find Familiar': {
                     'level': 1,
                     'classes': ['Wizard'],
                     'description': 'Summons a spirit in animal form that serves as your familiar and can assist with various tasks.',
                     'conditions_inflicted': [],
                     'conditions_granted': [],
                     'concentration': False,
                     'ritual': True,
                     'notable_requirements': 'Requires 10 gp worth of charcoal, incense, and herbs, consumed by fire in a brass brazier.'
                 },
                 }

spell_lists = {
    "Wizard": {},
    "Cleric": {}
}

for spell_name, spell_info in spell_details.items():

    spell_level = spell_info["level"]

    if spell_level == 0:
        continue

    for spell_class in spell_info["classes"]:

        if spell_class in spell_lists:

            if spell_level not in spell_lists[spell_class]:
                spell_lists[spell_class][spell_level] = []

            spell_lists[spell_class][spell_level].append(spell_name)

for class_spell_levels in spell_lists.values():
    for spells_at_level in class_spell_levels.values():
        spells_at_level.sort()

cleric_domain_spell_lists = {
    "Knowledge Domain": {
        1: ["Command", "Identify"],
        3: ["Augury", "Suggestion"],
        5: ["Nondetection", "Speak with Dead"],
        7: ["Arcane Eye", "Confusion"],
        9: ["Legend Lore", "Scrying"]
    },

    "Life Domain": {
        1: ["Bless", "Cure Wounds"],
        3: ["Lesser Restoration", "Spiritual Weapon"],
        5: ["Beacon of Hope", "Revivify"],
        7: ["Death Ward", "Guardian of Faith"],
        9: ["Mass Cure Wounds", "Raise Dead"]
    },

    "Light Domain": {
        1: ["Burning Hands", "Faerie Fire"],
        3: ["Flaming Sphere", "Scorching Ray"],
        5: ["Daylight", "Fireball"],
        7: ["Guardian of Faith", "Wall of Fire"],
        9: ["Flame Strike", "Scrying"]
    },

    "Nature Domain": {
        1: ["Animal Friendship", "Speak with Animals"],
        3: ["Barkskin", "Spike Growth"],
        5: ["Plant Growth", "Wind Wall"],
        7: ["Dominate Beast", "Grasping Vine"],
        9: ["Insect Plague", "Tree Stride"]
    },

    "Tempest Domain": {
        1: ["Fog Cloud", "Thunderwave"],
        3: ["Gust of Wind", "Shatter"],
        5: ["Call Lightning", "Sleet Storm"],
        7: ["Control Water", "Ice Storm"],
        9: ["Destructive Wave", "Insect Plague"]
    },

    "Trickery Domain": {
        1: ["Charm Person", "Disguise Self"],
        3: ["Mirror Image", "Pass without Trace"],
        5: ["Blink", "Dispel Magic"],
        7: ["Dimension Door", "Polymorph"],
        9: ["Dominate Person", "Modify Memory"]
    },

    "War Domain": {
        1: ["Divine Favor", "Shield of Faith"],
        3: ["Magic Weapon", "Spiritual Weapon"],
        5: ["Crusader's Mantle", "Spirit Guardians"],
        7: ["Freedom of Movement", "Stoneskin"],
        9: ["Flame Strike", "Hold Monster"]
    }
}

full_caster_spell_slots = {
    1: {1: 2},
    2: {1: 3},
    3: {1: 4, 2: 2},
    4: {1: 4, 2: 3},
    5: {1: 4, 2: 3, 3: 2},
    6: {1: 4, 2: 3, 3: 3},
    7: {1: 4, 2: 3, 3: 3, 4: 1},
    8: {1: 4, 2: 3, 3: 3, 4: 2},
    9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
    10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
    11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1},
    12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1},
    13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1},
    14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1},
    15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},
    16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},
    17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
    18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
    19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
    20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1}
}

third_caster_spell_slots = {
    3: {1: 2},
    4: {1: 3},
    7: {1: 4, 2: 2},
    10: {1: 4, 2: 3},
    13: {1: 4, 2: 3, 3: 2},
    16: {1: 4, 2: 3, 3: 3},
    19: {1: 4, 2: 3, 3: 3, 4: 1}
}

spell_schools_by_school = {
    "Abjuration": [
        "Alarm", "Arcane Lock", "Banishment",
        "Counterspell", "Dispel Magic", "Glyph of Warding",
        "Mage Armor", "Magic Circle",
        "Mordenkainen's Private Sanctum", "Nondetection",
        "Protection from Energy", "Protection from Evil and Good",
        "Remove Curse", "Shield", "Stoneskin"
    ],

    "Conjuration": [
        "Find Familiar",
        "Cloud of Daggers", "Conjure Minor Elementals",
        "Dimension Door", "Flaming Sphere", "Fog Cloud",
        "Grease", "Leomund's Secret Chest", "Misty Step",
        "Mordenkainen's Faithful Hound", "Sleet Storm",
        "Stinking Cloud", "Tenser's Floating Disk",
        "Unseen Servant", "Web"
    ],

    "Divination": [
        "Arcane Eye", "Clairvoyance", "Comprehend Languages",
        "Detect Magic", "Detect Thoughts", "Identify",
        "Locate Creature", "Locate Object",
        "See Invisibility", "Tongues"
    ],

    "Enchantment": [
        "Charm Person", "Confusion", "Crown of Madness",
        "Hold Person", "Sleep", "Suggestion",
        "Tasha's Hideous Laughter"
    ],

    "Evocation": [
        "Burning Hands", "Chromatic Orb", "Continual Flame",
        "Darkness", "Fire Shield", "Fireball", "Gust of Wind",
        "Ice Storm", "Leomund's Tiny Hut", "Lightning Bolt",
        "Magic Missile", "Melf's Acid Arrow",
        "Otiluke's Resilient Sphere", "Scorching Ray",
        "Sending", "Shatter", "Thunderwave",
        "Wall of Fire", "Witch Bolt"
    ],

    "Illusion": [
        "Fear",
        "Blur", "Color Spray", "Disguise Self",
        "Greater Invisibility", "Hallucinatory Terrain",
        "Hypnotic Pattern", "Illusory Script", "Invisibility",
        "Magic Mouth", "Major Image", "Mirror Image",
        "Nystul's Magic Aura", "Phantasmal Force",
        "Phantasmal Killer", "Phantom Steed", "Silent Image"
    ],

    "Necromancy": [
        "False Life",
        "Animate Dead", "Bestow Curse", "Blight",
        "Blindness/Deafness", "Gentle Repose",
        "Ray of Enfeeblement", "Ray of Sickness",
        "Vampiric Touch"
    ],

    "Transmutation": [
        "Darkvision", "Enlarge/Reduce",
        "Expeditious Retreat", "Feather Fall",
        "Alter Self", "Blink", "Control Water",
        "Fly", "Gaseous Form", "Haste", "Jump",
        "Knock", "Levitate", "Longstrider",
        "Magic Weapon", "Polymorph", "Rope Trick",
        "Slow", "Spider Climb", "Stone Shape",
        "Water Breathing"
    ]
}

spell_schools = {}

for school, spell_names in spell_schools_by_school.items():
    for spell_name in spell_names:
        spell_schools[spell_name] = school

missing_spell_schools = [
    spell_name
    for spell_level, spells in spell_lists["Wizard"].items()
    if spell_level <= 4
    for spell_name in spells
    if spell_name not in spell_schools
]

if missing_spell_schools:
    raise ValueError(
        f"Missing spell schools: {missing_spell_schools}"
    )

battle_master_manoeuvres = {
    "Commander's Strike": {
        "description": "Forgo one attack and use a bonus action to let an ally attack using their reaction, adding the superiority die to damage."
    },

    "Disarming Attack": {
        "description": "Add the superiority die to weapon damage. The target makes a Strength save or drops a held item."
    },

    "Distracting Strike": {
        "description": "Add the superiority die to weapon damage. The next attack by another creature against the target gains advantage before your next turn."
    },

    "Evasive Footwork": {
        "description": "While moving, add the superiority die roll to your AC until you stop moving."
    },

    "Feinting Attack": {
        "description": "Use a bonus action to gain advantage on your next attack this turn against a creature within 5 feet, adding the die to damage if it hits."
    },

    "Goading Attack": {
        "description": "Add the superiority die to weapon damage. A failed Wisdom save gives the target disadvantage on attacks against creatures other than you."
    },

    "Lunging Attack": {
        "description": "Increase the reach of a melee weapon attack by 5 feet on your turn, adding the superiority die to damage if it hits."
    },

    "Maneuvering Attack": {
        "description": "Add the superiority die to weapon damage. An ally can use their reaction to move up to half their speed without provoking an opportunity attack from the target."
    },

    "Menacing Attack": {
        "description": "Add the superiority die to weapon damage. A failed Wisdom save frightens the target until the end of your next turn."
    },

    "Parry": {
        "description": "Use your reaction when damaged by a melee attack to reduce the damage by the superiority die roll plus your Dexterity modifier."
    },

    "Precision Attack": {
        "description": "Add the superiority die roll to a weapon attack roll, before or after rolling but before the attack's effects are applied."
    },

    "Pushing Attack": {
        "description": "Add the superiority die to weapon damage. A Large or smaller target that fails a Strength save is pushed up to 15 feet."
    },

    "Rally": {
        "description": "Use a bonus action to grant an ally who can see or hear you temporary hit points equal to the superiority die roll plus your Charisma modifier."
    },

    "Riposte": {
        "description": "When a creature misses you with a melee attack, use your reaction to make a melee weapon attack, adding the die to damage if it hits."
    },

    "Sweeping Attack": {
        "description": "After hitting with a melee weapon attack, potentially damage a second nearby creature for an amount equal to the superiority die roll."
    },

    "Trip Attack": {
        "description": "Add the superiority die to weapon damage. A Large or smaller target that fails a Strength save falls prone."
    }
}

fighting_styles = {
    "Archery": {
        "description": "You gain a +2 bonus to attack rolls you make with ranged weapons."
    },
    "Defense": {
        "description": "While you are wearing armour, you gain a +1 bonus to AC."
    },
    "Dueling": {
        "description": "You gain a +2 damage bonus when wielding a melee weapon in one hand and no other weapons."
    },
    "Great Weapon Fighting": {
        "description": "You can reroll a 1 or 2 on eligible two-handed melee weapon damage dice."
    },
    "Protection": {
        "description": "While wielding a shield, you can use your reaction to impose disadvantage on an attack against another creature within 5 feet."
    },
    "Two-Weapon Fighting": {
        "description": "You can add your ability modifier to the damage of your second attack when two-weapon fighting."
    }
}

weapon_data = {
    "Club": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Light"],
        "damage": "1d4",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Dagger": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse", "Light", "Thrown"],
        "damage": "1d4",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Greatclub": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Two-Handed"],
        "damage": "1d8",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Handaxe": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Light", "Thrown"],
        "damage": "1d6",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Javelin": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Thrown"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Light Hammer": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Light", "Thrown"],
        "damage": "1d4",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Mace": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": [],
        "damage": "1d6",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Quarterstaff": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Versatile"],
        "damage": "1d6",
        "damage_type": "Bludgeoning",
        "versatile_damage": "1d8"
    },
    "Sickle": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Light"],
        "damage": "1d4",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Spear": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Thrown", "Versatile"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": "1d8"
    },

    # SIMPLE RANGED WEAPONS
    "Light Crossbow": {
        "category": "Simple Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Loading", "Two-Handed"],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Dart": {
        "category": "Simple Weapons",
        "attack_type": "Ranged",
        "properties": ["Finesse", "Thrown"],
        "damage": "1d4",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Shortbow": {
        "category": "Simple Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Two-Handed"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Sling": {
        "category": "Simple Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition"],
        "damage": "1d4",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },

    # MARTIAL MELEE WEAPONS
    "Battleaxe": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Versatile"],
        "damage": "1d8",
        "damage_type": "Slashing",
        "versatile_damage": "1d10"
    },
    "Flail": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": [],
        "damage": "1d8",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Glaive": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Reach", "Two-Handed"],
        "damage": "1d10",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Greataxe": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Two-Handed"],
        "damage": "1d12",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Greatsword": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Two-Handed"],
        "damage": "2d6",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Halberd": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Reach", "Two-Handed"],
        "damage": "1d10",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Lance": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Reach", "Special"],
        "damage": "1d12",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Longsword": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Versatile"],
        "damage": "1d8",
        "damage_type": "Slashing",
        "versatile_damage": "1d10"
    },
    "Maul": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Two-Handed"],
        "damage": "2d6",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Morningstar": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": [],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Pike": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Reach", "Two-Handed"],
        "damage": "1d10",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Rapier": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse"],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Scimitar": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse", "Light"],
        "damage": "1d6",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Shortsword": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse", "Light"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Trident": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Thrown", "Versatile"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": "1d8"
    },
    "War Pick": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": [],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Warhammer": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Versatile"],
        "damage": "1d8",
        "damage_type": "Bludgeoning",
        "versatile_damage": "1d10"
    },
    "Whip": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse", "Reach"],
        "damage": "1d4",
        "damage_type": "Slashing",
        "versatile_damage": None
    },

    # MARTIAL RANGED WEAPONS
    "Blowgun": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Loading"],
        "damage": "1",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Hand Crossbow": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Light", "Loading"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Heavy Crossbow": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Heavy", "Loading", "Two-Handed"],
        "damage": "1d10",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Longbow": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Heavy", "Two-Handed"],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Net": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Special", "Thrown"],
        "damage": None,
        "damage_type": None,
        "versatile_damage": None
    }
}

armour_names = {
    "Padded Armour": {"base_ac": 11, "category": "Light"},
    "Leather Armour": {"base_ac": 11, "category": "Light"},
    "Studded Leather Armour": {"base_ac": 12, "category": "Light"},

    "Hide Armour": {"base_ac": 12, "category": "Medium"},
    "Chain Shirt": {"base_ac": 13, "category": "Medium" },
    "Scale Mail": {"base_ac": 14, "category": "Medium"},
    "Breastplate": {"base_ac": 14, "category": "Medium"},
    "Half Plate": {"base_ac": 15, "category": "Medium"},

    "Ring Mail": {"base_ac": 14, "category": "Heavy"},
    "Chain Mail": {"base_ac": 16, "category": "Heavy"},
    "Splint": {"base_ac": 17, "category": "Heavy"},
    "Plate": {"base_ac": 18, "category": "Heavy"},
}

available_tool_types = {
    "Artisan's Tools": ["Smith's Tools", "Carpenter's Tools", "Alchemist's Tools", "Brewer's Supplies"
                        , "Calligrapher's Supplies", "Cartographer's Tools", "Cobbler's Tools", "Cook's Utensils", "Glassblower's Tools",
                        "Jeweler's Tools", "Leatherworker's Tools", "Mason's Tools", "Painter's Supplies", "Potter's Tools",
                        "Tinker's Tools", "Weaver's Tools", "Woodcarver's Tools"],
    "Gaming Set": ["Dice Set", "Dragonchess set", "Playing Card Set", "Three-Dragon Ante Set"]
}

skill_abilities = {
    "Acrobatics": "dexterity",
    "Animal Handling": "wisdom",
    "Arcana": "intelligence",
    "Athletics": "strength",
    "Deception": "charisma",
    "History": "intelligence",
    "Insight": "wisdom",
    "Intimidation": "charisma",
    "Investigation": "intelligence",
    "Medicine": "wisdom",
    "Nature": "intelligence",
    "Perception": "wisdom",
    "Performance": "charisma",
    "Persuasion": "charisma",
    "Religion": "intelligence",
    "Sleight of Hand": "dexterity",
    "Stealth": "dexterity",
    "Survival": "wisdom"
}

character_races = {
    1: {"name": "Elf",
        "speed": 30,
        "size": "Medium",
        "features": ["Darkvision", "Fey Ancestry", "Trance", "Keen Senses"],
        "skill_proficiencies": ["Perception"],
        "languages": ["Common", "Elvish"],

        "subraces": {
            1: {
                "name": "High Elf",
                "weapon_proficiencies": ["Longsword", "Shortsword", "Shortbow", "Longbow"],
                "extra_languages": 1,
                "features": ["Elf Weapon Training", "Cantrip", "Extra Language"],
                "racial_cantrip_choice_from": "Wizard",
                "racial_spellcasting_stat": "intelligence"
            },
            2: {
                "name": "Wood Elf",
                "speed": 35,
                "weapon_proficiencies": ["Longsword", "Shortsword", "Shortbow", "Longbow"],
                "features": ["Elf Weapon Training", "Fleet of Foot", "Mask Of The Wild"],
            },
            3: {"name": "Drow",
                "weapon_proficiencies": ["Rapier", "Shortsword", "Hand Crossbow"],
                "features": ["Superior Darkvision", "Sunlight Sensitivity", "Drow Magic", "Drow Weapon Training"],
                "racial_spells": {
                    1: ["Dancing Lights"],
                    3: ["Faerie Fire"],
                    5: ["Darkness"]
},
"racial_spellcasting_stat": "charisma"

            }

            }
        },


    2: {"name": "Human",
        "speed": 30,
        "size": "Medium",
        "features": [],
        "skill_proficiencies": [],
        "languages": ["Common"],
        "extra_languages": 1,
        "subraces": {}},

    3: {"name": "Dwarf",
        "speed": 25,
        "size": "Medium",
        "features": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning", "Dwarven Speed"],
        "skill_proficiencies": [],
        "weapon_proficiencies": ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"],
        "languages": ["Common", "Dwarvish"],
        "tool_proficiency_choice": ["Smiths Tools", "Brewers Supplies", "Masons Tools"],
        "tool_proficiency_choice_count": 1,

        "subraces": {
            1: {
                "name": "Hill Dwarf",
                "features": ["Dwarven Toughness"]
            },
            2: {
                "name": "Mountain Dwarf",
                "features": ["Dwarven Armour Training"],
                "armour_proficiencies": ["Light Armour", "Medium Armour"]

            }
        }
        },

    4: {"name": "Tiefling",
        "speed": 30,
        "size": "Medium",
        "features": ["Darkvision", "Hellish Resistance", "Infernal Legacy"],
        "skill_proficiencies": [],
        "languages": ["Common", "Infernal"],
        "subraces": {},
        "damage_Resistance": ["Fire"],

        "racial_spells": {
            1: ["Thaumaturgy"],
            3: ["Hellish Rebuke"],
            5: ["Darkness"]
        },
        "racial_spellcasting_stat": "charisma"

        },

    5: {"name": "Dragonborn",
        "speed": 30,
        "size": "Medium",
        "features": ["Draconic Ancestry", "Breath Weapon", "Damage Ressistance"],
        "skill_proficiencies": [],
        "languages": ["Common", "Draconic"],
        "subraces": {
            1: {
                "name": "Black",
                "damage_type": "Acid",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            2: {
                "name": "Blue",
                "damage_type": "Lightning",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            3: {
                "name": "Brass",
                "damage_type": "fire",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            4: {
                "name": "Bronze",
                "damage_type": "Lightning",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            5: {
                "name": "Copper",
                "damage_type": "Acid",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            6: {
                "name": "Gold",
                "damage_type": "Fire",
                "breath_shape": "15ft cone",
                "saving_throw": "dexterity"
            },
            7: {
                "name": "Green",
                "damage_type": "Poison",
                "breath_shape": "15ft cone",
                "saving_throw": "constitution"
            },
            8: {
                "name": "Red",
                "damage_type": "Fire",
                "breath_shape": "15ft cone",
                "saving_throw": "dexterity",
            },
            9: {
                "name": "Silver",
                "damage_type": "cold",
                "breath_shape": "15ft cone",
                "saving_throw": "constitution"
            },
            10: {
                "name": "White",
                "damage_type": "Cold",
                "breath_shape": "15ft cone",
                "saving_throw": "constitution"
            }
        }
        },
}

character_classes = {
    1: {"name": "Fighter",
        "hit_die": 10,
        "subclass_level": 3,
        "saving_throw_proficiencies": ["Strength", "Constitution"],
        "armour_proficiencies": ["Light Armour", "Medium Armour", "Heavy Armour", "Shields"],
        "weapon_proficiencies": ["Simple Weapons", "Martial Weapons"],
        "tool_proficiencies": [],
        "skill_choices": {
            "amount": 2,
            "options": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
        },
        "level_features": {
            1: ["Fighting Style", "Second Wind"],
            2: ["Action Surge"],
            3: ["Martial Archetype"],
            4: ["Ability Score Improvement"],
            5: ["Extra Attack (2 Attacks)"],
            6: ["Ability Score Improvement"],
            7: ["Martial Archetype Feature"],
            8: ["Ability Score Improvement"],
            9: ["Indomitable (1 Use)"],
            10: ["Martial Archetype Feature"],
            11: ["Extra Attack (3 Attacks)"],
            12: ["Ability Score Improvement"],
            13: ["Indomitable (2 Uses)"],
            14: ["Ability Score Improvement"],
            15: ["Martial Archetype Feature"],
            16: ["Ability Score Improvement"],
            17: ["Action Surge (2 Uses)", "Indomitable (3 Uses)"],
            18: ["Martial Archetype Feature"],
            19: ["Ability Score Improvement"],
            20: ["Extra Attack (4 Attacks)"],
        },
        "subclasses": {
            1: {
                "name": "Champion",
                "level_features": {
                    3: ["Improved Critical"],
                    7: ["Remarkable Athlete"],
                    10: ["Additional Fighting Style"],
                    15: ["Superior Critical"],
                    18: ["Survivor"]

                }
            },

            2: {
                "name": "Battle Master",
                "level_features": {
                    3: ["Combat Superiority", "Student of War"],
                    7: ["Know Your Enemy"],
                    10: ["Improved Combat Superiority (d10)"],
                    15: ["Relentless"],
                    18: ["Improved Combat Superiority (d12)"],
                }
                },
            3: {
                "name": "Eldritch Knight",
                "level_features": {
                    3: ["Spellcasting", "Weapon Bond"],
                    7: ["War Magic"],
                    10: ["Eldritch Strike"],
                    15: ["Arcane Charge"],
                    18: ["Improved War Magic"]
                },
                "spellcasting": {
                    "ability": "Intelligence",
                    "starts_at_level": 3,
                    "spell_list": "Wizard",

                    "cantrip_progression": {
                        3: 2,
                        10: 3
                    },

                    "spells_known_progression": {
                        3: 3,
                        4: 4,
                        7: 5,
                        8: 6,
                        10: 7,
                        11: 8,
                        13: 9,
                        14: 10,
                        16: 11,
                        19: 12,
                        20: 13
                    },

                    "spell_school_restrictions": ["Abjuration", "Evocation"],
                    "unrestricted_spell_levels": [3, 8, 14, 20]
                }
            }
        },
    },

    2: {"name": "Wizard",
        "hit_die": 6,
        "subclass_level": 2,
        "saving_throw_proficiencies": ["Intelligence", "Wisdom"],
        "armour_proficiencies": [],
        "weapon_proficiencies": ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
        "tool_proficiencies": [],
        "skill_choices": {
            "amount": 2,
            "options": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
        },
        "level_features": {
            1: ["Spellcasting", "Arcane Recovery"],
            2: ["Arcane Tradition"],
            3: [],
            4: ["Ability Score Improvement"],
            5: [],
            6: ["Arcane Tradition Feature"],
            7: [],
            8: ["Ability Score Improvement"],
            9: [],
            10: ["Arcane Tradition Feature"],
            11: [],
            12: ["Ability Score Improvement"],
            13: [],
            14: ["Arcane Tradition Feature"],
            15: [],
            16: ["Ability Score Improvement"],
            17: [],
            18: ["Spell Mastery"],
            19: ["Ability Score Improvement"],
            20: ["Signature Spells"]
        },
        "subclasses": {
            1: {
                "name": "School of Abjuration",
                "level_features": {
                    2: ["Abjuration Savant", "Arcane Ward"],
                    6: ["Projected Ward"],
                    10: ["Improved Abjuration"],
                    14: ["Spell Resistance"]
                }
            },
            2: {
                "name": "School of Conjuration",
                "level_features": {
                    2: ["Conjuration Savant", "Minor Conjuration"],
                    6: ["Benign Transposition"],
                    10: ["Focused Conjuration"],
                    14: ["Durable Summons"]
                }
            },
            3: {
                "name": "School of Divination",
                "level_features": {
                    2: ["Divination Savant", "Portent"],
                    6: ["Expert Divination"],
                    10: ["The Third Eye"],
                    14: ["Greater Portent"]
                }
            },
            4: {
                "name": "School of Enchantment",
                "level_features": {
                    2: ["Enchantment Savant", "Hypnotic Gaze"],
                    6: ["Instinctive Charm"],
                    10: ["Split Enchantment"],
                    14: ["Alter Memories"]

                }
            },
            5: {
                "name": "School of Evocation",
                "level_features": {
                    2: ["Evocation Savant", "Sculpt Spells"],
                    6: ["Potent Cantrip"],
                    10: ["Empowered Evocation"],
                    14: ["Overchannel"]
                }
            },
            6: {
                "name": "School of Illusion",
                "level_features": {
                    2: ["Illusion Savant", "Improved Minor Illusion"],
                    6: ["Malleable Illusions"],
                    10: ["Illusory Self"],
                    14: ["Illusory Reality"]
                }
            },
            7: {
                "name": "School of Necromancy",
                "level_features": {
                    2: ["Necromancy Savant", "Grim Harvest"],
                    6: ["Undead Thralls"],
                    10: ["Inured to Undeath"],
                    14: ["Command Undead"]
                }
            },
            8: {
                "name": "School of Transmutation",
                "level_features": {
                    2: ["Transmutation Savant", "Minor Alchemy"],
                    6: ["Transmuter's Stone"],
                    10: ["Shapechanger"],
                    14: ["Master Transmuter"]
                }
            },
        },
        "spellcasting": {
            "ability": "Intelligence",
            "starting_cantrips": 3,
            "starting_spellbook_spells": 6,
            "spells_added_per_level": 2,
            "cantrip_progression": {
                1: 3,
                4: 4,
                10: 5
            }
        }
        },

    3: {"name": "Rogue",
        "hit_die": 8,
        "subclass_level": 3,
        "saving_throw_proficiencies": ["Dexterity", "Intelligence"],
        "armour_proficiencies": ["Light Armour"],
        "weapon_proficiencies": ["Simple Weapons", "Hand Crossbow", "Longsword", "Rapier", "Shortsword",],
        "tool_proficiencies": ["Thieves' Tools"],
        "skill_choices": {
            "amount": 4,
            "options": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
        },
        "level_features": {
            1: ["Expertise", "Sneak Attack", "Thieves' Cant"],
            2: ["Cunning Action"],
            3: ["Roguish Archetype"],
            4: ["Ability Score Improvement"],
            5: ["Uncanny Dodge"],
            6: ["Expertise"],
            7: ["Evasion"],
            8: ["Ability Score Improvement"],
            9: ["Roguish Archetype Feature"],
            10: ["Ability Score Improvement"],
            11: ["Reliable Talent"],
            12: ["Ability Score Improvement"],
            13: ["Roguish Archetype Feature"],
            14: ["Blindsense"],
            15: ["Slippery Mind"],
            16: ["Ability Score Improvement"],
            17: ["Roguish Archetype Feature"],
            18: ["Elusive"],
            19: ["Ability Score Improvement"],
            20: ["Stroke of Luck"]
        },
        "subclasses": {
            1: {
                "name": "Thief",
                "level_features": {
                    3: ["Fast Hands", "Second-Story Work"],
                    9: ["Supreme Sneak"],
                    13: ["Use Magic Device"],
                    17: ["Thief's Reflexes"]
                }
            },
            2: {
                "name": "Assassin",
                "level_features": {
                    3: ["Bonus Proficiencies", "Assassinate"],
                    9: ["Infiltration Expertise"],
                    13: ["Impostor"],
                    17: ["Death Strike"]
                }
            },
            3: {
                "name": "Arcane Trickster",
                "level_features": {
                    3: ["Spellcasting", "Mage Hand Legerdemain"],
                    9: ["Magical Ambush"],
                    13: ["Versatile Trickster"],
                    17: ["Spell Thief"]
                },
                "spellcasting": {
                    "ability": "Intelligence",
                    "starts_at_level": 3,
                    "spell_list": "Wizard",
                    "required_cantrips": ["Mage Hand"],
                    "cantrip_progression": {
                        3: 3,
                        10: 4
                    },
                    "spells_known_progression": {
                        3: 3,
                        4: 4,
                        7: 5,
                        8: 6,
                        10: 7,
                        11: 8,
                        13: 9,
                        14: 10,
                        16: 11,
                        19: 12,
                        20: 13
                    },
                    "spell_school_restrictions": ["Enchantment", "Illusion"],
                    "unrestricted_spell_levels": [3,8,14,20]
                }
            }
        },
        "sneak_attack_progression": {
            1: "1d6",
            3: "2d6",
            5: "3d6",
            7: "4d6",
            9: "5d6",
            11: "6d6",
            13: "7d6",
            15: "8d6",
            17: "9d6",
            19: "10d6"
        }
        },


    4: {"name": "Cleric",
        "hit_die": 8,
        "subclass_level": 1,
        "saving_throw_proficiencies": ["Wisdom", "Charisma"],
        "armour_proficiencies": ["Light Armour", "Medium Armour", "Shields"],
        "weapon_proficiencies": ["Simple Weapons"],
        "tool_proficiencies": [],
        "skill_choices": {
            "amount": 2,
            "options": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
        },
        "level_features": {
            1: ["Spellcasting", "Divine Domain"],
            2: ["Channel Divinity (1 Use)","Turn Undead", "Divine Domain Feature"],
            3: [],
            4: ["Ability Score Improvement"],
            5: ["Destroy Undead (CR 1/2)"],
            6: ["Channel Divinity (2 Uses)", "Divine Domain Feature"],
            7: [],
            8: ["Ability Score Improvement", "Destroy Undead (CR 1)", "Divine Domain Feature"],
            9: [],
            10: ["Divine Intervention"],
            11: ["Destroy Undead (CR 2)"],
            12: ["Ability Score Improvement"],
            13: [],
            14: ["Destroy Undead (CR 3)"],
            15: [],
            16: ["Ability Score Improvement"],
            17: ["Destroy Undead (CR 4)", "Divine Domain Feature"],
            18: ["Channel Divinity (3 Uses)"],
            19: ["Ability Score Improvement"],
            20: ["Divine Intervention Improvement"],
        },
        "subclasses": {
            1: {
                "name": "Knowledge Domain",
                "extra_languages": 2,
                "level_features": {
                    1: ["Blessings of Knowledge"],
                    2: ["Channel Divinity: Knowledge of the Ages"],
                    6: ["Channel Divinity: Read Thoughts"],
                    8: ["Potent Spellcasting"],
                    17: ["Visions of the Past"]
                }
            } ,
            2: {
                "name": "Life Domain",
                "armour_proficiencies": ["Heavy Armour"],
                "level_features": {
                    1: ["Bonus Proficiency", "Disciple of Life"],
                    2: ["Channel Divinity: Preserve Life"],
                    6: ["Blessed Healer"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Supreme Healing"]
                }
            },
            3: {
                "name": "Light Domain",
                "level_features": {
                    1: ["Bonus Cantrip", "Warding Flare"],
                    2: ["Channel Divinity: Radiance of the Dawn"],
                    6: ["Improved Flare"],
                    8: ["Potent Spellcasting"],
                    17: ["Corona of Light"]
                }
            },
            4: {
                "name": "Nature Domain",
                "armour_proficiencies": ["Heavy Armour"],
                "level_features": {
                    1: ["Acolyte of Nature", "Bonus Proficiency"],
                    2: ["Channel Divinity: Charm Animals and Plants"],
                    6: ["Dampen Elements"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Master of Nature"]
                }
            },
            5: {
              "name": "Tempest Domain",
                "armour_proficiencies": ["Heavy Armour"],
                "weapon_proficiencies": ["Martial Weapons"],
                "level_features": {
                    1: ["Bonus Proficiencies", "Wrath of the Storm"],
                    2: ["Channel Divinity: Destructive Wrath"],
                    6: ["Thunderbolt Strike"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Stormborn"]
                }
            },
            6: {
              "name": "Trickery Domain",
                "level_features": {
                    1: ["Blessing of the Trickster"],
                    2: ["Channel Divinity: Invoke Duplicity"],
                    6: ["Channel Divinity: Cloak of Shadows"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Improved Duplicity"]
                }
            },
            7: {
                "name": "War Domain",
                "armour_proficiencies": ["Heavy Armour"],
                "weapon_proficiencies": ["Martial Weapons"],
                "level_features": {
                    1: ["Bonus Proficiencies", "War Priest"],
                    2: ["Channel Divinity: Guided Strike"],
                    6: ["Channel Divinity: War God's Blessing"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Avatar of Battle"]
                }
            }
        },
        "spellcasting": {
            "ability": "Wisdom",
            "spell_list": "Cleric",
            "preparation_method": "Prepared",
            "preparation_formula": "Cleric Level + Wisdom Modifier",
            "cantrip_progression": {
                1: 3,
                4: 4,
                10: 5
            }
        }

        },


    5: {"name": "Barbarian",
        "hit_die": 12,
        "subclass_level": 3,
        "saving_throw_proficiencies": ["Strength", "Constitution"],
        "armour_proficiencies": ["Light Armour", "Medium Armour", "Shields"],
        "weapon_proficiencies": ["Simple Weapons", "Martial Weapons"],
        "tool_proficiencies": [],
        "skill_choices": {
            "amount": 2,
            "options": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
        },
        "level_features": {
            1: ["Rage", "Unarmoured Defense"],
            2: ["Reckless Attack", "Danger Sense"],
            3: ["Primal Path"],
            4: ["Ability Score Improvement"],
            5: ["Extra Attack", "Fast Movement"],
            6: ["Primal Path Feature"],
            7: ["Feral Instinct"],
            8: ["Ability Score Improvement"],
            9: ["Brutal Critical (1 Die)"],
            10: ["Primal Path Feature"],
            11: ["Relentless Rage"],
            12: ["Ability Score Improvement"],
            13: ["Brutal Critical (2 Dice)"],
            14: ["Primal Path Feature"],
            15: ["Persistent Rage"],
            16: ["Ability Score Improvement"],
            17: ["Brutal Critical (3 Dice)"],
            18: ["Indomitable Might"],
            19: ["Ability Score Improvement"],
            20: ["Primal Champion"]
        },
        "subclasses": {
            1: {
                "name": "Path of the Berserker",
                "level_features": {
                    3: ["Frenzy"],
                    6: ["Mindless Rage"],
                    10: ["Intimidating Presence"],
                    14: ["Retaliation"],
                }
            },
            2: {
                "name": "Path of the Totem Warrior",
                "level_features": {
                    3: ["Spirit Seeker", "Totem Spirit"],
                    6: ["Aspect of the Beast"],
                    10: ["Spirit Walker"],
                    14: ["Totemic Attunement"]
                }
            }
        },
        "rage_progression": {
            1: {"uses": 2, "damage_bonus": 2},
            3: {"uses": 3, "damage_bonus": 2},
            6: {"uses": 4, "damage_bonus": 2},
            9: {"uses": 4, "damage_bonus": 3},
            12: {"uses": 5, "damage_bonus": 3},
            16: {"uses": 5, "damage_bonus": 4},
            17: {"uses": 6, "damage_bonus": 4},
            20: {"uses": "Unlimited", "damage_bonus": 4},
        }
        }
}
character_backgrounds = {
    1: {"name": "Acolyte",
        "skill_proficiencies": ["Insight", "Religion"],
        "tool_proficiencies": [],
        "tool_choices": {},
        "extra_languages": 2,
        "equipment": ["Holy Symbol", "Prayer book or Prayer Wheel", "5 Sticks of incense", "Vestments", "Common Clothes", "15GP"],
        "features": {
            "name": "Shelter of the Faithful",
            "description": "You can perform religious ceremonies and receive support from others who share your faith"}
        },

    2: {"name": "Criminal",
        "skill_proficiencies": ["Deception", "Stealth"],
        "tool_proficiencies": ["Thieves' Tools"],
        "tool_choices": {"Gaming Set": 1},
        "extra_languages": 0,
        "equipment": ["Crowbar", "Dark Common Clothes with Hood", "15 GP"],
        "features": {
            "name": "Criminal Contact",
            "description": "You have a reliable contact within the criminal underworld and know how to exchange information"
        }
        },

    3: {"name": "Folk Hero",
        "skill_proficiencies": ["Animal Handling", "Survival"],
        "tool_proficiencies": ["Vehicles (Land)"],
        "tool_choices": {"Artisan's Tools": 1},
        "extra_languages": 0,
        "equipment": ["One Set of Artisan's Tools (Chosen Type)", "Shovel", "Iron Pot", "Common Clothes", "10 GP"],
        "features": {
            "name": "Rustic Hospitality",
            "description": "Common people may shelter you, but they won't risk their lives for you, and you must not have made yourself dangerous to them"
        }
        },
    4: {"name": "Noble",
        "skill_proficiencies": ["History", "Persuasion"],
        "tool_proficiencies": [],
        "tool_choices": {"Gaming Set": 1},
        "extra_languages": 1,
        "equipment": ["Fine Clothes", "Signet Ring", "Scroll of Pedigree", "25 GP"],
        "features": {
            "name": "Position of Privilege",
            "description": "Your noble status grants you access to high society, favourable treatment and opportunities"
        }

        },
    5: {"name": "Sage",
        "skill_proficiencies": ["Arcana", "History"],
        "tool_proficiencies": [],
        "tool_choices": {},
        "extra_languages": 2,
        "equipment": ["Bottle of Black Ink", "Quill", "Small Knife", "Letter from a Deceased Colleague", "Common Clothes", "10 GP"],
        "features": {
            "name": "Researcher",
            "description": "When you do not know a piece of lore, you often know where or from whom you could find the source"
        }
        }
}

available_languages = [
    "Common",
    "Dwarvish",
    "Elvish",
    "Giant",
    "Gnomish",
    "Goblin",
    "Halfling",
    "Orc",
    "Abyssal",
    "Celestial",
    "Draconic",
    "Deep Speech",
    "Infernal",
    "Primordial",
    "Sylvan",
    "Undercommon"
]

def add_equipment(inventory, item_name,quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def get_available_weapons(category, attack_type=None):
    available_weapons = []

    for weapon_name, weapon_info in weapon_data.items():
        if weapon_info["category"] == category:
            if attack_type is None or weapon_info["attack_type"] == attack_type:
                available_weapons.append(weapon_name)

    return available_weapons

def get_available_armour(inventory):
    available_armour = []
    for items in inventory:
        if items in armour_names and inventory[items] > 0:
            available_armour.append(items)
    return available_armour

def get_owned_weapons(inventory):
    available_weapons = []
    for items in inventory:
        if items in weapon_data and inventory[items] > 0:
            available_weapons.append(items)
    return available_weapons

def confirm_unequip_shield():
    while True:
        answer = input("\nWould you like to unequip your shield? (yes/no): ").strip().lower()

        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("That's not a valid answer, please reply with yes or no!")

def choose_equipped_armour(inventory):
    available_armour = get_available_armour(inventory)
    print("\nChoose which armour you would like to equip:")

    print("0. Remain Unarmoured")
    for number, armour in enumerate(available_armour, start=1):
        print(f"{number}. {armour}")
    while True:
        try:
            choice = int(input("\nEnter the number of the armour you would like to equip:"))

            if choice == 0:
                return None

            elif 1 <= choice <= len(available_armour):
                return available_armour[choice - 1]

            else:
                print("That's not a valid armour!")

        except ValueError:
            print("Please enter a valid armour number!")

def choose_equipped_weapon(inventory, equipped_shield ):
    available_weapons = get_owned_weapons(inventory)

    if not available_weapons:
        print("You don't have any weapons to equip!")
        return [], equipped_shield, False

    while True:
        print("\nChoose which weapon you would like to equip:")
        print("""Choose how you want to hold your weapons for battle:
        1. One-handed weapon
        2. Two handed weapon
        3. Duel-wield weapons (Holding two weapons in both hands)
        4. Multiple weapons (Equipping 2 or more)""")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            print("One-handed weapon selected")

            one_handed_weapons = []

            for weapon in available_weapons:
                if "Two-Handed" not in weapon_data[weapon]["properties"]:
                    one_handed_weapons.append(weapon)

            if not one_handed_weapons:
                print("You don't own any suitable one-handed weapons!")

            else:
                for number, weapon in enumerate(one_handed_weapons, start=1):
                    print(f"{number}. {weapon}")
                while True:
                    try:
                        weapon_choice = int(input("\nEnter the number of the weapon you would like to equip:"))

                        if 1 <= weapon_choice <= len(one_handed_weapons):
                            break
                        else:
                            print("Please enter a valid NUMBER!")

                    except ValueError:
                        print("Please enter a valid number!")
                selected_weapon = one_handed_weapons[weapon_choice - 1]
                return [{"weapon": selected_weapon, "hands": 1}], equipped_shield, False

        elif choice == "2":
            print("Two-Handed weapon selected")

            two_handed_weapons = []

            for weapon in available_weapons:
                properties = weapon_data[weapon]["properties"]
                if "Two-Handed" in properties or "Versatile" in properties:
                    two_handed_weapons.append(weapon)

            if not two_handed_weapons:
                print("You don't own any suitable weapons to use two-handed!")
            else:
                if equipped_shield:
                    print("\nYou currently have a shield equipped...")
                    print("\nUnfortunately, you cannot use a two-handed weapon and a shield simultaneously.")

                    if confirm_unequip_shield():
                        equipped_shield = False
                        print("Your shield has been unequipped.")
                    else:
                        print("Keeping your shield equipped.")
                        continue

                for number, weapon in enumerate(two_handed_weapons, start=1):
                    print(f"{number}. {weapon}")
                while True:
                    try:
                        weapon_choice = int(input("\nEnter the number of the weapon you would like to equip:"))

                        if 1 <= weapon_choice <= len(two_handed_weapons):
                            break
                        else:
                            print("Please enter a valid NUMBER")

                    except ValueError:
                        print("Please enter a valid number!")
                selected_weapon = two_handed_weapons[weapon_choice - 1]
                print(f"You selected {selected_weapon} to wield with two hands!")

                return [{"weapon": selected_weapon, "hands": 2}], equipped_shield, False
        elif choice == "3":
            print("Dual-wielding selected")

            dual_wield_weapons = []

            for weapon in available_weapons:
                properties = weapon_data[weapon]["properties"]
                attack_type = weapon_data[weapon]["attack_type"]

                if "Light" in properties and attack_type == "Melee":
                    dual_wield_weapons.append(weapon)

            total_duel_wield_weapons = 0

            for weapon in dual_wield_weapons:
                total_duel_wield_weapons += inventory[weapon]

            if total_duel_wield_weapons < 2:
                print("You need atleast 2 suitable weapons to duel-wield!")

            else:
                if equipped_shield:
                    print("\nYou currently have a shield equipped...")
                    print("\nUnfortunately, you cannot use duel wield with a shield equipped.")

                    if confirm_unequip_shield():
                        equipped_shield = False
                        print("Your shield has been unequipped.")
                    else:
                        print("Keeping your shield equipped.")
                        continue

                for number, weapon in enumerate(dual_wield_weapons, start=1):
                    print(f"{number}. {weapon} (Owned: {inventory[weapon]})")

                while True:
                    try:
                        first_choice = int(input("\nChoose your first weapon:"))

                        if 1 <= first_choice <= len(dual_wield_weapons):
                            break
                        else:
                            print("Please enter a valid weapon NUMBER!")

                    except ValueError:
                        print("Please enter a valid number!")

                first_weapon = dual_wield_weapons[first_choice - 1]
                print(f"First weapon selected: {first_weapon}")

                second_weapon_options = []

                for weapon in dual_wield_weapons:
                    if weapon != first_weapon or inventory[weapon] >= 2:
                        second_weapon_options.append(weapon)

                if not second_weapon_options:
                    print("You don't own any suitable weapons for dual-wielding!")

                else:
                    print("\nChoose your second weapon:")

                    for number, weapon in enumerate(second_weapon_options, start=1):
                        print(f"{number}. {weapon}")

                    while True:
                        try:
                            second_choice = int(input("\nChoose your second weapon: "))

                            if 1<= second_choice <= len(second_weapon_options):
                                break
                            else:
                                print("Please enter a valid NUMBER!")

                        except ValueError:
                            print("Please enter a valid number!")

                    second_weapon = second_weapon_options[second_choice - 1]
                    return [
                        {"weapon": first_weapon, "hands": 1},
                        {"weapon": second_weapon, "hands": 1},
                    ], equipped_shield, True

        elif choice == "4":
            print("\nSelect the weapons you want available in battle.")
            print("You can switch between these weapons; they are not dual-wielded.")

            selected_weapons = []

            while True:
                remaining_weapons = [
                    weapon for weapon in available_weapons
                    if weapon not in [
                        selected["weapon"] for selected in selected_weapons
                    ]
                ]

                if not remaining_weapons:
                    print("\nAll available weapon types have been selected.")
                    break

                print("\nAvailable weapons:")

                for number, weapon in enumerate(remaining_weapons, start=1):
                    print(f"{number}. {weapon}")

                print("0. Finish selecting weapons")

                try:
                    weapon_choice = int(input("\nEnter your choice: "))
                except ValueError:
                    print("Please enter a valid number!")
                    continue

                if weapon_choice == 0:
                    if selected_weapons:
                        break

                    print("You must select at least one weapon!")
                    continue

                if not 1 <= weapon_choice <= len(remaining_weapons):
                    print("Please enter a valid weapon number!")
                    continue

                selected_weapon = remaining_weapons[weapon_choice - 1]
                properties = weapon_data[selected_weapon]["properties"]

                if "Two-Handed" in properties:
                    hands = 2

                elif "Versatile" in properties:
                    while True:
                        hand_choice = input(
                            "Use this weapon with one or two hands? (1/2): "
                        ).strip()

                        if hand_choice in ("1", "2"):
                            hands = int(hand_choice)
                            break

                        print("Please enter 1 or 2.")

                else:
                    hands = 1

                selected_weapons.append({
                    "weapon": selected_weapon,
                    "hands": hands
                })

                print(f"Added {selected_weapon} to your available weapons.")

            if equipped_shield and any(
                weapon["hands"] == 2 for weapon in selected_weapons
            ):
                print(
                    "\nYou have selected a two-handed weapon while "
                    "your shield is equipped."
                )

                if confirm_unequip_shield():
                    equipped_shield = False
                    print("Your shield has been unequipped.")
                else:
                    print("Keeping your shielf equipped.")
                    print(
                        "You can only use your one-handed weapons"
                        "while the shield is equipped."
                    )

            return selected_weapons, equipped_shield, False


        else:
            print("That's not a valid choice!")


def choose_equipped_shield(inventory):
    if inventory.get("Shield", 0) > 0:
        print("\nYou have a shield available to equip")
        while True:
            answer = input("Would you like to equip your shield? (yes/no): ").strip().lower()
            if answer == "yes":
                print("You have equipped your shield!")
                return True
            elif answer == "no":
                return False
            else:
                print("That's not a valid answer now, is it! Answer yes or no.")
    else:
        print("\nYou have no shield available to equip")
        return False


def choose_starting_weapon(category, attack_type=None):
    available_weapons = get_available_weapons(category, attack_type)
    if not available_weapons:
        raise ValueError(
            f"No weapons found for category '{category}' "
            f"and attack type {attack_type}"
        )

    print("\nChoose your starting weapon:")
    for number, weapon in enumerate(available_weapons, start=1):
        print(f"{number}. {weapon}")
    while True:
        try:
            choice = int(input("Choose a weapon by its number:"))
            if 1 <= choice <= len(available_weapons):
                selected_weapon = available_weapons[choice - 1]
                print(f"You have chosen {selected_weapon}!")
                return selected_weapon
            else:
                print("Please choose a number in the LIST!")

        except ValueError:
            print("Please choose a NUMBER in the list!")

def choose_equipment_option(options):
    print("\nChoose your starting equipment:")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        try:
            choice = int(input("Choose an equipment option by its number:"))
            if 1 <= choice <= len(options):
                selected_equipment = options[choice - 1]
                print(f"You have chosen {selected_equipment}!")
                return selected_equipment
            else:
                print("Please choose a number in the LIST!")

        except ValueError:
            print("Please choose a NUMBER in the list!")

def calculate_armour_class(equipped_armour, equipped_shield, dexterity_modifier, character_class, constitution_modifier):
    if character_class == "Barbarian" and equipped_armour is None:
        armour_class = max(
            10 + dexterity_modifier,
            10 + dexterity_modifier + constitution_modifier
        )

    elif equipped_armour is None:
        armour_class = 10 + dexterity_modifier


    else:
        armour_info = armour_names[equipped_armour]
        base_ac = armour_info["base_ac"]
        category = armour_info["category"]

        if category == "Light":
            armour_class = base_ac + dexterity_modifier

        elif category == "Medium":
            armour_class = base_ac + min(dexterity_modifier, 2)

        else:
            armour_class = base_ac

    if equipped_shield == True:
        armour_class += 2

    return armour_class

def calculate_weapon_attack_bonus(weapon_name, strength_modifier, dexterity_modifier, proficiency_bonus, known_weapon_proficiencies, attack_mode=None, finesse_ability=None):
    weapon_info = weapon_data[weapon_name]
    weapon_type = weapon_info["attack_type"]
    properties = weapon_info["properties"]

    if attack_mode is None:
        attack_mode = weapon_type

    if attack_mode not in ("Melee", "Ranged", "Thrown"):
        raise ValueError("Invalid attack mode.")

    if attack_mode == "Thrown":
        if weapon_type != "Melee" or "Thrown" not in properties:
            raise ValueError(f"{weapon_name} cannot be thrown.")

    elif attack_mode != weapon_type:
        raise ValueError(f"{weapon_name} cannot use {attack_mode} attacks.")

    if weapon_type == "Melee":
        ability_modifier = strength_modifier
    else:
        ability_modifier = dexterity_modifier

    if "Finesse" in properties:
        if finesse_ability == "Strength":
            ability_modifier = strength_modifier
        elif finesse_ability == "Dexterity":
            ability_modifier = dexterity_modifier
        elif finesse_ability is None:
            ability_modifier = max(strength_modifier, dexterity_modifier)
        else:
            raise ValueError("Finesse ability must be Strength or Dexterity.")

    attack_bonus = ability_modifier

    if (
        weapon_info["category"] in known_weapon_proficiencies
        or weapon_name in known_weapon_proficiencies
    ):
        attack_bonus += proficiency_bonus

    return attack_bonus

def calculate_weapon_damage(weapon_name, hands, strength_modifier, dexterity_modifier, off_hand=False, attack_mode=None, finesse_ability=None, chosen_fighting_styles=None):
    weapon_info = weapon_data[weapon_name]

    weapon_type = weapon_info["attack_type"]
    damage_dice = weapon_info["damage"]
    damage_type = weapon_info["damage_type"]
    properties = weapon_info["properties"]

    if attack_mode is None:
        attack_mode = weapon_type

    if attack_mode not in ("Melee", "Ranged", "Thrown"):
        raise ValueError("Invalid attack mode.")

    if attack_mode == "Thrown":
        if weapon_type != "Melee" or "Thrown" not in properties:
            raise ValueError(f"{weapon_name} cannot use {attack_mode} attacks.")

    elif attack_mode != weapon_type:
        raise ValueError(f"{weapon_name} cannot use {attack_mode} attacks.")

    if damage_dice is None:
        return None, None, None

    if hands == 2 and "Versatile" in properties:
        damage_dice = weapon_info["versatile_damage"]

    if weapon_type == "Melee":
        damage_modifier = strength_modifier
    else:
        damage_modifier = dexterity_modifier

    if "Finesse" in properties:
        if finesse_ability == "Strength":
            damage_modifier = strength_modifier
        elif finesse_ability == "Dexterity":
            damage_modifier = dexterity_modifier
        elif finesse_ability is None:
            damage_modifier = max(strength_modifier, dexterity_modifier)
        else:
            raise ValueError("Finesse ability must be strength or dexterity.")

    damage_modifier = apply_two_weapon_fighting_style(damage_modifier, chosen_fighting_styles or [], off_hand)

    return damage_dice, damage_modifier, damage_type

def get_rage_info(character_level):
    rage_progression = character_classes[5]["rage_progression"]

    applicable_level = max(
        level for level in rage_progression
        if level <= character_level
    )

    return rage_progression[applicable_level]

def qualifies_for_rage_damage(weapon_name, strength_modifier, dexterity_modifier, attack_mode="Melee", finesse_ability=None):
    weapon_info = weapon_data[weapon_name]

    if attack_mode != "Melee":
        return False

    if weapon_info["attack_type"] != "Melee":
        return False

    if "Finesse" in weapon_info["properties"]:
        if finesse_ability == "Strength":
            return True
        elif finesse_ability == "Dexterity":
            return False
        elif finesse_ability is None:
            return strength_modifier >= dexterity_modifier
        else:
            raise ValueError("Finesse ability must be Strength or Dexterity.")

    return True

def calculate_rage_damage_bonus(character_class, character_level, equipped_armour, weapon_name, strength_modifier, dexterity_modifier, attack_mode="Melee", finesse_ability=None):
    if character_class != "Barbarian":
        return 0

    if equipped_armour is not None:
        armour_category = armour_names[equipped_armour]["category"]

        if armour_category == "Heavy":
            return 0

    if not qualifies_for_rage_damage(weapon_name, strength_modifier, dexterity_modifier, attack_mode, finesse_ability):
        return 0

    rage_info = get_rage_info(character_level)

    return rage_info["damage_bonus"]

def calculate_rage_uses(character_class, character_level):
    if character_class != "Barbarian":
        return None

    rage_info = get_rage_info(character_level)
    return rage_info["uses"]

def calculate_movement_speed(base_speed, character_class, character_level, equipped_armour, strength_score, character_race):

    movement_speed = base_speed

    strength_requirements = {
        "Chain Mail": 13,
        "Splint": 15,
        "Plate": 15
    }

    required_strength = strength_requirements.get(equipped_armour)

    if (
        required_strength is not None
        and character_race != "Dwarf"
        and strength_score < required_strength
    ):
        movement_speed -= 10

    if character_class != "Barbarian" or character_level < 5:
        return movement_speed

    if equipped_armour is None:
        movement_speed += 10

    else:
        armour_category = armour_names[equipped_armour]["category"]
        if armour_category != "Heavy":
            movement_speed += 10

    return movement_speed

def choose_totem_animals(character_class, character_subclass, character_level):
    chosen_totems = {}

    if character_class != "Barbarian":
        return chosen_totems

    if character_subclass != "Path of the Totem Warrior":
        return chosen_totems

    totem_features = {
        3: "Totem Spirit",
        6: "Aspect of the Beast",
        14: "Totemic Attunement"
    }

    animals = ["Bear", "Eagle", "Wolf"]

    for level, feature in totem_features.items():
        if character_level >= level:
            print(f"\nChoose an animal for {feature} (Level {level}):")

            for number, animal in enumerate(animals, start=1):
                print(f"{number}. {animal}")

            while True:
                choice = input("Enter an animal number: ").strip()

                if choice in ["1", "2", "3"]:
                    chosen_totems[feature] = animals[int(choice) - 1]
                    break

                print("Please enter 1, 2 or 3.")

    return chosen_totems

def choose_fighting_styles(character_class, character_level, character_subclass):

    chosen_fighting_styles = []

    if character_class != "Fighter":
        return chosen_fighting_styles

    if character_subclass == "Champion" and character_level >= 10:
        number_of_styles = 2
    else:
        number_of_styles = 1

    print(f"\nAs a fighter you get to choose a fighting style, here is a list of them:")
    for style_name, style_details in fighting_styles.items():
        print(f"{style_name}: {style_details['description']}")

    for choice_number in range(number_of_styles):
        while True:
            chosen_style = input("\nChoose your fighting style: ").strip().title()

            if chosen_style not in fighting_styles:
                print("That Fighting Style does not exist. Choose an existing one.")

            elif chosen_style in chosen_fighting_styles:
                print("You've already selected that Fighting Style...Choose another!")

            else:
                chosen_fighting_styles.append(chosen_style)

                print(f"\nYou have chosen: {chosen_style}")
                print(fighting_styles[chosen_style]["description"])

                break

    return chosen_fighting_styles

def apply_defense_fighting_style(armour_class, chosen_fighting_styles, equipped_armour):

    if "Defense" in chosen_fighting_styles and equipped_armour is not None:
        armour_class += 1

    return armour_class

def apply_archery_fighting_style(attack_bonus, chosen_fighting_styles, weapon_name):

    if "Archery" in chosen_fighting_styles and weapon_data[weapon_name]["attack_type"] == "Ranged":
        attack_bonus += 2

    return attack_bonus

def apply_dueling_fighting_style(damage_modifier, chosen_fighting_styles, weapon_name, wielded_two_handed, wielding_another_weapon):

    if "Dueling" not in chosen_fighting_styles:
        return damage_modifier

    if weapon_data[weapon_name]["attack_type"] != "Melee":
        return damage_modifier

    if "Two-Handed" in weapon_data[weapon_name]["properties"]:
        return damage_modifier

    if wielded_two_handed:
        return damage_modifier

    if wielding_another_weapon:
        return damage_modifier

    damage_modifier += 2
    return damage_modifier

def apply_two_weapon_fighting_style(ability_modifier, chosen_fighting_styles, is_second_weapon_attack):

    if not is_second_weapon_attack:
        return ability_modifier

    if "Two-Weapon Fighting" in chosen_fighting_styles:
        return ability_modifier

    if ability_modifier < 0:
        return ability_modifier
    else:
        return 0

def calculate_sneak_attack(character_class, character_level):
    if character_class != "Rogue":
        return None

    progression = character_classes[3]["sneak_attack_progression"]

    eligible_levels = [
        level for level in progression
        if level <= character_level
    ]

    highest = max(eligible_levels)

    damage_value = progression[highest]

    return damage_value

def calculate_remarkable_athlete_bonus(character_class, character_level, subclass_name, proficiency_bonus):
    if character_class != "Fighter":
        return None

    if subclass_name != "Champion":
        return None

    if character_level < 7:
        return None

    athlete_bonus = math.ceil(proficiency_bonus / 2)

    return athlete_bonus

def calculate_superiority_dice(character_class, character_level, subclass_name):
    if character_class != "Fighter":
        return None

    if subclass_name != "Battle Master":
        return None

    if character_level < 3:
        return None

    if character_level < 3:
        return None

    if character_level >= 18:
        number_of_dice = 6
        die_size = "d12"

    elif character_level >= 15:
        number_of_dice = 6
        die_size = "d10"

    elif character_level >= 10:
        number_of_dice = 5
        die_size = "d10"

    elif character_level >= 7:
        number_of_dice = 5
        die_size = "d8"

    else:
        number_of_dice = 4
        die_size = "d8"

    return number_of_dice, die_size

def calculate_manoeuvre_save_dc(character_class, character_level, subclass_name, proficiency_bonus, ability_modifier):
    if character_class != "Fighter":
        return None

    if subclass_name != "Battle Master":
        return None

    if character_level < 3:
        return None

    save_dc = 8 + proficiency_bonus + ability_modifier

    return save_dc

def calculate_manoeuvres_known (character_class, character_level, subclass_name):
    if character_class != "Fighter":
        return None

    if subclass_name != "Battle Master":
        return None

    if character_level < 3:
        return None

    if character_level <= 6:
        manoeuvres_known = 3

    elif character_level <= 9:
        manoeuvres_known = 5

    elif character_level <= 14:
        manoeuvres_known = 7

    else:
        manoeuvres_known = 9

    return manoeuvres_known

def choose_manoeuvres(manoeuvres_known):
    if manoeuvres_known is None:
        return []

    chosen_manoeuvres = []

    manoeuvre_names = list(battle_master_manoeuvres)

    for number, name in enumerate(manoeuvre_names, start=1):
        print(f"{number}. {name}")

    for selection in range(manoeuvres_known):
        while True:
            choice = input(f"Choose manoeuvre {selection + 1}: ")

            if not choice.isdigit():
                print("Please enter a number.")
                continue

            choice_number = int(choice)

            if not 1 <= choice_number <= len(manoeuvre_names):
                print("Please choose a valid number.")
                continue

            selected_manoeuvre = manoeuvre_names[choice_number - 1]

            if selected_manoeuvre in chosen_manoeuvres:
                print("You chose this manoeuvre, please pick another one.")
                continue

            chosen_manoeuvres.append(selected_manoeuvre)
            print(f"You have selected: {selected_manoeuvre}")
            break

    return chosen_manoeuvres

def calculate_champion_critical_range(character_class, character_level, subclass_name):
    if character_class != "Fighter":
        return None

    if subclass_name != "Champion":
        return None

    if character_level >= 15:
        return 18

    elif character_level >= 3:
        return 19

    return None

def calculate_channel_divinity_uses(character_class, character_level):
    channel_divinity_uses = None
    if character_class != "Cleric":
        return None

    if character_level < 2:
        return None

    if character_level <= 5:
        channel_divinity_uses = 1

    elif character_level <= 17:
        channel_divinity_uses = 2

    elif character_level <= 20:
        channel_divinity_uses = 3

    return channel_divinity_uses

def calculate_destroy_undead_cr(character_class, character_level):
    destroy_undead_cr = None

    if character_class != "Cleric" or character_level < 5:
        destroy_undead_cr = None

    elif character_level >= 17:
        destroy_undead_cr = 4

    elif character_level >= 14:
        destroy_undead_cr = 3

    elif character_level >= 11:
        destroy_undead_cr = 2

    elif character_level >= 8:
        destroy_undead_cr = 1

    elif character_level >= 5:
        destroy_undead_cr = 0.5

    return destroy_undead_cr

def calculate_divine_intervention_chance(character_class, character_level):
    divine_intervention_chance = None

    if character_class != "Cleric" or character_level < 10:
        return None

    if character_level == 20:
        divine_intervention_chance = 100

    else:
        divine_intervention_chance = character_level

    return divine_intervention_chance

def calculate_preserve_life_pool(character_class, character_level, subclass_name):
    preserve_life_pool = None

    if character_class != "Cleric":
        return None

    if subclass_name != "Life Domain":
        return None

    if character_level < 2:
        return None

    else:
        preserve_life_pool = character_level * 5

    return preserve_life_pool

def calculate_radiance_of_the_dawn_damage(character_class, character_level, subclass_name):
    if character_class != "Cleric":
        return None

    if subclass_name != "Light Domain":
        return None

    if character_level < 2:
        return None

    damage_dice = "2d10"
    damage_modifier = character_level

    damage = f"{damage_dice} + {damage_modifier}"
    return damage

def calculate_dragonborn_breath_damage(character_race, character_level):
    if character_race != "Dragonborn":
        return None

    if character_level >= 16:
        return "5d6"

    if character_level >= 11:
        return "4d6"

    if character_level >= 6:
        return "3d6"

    else:
        return "2d6"

def get_dragonborn_breath_damage_type(character_race, character_subrace):
    if character_race != "Dragonborn":
        return None

    for ancestry in character_races[5]["subraces"].values():
        if ancestry["name"] == character_subrace:
            return ancestry["damage_type"]

    return None

def calculate_dragonborn_breath_save_dc(character_race, proficiency_bonus, constitution_modifier):
    if character_race != "Dragonborn":
        return None

    save_DC = 8 + proficiency_bonus + constitution_modifier

    return save_DC

def get_dragonborn_breath_details(character_race, character_subrace):
    if character_race != "Dragonborn":
        return None, None

    for ancestry in character_races[5]["subraces"].values():
        if ancestry["name"] == character_subrace:
            return ancestry["breath_shape"], ancestry["saving_throw"]

    return None, None

def calculate_second_wind_healing(character_class, character_level):
    if character_class != "Fighter":
        return None

    healing = f"1d10 + {character_level}"
    return healing

def calculate_action_surge_uses(character_class, character_level):
    if character_class != "Fighter" or character_level < 2:
        return None

    if character_level >= 17:
        return 2

    return 1

def calculate_indomitable_uses(character_class, character_level):
    if character_class != "Fighter" or character_level <= 8:
        return None

    if character_level >= 17:
        return 3

    if character_level >= 13:
        return 2

    return 1

def get_spell_casting_modifier(character_class, character_modifiers,subclass_name=None):

    if subclass_name is not None:
        spellcasting = get_subclass_spellcasting_data(character_class, subclass_name)

        if spellcasting is not None:
            ability = spellcasting["ability"].lower()
            return character_modifiers[ability]

    for class_data in character_classes.values():

        if class_data["name"] == character_class:

            spellcasting = class_data.get("spellcasting")

            if spellcasting is None:
                return None

            ability = spellcasting["ability"].lower()
            return character_modifiers[ability]

    return None

def calculate_spell_save_dc(proficiency_bonus, spellcasting_modifier):
    if spellcasting_modifier is None:
        return None

    spell_save_dc = 8 + proficiency_bonus + spellcasting_modifier
    return spell_save_dc

def calculate_spell_attack_bonus(proficiency_bonus, spellcasting_modifier):
    if spellcasting_modifier is None:
        return None

    spell_attack_bonus = proficiency_bonus + spellcasting_modifier

    return spell_attack_bonus

def get_racial_spellcasting_data(character_race, character_subrace):
    for race_data in character_races.values():
        if race_data["name"] != character_race:
            continue

        if character_subrace:
            for subrace_data in race_data.get("subraces", {}).values():
                if subrace_data["name"] == character_subrace:
                    return subrace_data

        return race_data

    return None

def get_racial_spells(character_race, character_subrace, character_level):
    racial_data = get_racial_spellcasting_data(character_race, character_subrace)

    if racial_data is None:
        return []

    racial_spell_progression = racial_data.get("racial_spells", {})

    unlocked_spells = []

    for required_level, spells in sorted(racial_spell_progression.items()):
        if character_level >= required_level:
            unlocked_spells.extend(spells)

    return unlocked_spells

def choose_racial_cantrip(character_race, character_subrace):
    racial_data = get_racial_spellcasting_data(character_race, character_subrace)

    if racial_data is None:
        return None

    cantrip_class = racial_data.get("racial_cantrip_choice_from")

    if cantrip_class is None:
        return None

    print(f"\nYour {character_subrace or character_race} heritage grants you a cantrip!")
    print(f"Choose one cantrip from the {cantrip_class} spell list!")

    selected_cantrips = choose_cantrips(cantrip_class, 1)

    return selected_cantrips[0]

def get_racial_spellcasting_ability(character_race, character_subrace):
    racial_data = get_racial_spellcasting_data(character_race, character_subrace)

    if racial_data is None:
        return None

    return racial_data.get("racial_spellcasting_stat")

def get_subclass_spellcasting_data(character_class, subclass_name):
    for class_data in character_classes.values():

        if class_data["name"] == character_class:

            for subclass_data in class_data.get("subclasses", {}).values():

                if subclass_data["name"] == subclass_name:
                    return subclass_data.get("spellcasting")


    return None

def get_subclass_spells_known_count(character_class, character_level, subclass_name):
    spellcasting_data = get_subclass_spellcasting_data(character_class, subclass_name)

    if spellcasting_data is None:
        return None

    progression = spellcasting_data.get("spells_known_progression")

    if progression is None:
        return None

    eligible_levels = [
        level for level in progression
        if level <= character_level
    ]

    if not eligible_levels:
        return None

    latest_level = max(eligible_levels)
    return progression[latest_level]


def replace_subclass_known_spell(
    character_class, character_level, subclass_name,
    known_spells, unrestricted_spells
):
    if not known_spells:
        return

    while True:
        replace = input(
            f"\nAt {character_class} level {character_level}, "
            "would you like to replace a known spell? (yes/no): "
        ).strip().lower()

        if replace in ("n", "no"):
            return

        if replace in ("y", "yes"):
            break

        print("Please enter y or n.")

    print("\nChoose a spell to replace:")

    for number, spell in enumerate(known_spells, start=1):
        print(f"{number}. {spell}")

    while True:
        choice = input("Enter the spell number: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(known_spells):
            old_index = int(choice) - 1
            break

        print("Please choose a valid spell number.")

    old_spell = known_spells[old_index]
    is_unrestricted = old_spell in unrestricted_spells

    spellcasting_data = get_subclass_spellcasting_data(
        character_class, subclass_name
    )

    spell_slots = get_spell_slots(
        character_class, character_level, subclass_name
    )

    highest_spell_level = max(spell_slots)
    available_spells = []

    for spell_level in range(1, highest_spell_level + 1):

        spells_at_level = get_available_spells(
            spellcasting_data["spell_list"], spell_level
        ) or []

        for spell_name in spells_at_level:

            if spell_name in known_spells:
                continue

            if not is_unrestricted:
                if spell_schools.get(spell_name) not in spellcasting_data["spell_school_restrictions"]:
                    continue

            available_spells.append((spell_name, spell_level))

    if not available_spells:
        print("No eligible replacement spells are available.")
        return

    print(f"\nChoose a replacement for {old_spell}:")

    for number, (spell_name, spell_level) in enumerate(available_spells, start=1):
        print(f"{number}. {spell_name} (Level {spell_level})")

    while True:
        choice = input("Choose a replacement spell number: ").strip()

        if not choice.isdigit() or not 1 <= int(choice) <= len(available_spells):
            print("Please choose a valid spell number.")
            continue

        new_spell, new_spell_level = available_spells[int(choice) - 1]

        known_spells[old_index] = new_spell

        if is_unrestricted:
            unrestricted_spells.discard(old_spell)
            unrestricted_spells.add(new_spell)

        print(
            f"You replaced {old_spell} with {new_spell} "
            f"(Level {new_spell_level})."
        )

        return


def choose_subclass_known_spells(character_class, character_level, subclass_name):
    spellcasting_data = get_subclass_spellcasting_data(
        character_class, subclass_name
    )

    total_spells = get_subclass_spells_known_count(
        character_class, character_level, subclass_name
    )

    if spellcasting_data is None or total_spells is None:
        return None

    known_spells = []
    unrestricted_spells = set()

    progression = spellcasting_data["spells_known_progression"]

    previous_total = 0

    for learning_level in range(3, character_level + 1):

        new_total = progression.get(learning_level, previous_total)

        new_spells = new_total - previous_total
        previous_total = new_total

        spell_slots = get_spell_slots(character_class, learning_level, subclass_name)

        highest_spell_level = max(spell_slots)

        allowed_schools = spellcasting_data["spell_school_restrictions"]
        unrestricted_levels = spellcasting_data["unrestricted_spell_levels"]

        for selection_number in range(1, new_spells + 1):

            unrestricted_choice = (
                learning_level in unrestricted_levels
                and (learning_level != 3 or selection_number == 3)
            )

            available_spells = []

            for spell_level in range(1, highest_spell_level + 1):

                spells_at_level = get_available_spells(spellcasting_data["spell_list"], spell_level) or []

                for spell_name in spells_at_level:

                    if spell_name in known_spells:
                        continue

                    if not unrestricted_choice:
                        if spell_schools.get(spell_name) not in allowed_schools:
                            continue

                    available_spells.append((spell_name, spell_level))

            if not available_spells:
                print("No eligible spells are available. Please check your spell data.")
                return None

            if unrestricted_choice:
                print("UNRESTRICTED SPELL CHOICE")

                print(
                    "This spell can be chosen from ANY school of magic "
                    "on the Wizard spell list."
                )

                if learning_level == 3:
                    print(
                        "At level 3, your first two spells must follow "
                        "your subclass's school restrictions, "
                        "but your third spell can come from any school."
                    )

                print(
                    "This is why more spells are available for this choice."
                )

            else:
                print(
                    "\nThis spell must follow your subclass's "
                    "school restrictions."
                )

            print(f"\nChoose spell {selection_number} of {new_spells} learned at {character_class} level {learning_level}:")

            for number, (spell_name, spell_level) in enumerate(available_spells, start=1):
                print(f"{number}. {spell_name} (Level {spell_level})")

            while True:
                choice = input("Choose a spell number: ").strip()

                if not choice.isdigit():
                    print("Please enter a valid number")
                    continue

                choice_number = int(choice)

                if not 1<= choice_number <= len(available_spells):
                    print("Please choose a number from the list")
                    continue

                selected_spell, selected_level = available_spells[choice_number - 1]

                known_spells.append(selected_spell)

                if unrestricted_choice:
                    unrestricted_spells.add(selected_spell)

                print(f"You have learned {selected_spell} (Level {selected_level})")

                break
        if learning_level >= 4:
            replace_subclass_known_spell(character_class, learning_level, subclass_name, known_spells, unrestricted_spells)

    return known_spells

def get_spell_slots(character_class, character_level,subclass_name=None):
    if (
        (character_class == "Fighter" and subclass_name == "Eldritch Knight")
        or
            (character_class == "Rogue" and subclass_name == "Arcane Trickster")
    ):
        if character_level < 3:
            return None

        eligible_levels = [
            level for level in third_caster_spell_slots
            if level <= character_level
        ]

        latest_level = max(eligible_levels)
        return third_caster_spell_slots[latest_level].copy()

    if character_class not in ("Wizard", "Cleric"):
        return None

    total_spell_slots = full_caster_spell_slots.get(character_level)

    return total_spell_slots.copy()


def calculate_arcane_recovery(character_class, character_level):
    if character_class != "Wizard":
        return None

    recovery_levels = (character_level + 1) // 2

    spell_slots = get_spell_slots(character_class, character_level)

    max_recoverable_slot_level = min(
        5,
        recovery_levels,
        max(spell_slots)
    )

    return {
        "total_levels": recovery_levels,
        "max_slot_level": max_recoverable_slot_level
    }


def get_cantrip_count(character_class, character_level, subclass_name=None):

    spellcasting = None

    if subclass_name is not None:
        spellcasting = get_subclass_spellcasting_data(
            character_class, subclass_name
        )

    if spellcasting is None:
        for class_data in character_classes.values():
            if class_data["name"] == character_class:
                spellcasting = class_data.get("spellcasting")
                break

    if spellcasting is None:
        return None

    progression = spellcasting.get("cantrip_progression", {})

    eligible_levels = [
        level for level in progression
        if level <= character_level
    ]

    if not eligible_levels:
        return None

    latest_level = max(eligible_levels)

    return progression[latest_level]

def choose_cantrips(character_class, cantrip_count, required_cantrips=None):
    if cantrip_count is None:
        return None

    available_cantrips = cantrip_lists[character_class]
    chosen_cantrips = list(required_cantrips or [])

    if required_cantrips:
        print(
            "\nThe following cantrip(s) are automatically granted "
            "by your subclass:"
        )

        for cantrip in required_cantrips:
            print(f"- {cantrip}")

    while len(chosen_cantrips) < cantrip_count:

        selectable_cantrips = [
            cantrip for cantrip in available_cantrips
            if cantrip not in chosen_cantrips
        ]

        required_count = len(required_cantrips or [])

        if required_count:
            print(
                f"\nChoose additional cantrip "
                f"{len(chosen_cantrips) - required_count + 1} "
                f"of {cantrip_count - required_count}:"
            )
        else:
            print(f"\nChoose cantrip {len(chosen_cantrips) + 1} of {cantrip_count}:")

        for number, cantrip in enumerate(selectable_cantrips, start=1):
            print(f"{number}. {cantrip}")

        choice = input("Enter a cantrip number: ").strip()

        if not choice.isdigit():
            print("Please enter a NUMBER!")
            continue

        choice_number = int(choice)

        if not 1 <= choice_number <= len(selectable_cantrips):
            print("Please choose a number from 1 to " + str(len(selectable_cantrips)))
            continue

        selected_cantrip = selectable_cantrips[choice_number - 1]

        if selected_cantrip in chosen_cantrips:
            print(f"You have already selected {selected_cantrip}, choose another cantrip!")
            continue

        chosen_cantrips.append(selected_cantrip)

    return chosen_cantrips

def calculate_wizard_spellbook_count(character_class, character_level):
    if character_class != "Wizard":
        return None

    starting_spells = 6

    level_difference = character_level - 1
    current_spells = (level_difference * 2) + starting_spells
    return current_spells

def get_max_spell_level(character_class, character_level):
    spell_slots = get_spell_slots(character_class, character_level)
    if spell_slots is None:
        return None

    max_spell_level = max(spell_slots.keys())
    return max_spell_level

def get_available_spells(character_class, spell_level):
    class_spells = spell_lists.get(character_class)

    if class_spells is None:
        return None

    available_spells = class_spells.get(spell_level)

    if available_spells is None:
        return None

    return available_spells.copy()


def choose_wizard_spellbook(character_class: str, character_level: int, subclass_name=None):
    if character_class != "Wizard":
        return None

    spellbook = []

    for current_level in range(1, character_level + 1):

        if current_level == 1:
            spells_to_choose = 6
        else:
            spells_to_choose = 2

        if (
            subclass_name == "School of Necromancy"
            and current_level == 6
        ):
            if "Animate Dead" not in spellbook:
                spellbook.append("Animate Dead")

                print("\nUndead Thralls:")
                print("Animate Dead has been added to your spellbook!")

        if (
            subclass_name == "School of Transmutation"
            and current_level == 10
        ):
            print("\nShapechanger:")

            if "Polymorph" not in spellbook:
                spellbook.append("Polymorph")
                print("Polymorph has been added to your spellbook!")

            print(
                "You can cast Polymorph once without using a spell slot, "
                "targeting only yourself and transforming into a beast "
                "of CR 1 or lower."
            )
            print("This special use recharges after a short or long rest.")

        highest_spell_level = get_max_spell_level(
            character_class, current_level
        )

        available_spells = []

        for spell_level in range(1, highest_spell_level + 1):

            spells_at_level = get_available_spells(
                character_class, spell_level
            )

            if spells_at_level is not None:

                for spell in spells_at_level:

                    if spell not in spellbook:
                        available_spells.append((spell, spell_level))

        for selection_number in range(1, spells_to_choose + 1):

            # Level 18: Ensure a 2nd-level spell for Spell Mastery.
            if current_level == 18 and selection_number == 2:

                level_two_spells = get_available_spells("Wizard", 2) or []

                has_level_two_spell = any(
                    spell in level_two_spells
                    for spell in spellbook
                )

                if not has_level_two_spell:

                    available_spells = [
                        (spell, level)
                        for spell, level in available_spells
                        if level == 2
                    ]

                    print(
                        "\nSpell Mastery requires a 2nd-level "
                        "spell in your spellbook. Choose one now."
                    )

            # Level 20: Ensure two 3rd-level Signature Spells.
            if current_level == 20:

                level_three_spells = get_available_spells("Wizard", 3) or []

                level_three_known = sum(
                    spell in level_three_spells
                    for spell in spellbook
                )

                spells_still_needed = max(
                    0,
                    2 - level_three_known
                )

                choices_remaining = (
                    spells_to_choose - selection_number + 1
                )

                if spells_still_needed >= choices_remaining:

                    available_spells = [
                        (spell, level)
                        for spell, level in available_spells
                        if level == 3
                    ]

                    print(
                        "\nSignature Spells requires two "
                        "3rd-level spells in your spellbook. "
                        "Choose a 3rd-level spell now."
                    )

            # Display available spells and ask for a selection.
            while True:

                print(
                    f"\nLevel {current_level} Spells - "
                    f"Choice {selection_number}/{spells_to_choose}"
                )

                for number, (spell_name, spell_level) in enumerate(
                    available_spells, start=1
                ):
                    print(
                        f"{number}. {spell_name} "
                        f"(Level {spell_level})"
                    )

                choice = input("Enter a spell number: ").strip()

                if not choice.isdigit():
                    print("Please enter a NUMBER!")
                    continue

                choice_number = int(choice)

                if not 1 <= choice_number <= len(available_spells):
                    print("Please choose a valid spell number!")
                    continue

                selected_spell, selected_level = available_spells.pop(
                    choice_number - 1
                )

                spellbook.append(selected_spell)

                print(f"You have learned {selected_spell}!")

                break

    return spellbook


def choose_wizard_spell_mastery(
    character_class, character_level, wizard_spellbook
):
    if character_class != "Wizard" or character_level < 18:
        return None

    spell_mastery = {}

    print("SPELL MASTERY:")

    for spell_level in (1, 2):

        spells_at_level = get_available_spells(
            "Wizard", spell_level
        ) or []

        available_spells = [
            spell for spell in wizard_spellbook
            if spell in spells_at_level
        ]

        if not available_spells:
            print(
                f"No level {spell_level} spells are in your spellbook. "
                "Cannot select Spell Mastery for this level."
            )
            continue

        print(f"\nChoose a level {spell_level} spell for Spell Mastery:")

        for number, spell in enumerate(available_spells, start=1):
            print(f"{number}. {spell}")

        while True:
            choice = input("Enter a spell number: ").strip()

            if not choice.isdigit():
                print("Please enter a NUMBER!")
                continue

            choice_number = int(choice)

            if not 1 <= choice_number <= len(available_spells):
                print("Please choose a valid spell number!")
                continue

            selected_spell = available_spells[choice_number - 1]

            spell_mastery[spell_level] = selected_spell

            print(f"Spell Mastery selected: {selected_spell}")

            break

    return spell_mastery


def choose_wizard_signature_spells(
    character_class, character_level, wizard_spellbook
):
    if character_class != "Wizard" or character_level < 20:
        return []

    level_three_spells = get_available_spells("Wizard", 3) or []

    available_spells = [
        spell for spell in wizard_spellbook
        if spell in level_three_spells
    ]

    if len(available_spells) < 2:
        print(
            "\nSignature Spells requires two 3rd-level "
            "spells in your spellbook."
        )
        return []

    signature_spells = []

    print("SIGNATURE SPELLS:")

    for selection_number in range(1, 3):

        print(
            f"\nChoose signature spell "
            f"{selection_number} of 2:"
        )

        for number, spell in enumerate(available_spells, start=1):
            print(f"{number}. {spell}")

        while True:
            choice = input("Enter a spell number: ").strip()

            if (
                not choice.isdigit()
                or not 1 <= int(choice) <= len(available_spells)
            ):
                print("Please choose a valid spell number.")
                continue

            selected_spell = available_spells.pop(int(choice) - 1)

            signature_spells.append(selected_spell)

            print(f"Signature spell selected: {selected_spell}")
            break

    return signature_spells


def calculate_prepared_spell_count(character_class, character_level, spellcasting_modifier):
    if character_class not in ("Wizard", "Cleric"):
        return None

    max_spells_prepared = character_level + spellcasting_modifier

    return max(1, max_spells_prepared)

def choose_prepared_spells(character_class, character_level, prepared_spell_count, wizard_spellbook=None, domain_spells=None, signature_spells=None):
    if character_class not in ("Wizard", "Cleric"):
        return None

    available_spells = []

    if character_class == "Wizard":
        available_spells = [
            spell for spell in wizard_spellbook
            if spell not in (signature_spells or [])
        ]

    elif character_class == "Cleric":
        max_spell_level = get_max_spell_level(character_class, character_level)

        for spell_level in range(1, max_spell_level + 1):

            spells_at_level = get_available_spells(character_class, spell_level)

            if spells_at_level is not None:
                available_spells.extend(spells_at_level)

        if domain_spells is not None:
            for spell in domain_spells:
                if spell in available_spells:
                    available_spells.remove(spell)

    prepared_spells = []

    for selection_number in range(1, prepared_spell_count + 1):

        while True:

            print(
                f"\nChoose a spell to prepare "
                f"{selection_number} of {prepared_spell_count}"
            )

            for number, spell in enumerate(available_spells, start=1):
                print(f"{number}. {spell}")

            choice = input("Enter a spell number: ").strip()

            if not choice.isdigit():
                print("Please enter a NUMBER!")
                continue

            choice_number = int(choice)

            if not 1 <= choice_number <= len(available_spells):
                print(
                    f"Please choose a number from 1 to {len(available_spells)}"
                )
                continue

            selected_spell = available_spells.pop(choice_number - 1)

            prepared_spells.append(selected_spell)

            print(f"You have prepared {selected_spell}!")

            break

    return prepared_spells

def get_cleric_domain_spells(character_class, character_level, subclass_name):

    if character_class != "Cleric":
        return None

    domain_spell_levels = cleric_domain_spell_lists.get(subclass_name)

    if domain_spell_levels is None:
        return []

    domain_spells = []

    for required_level, spells in domain_spell_levels.items():
        if character_level >= required_level:
            domain_spells.extend(spells)

    return domain_spells



def barbarian_starting_equipment():
    first_choice = choose_equipment_option(["Greataxe", "Any martial melee weapon"])
    if first_choice == "Greataxe":
        add_equipment(character_equipment, "Greataxe", 1)
    else:
        chosen_weapon = choose_starting_weapon("Martial Weapons", "Melee")
        add_equipment(character_equipment, chosen_weapon, 1)

    second_choice = choose_equipment_option(["Two Handaxes", "Any simple weapon"])
    if second_choice == "Two Handaxes":
        add_equipment(character_equipment, "Handaxe", 2)
    else:
        chosen_weapon = choose_starting_weapon("Simple Weapons")
        add_equipment(character_equipment, chosen_weapon, 1)

    add_equipment(character_equipment, "Explorer's Pack", 1)
    add_equipment(character_equipment, "Javelin", 4)

def wizard_starting_equipment():
    first_choice = choose_equipment_option(["Quarterstaff", "Dagger"])
    add_equipment(character_equipment, first_choice, 1)

    second_choice = choose_equipment_option(["Component Pouch", "Arcane Focus"])
    add_equipment(character_equipment, second_choice, 1)

    third_choice = choose_equipment_option(["Scholar's Pack", "Explorer's Pack"])
    add_equipment(character_equipment, third_choice, 1)

    add_equipment(character_equipment, "Spellbook", 1)

def rogue_starting_equipment():
    first_choice = choose_equipment_option(["Rapier", "Shortsword"])
    add_equipment(character_equipment, first_choice, 1)

    second_choice = choose_equipment_option(["Shortbow and 20 Arrows", "Shortsword"])
    if second_choice == "Shortbow and 20 Arrows":
        add_equipment(character_equipment, "Shortbow", 1)
        add_equipment(character_equipment, "Arrow", 20)
    else:
        add_equipment(character_equipment, "Shortsword", 1)

    third_choice = choose_equipment_option(["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"])
    add_equipment(character_equipment, third_choice, 1)

    add_equipment(character_equipment, "Leather Armour", 1)
    add_equipment(character_equipment, "Dagger", 2)
    add_equipment(character_equipment, "Thieves' Tools", 1)

def fighter_starting_equipment():
    first_choice = choose_equipment_option(["Chain Mail", "Leather Armour, Longbow and 20 Arrows"])
    if first_choice == "Chain Mail":
        add_equipment(character_equipment, "Chain Mail", 1)
    else:
        add_equipment(character_equipment, "Leather Armour", 1)
        add_equipment(character_equipment, "Longbow", 1)
        add_equipment(character_equipment, "Arrow", 20)

    second_choice = choose_equipment_option(["Martial weapon and Shield", "Two martial weapons"])
    if second_choice == "Martial weapon and Shield":
        chosen_weapon = choose_starting_weapon("Martial Weapons")
        add_equipment(character_equipment, chosen_weapon, 1)
        add_equipment(character_equipment, "Shield", 1)
    else:
        first_weapon = choose_starting_weapon("Martial Weapons")
        add_equipment(character_equipment, first_weapon, 1)

        second_weapon = choose_starting_weapon("Martial Weapons")
        add_equipment(character_equipment, second_weapon, 1)

    third_choice = choose_equipment_option(["Light Crossbow and 20 Bolts", "Two Handaxes"])
    if third_choice == "Light Crossbow and 20 Bolts":
        add_equipment(character_equipment, "Light Crossbow", 1)
        add_equipment(character_equipment, "Crossbow Bolt", 20)
    else:
        add_equipment(character_equipment, "Handaxe", 2)

    fourth_choice = choose_equipment_option(["Dungeoneer's Pack", "Explorer's Pack"])
    add_equipment(character_equipment, fourth_choice, 1)

def cleric_starting_equipment():
    first_options = ["Mace"]
    if "Martial Weapons" in known_weapon_proficiencies or "Warhammer" in known_weapon_proficiencies:
        first_options.append("Warhammer")

    first_choice = choose_equipment_option(first_options)
    add_equipment(character_equipment, first_choice, 1)

    second_options = ["Scale Mail", "Leather Armour"]
    if "Heavy Armour" in known_armour_proficiencies:
        second_options.append("Chain Mail")

    second_choice = choose_equipment_option(second_options)
    add_equipment(character_equipment, second_choice, 1)

    third_choice = choose_equipment_option(["Light Crossbow and 20 Bolts", "Any simple weapon"])
    if third_choice == "Light Crossbow and 20 Bolts":
        add_equipment(character_equipment, "Light Crossbow", 1)
        add_equipment(character_equipment, "Crossbow Bolt", 20)

    else:
        chosen_weapon = choose_starting_weapon("Simple Weapons")
        add_equipment(character_equipment, chosen_weapon, 1)

    fourth_choice = choose_equipment_option(["Priest's Pack", "Explorer's Pack"])
    add_equipment(character_equipment, fourth_choice, 1)

    add_equipment(character_equipment, "Shield", 1)
    add_equipment(character_equipment, "Holy Symbol", 1)


def stat_sheet():
    print('\nYour stats:')
    for character_stat, stat in character_stats.items():
        modifier = calculate_modifier(stat)
        print(f"{character_stat.capitalize()}: {stat} ({modifier:+})")

def stat_bonus_allocation(bonus, excluded_stat=None):
    while True:
        choice = input(f'Choose a stat to allocate +{bonus} to ').strip().lower()

        if choice not in character_stats:
            print("Please choose a valid stat!")

        elif choice == excluded_stat:
            print("You've already allocated this bonus to a stat! Choose another.")

        elif character_stats[choice] + bonus > 20:
            print("That increase would take your stat above 20! Choose another stat.")

        else:
            character_stats[choice] += bonus
            print(f"{choice.capitalize()} has increased to {character_stats[choice]}!")
            return choice

def character_race_creation():
    for number, race in character_races.items():
        print(f"{number}. {race["name"]}")
    while True:
        try:
            choice = int(input("choose your race 1-5: "))

            if choice in character_races:
                character_race = character_races[choice]["name"]

                if character_race == "Elf":
                    print(f"Ah, you have chosen to be an {character_race}!")
                else:
                    print(f"You have chosen to be a {character_race}!")


                return character_race

            else:
                print("Choose a valid race!")

        except ValueError:
            print("Please enter a NUMBER between 1 and 5!")

character_race = character_race_creation()

def character_subrace_selection():
    for race_details in character_races.values():
        if race_details["name"] == character_race:

            if race_details["subraces"]:
                print(f"Here are the {character_race}'s subraces:")
                for number, subrace in race_details["subraces"].items():
                    print(f"{number}. {subrace['name']}")
                while True:
                    try:
                        choice = int(input(f"choose a subrace between 1 and {len(race_details['subraces'])}: "))

                        if choice in race_details["subraces"]:
                            subrace = race_details["subraces"][choice]["name"]
                            if character_race == "Dragonborn":
                                print(f"You have chosen to be a {subrace} Dragonborn!")
                            else:
                                print(f"You have chosen to be a {subrace}!")

                            return subrace
                        else:
                            print("Choose a valid subrace!")

                    except ValueError:
                        print(f"Please enter a NUMBER between 1 and {len(race_details['subraces'])}!")

character_subrace =character_subrace_selection()





print(f'Okay {character_name}, tell me what starting class you wish to be? Are you a bruising barbarian, a sneaky rogue, or perhaps an intelligent wizard?')

def character_class_creation():
    for number, class_1 in character_classes.items():
        print(f"{number}. {class_1["name"]}")
    while True:
        try:
            choice = int(input("choose your class 1-5: "))

            if choice in character_classes:
                character_class = character_classes[choice]["name"]
                print(f"Marvellous! You have chosen to be a {character_class}!")

                return character_class

            else:
                print("Choose a valid class!")

        except ValueError:
            print("Please enter a NUMBER between 1 and 5!")

character_class = character_class_creation()

print(f''' 
=========================
YOUR CHARACTER (so far!) 
======================== 
Name: {character_name}
Race: {character_race}
Class: {character_class}
''')

print("""Welcome to the next stage of your adventure: Stats!

Every adventurer has six stats that determine their strengths, weaknesses and talents.

Physical stats
- Strength: Your physical power and athleticism.
- Dexterity: Your agility, coordination and reflexes.
- Constitution: Your stamina and endurance.

Mental stats
- Intelligence: Your knowledge, memory and book-smarts.
- Wisdom: Your awareness, intuition and street-smarts.
- Charisma: Your social confidence and ability to influence others.

How are your stats generated?
For each stat, four six-sided die are rolled and then we discard the lowest result and add the remaining three together.
Each stat sits between 3 and 18
We'll repeat this six times, then you'll get to assign your scores to the six abilities.

Now, adventurer... let the dice decide your fate! 🎲""")

def stat_generation(stat_number):
    dice_rolls = []
    print(f"\nRolling stat {stat_number} of 6...")
    for dice in range(4):
        roll = roll_dice(6)
        dice_rolls.append(roll)
    print('So, you rolled:', dice_rolls)

    lowest = min(dice_rolls)
    print(lowest, "is the lowest die and has been discarded.")

    dice_rolls.remove(lowest)
    stat_total = sum(dice_rolls)

    print(f"Your stat {stat_number} is:", stat_total)

    return stat_total

all_generated_character_stats = []

for number in range(1, 7):
    stat = stat_generation(number)
    all_generated_character_stats.append(stat)

print("\nSo far, these are your stats:")

for number, stat in enumerate(all_generated_character_stats, start=1):
    print(f"{number}. {stat}")

character_stats = {
    "strength": None,
    "dexterity": None,
    "constitution": None,
    "intelligence": None,
    "wisdom": None,
    "charisma": None,
}

used_score = set()

for character_stat in character_stats:
    while True:
        print("\nAvailable stats:")
        for number, stat in enumerate(all_generated_character_stats, start=1):
            if number not in used_score:
                print(f"{number}. {stat}")
        try:
            choice = int(input(f"\nAssign a stat for {character_stat} (1-6): "))

            if choice < 1 or choice > 6:
                print("please choose a number between 1 and 6!")

            elif choice in used_score:
                print("You've already allocated this roll to a stat! Choose another.")

            else:
                selected_score = all_generated_character_stats[choice - 1]
                character_stats[character_stat] = selected_score
                used_score.add(choice)
                break
        except ValueError:
            print("Please enter a NUMBER between 1 and 6!")


def calculate_modifier(stat):
        modifier = (stat - 10) // 2
        return modifier

if character_race == 'Human':
    for character_stat in character_stats:
        character_stats[character_stat]+= 1

    print('\nAs a human, all your stats have increased by +1!')

else:
    stat_sheet()

    print('Now you have your stats, you need to choose where to add your racial modifiers, you can choose one stat to add +2 and one stat to add +1.')
    plus_two_stat = stat_bonus_allocation(2)
    stat_bonus_allocation(1, plus_two_stat)
stat_sheet()


def character_background_creation():
    print("\nChoose your background:")
    for number, background_1 in character_backgrounds.items():
        print(f"{number}. {background_1["name"]}")
    while True:
        try:
            choice = int(input("\nSelect one using 1-5: "))

            if choice in character_backgrounds:
                character_background = character_backgrounds.get(choice)

                if character_background["name"][0].lower() in "aeiou":
                    article = "an"
                else:
                    article = "a"
                print(f"ahh! I hear you used to be/still are {article} {character_background["name"]}!")
                return character_background

            else:
                print("Choose a number for your background from the list!")

        except ValueError:
            print("Please enter a NUMBER between 1 and 5!")

character_background = character_background_creation()

character_appearance = input("Describe your character's physical appearance: ").strip()
character_backstory = input("Enter your character's backstory: ").strip()

def character_level_creation():
    while True:
        try:
            choice = int(input("choose your character's level from 1-20:"))
            if choice > 20 or choice < 1:
                print("Please choose a number between 1 and 20!")
            else:
                print(f"Your Character level is now {choice}")
                return choice

        except ValueError:
            print("Please enter a NUMBER between 1 and 20!")

character_level = character_level_creation()

earned_asi_levels = []

for class_data in character_classes.values():
    if class_data["name"] == character_class:
        for level, features in class_data["level_features"].items():
            if level <= character_level and "Ability Score Improvement" in features:
                earned_asi_levels.append(level)
        break

print(f"\nYou have earned {len(earned_asi_levels)} Ability Score Improvements.")

for asi_level in earned_asi_levels:
    print(f"\nAllocating your Level {asi_level} Ability Score Improvements.")
    stat_sheet()

    plus_two_options = []
    plus_one_options = []

    for stat_name, stat_value in character_stats.items():
        if stat_value <= 18:
            plus_two_options.append(stat_name)

        if stat_value <= 19:
            plus_one_options.append(stat_name)

    if not plus_two_options and len(plus_one_options) < 2:
        print("All available ability scores are too high to allocate this ability score improvement!")
        print("Fear not adventurer, this ability score Improvement shall remain unused!")
        continue

    while True:
        print("\nHow would you like to allocate this ASI?")
        print("1. Increase one stat by +2")
        print("2. Increase two stats by +1 each")

        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":

            if not plus_two_options:
                print("No stat can receive a +2 bonus. Choose option 2 please.")
                continue

            stat_bonus_allocation(2)
            break

        elif choice == "2":

            if len(plus_one_options) < 2:
                print("You need two different stats that can receive +1.")
                print("Choose option 1 please.")
                continue

            first_stat = stat_bonus_allocation(1)
            stat_bonus_allocation(1, first_stat)
            break

        else:
            print("It was a simple question, 1 or 2...")

if character_class == "Barbarian" and character_level == 20:
    print("\nPRIMAL CHAMPION!")
    print("Your strength and constitution increase by 4, up to a max of 24 - enjoy!")

    for stat in ["strength", "constitution"]:
        character_stats[stat] = min(24, character_stats[stat] + 4)
        print(f"{stat.capitalize()} is now {character_stats[stat]}!")

    stat_sheet()

character_modifiers = {}

for stat_name, stat_value in character_stats.items():
    character_modifiers[stat_name] = calculate_modifier(stat_value)



def calculate_proficiency_bonus(level):
    if level <= 4:
        return 2
    elif level <= 8:
        return 3
    elif level <= 12:
        return 4
    elif level <= 16:
        return 5
    else:
        return 6
proficiency_bonus = calculate_proficiency_bonus(character_level)
print(f"Your proficiency bonus is {proficiency_bonus:+}")


racial_spells = get_racial_spells(
    character_race,
    character_subrace,
    character_level
)

racial_cantrip = choose_racial_cantrip(
    character_race,
    character_subrace
)

if racial_cantrip is not None:
    racial_spells.append(racial_cantrip)

racial_spellcasting_ability = get_racial_spellcasting_ability(
    character_race,
    character_subrace
)

racial_spellcasting_modifier = None
racial_spell_save_dc = None
racial_spell_attack_bonus = None

if racial_spellcasting_ability is not None:
    racial_spellcasting_modifier = character_modifiers[
        racial_spellcasting_ability
    ]

    racial_spell_save_dc = calculate_spell_save_dc(
        proficiency_bonus,
        racial_spellcasting_modifier
    )

    racial_spell_attack_bonus = calculate_spell_attack_bonus(
        proficiency_bonus,
        racial_spellcasting_modifier
    )

racial_spell_details = []

for spell in racial_spells:

    if spell in ("Dancing Lights", "Thaumaturgy") or spell == racial_cantrip:
        usage = "At will"

    else:
        usage = "Once per long rest"

    casting_level = 2 if (
        character_race == "Tiefling"
        and spell == "Hellish Rebuke"
    ) else None

    racial_spell_details.append({
        "name": spell,
        "usage": usage,
        "casting_level": casting_level
    })


spellcasting_modifier = get_spell_casting_modifier(character_class, character_modifiers)

spell_save_dc = calculate_spell_save_dc(proficiency_bonus, spellcasting_modifier)

spell_attack_bonus = calculate_spell_attack_bonus(proficiency_bonus, spellcasting_modifier)

spell_slots = get_spell_slots(character_class, character_level)

arcane_recovery = calculate_arcane_recovery(
    character_class,
    character_level
)

cantrip_count = get_cantrip_count(character_class, character_level)

if cantrip_count is not None:
    chosen_cantrips = choose_cantrips(character_class, cantrip_count)
    print(f"You have chosen: {chosen_cantrips}")
else:
    chosen_cantrips = None

wizard_spellbook_count = calculate_wizard_spellbook_count(character_class, character_level)

if wizard_spellbook_count is not None:
    print(f"Wizard spells from normal progression: {wizard_spellbook_count}")

max_spell_level = get_max_spell_level(character_class, character_level)
if max_spell_level is not None:
    print(f"Max spell level: {max_spell_level}")



saving_throw_proficiencies = []

for class_data in character_classes.values():
    if class_data["name"] == character_class:
        saving_throw_proficiencies = class_data["saving_throw_proficiencies"].copy()
        break

if character_class == "Rogue" and character_level >= 15:
    saving_throw_proficiencies.append("Wisdom")

saving_throw_bonuses = {}

for stat_name, modifier in character_modifiers.items():
    saving_throw_bonuses[stat_name] = modifier
    if stat_name.capitalize() in saving_throw_proficiencies:
        saving_throw_bonuses[stat_name] = modifier + proficiency_bonus

print("\nYour saving throw bonuses:")

for stat_name, bonus in saving_throw_bonuses.items():
    print(f"{stat_name.capitalize()}: {bonus:+}")

for class_details in character_classes.values():
    if class_details["name"] == character_class:
        hit_die = class_details["hit_die"]
        break

def character_subclass_selection(character_class, character_level):
    for class_data in character_classes.values():
        if class_data["name"] == character_class:
            character_class = class_data
            break
    subclass_level = character_class["subclass_level"]

    if character_level < subclass_level:
        return None

    print("\nChoose your subclass:")

    for number, subclass in character_class["subclasses"].items():
        print(f"{number}. {subclass["name"]}")
    while True:
        try:
            choice = int(input("\n Choose a subclass by its number: "))

            if choice in character_class["subclasses"]:
                selected_subclass = character_class["subclasses"][choice]

                print(f"You have chosen the {selected_subclass["name"]} subclass!")
                return selected_subclass
            else:
                print("Please choose a valid number!")

        except ValueError:
            print("Please enter a NUMBER!")

character_subclass = character_subclass_selection(character_class, character_level)

subclass_name = (
    character_subclass["name"]
    if character_subclass is not None
    else None
)

chosen_totems = choose_totem_animals(character_class, subclass_name, character_level)

if character_class == "Wizard" and subclass_name == "School of Illusion":

    if "Minor Illusion" not in chosen_cantrips:
        chosen_cantrips.append("Minor Illusion")

        print("\nImproved Minor Illusion:")
        print("You have learned Minor Illusion as a bonus cantrip!")

    else:
        print("\nImproved Minor Illusion:")
        print("You already know Minor Illusion.")
        print("Choose another Wizard cantrip instead.")

        while True:
            bonus_cantrip = choose_cantrips("Wizard", 1)[0]

            if bonus_cantrip not in chosen_cantrips:
                chosen_cantrips.append(bonus_cantrip)

                print(f"You have learned {bonus_cantrip} as a bonus cantrip!")
                break

            print("You already know that cantrip. Choose another.")


subclass_spellcasting = get_subclass_spellcasting_data(character_class, subclass_name)

if subclass_spellcasting is not None:
    spellcasting_modifier = get_spell_casting_modifier(
        character_class, character_modifiers, subclass_name
    )

    spell_save_dc = calculate_spell_save_dc(
        proficiency_bonus, spellcasting_modifier
    )

    spell_attack_bonus = calculate_spell_attack_bonus(
        proficiency_bonus, spellcasting_modifier
    )

if subclass_spellcasting is not None:

    cantrip_count = get_cantrip_count(character_class, character_level, subclass_name)

    required_cantrips = subclass_spellcasting.get("required_cantrips", [])

    chosen_cantrips = choose_cantrips(
        subclass_spellcasting["spell_list"],
        cantrip_count,
        required_cantrips
    )

    print(f"You have chosen: {chosen_cantrips}")

known_spells = None

if subclass_spellcasting is not None:

    spell_slots = get_spell_slots(
        character_class, character_level, subclass_name
    )

    max_spell_level = max(spell_slots) if spell_slots else None

    known_spells = choose_subclass_known_spells(
        character_class, character_level, subclass_name
    )

wizard_spellbook = choose_wizard_spellbook(
    character_class, character_level, subclass_name
)

spell_mastery = choose_wizard_spell_mastery(
    character_class,
    character_level,
    wizard_spellbook
)

signature_spells = choose_wizard_signature_spells(
    character_class,
    character_level,
    wizard_spellbook
)

prepared_spell_count = calculate_prepared_spell_count(
    character_class, character_level, spellcasting_modifier
)

domain_spells = get_cleric_domain_spells(
    character_class, character_level, subclass_name
)

if character_class == "Cleric" and subclass_name == "Light Domain":

    if "Light" not in chosen_cantrips:
        chosen_cantrips.append("Light")
        print("\nLight Domain bonus cantrip: Light")

if character_class == "Cleric" and subclass_name == "Nature Domain":

    while True:

        nature_cantrip = choose_cantrips("Druid", 1)[0]

        if nature_cantrip not in chosen_cantrips:

            chosen_cantrips.append(nature_cantrip)

            print(f"\nNature Domain bonus cantrip: {nature_cantrip}")

            break

        print("You already know that cantrip. Choose another.")


if prepared_spell_count is not None:

    prepared_spells = choose_prepared_spells(
        character_class,
        character_level,
        prepared_spell_count,
        wizard_spellbook=wizard_spellbook,
        domain_spells=domain_spells,
        signature_spells=signature_spells
    )

else:
    prepared_spells = None

all_prepared_spells = None

if prepared_spells is not None:
    all_prepared_spells = (
        prepared_spells
        + (domain_spells or [])
        + signature_spells
    )


if racial_spell_details:

    print("\nRACIAL SPELLCASTING")

    print(f"Spellcasting Ability: {racial_spellcasting_ability.title()}")
    print(f"Spellcasting Modifier: {racial_spellcasting_modifier:+}")
    print(f"Spell Save DC: {racial_spell_save_dc}")
    print(f"Spell Attack Bonus: {racial_spell_attack_bonus:+}")

    print("\nRacial Spells:")

    for spell in racial_spell_details:

        spell_description = f"- {spell['name']} ({spell['usage']})"

        if spell["casting_level"] is not None:
            spell_description += (
                f" - Cast at spell level {spell['casting_level']}"
            )

        print(spell_description)


if spellcasting_modifier is not None:

    print("\nSPELLCASTING")

    print(f"Spellcasting modifier: {spellcasting_modifier:+}")
    print(f"Spell Save DC: {spell_save_dc}")
    print(f"Spell Attack Bonus: {spell_attack_bonus:+}")
    print(f"Highest Spell Level: {max_spell_level}")

    print(f"\nCantrips Known ({len(chosen_cantrips)}):")
    for cantrip in chosen_cantrips:
        print(f"- {cantrip}")

    if known_spells is not None:
        print(f"\nSpells Known ({len(known_spells)}):")

        for spell in known_spells:
            print(f"- {spell}")

    print("\nSpell Slots:")
    for spell_level, slot_count in spell_slots.items():
        print(f"- Level {spell_level}: {slot_count} slots")

    if arcane_recovery is not None:

        print("\nArcane Recovery:")

        print(
            f"Recover up to "
            f"{arcane_recovery['total_levels']} "
            f"total spell-slot levels."
        )

        print(
            f"Highest recoverable slot level: "
            f"{arcane_recovery['max_slot_level']}"
        )

        print("Usable once per day after finishing a short rest.")
        print("Only expended spell slots can be recovered.")

    if wizard_spellbook is not None:

        print(f"\nWizard Spellbook ({len(wizard_spellbook)} spells):")

        for spell in wizard_spellbook:
            print(f"- {spell}")

    if prepared_spells is not None:

        print(
            f"\nChosen Prepared Spells "
            f"({len(prepared_spells)}/{prepared_spell_count}):"
        )

        for spell in prepared_spells:
            print(f"- {spell}")

    if domain_spells:

        print("\nDomain Spells (Always Prepared):")

        for spell in domain_spells:
            print(f"- {spell}")

    if all_prepared_spells is not None:
        print(
            f"\nTotal Prepared Spells: "
            f"{len(all_prepared_spells)}"
        )


    if signature_spells:

        print("\nSignature Spells (Always Prepared):")

        for spell in signature_spells:
            print(f"- {spell}")

        print(
            "Each spell can be cast once at 3rd level "
            "without expending a spell slot."
        )
        print("Each use recharges after a short or long rest.")

    if spell_mastery:

        print("\nSpell Mastery:")

        for spell_level, spell in spell_mastery.items():

            is_prepared = (
                prepared_spells is not None
                and spell in prepared_spells
            )

            preparation_status = (
                "Prepared" if is_prepared else "Not prepared"
            )

            print(
                f"- Level {spell_level}: {spell} "
                f"({preparation_status})"
            )

        print(
            "These spells can be cast at their lowest level "
            "without expending a spell slot while prepared."
        )


chosen_fighting_styles = choose_fighting_styles(character_class, character_level, subclass_name)

superiority_dice = calculate_superiority_dice(
    character_class, character_level, subclass_name
)

manoeuvres_known = calculate_manoeuvres_known(
    character_class, character_level, subclass_name
)

chosen_manoeuvres = choose_manoeuvres(manoeuvres_known)

manoeuvre_save_dc = None

if superiority_dice is not None:
    while True:
        chosen_ability = input("Choose to use strength or dexterity for your manoeuvre save DC: ").strip().lower()

        if chosen_ability in ("strength", "dexterity"):
            break

        print("Please enter strength or dexterity for your manoeuvre save DC:")

    chosen_modifier = character_modifiers[chosen_ability]

    manoeuvre_save_dc = calculate_manoeuvre_save_dc(character_class, character_level, subclass_name, proficiency_bonus, chosen_modifier)

if superiority_dice is not None:
    number_of_dice, die_size = superiority_dice

    print(f"""\nBATTLE MASTER FEATURES:
Superiority Dice: {number_of_dice}{die_size}
Superiority Dice Recovery: short or long rest
Manouevre Save DC: {manoeuvre_save_dc}
Manoeuvres Known: {manoeuvres_known}""")
    print("\nChosen Manoeuvres:")

    for manoeuvre in chosen_manoeuvres:
        description = battle_master_manoeuvres[manoeuvre]["description"]
        print(f" {manoeuvre}: {description}")


remarkable_athlete_bonus = calculate_remarkable_athlete_bonus(
    character_class,
    character_level,
    subclass_name,
    proficiency_bonus
)

champion_critical_range = calculate_champion_critical_range(character_class, character_level, subclass_name)

channel_divinity_uses = calculate_channel_divinity_uses(character_class, character_level)
if channel_divinity_uses is not None:
    print(f"\nAs a cleric, you have {channel_divinity_uses} use(s) of channel divinity, use it wisely! ")

destroy_undead_cr = calculate_destroy_undead_cr(character_class, character_level)
if destroy_undead_cr is not None:
    print(f"\nYour destroy undead CR is {destroy_undead_cr}")

divine_intervention_chance = calculate_divine_intervention_chance(character_class, character_level)
if divine_intervention_chance is not None:
    print(f"\nYour divine intervention chance is {divine_intervention_chance}")

preserve_life_pool = calculate_preserve_life_pool(character_class, character_level, subclass_name)
if preserve_life_pool is not None:
    print(f"\nYour preserve life pool has {preserve_life_pool} points")

radiance_of_the_dawn_damage = calculate_radiance_of_the_dawn_damage(character_class, character_level, subclass_name)
if radiance_of_the_dawn_damage is not None:
    print(f"\nYour radiance of the dawn damage is {radiance_of_the_dawn_damage}")

dragonborn_breath_damage = calculate_dragonborn_breath_damage(character_race, character_level)
dragonborn_breath_damage_type = get_dragonborn_breath_damage_type(character_race, character_subrace)
dragonborn_breath_save_dc = calculate_dragonborn_breath_save_dc(character_race, proficiency_bonus, character_modifiers["constitution"])
dragonborn_breath_shape, dragonborn_breath_save_ability = get_dragonborn_breath_details(character_race, character_subrace)

if character_race == "Dragonborn":
    print("\nDRAGONBORN BREATH WEAPON")
    print(f"Damage: {dragonborn_breath_damage} {dragonborn_breath_damage_type}")
    print(f"Area: {dragonborn_breath_shape}")
    print(f"Saving Throw: {dragonborn_breath_save_ability.capitalize()} DC {dragonborn_breath_save_dc}")
    print("You can use your breath weapon once per short or long rest and if the enemy passes your saving throw they take half ot the total damage rolled.")

second_wind_healing = calculate_second_wind_healing(character_class, character_level)

if character_class == "Fighter":
    print(f"\nYour second wind healing is {second_wind_healing} HP")

action_surge_uses = calculate_action_surge_uses(character_class, character_level)

if character_class == "Fighter" and action_surge_uses is not None:
    print(f"\nYou have {action_surge_uses} action surge uses at level {character_level}. It recovers after a long or short rest.")

indomitable_uses = calculate_indomitable_uses(character_class, character_level)
if character_class == "Fighter" and indomitable_uses is not None:
    print(f"\nYou have {indomitable_uses} uses of indomitable.")

rage_uses = calculate_rage_uses(character_class, character_level)
if rage_uses is not None:
    print(f"\nYou have {rage_uses} rages per long rest.")

print("""\n 
===================
Hit Points (HP) 
==================

Hit points show how much damage your character can take before falling unconscious. 

If your character falls below to zero HP or lower then they will be unconscious and have to roll death saving throws to stay alive. 

At level 1, your HP is calculated by your constitution stat-bonus, added to your classes hit die. 

Every additional level gained gives you more HP to reflect your character getting tougher, you roll your character's hit die and add your constitution stat-bonus to determine your new max HP.

Did you know: some DMS consider catastrophic damage a rule, where if your character drops below their HP in the negative value then they instantly die! Be careful, adventurer...

""")

def calculate_hit_points(level, hit_die, constitution_modifier):
    first_level_hp = max(1, hit_die + constitution_modifier)
    print(f'Your starting HP at Level 1 is {first_level_hp}!')
    print(f"Your final constitution modifier is {constitution_modifier:+} - we use this when you level up to add to the HP roll!")
    total_hp = first_level_hp

    for current_level in range(2, level + 1):
        print(f"\nGenerating HP for level {current_level}...")
        hp_roll = roll_dice(hit_die)
        print(f"\nrolled {hp_roll} on a d{hit_die}")


        new_level_hp_bonus = max(1, hp_roll + constitution_modifier)
        print(f"Your level {current_level} HP increase is +{new_level_hp_bonus}!")


        total_hp += new_level_hp_bonus
        print(f"Your total HP at Level {current_level} is now {total_hp}!")

    if character_subrace == "Hill Dwarf":
        total_hp += level
        print(f"\nDwarven Toughness grants you {level} more HP!")

    print(f"\nYour final maximum HP at level {level} is {total_hp}!")
    return total_hp

character_hp = calculate_hit_points(character_level, hit_die, character_modifiers["constitution"])

initiative_bonus = character_modifiers["dexterity"]

if remarkable_athlete_bonus is not None:
    initiative_bonus += remarkable_athlete_bonus


print(f"""\n To determine how quickly your character reacts to combat, you will need to roll initiative when your DM asks! 

Your initiative bonus is {initiative_bonus:+}! 
Add this to your roll for that sweet added bonus!""")

for race_details in character_races.values():
    if race_details["name"] == character_race:
        movement_speed = race_details["speed"]

        if character_subrace == "Wood Elf":
            movement_speed = race_details["subraces"][2]["speed"]

        break


if character_race == "Dragonborn":
    display_race = f"{character_subrace} Dragonborn"
elif character_subrace:
    display_race = character_subrace
else:
    display_race = character_race

if display_race[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"


for languages in character_races.values():
    if languages["name"] == character_race:
        known_character_languages = languages["languages"].copy()
        extra_languages = languages.get("extra_languages", 0)

        extra_languages += character_background.get("extra_languages", 0)

        if character_subclass is not None:
            extra_languages += character_subclass.get("extra_languages", 0)

        for subrace in languages["subraces"].values():
            if subrace["name"] == character_subrace:
                extra_languages += subrace.get("extra_languages", 0)
                break

        if extra_languages > 0:
            print(f"\nYou can choose {extra_languages} additional language(s)!")



            for language_choice in range(extra_languages):
                print(f"\nChoose language {language_choice + 1} of {extra_languages}:")
                print("Here is a list of available languages:")

                selectable_languages = []

                for language in available_languages:
                    if language not in known_character_languages:
                        selectable_languages.append(language)

                for number, language in enumerate(selectable_languages, start=1):
                    print(f"{number}. {language}")
                while True:
                    try:
                        choice = int(input(f"Choose a language by its number: "))

                        if 1 <= choice <= len(selectable_languages):
                            selected_language = selectable_languages[choice - 1]
                            known_character_languages.append(selected_language)

                            print(f"You have chosen to learn {selected_language}!")
                            break
                        else:
                            print("Please choose a valid number!")

                    except ValueError:
                        print("Please enter a NUMBER!")


        break

if character_class == "Rogue":
    known_character_languages.append("Thieves' Cant")

print("\nYour character knows the following languages:")

for language in known_character_languages:
    print(f"- {language}")

known_character_skills = []
expertise_skills = []
expertise_tools = []
known_character_tools = []

character_equipment = {}
equipped_armour = None
equipped_shield = False
equipped_weapons = []

for race in character_races.values():
    if race["name"] == character_race:
        known_character_skills.extend(race.get("skill_proficiencies", []))
        break

known_character_skills.extend(character_background.get("skill_proficiencies", []))

print("\n Your starting skill proficiencies:")
for skill in known_character_skills:
    print(f"- {skill}")

available_skill_choices = []
for classes in character_classes.values():
    if classes["name"] == character_class:
        for skill in classes["skill_choices"]["options"]:
            if skill not in known_character_skills:
                available_skill_choices.append(skill)

        skill_choice_amount = classes["skill_choices"]["amount"]
        for skill_choice in range(skill_choice_amount):
            print(f"\nChoose skill {skill_choice + 1} of {skill_choice_amount}:")
            for number, skill in enumerate(available_skill_choices, start=1):
                print(f"{number}. {skill}")
            while True:
                try:
                    choice = int(input(f"Choose a skill by its number to be proficient in: "))
                except ValueError:
                    print("please enter a NUMBER!")
                    continue

                if 1 <= choice <= len(available_skill_choices):
                   break
                else:
                   print("Please choose a number listed in the menu!")

            selected_skill = available_skill_choices[choice - 1]
            known_character_skills.append(selected_skill)
            available_skill_choices.remove(selected_skill)

        break
if character_class == "Cleric":
    if character_subclass is not None:
        if character_subclass["name"] == "Knowledge Domain":
            if character_level >= 1:

                knowledge_skill_options = ["Arcana", "History", "Nature", "Religion"]

                available_knowledge_skills = knowledge_skill_options.copy()

                for skill_choice in range(2):
                    print(f"\nChoose Knowledge Skill {skill_choice + 1} of 2:")

                    for number, skill in enumerate(available_knowledge_skills, start=1):
                        print(f"{number}. {skill}")

                    while True:
                        try:
                            choice = int(input(f"Choose a skill by its number to be proficient in: "))
                        except ValueError:
                            print("please enter a NUMBER!")
                            continue

                        if 1 <= choice <= len(available_knowledge_skills):
                            break
                        else:
                            print("Please choose a number listed in the menu!")

                    selected_skill = available_knowledge_skills[choice - 1]


                    if selected_skill not in known_character_skills:
                        known_character_skills.append(selected_skill)

                    if selected_skill not in expertise_skills:
                        expertise_skills.append(selected_skill)

                    available_knowledge_skills.remove(selected_skill)


if character_class == "Cleric":
    if character_subclass is not None:
        if character_subclass["name"] == "Nature Domain":
            if character_level >= 1:
                available_nature_skills = []
                nature_skill_options = ["Animal Handling", "Nature", "Survival"]

                for skill in nature_skill_options:
                    if skill not in known_character_skills:
                        available_nature_skills.append(skill)

                if not available_nature_skills:
                    print("\nYou are already proficient in all three Nature Domain Skills!")
                    print("Choose a different skill:")

                    for skill in all_skill_options:
                        if skill not in known_character_skills:
                            available_nature_skills.append(skill)

                if available_nature_skills:
                    print("\nChoose 1 Skill proficiency:")

                    for number, skill in enumerate(available_nature_skills, start=1):
                        print(f"{number}. {skill}")

                    while True:
                        try:
                            choice = int(input(f"Choose a skill by its number to be proficient in: "))
                        except ValueError:
                            print("please enter a NUMBER!")
                            continue

                        if 1 <= choice <= len(available_nature_skills):
                            break
                        else:
                            print("Please choose a number listed in the menu!")

                    selected_skill = available_nature_skills[choice - 1]

                    if selected_skill not in known_character_skills:
                        known_character_skills.append(selected_skill)

                else:
                    print("You have every skill proficiency in the game, fucking nerd...")


def choose_tools(tool_options, amount):
    available_tool_choices = tool_options.copy()

    for tool in known_character_tools:
        if tool in available_tool_choices:
            available_tool_choices.remove(tool)

    for tool_choice in range(amount):
        print(f"\nChoose Tool {tool_choice + 1} of {amount}:")

        for number, tool in enumerate(available_tool_choices, start=1):
            print(f"{number}. {tool}")

        while True:
            try:
                choice = int(input("Choose a tool by its number to be proficient in: "))
            except ValueError:
                print("Please enter a NUMBER!")
                continue

            if 1 <= choice <= len(available_tool_choices):
                break
            else:
                print("Please choose a number listed in the menu!")

        selected_tool = available_tool_choices[choice - 1]

        known_character_tools.append(selected_tool)
        available_tool_choices.remove(selected_tool)


for race in character_races.values():
    if race["name"] == character_race:
        for tool in race.get("tool_proficiencies", []):
            if tool not in known_character_tools:
                known_character_tools.append(tool)
        break

for tool in character_background.get("tool_proficiencies", []):
    if tool not in known_character_tools:
        known_character_tools.append(tool)

for classes in character_classes.values():
    if classes["name"] == character_class:
        for tool in classes["tool_proficiencies"]:
            if tool not in known_character_tools:
                known_character_tools.append(tool)
        break


background_tools_choices = character_background.get("tool_choices", {})

for tool_category, tool_choice_amount in background_tools_choices.items():
    choose_tools(available_tool_types[tool_category], tool_choice_amount)

if character_race == "Dwarf":
    dwarf_tools = [
        "Smith's Tools",
        "Brewer's Supplies",
        "Mason's Tools"
    ]

    choose_tools(dwarf_tools, 1)

if character_class == "Fighter":
    if character_subclass is not None:
        if character_subclass["name"] == "Battle Master":
            if character_level >= 3:
                choose_tools(available_tool_types["Artisan's Tools"], 1)


if character_class == "Rogue":
    if character_subclass is not None:
        if character_subclass["name"] == "Assassin":
            if character_level >= 3:
                for tool in ["Disguise Kit", "Poisoner's Kit"]:
                    if tool not in known_character_tools:
                        known_character_tools.append(tool)


print("\nKnown tool proficiencies:", known_character_tools)

if character_class == "Rogue":
    if character_level >= 1:
        print("\nAs a rogue, you gain expertise at Level 1!")

        available_expertise_skills = []

        for skill in known_character_skills:
            if skill not in expertise_skills:
                available_expertise_skills.append(skill)

        if "Thieves' Tools" in known_character_tools:
            if "Thieves' Tools" not in expertise_tools:
                available_expertise_skills.append("Thieves' Tools")


        expertise_choices_made = 0
        while expertise_choices_made < 2:
            print("\nChoose your Rogue Expertise Proficiencies:")

            for number, option in enumerate(available_expertise_skills, start=1):
                print(f"{number}. {option}")

            choice = input("\nChoose an expertise proficiency with the numbers in the list: ")
            if not choice.isdigit():
                print("Please enter a NUMBER!")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(available_expertise_skills):
                print("Please choose an expertise proficiency with the NUMBERS in the LIST!")
                continue

            selected_expertise = available_expertise_skills[choice - 1]

            if selected_expertise == "Thieves' Tools":
                expertise_tools.append(selected_expertise)
            else:
                expertise_skills.append(selected_expertise)

            available_expertise_skills.remove(selected_expertise)

            expertise_choices_made += 1
            print(f"Expertise gained: {selected_expertise}")

        print("\nExpertise skills:", expertise_skills)
        print("Expertise tools:", expertise_tools)

    if character_level >=6:
        print("\nAs a rogue, you gain two more expertise at Level 6!")
        available_expertise_skills = []

        for skill in known_character_skills:
            if skill not in expertise_skills:
                available_expertise_skills.append(skill)

        if "Thieves' Tools" in known_character_tools and "Thieves' Tools" not in expertise_tools:
            available_expertise_skills.append("Thieves' Tools")

        expertise_choices_made = 0

        while expertise_choices_made < 2:
            print("\nChoose your Level 6 Rogue Expertise Proficiencies:")

            for number, option in enumerate(available_expertise_skills, start=1):
                print(f"{number}. {option}")

            choice = input("\nChoose an expertise proficiency with the numbers in the list: ")

            if not choice.isdigit():
                print("Please enter a NUMBER!")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(available_expertise_skills):
                print("Please choose an expertise proficiency with the NUMBERS in the LIST!")
                continue

            selected_expertise = available_expertise_skills[choice - 1]

            if selected_expertise == "Thieves' Tools":
                expertise_tools.append(selected_expertise)
            else:
                expertise_skills.append(selected_expertise)

            available_expertise_skills.remove(selected_expertise)

            expertise_choices_made += 1
            print(f"Expertise gained: {selected_expertise}")

skill_bonuses = {}

for skill_name, ability_name in skill_abilities.items():
    modifier = character_modifiers[ability_name]
    skill_bonuses[skill_name] = modifier

    if skill_name in expertise_skills:
        skill_bonuses[skill_name] = modifier + (proficiency_bonus * 2)

    elif skill_name in known_character_skills:
        skill_bonuses[skill_name] = modifier + proficiency_bonus

    elif remarkable_athlete_bonus is not None and ability_name in ("strength", "dexterity", "constitution"):
        skill_bonuses[skill_name] = modifier + remarkable_athlete_bonus

print("\nYour Skill proficiencies and bonuses:")
for skill,bonus in skill_bonuses.items():
    if skill in expertise_skills:
        print(f"- {skill}: {bonus:+} (Expertise)")
    elif skill in known_character_skills:
        print(f"- {skill}: {bonus:+} (Proficient)")
    elif remarkable_athlete_bonus is not None and skill_abilities[skill] in ("strength", "dexterity", "constitution"):
        print(f"- {skill}: {bonus:+} (Remarkable Athlete)")
    else:
        print(f"- {skill}: {bonus:+}")



print('\nYour tools proficiencies:')
for tool in known_character_tools:
    if tool in expertise_tools:
        print(f"- {tool} (Expertise)")
    else:
        print(f"- {tool} (Proficient)")


known_armour_proficiencies = []
known_weapon_proficiencies = []

for class_details in character_classes.values():
    if class_details["name"] == character_class:
        known_armour_proficiencies.extend(class_details.get("armour_proficiencies", []))
        known_weapon_proficiencies.extend(class_details.get("weapon_proficiencies", []))
        break

for race_details in character_races.values():
    if race_details["name"] == character_race:

        for armour in race_details.get("armour_proficiencies", []):
            if armour not in known_armour_proficiencies:
                known_armour_proficiencies.append(armour)

        for weapon in race_details.get("weapon_proficiencies", []):
            if weapon not in known_weapon_proficiencies:
                known_weapon_proficiencies.append(weapon)

        for subrace_details in race_details["subraces"].values():
            if subrace_details["name"] == character_subrace:

                for armour in subrace_details.get("armour_proficiencies", []):
                    if armour not in known_armour_proficiencies:
                        known_armour_proficiencies.append(armour)

                for weapon in subrace_details.get("weapon_proficiencies", []):
                    if weapon not in known_weapon_proficiencies:
                        known_weapon_proficiencies.append(weapon)

                break

        break


if character_subclass is not None:
    for armour in character_subclass.get("armour_proficiencies", []):
        if armour not in known_armour_proficiencies:
            known_armour_proficiencies.append(armour)

    for weapon in character_subclass.get("weapon_proficiencies", []):
        if weapon not in known_weapon_proficiencies:
            known_weapon_proficiencies.append(weapon)



filtered_weapon_proficiencies = []
for weapon in known_weapon_proficiencies:
    category = weapon_data.get(weapon, {}).get("category")
    if category not in known_weapon_proficiencies:
        filtered_weapon_proficiencies.append(weapon)

known_weapon_proficiencies = filtered_weapon_proficiencies

print("\nArmour proficiencies:", known_armour_proficiencies)
print("Weapon proficiencies:", known_weapon_proficiencies)

if character_class == "Barbarian":
    barbarian_starting_equipment()
if character_class == "Wizard":
    wizard_starting_equipment()
if character_class == "Rogue":
    rogue_starting_equipment()
if character_class == "Fighter":
    fighter_starting_equipment()
if character_class == "Cleric":
    cleric_starting_equipment()

for item in character_background.get("equipment", []):
    add_equipment(character_equipment, item, 1)

print("\nCurrent inventory", character_equipment)

equipped_armour = choose_equipped_armour(character_equipment)
movement_speed = calculate_movement_speed(movement_speed, character_class, character_level, equipped_armour, character_stats["strength"], character_race)
equipped_shield = choose_equipped_shield(character_equipment)

equipped_weapons, equipped_shield, is_dual_wielding = choose_equipped_weapon(character_equipment, equipped_shield)

print(f"\nEquipped weapons: {equipped_weapons}")
print(f"Shield equipped: {equipped_shield}")

armour_class = calculate_armour_class(equipped_armour, equipped_shield, character_modifiers["dexterity"], character_class, character_modifiers["constitution"])

armour_class = apply_defense_fighting_style(armour_class, chosen_fighting_styles, equipped_armour)

print(f"Armour class: {armour_class}")

for equipped_weapon in equipped_weapons:
    weapon_name = equipped_weapon["weapon"]
    attack_bonus = calculate_weapon_attack_bonus(weapon_name, character_modifiers["strength"], character_modifiers["dexterity"], proficiency_bonus, known_weapon_proficiencies)

    attack_bonus = apply_archery_fighting_style(attack_bonus, chosen_fighting_styles, weapon_name)

    print(f"{weapon_name} attack bonus: {attack_bonus:+d}")

if character_class == "Rogue":
    sneak_attack_damage = calculate_sneak_attack(
        character_class,
        character_level
    )
    print(
        f"Sneak Attack: +{sneak_attack_damage} damage "
        "(once per turn when eligible)"
    )

for index, equipped_weapon in enumerate(equipped_weapons):
    weapon_name = equipped_weapon["weapon"]
    hands = equipped_weapon["hands"]
    wielded_two_handed = hands == 2
    wielding_another_weapon = is_dual_wielding

    off_hand = is_dual_wielding and index == 1

    damage_dice, damage_modifier, damage_type = calculate_weapon_damage(weapon_name, hands, character_modifiers["strength"], character_modifiers["dexterity"], off_hand, chosen_fighting_styles=chosen_fighting_styles)

    if damage_dice is None:
        print(f"{weapon_name} damage: No Damage")
        continue

    sneak_attack_damage = calculate_sneak_attack(character_class,character_level)

    damage_modifier = apply_dueling_fighting_style(damage_modifier, chosen_fighting_styles, weapon_name, wielded_two_handed, wielding_another_weapon)

    if damage_modifier > 0:
        damage_display = f"{damage_dice} + {damage_modifier}"
    elif damage_modifier < 0:
        damage_display = f"{damage_dice} - {abs(damage_modifier)}"
    else:
        damage_display = damage_dice

    hand_label = " (Off-hand)" if off_hand else ""

    print(f"{weapon_name}{hand_label} damage: {damage_display} {damage_type}")

    if character_class == "Barbarian":
        rage_bonus = calculate_rage_damage_bonus(character_class, character_level, equipped_armour, weapon_name, character_modifiers["strength"], character_modifiers["dexterity"])

        raging_modifier = damage_modifier + rage_bonus

        if raging_modifier > 0:
            raging_damage_display = f"{damage_dice} + {raging_modifier}"
        elif raging_modifier < 0:
            raging_damage_display = f"{damage_dice} - {abs(raging_modifier)}"
        else:
            raging_damage_display = damage_dice

        print(
            f"{weapon_name}{hand_label} damage while Raging: "
            f"{raging_damage_display} {damage_type}"
        )

print(f"\nAs you're {article} {display_race} your movement speed is {movement_speed}!")

if remarkable_athlete_bonus is not None:
    running_long_jump = character_stats["strength"]
    running_long_jump += character_modifiers["strength"]

    print(f"Remarkable Athlete Running Long Jump distance: {running_long_jump} ft")

if chosen_fighting_styles:
    print("\nFIGHTING STYLES:")

    for style in chosen_fighting_styles:
        print(f"\t{style}")

if champion_critical_range is not None:
    print("\nCHAMPION FEATURES:")
    print(f"Critical Hit range: {champion_critical_range}-20")

def display_character_sheet_header(character_name, character_race, character_subrace, character_class, character_level, subclass_name, character_background):
    print("\n" + "=" * 60)
    print("DUNGEONS & DRAGONS 5th EDITION - CHARACTER SHEET".center(60))
    print("=" * 60)

    print(f"Character Name: {character_name}")
    print(f"Race: {character_race}")

    if character_subrace:
        print(f"Subrace: {character_subrace}")

    print(f"Class: {character_class}")
    print(f"Level: {character_level}")

    if subclass_name:
        print(f"Subclass: {subclass_name}")

    print(f"Background: {character_background['name']}")

    print("=" * 60)



display_character_sheet_header(
    character_name,
    character_race,
    character_subrace,
    character_class,
    character_level,
    subclass_name,
    character_background
)


def display_character_sheet_abilities(character_stats, character_modifiers):
    print("\nABILITY SCORES")
    print("-" * 60)

    for ability, score in character_stats.items():
        modifier = character_modifiers[ability]
        print(f"{ability.capitalize():<15} {score:>2} ({modifier:+})")

    print("-" * 60)


display_character_sheet_abilities(
    character_stats,
    character_modifiers
)


def display_character_sheet_saving_throws(saving_throw_bonuses, saving_throw_proficiencies):
    print("\nSAVING THROWS")
    print("-" * 60)

    for ability, bonus in saving_throw_bonuses.items():
        proficient = ability.capitalize() in saving_throw_proficiencies

        marker = "*" if proficient else " "

        print(f"{marker} {ability.capitalize():<15} {bonus:+}")

    print("-" * 60)


display_character_sheet_saving_throws(
    saving_throw_bonuses,
    saving_throw_proficiencies
)


def display_character_sheet_skills(skill_bonuses, known_character_skills, expertise_skills):
    print("\nSKILLS")
    print("-" * 60)

    for skill, bonus in skill_bonuses.items():

        if skill in expertise_skills:
            marker = "**"
        elif skill in known_character_skills:
            marker = "* "
        else:
            marker = "  "

        print(f"{marker} {skill:<20} {bonus:+}")

    print("-" * 60)


display_character_sheet_skills(
    skill_bonuses,
    known_character_skills,
    expertise_skills
)


def display_character_sheet_combat(
    character_hp,
    armour_class,
    initiative_bonus,
    movement_speed,
    proficiency_bonus,
    hit_die,
    character_level
):
    print("\nCOMBAT STATISTICS")
    print("-" * 60)

    print(f"Maximum Hit Points: {character_hp}")
    print(f"Armour Class: {armour_class}")
    print(f"Initiative Bonus: {initiative_bonus:+}")
    print(f"Movement Speed: {movement_speed} ft.")
    print(f"Proficiency Bonus: {proficiency_bonus:+}")
    print(f"Hit Dice: {character_level}d{hit_die}")

    print("-" * 60)


display_character_sheet_combat(
    character_hp,
    armour_class,
    initiative_bonus,
    movement_speed,
    proficiency_bonus,
    hit_die,
    character_level
)


def display_character_sheet_weapons(
    equipped_weapons,
    character_modifiers,
    proficiency_bonus,
    known_weapon_proficiencies,
    chosen_fighting_styles,
    is_dual_wielding
):
    print("\nWEAPONS AND ATTACKS")
    print("-" * 60)

    if not equipped_weapons:
        print("No weapons equipped.")
        print("-" * 60)
        return

    for index, equipped_weapon in enumerate(equipped_weapons):
        weapon_name = equipped_weapon["weapon"]
        hands = equipped_weapon["hands"]
        off_hand = is_dual_wielding and index == 1

        attack_bonus = calculate_weapon_attack_bonus(
            weapon_name,
            character_modifiers["strength"],
            character_modifiers["dexterity"],
            proficiency_bonus,
            known_weapon_proficiencies
        )

        attack_bonus = apply_archery_fighting_style(
            attack_bonus,
            chosen_fighting_styles,
            weapon_name
        )

        damage_dice, damage_modifier, damage_type = calculate_weapon_damage(
            weapon_name,
            hands,
            character_modifiers["strength"],
            character_modifiers["dexterity"],
            off_hand,
            chosen_fighting_styles=chosen_fighting_styles
        )

        damage_modifier = apply_dueling_fighting_style(
            damage_modifier,
            chosen_fighting_styles,
            weapon_name,
            hands == 2,
            is_dual_wielding
        ) if damage_dice is not None else None

        hand_label = " (Off-hand)" if off_hand else ""

        print(f"\n{weapon_name}{hand_label}")
        print(f"  Attack Bonus: {attack_bonus:+}")

        if damage_dice is None:
            print("  Damage: No Damage")
        else:
            if damage_modifier > 0:
                damage_display = f"{damage_dice} + {damage_modifier}"
            elif damage_modifier < 0:
                damage_display = f"{damage_dice} - {abs(damage_modifier)}"
            else:
                damage_display = damage_dice

            print(f"  Damage: {damage_display} {damage_type}")

    print("-" * 60)


display_character_sheet_weapons(
    equipped_weapons,
    character_modifiers,
    proficiency_bonus,
    known_weapon_proficiencies,
    chosen_fighting_styles,
    is_dual_wielding
)


def display_character_sheet_spellcasting(
    spellcasting_modifier,
    spell_save_dc,
    spell_attack_bonus,
    max_spell_level,
    chosen_cantrips,
    known_spells,
    spell_slots,
    wizard_spellbook,
    prepared_spells,
    domain_spells,
    signature_spells,
    racial_spell_details,
    racial_spellcasting_ability,
    racial_spellcasting_modifier,
    racial_spell_save_dc,
    racial_spell_attack_bonus
):
    if spellcasting_modifier is None and not racial_spell_details:
        return

    print("\nSPELLCASTING")
    print("-" * 60)

    if spellcasting_modifier is not None:
        print(f"Spellcasting Modifier: {spellcasting_modifier:+}")
        print(f"Spell Save DC: {spell_save_dc}")
        print(f"Spell Attack Bonus: {spell_attack_bonus:+}")
        print(f"Highest Spell Level: {max_spell_level}")

        if chosen_cantrips:
            print(f"\nCantrips Known ({len(chosen_cantrips)}):")
            for cantrip in chosen_cantrips:
                print(f"  - {cantrip}")

        if known_spells is not None:
            print(f"\nSpells Known ({len(known_spells)}):")
            for spell in known_spells:
                print(f"  - {spell}")

        if spell_slots:
            print("\nSpell Slots:")
            for level, slots in spell_slots.items():
                print(f"  Level {level}: {slots} slots")

        if wizard_spellbook is not None:
            print(f"\nWizard Spellbook ({len(wizard_spellbook)}):")
            for spell in wizard_spellbook:
                print(f"  - {spell}")

        if prepared_spells is not None:
            print(f"\nPrepared Spells ({len(prepared_spells)}):")
            for spell in prepared_spells:
                print(f"  - {spell}")

        if domain_spells:
            print("\nCleric Domain Spells:")
            for spell in domain_spells:
                print(f"  - {spell}")

        if signature_spells:
            print("\nSignature Spells:")
            for spell in signature_spells:
                print(f"  - {spell}")

    if racial_spell_details:
        print("\nRACIAL SPELLCASTING")
        print(f"Spellcasting Ability: {racial_spellcasting_ability.title()}")
        print(f"Spellcasting Modifier: {racial_spellcasting_modifier:+}")
        print(f"Spell Save DC: {racial_spell_save_dc}")
        print(f"Spell Attack Bonus: {racial_spell_attack_bonus:+}")

        print("\nRacial Spells:")
        for spell in racial_spell_details:
            description = f"  - {spell['name']} ({spell['usage']})"

            if spell["casting_level"] is not None:
                description += f" - Level {spell['casting_level']}"

            print(description)

    print("-" * 60)


display_character_sheet_spellcasting(
    spellcasting_modifier,
    spell_save_dc,
    spell_attack_bonus,
    max_spell_level,
    chosen_cantrips,
    known_spells,
    spell_slots,
    wizard_spellbook,
    prepared_spells,
    domain_spells,
    signature_spells,
    racial_spell_details,
    racial_spellcasting_ability,
    racial_spellcasting_modifier,
    racial_spell_save_dc,
    racial_spell_attack_bonus
)


def display_character_sheet_equipment(
    character_equipment,
    equipped_armour,
    equipped_shield,
    equipped_weapons
):
    print("\nEQUIPMENT AND INVENTORY")
    print("-" * 60)

    print("\nEQUIPPED ITEMS")

    if equipped_armour:
        print(f"Armour: {equipped_armour}")
    else:
        print("Armour: None")

    print(f"Shield: {'Equipped' if equipped_shield else 'Not equipped'}")

    if equipped_weapons:
        print("Weapons:")
        for equipped_weapon in equipped_weapons:
            print(f"  - {equipped_weapon['weapon']}")
    else:
        print("Weapons: None")

    print("\nINVENTORY")

    if character_equipment:
        for item_name, quantity in character_equipment.items():
            print(f"  - {item_name} x{quantity}")
    else:
        print("  No items in inventory.")

    print("-" * 60)


display_character_sheet_equipment(
    character_equipment,
    equipped_armour,
    equipped_shield,
    equipped_weapons
)


def display_character_sheet_proficiencies(
    known_armour_proficiencies,
    known_weapon_proficiencies,
    known_character_tools,
    known_character_languages,
    expertise_tools
):
    print("\nPROFICIENCIES AND LANGUAGES")
    print("-" * 60)

    print("\nArmour Proficiencies:")
    if known_armour_proficiencies:
        for armour in known_armour_proficiencies:
            print(f"  - {armour}")
    else:
        print("  None")

    print("\nWeapon Proficiencies:")
    if known_weapon_proficiencies:
        for weapon in known_weapon_proficiencies:
            print(f"  - {weapon}")
    else:
        print("  None")

    print("\nTool Proficiencies:")
    if known_character_tools:
        for tool in known_character_tools:
            if tool in expertise_tools:
                print(f"   - {tool} (Expertise)")
            else:
                print(f"  - {tool}")
    else:
        print("  None")

    print("\nLanguages:")
    if known_character_languages:
        for language in known_character_languages:
            print(f"  - {language}")
    else:
        print("  None")

    print("-" * 60)


display_character_sheet_proficiencies(
    known_armour_proficiencies,
    known_weapon_proficiencies,
    known_character_tools,
    known_character_languages,
    expertise_tools
)


def display_character_sheet_features(
    race_details,
    character_subrace,
    class_details,
    character_level,
    character_subclass,
    character_background,
    chosen_fighting_styles,
    chosen_manoeuvres,
    spell_mastery,
    chosen_totems,
    superiority_dice,
    manoeuvre_save_dc,
    dragonborn_breath_damage,
    dragonborn_breath_damage_type,
    dragonborn_breath_shape,
    dragonborn_breath_save_ability,
    dragonborn_breath_save_dc
):

    print("\nCHARACTER FEATURES")
    print("-" * 60)

    if race_details["name"] == "Dragonborn":
        print("\nDRAGONBORN ANCESTRY")
        print(f"  - Breath Weapon Damage: {dragonborn_breath_damage}")
        print(f"  - Damage Type: {dragonborn_breath_damage_type}")
        print(f"  - Breath Weapon Shape: {dragonborn_breath_shape}")
        print(f"  - Saving Throw: {dragonborn_breath_save_ability}")
        print(f"  - Breath Weapon Save DC: {dragonborn_breath_save_dc}")
        print(f"  - Damage Resistance: {dragonborn_breath_damage_type}")

    print("\nRACIAL FEATURES")

    for feature in race_details.get("features", []):
        print(f"  - {feature}")

        description = racial_feature_descriptions.get(feature)

        if description:
            print(f"    {description}")

    for subrace in race_details.get("subraces", {}).values():
        if subrace["name"] == character_subrace:
            for feature in subrace.get("features", []):
                print(f"  - {feature}")

                description = subrace_feature_descriptions.get(feature)

                if description:
                    print(f"    {description}")

    print("\nCLASS FEATURES")

    for level, features in sorted(
        class_details["level_features"].items()
    ):
        if level <= character_level:
            for feature in features:
                print(f"  - {feature} (Level {level})")

                description = class_feature_descriptions.get(feature)

                if description:
                    print(f"    {description}")

    if class_details["name"] == "Rogue":
        sneak_attack_dice = (character_level + 1) // 2

        print("\nSNEAK ATTACK")
        print(f"  - Extra Damage: {sneak_attack_dice}d6")

    if class_details["name"] == "Barbarian":
        rage_uses = calculate_rage_uses("Barbarian", character_level)

        print("\nBARBARIAN RESOURCES")
        print(f"  - Rages per Long Rest: {rage_uses}")

    if class_details["name"] == "Fighter":
        print("\nFIGHTER RESOURCES")

        if character_level >= 2:
            action_surge_uses = calculate_action_surge_uses("Fighter", character_level)
            print(f"   - Action Surge Uses: {action_surge_uses}")
            print("    - Action Surge Recovery: Long or Short Rest")
        else:
            print("    - Action Surge not yet unlocked (unlocks at level 2)")

    if class_details["name"] == "Cleric":
        print("\nCLERIC RESOURCES")

        if character_level >= 18:
            channel_divinity_uses = 3
        elif character_level >= 6:
            channel_divinity_uses = 2
        elif character_level >= 2:
            channel_divinity_uses = 1
        else:
            channel_divinity_uses = 0

        if channel_divinity_uses > 0:
            print(f"  - Channel Divinity Uses: {channel_divinity_uses}")
            print("  - Channel Divinity Recovery: Short or Long Rest")
        else:
            print("  - Channel Divinity: Not yet unlocked")

    if class_details["name"] == "Wizard":
        arcane_recovery_levels = (character_level + 1) // 2
        maximum_recovery_slot_level = min(5, arcane_recovery_levels)


        print("\nWIZARD RESOURCES")
        print(f"  - Arcane Recovery: {arcane_recovery_levels} combined spell slot levels")
        print(f"  - Maximum Recovered Slot Level: {maximum_recovery_slot_level}")
        print("  - Arcane Recovery: Once per day, after a Short Rest")

    if chosen_fighting_styles:
        print("\nFIGHTING STYLES")

        for style in chosen_fighting_styles:
            print(f"  - {style}")

            description = fighting_styles[style]["description"]
            print(f"    {description}")

    if superiority_dice is not None:
        number_of_dice, die_size = superiority_dice

        print("\nBATTLE MASTER RESOURCES")
        print(f"  - Superiority Dice: {number_of_dice}{die_size}")
        print("  - Superiority Dice Recovery: Short or Long Rest")
        print(f"  - Manoeuvre Save DC: {manoeuvre_save_dc}")

    if chosen_manoeuvres:
        print("\nBATTLE MASTER MANOEUVRES")

        for manoeuvre in chosen_manoeuvres:
            print(f"  - {manoeuvre}")

            description = battle_master_manoeuvres[manoeuvre]["description"]
            print(f"    {description}")


    if spell_mastery:
        print("\nSPELL MASTERY")

        for spell_level, spell in sorted(spell_mastery.items()):
            print(f"  - Level {spell_level}: {spell}")

    if chosen_totems:
        print("\nTOTEM WARRIOR CHOICES")

        for feature, animal in chosen_totems.items():
            print(f"  - {feature}: {animal}")

    if character_subclass is not None:
        print(f"\nSUBCLASS FEATURES - {character_subclass['name']}")

        for level, features in sorted(
            character_subclass.get("level_features", {}).items()
        ):
            if level <= character_level:
                for feature in features:
                    print(f"  - {feature} (Level {level})")

                    description = subclass_feature_descriptions.get(feature)

                    if description:
                        print(f"    {description}")

    print("\nBACKGROUND FEATURES")

    background_feature = character_background["features"]

    print(f"  - {background_feature['name']}")
    print(f"    {background_feature['description']}")

    print("-" * 60)


display_character_sheet_features(
    race_details,
    character_subrace,
    class_details,
    character_level,
    character_subclass,
    character_background,
    chosen_fighting_styles,
    chosen_manoeuvres,
    spell_mastery,
    chosen_totems,
    superiority_dice,
    manoeuvre_save_dc,
    dragonborn_breath_damage,
    dragonborn_breath_damage_type,
    dragonborn_breath_shape,
    dragonborn_breath_save_ability,
    dragonborn_breath_save_dc
)


def display_character_sheet_description(
    character_appearance,
    character_backstory
):
    print("\nCHARACTER DESCRIPTION")
    print("-" * 60)

    print("\nPHYSICAL APPEARANCE")
    if character_appearance:
        print(character_appearance)
    else:
        print("Not provided.")

    print("\nBACKSTORY")
    if character_backstory:
        print(character_backstory)
    else:
        print("Not provided.")

    print("-" * 60)

display_character_sheet_description(
    character_appearance,
    character_backstory
)








































