import random

import Weapon

class Body(object):

    money = random.randrange(0, 100)

    def __init__(self, name, weapon, maxHealth, currentHealth):
        self.Name = name
        self.Weapon = weapon
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth

    def healthBar(self):
        return str(self.currentHealth) + "/" + str(self.maxHealth)

    def healthDisplay(self):
        return self.Name + " current health: " + self.healthBar()

    def weaponDisplay(self):
        return self.Name + " has a " + self.Weapon.name + "\nit will do "+ str(self.Weapon.lowDamage) + "-" + str(self.Weapon.highDamage) + " damage"

    def attack(self, damageAmount):
        return self.Name + " uses its " + self.Weapon.name + " to attack and dispenses " + str(damageAmount) + " damage."

    def decreaseHealth(self, countDown):
        self.currentHealth = self.currentHealth - countDown

    def alive(self):
        if self.currentHealth <= 0:
            return False
        else:
            return True

    def increaseMoney(self, passedMoney):
        self.money += passedMoney

    def decreaseMoney(self, passedMoney):
        self.increaseMoney(-1 * passedMoney)