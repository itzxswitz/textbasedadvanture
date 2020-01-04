import random
class Armor:
    def __init__(self, name, block, durability):
        self.name = name
        self.block = block
        self.durability = durability

# create a set of armor, protection is set based on the quality of the armor, durability is rng.
    def create_armor\
                    (self, name, block, durability):
        names = ["cloth", "wood", "leather", "iron", "chainmail", "silver", "platinum"]
        self.name = name
        self.block = block
        self.durability = durability
        self.name = random.choice(names)
        if self.name == "cloth":
            self.block = 1
            self.durability = durability
            self.durability = random.randint(1,100)
        elif self.name == "wood":
            self.block = 2
            self.durability = durability
            self.durability = random.randint(1,100)
        elif self.name == "leather":
            self.block = 3
            self.durability = durability
            self.durability = random.randint(1,100)
        elif self.name == "iron":
            self.block = 4
            self.durability = durability
            self.durability = random.randint(1,100)
        elif self.name == "chainmail":
            self.block = 5
            self.durability = durability
            self.durability = random.randint(1,100)
        elif self.name == "silver":
            self.block = 6
            self.durability = durability
            self.durability = random.randint(1,100)
        elif self.name == "platinum":
            self.block = 7
            self.durability = durability
            self.durability = random.randint(1,100)
        print("There is some " + self.name + " armor on the floor that does " + str(self.block) + " points of protection with a durability of " + str(self.durability))
