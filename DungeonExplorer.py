
from armor import Armor
from player import Player
from rooms import Room
from weapon import Weapon

######## notes on to add
# upon entrance spawn enemies, upon examine spawn items and armor
# armor and weapon durability depletes with battle, when hit deplete armor, when attacking deplete weapon
# where do i need to have the rooms stored, here or in their own file?
# can i create enemies using the player class?
# remember to check for player health before every input
# can room be represented by calling a single variable, or do i need to input every variable?
# do we need charisma? - for the king only, can convince him to leave
# consider adding separation lines to the text for easier use.
# start menu?
# on combat: do i add misses and critical hits? too much rng?
# equip will not be an input as it is already asked upon examine
# go/move, eat, examine, attack,

#functions used throughout the program
# equip or pick up the items on the ground
def equip_weapon():
      ground_weapon = Weapon("self", 0, 0)
      ground_weapon.create_weapon(ground_weapon.name, ground_weapon.damage, ground_weapon.durability)
      while True:
            print("Would you like to equip this weapon? Yes/No:")
            answer = input()
            if answer.lower() == "yes":
                  equipped_weapon = ground_weapon
                  player.update_damage(equipped_weapon.damage)
                  return
            elif answer.lower() == "no":
                  print ("You leave the " + ground_weapon.name + " behind.")
                  return
            else:
                  print("Invalid input, please enter yes or no as your answer.")
def equip_armor():
      ground_armor = Armor("self", 0, 100)
      ground_armor.create_armor(ground_armor.name, ground_armor.block, ground_armor.durability)
      while True:
            print("Would you like to equip this armor? Yes/No:")
            answer = input()
            if answer.lower() == "yes":
                  armor = ground_armor
                  print("You now have " + str(armor.block) + " point(s) of protection")
                  return
            elif answer.lower() == "no":
                  print ("You leave the " + ground_armor.name + " armor behind.")
                  return
            else:
                  print("Invalid input, please enter yes or no as your answer.")
# describe the items the character currently has
def describe_weapon():
      print("You currently have " + equipped_weapon.name + " that deal a damage of " + str(
      equipped_weapon.damage) + " with a durability of " + str(equipped_weapon.durability))
def describe_armor():
      print ("You are currently wearing " + armor.name + " that does " + str(armor.block) + " points of protection. It has " + str(armor.durability) + " hitpoints left.")


def command(current_room, new=None):
    while player.health > 0:
        print("What would you like to do?")
        answer = input()
        if answer == "look":
            desc = current_room["description"]
            print(desc)
        elif answer == "examine":
            # add ability to examine weapon, inventory, armor, room, items etc.
            print(current_room["examine"])
        elif answer == "go":
            while True:
                print("Which direction would you like to go?")
                movement = input()
                if movement.lower == "up" or "north":
                    if current_room["up"] == "none":
                        print("You cannot go that way.")
                    else:
                        new = current_room["up"]
                        current_room = Room.zonemap[new]
                        return
                elif movement.lower == "down" or "south":
                    if current_room["down"] == "none":
                        print("You cannot go that way.")
                    else:
                        new = current_room["down"]
                        current_room = Room.zonemap[new]
                        return
                elif movement.lower == "left" or "west":
                    if current_room["left"] == "none":
                        print("You cannot go that way.")
                    else:
                        new = current_room["left"]
                        current_room = Room.zonemap[new]
                        return
                elif movement.lower == "right" or "east":
                    if current_room["right"] == "none":
                        print("You cannot go that way.")
                    else:
                        new = current_room["right"]
                        current_room = Room.zonemap[new]
                        return
                else:
                    print(
                        "That is not a valid direction. Up/north, down/south, left/west, or right/east are all valid directions.")

######## Game commences ############
#Introduce character and allowcate points
print("Welcome to Dungeon Explorer!  \nLet us introduce you to the town of Shamble!\nShamble is a small "
      "European town in the 1600's who has been overrun by a corrupt king, King Leopold.\nThere are rumours "
      "of a dungeon that stretches underneath Shamble Castle where King Leopold's weakness can be found. \nIf "
      "you can find his weakness you can take it to the throne room and use it against him to drive the evil \n"
      "king out!\nIt is up to you to find this weakness and rid the town of this evil overlord and bring \n"
      "Shamble back from the *ahem* shambles it has become."
      "\n____________________________________________________________________________________________________________________"
      "\n\nWhat is your player name?"
      "")
Char_name = input()
player = Player(Char_name, 1,1,1,1,100,.1)
print("\nHello " + player.name + " of Shamble! Let's take a look at your stats!")
player.displaystats()
equipped_weapon = Weapon("fists", .1, 100)
armor = Armor("rugged cloth", 0, player.health)
print("\nThat's not good! You have no skills! Lucky for you we have a few skill points lying around that you "
      "can use! \nHave 5 free skill points on us!")
print ("_____________________________________________________________________________________________________________________\n")
player.assign_stats(5,5)
print ("_____________________________________________________________________________________________________________________")
print ("\nCongratulations on gaining some skills!")
player.displaystats()
player.update_damage(equipped_weapon.damage)
print ("_____________________________________________________________________________________________________________________")

#begin the story
print("\nYou find yourself at Shirkin's Inn, the oldest building in town. It has hosted travellers for decades, maybe \n"
      "even centuries, but no one is sure anymore how long the building has been standing, all they know is that it was \n"
      "built when they got there. Since Leopold conquered the town and reigned supreme, it's become a local drinking \n"
      "spot more than an inn, as travellers don't visit Shamble anymore. The many rooms that make up the inn have become host to those that \n"
      "have lost everything to the cruel reign of the new king, and every Sunday when the guards go on their pillaging runs \n"
      "it becomes home to the revolution meetings that have taken place for the last 6 months or so. After a few months thought\n"
      "you have decided to volunteer to enter the castle sewers and make your way through the castle to find a way to restore\n"
      "Shamble to it's former glory.\n"
      "\nThe meeting commences, and you offer your limited services as what seems like a pointless sacrifice to the local townspeople.\n"
      "All are hesitant that you would be able to complete such a task, but with the current state of the town, no one\n"
      "is going to stop your valiant efforts. Jen Shirkin comes forward.\n"
      "_______________________________________________________________________________________________________________________\n"
      "\nI want to thank you child, for as long as my ancestors have resided in Shamble, we have never seen such bravery\n"
      "come from one of the townsfolk. I don't have much to offer, but I will give you the weapon and armor that my brother\n"
      "carried into battle when Leopold first entered Shamble. It's all I have left of him except my memory, but I pray\n"
      "that you will carry them to deliver us from this tyrant as my brother hoped to with his last dying breath.\n"
      "_______________________________________________________________________________________________________________________")
describe_weapon()
equip_weapon()
describe_armor()
equip_armor()
# noinspection PyArgumentList
current_room = Room.zonemap["r1"]
command(current_room)

