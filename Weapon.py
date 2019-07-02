import random

class Weapon(object):
    name = ""
    money = 0
    low_damage = 0
    high_damage = 0

    def create_weapon(self, passed_name):
        self.name = passed_name
        self.generate_low_damage()
        self.generate_high_damage()
        self.generate_price()
        return self

    def generate_weapon(self):
        self.name = self.generate_weapon_name()
        self.generate_low_damage()
        self.generate_high_damage()
        self.generate_price()
        return self

    def upgrade_weapon(self, passed_name):
        if "Fists" in passed_name:
            self.name = passed_name
            self.low_damage = 2
            self.high_damage = 3
            self.money = 0
        else:
            self.name = passed_name
            self.generate_low_damage()
            self.generate_high_damage()
            self.generate_price()

    def generate_weapon_name(self):
        prefix_names = ["stiff", "strong", "brittle", "hardened", "cracked", "broken"]
        material_names = ["iron", "steel", "gold", "silver", "wood", "jade"]
        arm_names = ["axe", "sword", "dagger", "bow", "staff"]
        return random.choice(prefix_names) + " " + random.choice(material_names) + " " + random.choice(arm_names)


    def dispense_damage(self):
        return random.randrange(self.low_damage, self.high_damage)

    def generate_low_damage(self):
        weapon_low_damage = {"gold": -2, "silver": 3, "jade": 3, "iron": 2, "wood": 1, "cracked": -2, "broken": -2, "strong": 4, "brittle": -2, "hardened": 6, "dagger": 4, "axe": 7, "sword": 7, "bow": 4, "staff": 5}
        for key, value in weapon_low_damage.items():
            if key in self.name:
                self.low_damage += value


    def generate_high_damage(self):
        weapon_high_damage = {"gold": -2, "silver": 4, "jade": 4, "iron": 2, "wood": 2, "cracked": -3, "broken": -3, "strong": 2, "brittle": -2, "hardened": 3, "dagger": 8, "axe": 14, "sword": 13, "bow": 10, "staff": 10}
        for key, value in weapon_high_damage.items():
            if key in self.name:
                self.high_damage += value

    def generate_price(self):
        weapon_price = {"gold": 20, "silver": 10, "jade": 10, "iron": 4, "wood": 4, "cracked": -10, "broken": -10, "strong": 4, "brittle": -4, "hardened": 8, "dagger": 10, "axe": 20, "sword": 20, "bow": 8, "staff": 8}
        for key, value in weapon_price.items():
            if key in self.name:
                self.money += value

class weapon_pile(object):
    weapon_grouping = []

    def __init__(self):
        self.generate_group()

    def generate_group(self):
        for x in range(5):
            self.weapon_grouping.append(Weapon().generate_weapon())

    def get_weapon_pile(self):
        return self.weapon_grouping

    def get_random_weapon(self):
        return random.choice(self.weapon_grouping)