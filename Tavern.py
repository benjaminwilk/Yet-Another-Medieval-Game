import random

from Hero import Hero
from Weapon import Weapon


class Tavern():
    def __init__(self, hero):
        print(hero.char.name + " walks into the tavern, it's dark and smoky.")
        print("You make your way to the bar.")
        input()
        self.tavern_menu(hero)

    def tavern_menu(self, hero):
        print("The barkeep says \"What will it be?\"")
        bar_option = ["Get a drink", "Hear rumors", "Hire mercenaries", "Leave"]
        print("Options:")
        counter = 1
        for bo in bar_option:
            print(str(counter) + ". " + bo)
            counter += 1
        user_bar_option = input("Your choice: ")
        if int(user_bar_option) is 1:
            self.order_drink(hero)
        if int(user_bar_option) is 2:
            self.hear_rumors(hero)
        if int(user_bar_option) is 3:
            self.hire_mercenaries(hero)

        print("You leave the tavern.")

    def hear_rumors(self, hero):
        print(hero.char.name + " leans over to the bar, and asks the bartender, \"Have you heard any rumors around town?\"")
        print("Sorry, no news around here.")
        input()

    def order_drink(self, hero):
        print("The barkeep smiles and says \"We have mead; it's 10 gold a mug.\"")
        drink_order = input("Order a drink?: ")
        if "Y" in drink_order.upper():
            hero.decrease_money(10)
            print("The barkeep dips a clean mug into a barrel, and hands it to you.")
            print(hero.char.name + " drinks the mug of mead while relaxing.")

    def hire_mercenaries(self, hero):
        merc_count = random.randrange(1, 6)
        available_mercs = []
        print(hero.char.name + " asks for where to find mercenaries, and the barkeep points you towards the back of the tavern.")
        print(hero.char.name + " finds " + str(merc_count) + " mercenaries available.")
        count = 1
        for i in range(merc_count):
            generated_merc = Hero(Weapon().generate_weapon())
            available_mercs.append(generated_merc)
            print(str(count) + "Name: " + generated_merc.char.name + "\t" + generated_merc.char.health_bar() + "\t" + "Weapon: " + generated_merc.char.weapon.name + " " + str(generated_merc.char.weapon.low_damage) + "-" + str(generated_merc.char.weapon.high_damage))
            count += 1
        hire_merc = input("Would you like to hire a mercenary?: ")
        if hire_merc <= merc_count - 1 and hire_merc >= 0:
            hired_merc = available_mercs[hire_merc - 1]
            #hero.append(hired_merc)