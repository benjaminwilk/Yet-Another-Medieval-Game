import random

class Weapon(object):
    money = 0
    lowDamage = 0
    highDamage = 0

    def __init__(self, passedName):
        self.name = passedName
        self.generateLowDamage()
        self.generateHighDamage()
        self.generatePrice()

    def upgradeWeapon(self, passedName):
        if "Fists" in passedName:
            self.name = passedName
            self.lowDamage = 2
            self.highDamage = 3
            self.money = 0
        else:
            self.name = passedName
            self.generateLowDamage()
            self.generateHighDamage()
            self.generatePrice()

    def damageSanityCheck(self):
        while self.lowDamage == self.highDamage:
            self.highDamage += 1

    def dispenseDamage(self):
        return random.randrange(self.lowDamage, self.highDamage)


    def generateLowDamage(self):
        accumulation = 0
        if "gold" in self.name:
            self.lowDamage -= 2
        if "silver" in self.name or "jade" in self.name:
            self.lowDamage += 3
        if "iron" in self.name or "wood" in self.name:
            self.lowDamage += 2
        if "cracked" in self.name or "broken" in self.name:
            self.lowDamage -= 2
        if "strong" in self.name:
            self.lowDamage += 4
        if "brittle" in self.name:
            self.lowDamage -= 2
        if "hardened" in self.name:
            self.lowDamage += 8
        if "dagger" in self.name:
            self.lowDamage += 4
        if "axe" in self.name or "sword" in self.name:
            self.lowDamage += 7
        if "bow" in self.name or "staff" in self.name:
            self.lowDamage += 5

    def generateHighDamage(self):
        accumulation = 0
        if "gold" in self.name:
            self.highDamage -= 2
        if "silver" in self.name or "jade" in self.name:
            self.highDamage += 4
        if "iron" in self.name or "wood" in self.name:
            self.highDamage += 2
        if "cracked" in self.name or "broken" in self.name:
            self.highDamage -= 3
        if "strong" in self.name:
            self.highDamage += 2
        if "brittle" in self.name:
            self.highDamage -= 2
        if "hardened" in self.name:
            self.highDamage += 3
        if "dagger" in self.name:
            self.highDamage += 7
        if "axe" in self.name or "sword" in self.name:
            self.highDamage += 12
        if "bow" in self.name or "staff" in self.name:
            self.highDamage += 10

    def generatePrice(self):
        if "gold" in self.name:
            self.money += 20
        if "silver" in self.name or "jade" in self.name:
            self.money += 10
        if "iron" in self.name or "wood" in self.name:
            self.money += 4
        if "cracked" in self.name or "broken" in self.name:
            self.money -= 10
        if "strong" in self.name:
            self.money += 4
        if "brittle" in self.name:
            self.money -= 4
        if "hardened" in self.name:
            self.money += 8
        if "dagger" in self.name:
            self.money += 10
        if "axe" in self.name or "sword" in self.name:
            self.money += 20
        if "bow" in self.name or "staff" in self.name:
            self.money += 8