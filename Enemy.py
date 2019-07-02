import random

from Body import Body


class Enemy(object):

    def __init__(self, passed_weapon):
        self.char = Body(self.generate_enemy(), passed_weapon)

    def generate_enemy(self):
        enemy_types = ["Gremlin", "Ogre", "Thief", "Dragon", "Kobold", "Dark Knight", "Ghoul", "Satyr", "Gnoll"]
        return random.choice(enemy_types)

    def get_weapon(self):
        return self.char.weapon