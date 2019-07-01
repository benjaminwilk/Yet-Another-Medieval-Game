import random

import Weapon

class Body(object):

    maxHealth = 1
    currentHealth = 1
    money = 1

    def __init__(self, passedName, passedWeapon):
        self.name = passedName
        self.weapon = passedWeapon
        self.maxHealth = self.generateHealth()
        self.currentHealth = self.maxHealth
        self.money = self.generateMoney()

    def generateHero(self):
        heroPrefix = ["Human", "Elf", "Halfling", "Dwarf", "Lizard person"]
        heroTypes = ["Paladin", "Knight", "Mage", "Rogue", "Priest", "Hunter", "Assassin", "Warlock"]
        return random.choice(heroPrefix) + " " + random.choice(heroTypes)

    def healthBar(self):
        return str(self.currentHealth) + "/" + str(self.maxHealth)

    def attack(self, damageAmount):
        return self.name + " uses its " + self.weapon.name + " to attack and dispenses " + str(damageAmount) + " damage."

    def healthDisplay(self):
        return self.name + " current health: " + self.healthBar()

    def weaponDisplay(self):
        return self.name + " has a " + self.weapon.name + "\nit will do "+ str(self.weapon.lowDamage) + "-" + str(self.weapon.highDamage) + " damage"

    def attack(self, damageAmount):
        return self.name + " uses its " + self.weapon.name + " to attack and dispenses " + str(damageAmount) + " damage."

    def decreaseHealth(self, countDown):
        self.currentHealth = self.currentHealth - countDown

    def alive(self):
        if self.currentHealth <= 0:
            return False
        else:
            return True

    def generateHealth(self):
        healthValue = 1
        if "Gremlin" in self.name:
            healthValue = 20
        if "Ogre" in self.name:
            healthValue = 40
        if "Thief" in self.name:
            healthValue = 25
        if "Dragon" in self.name:
            healthValue = 75
        if "Kobold" in self.name:
            healthValue = 15
        if "Dark Knight" in self.name:
            healthValue = 50
        if "Ghoul" in self.name:
            healthValue = 10
        if "Satyr" in self.name:
            healthValue = 20
        if "Gnoll" in self.name:
            healthValue = 15
        if "Human" in self.name:
            healthValue = 30
        if "Elf" in self.name:
            healthValue = 20
        if "Halfling" in self.name:
            healthValue = 25
        if "Dwarf" in self.name:
            healthValue = 40
        if "Lizard person" in self.name:
            healthValue = 35
        return healthValue

    def generateMoney(self):
        return random.randrange(50, 400)

    def increaseMoney(self, passedMoney):
        self.money += passedMoney

    def decreaseMoney(self, passedMoney):
        self.increaseMoney(-1 * passedMoney)