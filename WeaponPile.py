import random

from Weapon import Weapon


class WeaponPile(object):
    def __init__(self):
        self.availableWeapons = self.generateWeapons()

    def getWeapons(self):
        return self.availableWeapons

    def generateWeapons(self):
        prefixNames = ["stiff", "strong", "brittle", "hardened", "", "cracked", "broken"]
        materialNames = ["iron", "steel", "gold", "silver", "wood", "jade"]
        armNames = ["axe", "sword", "dagger", "bow", "staff"]
        weaponSets = []

        for i in range(5):
            highVal = 0
            lowVal = 0
            while highVal == 0 and lowVal == 0:
                highVal = random.randrange(1, 20) + 1
                lowVal = random.randrange(1, highVal)
            weaponSets.append(Weapon(random.choice(prefixNames) + " " + random.choice(materialNames) + " " + armNames[i]))

        return weaponSets

    def getRandomWeapon(self):
        return random.choice(self.availableWeapons)