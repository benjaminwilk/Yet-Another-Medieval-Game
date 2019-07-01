from Body import Body
import random

class Hero():
    kills = 0
    title = "Nobody"

    def __init__(self, passedWeapon):
        self.char = Body(self.generateHero(), passedWeapon)

    def generateHero(self):
        heroPrefix = ["Human", "Elf", "Halfling", "Dwarf", "Lizard person"]
        heroTypes = ["Paladin", "Knight", "Mage", "Rogue", "Priest", "Hunter", "Assassin", "Warlock"]
        return random.choice(heroPrefix) + " " + random.choice(heroTypes)

    def GetWeapon(self):
        return self.char.weapon

    def increaseKills(self):
        self.kills += 1

    def changeTitle(self, passedTitle):
        self.title = passedTitle

#class HeroCreation():
 #   def heroCreation(self, availableWeapons):
  #      heroC = Humanoid()
       # healthValue = heroC.generateHealth()
   #     return heroC.heroCreation(random.choice(availableWeapons))#, healthValue)


