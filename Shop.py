import random

from Battle import Battle
from NPC import NPC
from Weapon import Weapon
from WeaponPile import WeaponPile

class Shop():
    def __init__(self, hero):
        print("\n" + hero.char.name + " currently has " + str(hero.char.money) + " gold.")
        print("The shopkeeper greets you")
        input()
        storeWeapons = WeaponPile().getWeapons()
        shopkeep = NPC(storeWeapons)
        userChoice = input("Are you buying or selling?: ")

        if str(userChoice) is "B" or str(userChoice) is "b" or "buy" in str(userChoice):
            self.buyingMenu(hero, storeWeapons)
        if str(userChoice) is "S" or str(userChoice) is "s" or "sell" in str(userChoice):
            self.sellingMenu(hero)
        if str(userChoice) is "K" or str(userChoice) is "k" or "attack" in str(userChoice) or "kill" in str(userChoice):
            print("\nYou lunge at the " + shopkeep.Name + " with your " + shopkeep.Weapon.name + "!\n")
            Battle(hero, shopkeep)



    def buyingMenu(self, hero, availableWeapons):
        print("Lets see what I have...")
        counter = 1
        for aw in availableWeapons:
            print(str(counter) + ". " + aw.name + " -- " + str(aw.lowDamage) + "-" + str(aw.highDamage) + " -- $" + str(random.randrange(30, 200)))
            counter += 1
        weaponChoice = input("Which one would you like to buy: ")
 #       sellOther = input("Would you like to sell your current weapon?: ")
        if int(weaponChoice) == 1 or int(weaponChoice) == 2 or int(weaponChoice) == 3 or int(weaponChoice) == 4 or int(weaponChoice) == 5:
          #  print("You replace your " + hero.Weapon.name + " with a " + availableWeapons[int(weaponChoice)].name)
         #   if sellOther is "y" or sellOther is "Y" or sellOther is "Yes":
            buyingWeapon =  Weapon(availableWeapons[int(weaponChoice) - 1].name)
            if hero.char.money > buyingWeapon.money:
                hero.GetWeapon().upgradeWeapon(buyingWeapon.name)
                hero.char.decreaseMoney(buyingWeapon.money)
                print(hero.char.name + " now has " + str(hero.char.money) + " gold.")
            else:
                print("The shopkeep grimmaces and says, \"Sorry, you don't have enough money!\"")
            print("You leave the shop")
        #if int(weaponChoice) == 0:


    def sellingMenu(self, hero):
        print("What do you have to sell...")
        input()
        sellingWeapon = Weapon(hero.GetWeapon().name)
        print("The shopkeep says, \"Your " + sellingWeapon.name + " is worth about " + str(sellingWeapon.money) + " gold.\"")
        userSell = input("Are you sure you would like to sell?: ")
        if userSell is "y" or userSell is "Y":
            hero.GetWeapon().upgradeWeapon("Fists")
            hero.char.increaseMoney(sellingWeapon.money)
            print(hero.char.name + " now has " + str(hero.char.money) + " gold.")
        print("You leave the shop")
