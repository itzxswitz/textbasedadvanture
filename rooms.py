class Room:
    def __init__(self, name, description, solved, up, down, left, right, enemy, food, key, chest):
        self.name = name
        self.description = description
        self.solved = solved
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.enemy = enemy
        self.food = food
        self.key = key
        self.chest = chest
    def get_room(self, room):
        return zonemap(room)
    def get_up(self):
        return self.up
    def get_down(self):
        return self.down
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def descibe_room(self):
        print (self.description)
    def examine_room(self):
        print (self.examine)




    # constant variables.
    name = "name"
    description = "description"
    examine = "examine"
    solved = "solved"
    up = 'up', 'north'
    down= 'down', 'south'
    left = 'left','west'
    right = 'right', 'east'
    enemy = False
    food = False
    key = False
    chest = False
    armor = False
    weapon = False

    # a list of rooms with all their factors, whether is contains weapons, items, armor, or enemies, as well as directions
    # to the next room.
    zonemap = {
        "r1": {
            name: "inn",
            description: "Shirkin's inn, a home to the revolution. The exit is to the left",
            examine: "There is close to 40 people, anxious to see what your endeavor will result in.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r2',
            right: "none",
            enemy: False,
            food: True,
            key: False,
            chest: False,
            armor: True,
            weapon: True
        },
        "r2": {
            name: "road",
            description: "the main road of Shamble. The road continues to the north towards the castle. Shirkin's Inn "
                         "\nresides to the right",
            examine: "the dirt road is rarely travelled anymore. residents of Shamble avoid the guards as much as possible.",
            solved: False,
            up: "r3",
            down: "none",
            left: 'none',
            right: "none",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
        },
        "r3": {
            name: "road",
            description: "the main road of Shamble. The road will lead you north towards the castle or south towards Shirkin's Inn.",
            examine: "the dirt road is rarely travelled anymore. residents of Shamble avoid the guards as much as possible.",
            solved: False,
            up: "r4",
            down: "r2",
            left: 'none',
            right: "none",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
            },
        "r4": {
            name: "road",
            description: "the main road of Shamble. The road will lead you north towards the castle or south towards "
                         "\nShirkin's Inn. Your home is to the left.",
            examine: "the dirt road is rarely travelled anymore. residents of Shamble avoid the guards as much as possible.",
            solved: False,
            up: "r6",
            down: "r3",
            left: 'r5',
            right: "none",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
            },
        "r5": {
            name: "home",
            description: "your home, it doesn't feel the same as it once did. The exit is to the right.",
            examine: "This is your home. Your once cozy abode has deteriorated with the decline of the town's economy. It "
                     "\nis invested with rats.",
            solved: False,
            up: "none",
            down: "none",
            left: 'none',
            right: "r4",
            enemy: True,
            food: True,
            key: False,
            chest: False,
            armor: False,
            weapon: False
            },
        "r6": {
            name: "road",
            description: "the main road of Shamble. The road will lead you north towards the castle or south towards "
                         "\nShirkin's Inn. The castle's sewage outflow pipe is to the right",
            examine: "the dirt road is rarely travelled anymore. residents of Shamble avoid the guards as much as possible.",
            solved: False,
            up: "r7",
            down: "r4",
            left: 'none',
            right: "r9",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
            },
        "r7": {
            name: "castle gate",
            description: "the gate to the castle grounds. The grounds are heavily guarded, any attempts to enter this way "
                         "\nwould be futile.",
            examine: "You look through the gate and see multiple heavily armored guards. There is nowhere to go except south",
            solved: False,
            up: "none",
            down: "r6",
            left: 'none',
            right: "none",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
            },
        "r9": {
            name: "sewage outflow",
            description: "the sewage outflow pipe of the castle.",
            examine: "it smells disgusting, you can barely see anything except what the light reveals from the entrance to "
                     "\nthe pipe. There is a small hatch to the north, and the exit to the pipe is to the left.",
            solved: False,
            up: "r6",
            down: "r3",
            left: 'r5',
            right: "none",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
            },
        "r11": {
            name: "maintenance room",
            description: "the maintenance room of the castle. There is a door to the north, or the outflow pipe to the "
                    "\nsouth.",
            examine: "You can see the drains from the toilets all leading towards "
                    "\nwhere you just entered, there is a stockpile of lantern oil in the corner as well as some brooms "
                    "\nthat the servants use for cleaning the grounds.",
            solved: False,
            up: "r12",
            down: "r10",
            left: 'none',
            right: "none",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
            },
        "r12": {
            name: "castle hall",
            description: "the castle's basement. There is luxurious flooring, and torches that line the wall. The hall "
                         "\ncontinues north, and the maintenance closet is to the south. ",
            examine: "you cannot find a speck of dirt anywhere, this is the cleanest room you've ever seen. You've only "
                     "\ndreamt of living in such luxury.",
            solved: False,
            up: "r15",
            down: "r11",
            left: 'none',
            right: "none",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
            },
        "r13": {
            name: "guard's quarters",
            description: "the guard's quarters, it is full of sleeping sacks on the floor and dimly lit. To be a guard is "
                         "\nleads to a poor quality of life apparently. A guard who seemed to have been asleep wakes upon your "
                         "\nentrance. The exit to the room resides to the right. There appears to be a set of armor in the "
                         "\ncorner of the room.",
            examine: "Sack cloth for sleeping and very basic essentials of a living space are provided. As poor a living"
                     "\nsituation this may seem, it is still a richer life than most of those in the town have. You begin to "
                     "\nunderstand why the guards stay loyal to the king, because it is better to have little than to have "
                     "\nnothing",
            solved: False,
            up: "none",
            down: "none",
            left: 'none',
            right: "r14",
            enemy: True,
            food: False,
            key: False,
            chest: False,
            armor: True,
            weapon: False
            },
        "r14": {
            name: "castle hall",
            description: "the castle's basement. There is luxurious flooring, and torches that line the wall. The hall "
                         "\ncontinues to the left and the right.",
            examine: "you cannot find a speck of dirt anywhere, this is the cleanest room you've ever seen. You've only "
                     "\ndreamt of living in such luxury.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r13',
            right: "r15",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
        },
        "r15": {
            name: "castle hall",
            description: "the castle's basement. There is luxurious flooring, and torches that line the wall. The hall "
                         "\ncontinues in all four directions",
            examine: "you cannot find a speck of dirt anywhere, this is the cleanest room you've ever seen. You've only "
                     "\ndreamt of living in such luxury.",
            solved: False,
            up: "r20",
            down: "r12",
            left: 'r14',
            right: "r16",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
        },
        "r16": {
            name: "castle hall",
            description: "the castle's basement. There is luxurious flooring, and torches that line the wall. The hall "
                         "\nsplit's into two different rooms. One to your right, and one to the north.",
            examine: "you cannot find a speck of dirt anywhere, this is the cleanest room you've ever seen. You've only "
                     "\ndreamt of living in such luxury.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r15',
            right: "r17",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
        },
        "r17": {
            name: "castle hall",
            description: "the castle's basement. There is luxurious flooring, and torches that line the wall. The hall "
                         "\nsplit's into two different rooms. One to your right, and one to the north. The hall stretches to"
                         "\nthe left.",
            examine: "you cannot find a speck of dirt anywhere, this is the cleanest room you've ever seen. You've only "
                     "\ndreamt of living in such luxury.",
            solved: False,
            up: "r19",
            down: "none",
            left: 'r16',
            right: "r18",
            enemy: True,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: False
        },
        "r18": {
            name: "storage room",
            description: "a storage room. There is an abundant amount of robes that, based on the cobwebs, the king no "
                         "\nlonger uses, and some furniture that has barely been used. The exit is to the left.",
            examine: "there looks to be a weapon in the corner of the room.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r17',
            right: "none",
            enemy: False,
            food: False,
            key: False,
            chest: False,
            armor: False,
            weapon: True
        },
        "r19": {
            name: "armor room",
            description: "the armor room. The room smells of death, clearly this rooms contains the armor of lost soldiers. The exit is to the south.",
            examine: "There are quite a few sets of armor in the room, most of which are heavily damaged or blood stained. "
                     "\nThere looks to be one set of armor that can be salvaged.",
            solved: False,
            up: "none",
            down: "r17",
            left: 'none',
            right: "none",
            enemy: False,
            food: True,
            key: False,
            chest: False,
            armor: True,
            weapon: True
        },
        "r20": {
            name: "inn",
            description: "Shirkin's inn, a home to the revolution. The exit is to the left",
            examine: "There is close to 40 people, anxious to see what your endeavor will result in.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r2',
            right: "none",
            enemy: False,
            food: True,
            key: False,
            chest: False,
            armor: True,
            weapon: True
        },
        "r1": {
            name: "inn",
            description: "Shirkin's inn, a home to the revolution. The exit is to the left",
            examine: "There is close to 40 people, anxious to see what your endeavor will result in.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r2',
            right: "none",
            enemy: False,
            food: True,
            key: False,
            chest: False,
            armor: True,
            weapon: True
        },
        "r1": {
            name: "inn",
            description: "Shirkin's inn, a home to the revolution. The exit is to the left",
            examine: "There is close to 40 people, anxious to see what your endeavor will result in.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r2',
            right: "none",
            enemy: False,
            food: True,
            key: False,
            chest: False,
            armor: True,
            weapon: True
        },
        "r1": {
            name: "inn",
            description: "Shirkin's inn, a home to the revolution. The exit is to the left",
            examine: "There is close to 40 people, anxious to see what your endeavor will result in.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r2',
            right: "none",
            enemy: False,
            food: True,
            key: False,
            chest: False,
            armor: True,
            weapon: True
        },
        "r1": {
            name: "inn",
            description: "Shirkin's inn, a home to the revolution. The exit is to the left",
            examine: "There is close to 40 people, anxious to see what your endeavor will result in.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r2',
            right: "none",
            enemy: False,
            food: True,
            key: False,
            chest: False,
            armor: True,
            weapon: True
        },
        "r1": {
            name: "inn",
            description: "Shirkin's inn, a home to the revolution. The exit is to the left",
            examine: "There is close to 40 people, anxious to see what your endeavor will result in.",
            solved: False,
            up: "none",
            down: "none",
            left: 'r2',
            right: "none",
            enemy: False,
            food: True,
            key: False,
            chest: False,
            armor: True,
            weapon: True
        },
    }

