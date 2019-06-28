import random

from Battle import Battle
from Humanoid import NPCCreation
from Weapon import Weapon
from WeaponPile import WeaponPile

class Shop():
    def __init__(self, hero):
        print("\n" + hero.Name + " currently has " + str(hero.money) + " gold.")
        print("The shopkeeper greets you")
        input()
        storeWeapons = WeaponPile().getWeapons()
        shopkeep = NPCCreation()
        shopkeep = shopkeep.NPCCreation(storeWeapons)
        userChoice = input("Are you buying or selling?: ")

        if str(userChoice) is "B" or str(userChoice) is "b":
            self.buyingMenu(hero, storeWeapons)
        if str(userChoice) is "S" or str(userChoice) is "s":
            self.sellingMenu(hero)
        if str(userChoice) is "K" or str(userChoice) is "k":
            print("\nYou lunge at the " + shopkeep.Name + " with your " + shopkeep.Weapon.name + "!\n")
            Battle(hero, shopkeep)

    def buyingMenu(self, hero, availableWeapons):
        print("Lets see what I have...")
        counter = 1
        for aw in availableWeapons:
            print(str(counter) + ". " + aw.name + " -- " + str(aw.lowDamage) + "-" + str(aw.highDamage) + " -- $" + str(random.randrange(5, 200)))
            counter += 1
        weaponChoice = input("Which one would you like to buy: ")
 #       sellOther = input("Would you like to sell your current weapon?: ")
        if int(weaponChoice) == 1 or int(weaponChoice) == 2 or int(weaponChoice) == 3 or int(weaponChoice) == 4 or int(weaponChoice) == 5:
          #  print("You replace your " + hero.Weapon.name + " with a " + availableWeapons[int(weaponChoice)].name)
         #   if sellOther is "y" or sellOther is "Y" or sellOther is "Yes":
            buyingWeapon =  Weapon(availableWeapons[int(weaponChoice) - 1].name, availableWeapons[int(weaponChoice) - 1].lowDamage, availableWeapons[int(weaponChoice) - 1].highDamage)
            if hero.money > buyingWeapon.money:
                hero.Weapon.upgradeWeapon(buyingWeapon.name, buyingWeapon.lowDamage, buyingWeapon.highDamage)
                hero.decreaseMoney(buyingWeapon.money)
                print(hero.Name + " now has " + str(hero.money) + " gold.")
            else:
                print("The shopkeep says, \"Sorry, you don't have enough money!\"")
            print("You leave the shop")
        #if int(weaponChoice) == 0:


    def sellingMenu(self, hero):
        print("What do you have to sell...")
        input()
        sellingWeapon = Weapon(hero.Weapon.name, hero.Weapon.lowDamage, hero.Weapon.highDamage)
        print("The shopkeep says, \"Your " + sellingWeapon.name + " is worth about " + str(sellingWeapon.money) + " gold.\"")
        userSell = input("Are you sure you would like to sell?: ")
        if userSell is "y" or userSell is "Y":
            hero.Weapon.upgradeWeapon("Fists", 2, 3)
            hero.increaseMoney(sellingWeapon.money)
            print(hero.Name + " now has " + str(hero.money) + " gold.")
