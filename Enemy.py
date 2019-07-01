import random

from Body import Body


class Enemy(object):

    def __init__(self, passedWeapon):
        self.char = Body(self.generateEnemy(), passedWeapon)

    def generateEnemy(self):
        enemyTypes = ["Gremlin", "Ogre", "Thief", "Dragon", "Kobold", "Dark Knight", "Ghoul", "Satyr", "Gnoll"]
        return random.choice(enemyTypes)

    def GetWeapon(self):
        return self.char.weapon