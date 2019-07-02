import random

from Body import Body


class NPC(object):
    def __init__(self, passed_weapon):
        self.char = Body(self.generate_NPC(), passed_weapon)

    def generate_NPC(self):
        npc_types = ["Shopkeep", "Guard", "Barkeep", "Stable boy"]
        return random.choice(npc_types)
