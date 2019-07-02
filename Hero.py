from Body import Body
import random

class Hero():
    kills = 0
    title = "Nobody"

    def __init__(self, passedWeapon):
        self.char = Body(self.generate_hero(), passedWeapon)

    def generate_hero(self):
        hero_prefix = ["Human", "Elf", "Halfling", "Dwarf", "Lizard person"]
        hero_types = ["Paladin", "Knight", "Mage", "Rogue", "Priest", "Hunter", "Assassin", "Warlock"]
        return random.choice(hero_prefix) + " " + random.choice(hero_types)

    def get_weapon(self):
        return self.char.weapon

    def increase_kills(self):
        self.kills += 1

    def change_title(self, passed_title):
        self.title = passed_title

    def statistics_readout(self):
        print("Character type: " + self.char.name)
        print("Weapon used: " + self.char.weapon.name + "\tDamage: " + self.char.weapon.low_damage + "-" + self.char.weapon.high_damage)
        print("Enemies vanquished: " + self.kills)
        print("Official title: " + self.title)

#class HeroCreation():
 #   def heroCreation(self, availableWeapons):
  #      heroC = Humanoid()
       # healthValue = heroC.generateHealth()
   #     return heroC.heroCreation(random.choice(availableWeapons))#, healthValue)


