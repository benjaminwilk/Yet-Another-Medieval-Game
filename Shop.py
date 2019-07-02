import random

from Battle import Battle
from NPC import NPC
from Weapon import Weapon, weapon_pile


class Shop():
    def __init__(self, hero):
        print("\n" + hero.char.name + " currently has " + str(hero.char.money) + " gold.")
        print("The shopkeeper greets you")
        input()
        shopkeep = NPC(weapon_pile().get_random_weapon())
        shopper_choice = input("Are you buying or selling?: ")

        if "B" in str(shopper_choice).upper():
            self.buying_menu(hero)
        if "S" in str(shopper_choice).upper():
            self.sellingMenu(hero)
        if "K" in str(shopper_choice).upper() or "A" in str(shopper_choice).upper():
            print("\nYou lunge at the " + shopkeep.Name + " with your " + shopkeep.Weapon.name + "!\n")
            Battle(hero, shopkeep)

    def buying_menu(self, hero):
        print("Lets see what I have...")
        available_weapons = weapon_pile().get_weapon_pile()
        counter = 1
        for aw in available_weapons:
            print(str(counter) + ". " + aw.name + " -- " + str(aw.low_damage) + "-" + str(aw.high_damage) + " -- $" + str(random.randrange(30, 200)))
            counter += 1
        weapon_choice = input("Which one would you like to buy: ")
        if int(weapon_choice) >= 1  and int(weapon_choice) <= len(available_weapons):
            buying_weapon =  Weapon(available_weapons[int(weapon_choice) - 1].name)
            if hero.char.money > buying_weapon.money:
                hero.GetWeapon().upgrade_weapon(buying_weapon.name)
                hero.char.decrease_money(buying_weapon.money)
                print(hero.char.name + " now has " + str(hero.char.money) + " gold.")
            else:
                print("The shopkeep grimmaces and says, \"Sorry, you don't have enough money!\"")
            print("You leave the shop")

    def selling_menu(self, hero):
        print("What do you have to sell...")
        input()
        selling_weapon = Weapon(hero.get_weapon().name)
        print("The shopkeep says, \"Your " + selling_weapon.name + " is worth about " + str(selling_weapon.money) + " gold.\"")
        user_sale = input("Are you sure you would like to sell?: ")
        if user_sale.upper() is "Y":
            hero.get_weapon().upgrade_weapon("Fists")
            hero.char.increase_money(selling_weapon.money)
            print(hero.char.name + " now has " + str(hero.char.money) + " gold.")
        print("You leave the shop")