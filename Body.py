import random

class Body(object):

    max_health = 1
    current_health = 1
    money = 1
    critical_chance = 1

    def __init__(self, passed_name, passed_weapon):
        self.name = passed_name
        self.weapon = passed_weapon
        self.generate_health()
        self.money = self.generate_money()

    def generate_hero(self):
        hero_prefix = ["Human", "Elf", "Halfling", "Dwarf", "Lizard person"]
        hero_types = ["Paladin", "Knight", "Mage", "Rogue", "Priest", "Hunter", "Assassin", "Warlock"]
        return random.choice(hero_prefix) + " " + random.choice(hero_types)

    def health_bar(self):
        return str(self.current_health) + "/" + str(self.max_health)

    def attack(self, damage_amount):
        return self.name + " uses its " + self.weapon.name + " to attack and dispenses " + str(damage_amount) + " damage."

    def health_display(self):
        return self.name + " current health: " + self.health_bar()

    def weapon_display(self):
        return self.name + " has a " + self.weapon.name + "\nit will do "+ str(self.weapon.low_damage) + "-" + str(self.weapon.high_damage) + " damage"

   # def doesCritical(self):
    #    criticalValue = random.randrange(0, 100)
     #   if criticalValue =< self.criticalChance:
        #  return True
       #else:
           #return False


    def decrease_health(self, count_down):
        self.current_health = self.current_health - count_down

    def alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def generate_health(self):
        health_dictonary = {"Gremlin": 20, "Ogre": 40, "Thief": 25, "Dragon": 75, "Kobold": 15, "Dark Knight": 50, "Ghoul": 10, "Satyr": 20, "Gnoll": 15, "Human": 30, "Elf": 20, "Halfling": 25, "Dwarf": 40, "Lizard Person": 35}
        for key, value in health_dictonary.items():
            if key in self.name:
                self.max_health += value
                self.current_health += value

    def generate_money(self):
        return random.randrange(50, 400)

    def increase_money(self, passed_money):
        self.money += passed_money

    def decrease_money(self, passed_money):
        self.increaseMoney(-1 * passed_money)