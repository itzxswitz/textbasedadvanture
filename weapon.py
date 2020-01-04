import random

class Weapon:

    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

# create a weapon with rng stats
    def create_weapon(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability
        names = ["mace", "machete", "sword", "dagger", "hammer", "whip", "axe", "shiv", "club", "ball and chain", "knife", "bat", "spear", "pipe", "stick"]
        self.name = random.choice(names)
        self.damage = random.randint(1,10)
        self.durability = random.randint(1,100)
        print("There is a " + self.name + " on the floor that does " + str(self.damage) + " damage with a durability of " + str(self.durability))
