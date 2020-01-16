import random

class Weapon:

    #def assign_weapon(self,weapon):
       # return Weapon.weapons(weapon)
    name = "name"
    damage = 1
    durability = 100
    weapons = {
        "mace": {
            name: "mace",
            damage: random.randint(3, 4),
            durability: random.randint(20, 80)
        },
        "machete":{
            name: "machete",
            damage: random.randint(3, 5),
            durability: random.randint(20, 70)
       },
        "sword":{
            name: "sword",
            damage: random.randint(2, 5),
            durability: random.randint(40, 70)
        },
        "dagger":{
            name: "dagger",
            damage: random.randint(1, 2),
            durability: random.randint(40, 80)
        },
        "hammer":{
            name: "machete",
            damage: random.randint(2, 3),
            durability: random.randint(50, 90)
        },
        "fists":{
        name: "fists",
        damage: .5,
        durability: 100
        }
    }
    def get_weapon(self):
        weapon = random.choice(Weapon.weapons)
        return weapon
