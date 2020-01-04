class Player:
    def __init__(self, name, strength, intelligence, charisma, stealth, health, damage):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.charisma = charisma
        self.stealth = stealth
        self.health = health
        self.damage = damage

# run through the current stat that the player can update and check for any invalid input.
    def _set_stat(self, stat_name, remaining, max_value, current):
        stats_to_give = max_value
        stats_to_give = min(remaining, stats_to_give)
        currentlevel = current
        while True:
            try:
                value = int(input(f"How much would you like to increase {stat_name} by? (max {stats_to_give}) \nPoints:"))
            except ValueError:
                print(f"Invalid input, please input a whole number less than or equal to {stats_to_give}.")
                continue
            if value <= -1:
                print("Invalid input, you cannot subtract from your stats.")
                continue
            elif value > stats_to_give:
                print(f"You only have {stats_to_give} points left - can't allocate {value}")
                continue
            elif value <= stats_to_give:
                currentlevel += value
                return remaining-value, currentlevel

    #assign skill points based on how many the user has earned
    def assign_stats(self, total_points,pta):
        print(f'Please allocate {total_points} skill points into strength, intelligence, charisma, stealth, and health')
        remaining = total_points
        max_value = pta
        #loop until all skill points are assigned, if skill points have all been assigned then stop the assignment
        while remaining >=1:
            print("Make sure to assign all your skill points!")
            if remaining >= 1:
                remaining, self.strength     = self._set_stat('strength', remaining, max_value,self.strength)
            if remaining >= 1:
                remaining, self.intelligence = self._set_stat('intelligence', remaining, max_value,self.intelligence)
            if remaining >= 1:
                remaining, self.charisma     = self._set_stat('charisma', remaining, max_value,self.charisma)
            if remaining >= 1:
                remaining, self.stealth      = self._set_stat('stealth', remaining, max_value, self.stealth)
            if remaining >= 1:
                remaining, self.health       = self._set_stat('health', remaining, max_value, self.health)
        print("You have no more skill points left to assign.")

    # display the stats of the user
    def displaystats(self):
        print("Here are your current stats: \nName: " + self.name + " of Shamble\nHealth " + str(self.health) + "\nStrength: " + str(
                self.strength) + "\nIntelligence: " + str(self.intelligence) + "\nCharisma: " + str(
                self.charisma) + "\nStealth:" + str(self.stealth) + "\nAttack Damage: " + str(self.damage))
    def get_strength(self):
        return self.strength

# update how much damage the player can do based on the weapon they use and their strength
    def update_damage(self,newdamage):
        self.damage = (newdamage*self.strength)/2
        print("You can deal " + str(self.damage) + " damage")