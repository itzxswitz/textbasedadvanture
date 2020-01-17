import random

class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability
    ## create a list for the weapons in game
    name = "name"
    damage = "damage"
    durability = "durability"
    weapons = {
        "mace": {
            name: "mace",
            damage: random.randint(3, 4),
            durability: random.randint(20, 80)
        },
        "machete": {
            name: "machete",
            damage: random.randint(3, 5),
            durability: random.randint(20, 70)
        },
        "sword": {
            name: "sword",
            damage: random.randint(2, 5),
            durability: random.randint(40, 70)
        },
        "dagger": {
            name: "dagger",
            damage: random.randint(1, 2),
            durability: random.randint(40, 80)
        },
        "hammer": {
            name: "hammer",
            damage: random.randint(2, 3),
            durability: random.randint(50, 90)
        },
        "fists": {
            name: "fists",
            damage: .5,
            durability: 100
        }
    }
    #pull a random weapon from the list, the player can choose to take this or not
    def get_weapon(self):
        weapon = Weapon.weapons["fists"]
        while weapon["name"] == "fists":
            weapon = Weapon.weapons[random.choice(list(Weapon.weapons))]
        print ("There is a " + weapon["name"] + " that deals " + str(weapon["damage"]) + " damage, with a durability of " + str(weapon["durability"]))
        return weapon
    def assign_weapon(self,weapon):
        ## create a list for the weapons in game
        name = "name"
        damage = 1
        durability = 100
        weapons = {
            "mace": {
                name: "mace",
                damage: random.randint(3, 4),
                durability: random.randint(20, 80)
            },
            "machete": {
                name: "machete",
                damage: random.randint(3, 5),
                durability: random.randint(20, 70)
            },
            "sword": {
                name: "sword",
                damage: random.randint(2, 5),
                durability: random.randint(40, 70)
            },
            "dagger": {
                name: "dagger",
                damage: random.randint(1, 2),
                durability: random.randint(40, 80)
            },
            "hammer": {
                name: "hammer",
                damage: random.randint(2, 3),
                durability: random.randint(50, 90)
            },
            "fists": {
                name: "fists",
                damage: .5,
                durability: 100
            }
        }
        new = weapons[weapon]
        return new
