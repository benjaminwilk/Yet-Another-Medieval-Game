import random

from Body import Body


class NPC(object):
    def __init__(self, passedWeapon):
        self.char = Body(self.generateNPC(), random.choice(passedWeapon))

    def generateNPC(self):
        npcTypes = ["Shopkeep", "Guard", "Barkeep", "Stable boy"]
        return random.choice(npcTypes)
