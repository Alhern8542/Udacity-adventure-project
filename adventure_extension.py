import random

creatures = ["crazy pirate","angry troll","wicked witch","ghost","evil fairy","zombie","cute kitten","flat earther"]

super_weapons = ["the spear of destiny","a lightsaber","a M41A pulse-rifle","a rocket launcher","the sword of Ogoroth"]

items = ["dagger","stick","lollipop","pencil","pepper spray","rubberband"]

#life remaining
lives = 2
#items carried
item = random.choice(items)
#super_weapon
super_weapon = random.choice(super_weapons)
is_super = False
#random creature
creature = random.choice(creatures)