import random

from Battle import Battle
from Body import Body
from Castle import Castle
from Forest import Forest
from Hero import Hero
from Inn import Inn
from Shop import Shop
from Tavern import Tavern
from Weapon import Weapon
from WeaponPile import WeaponPile

class World():
    def __init__(self):
        locations = ["Tavern", "Shop", "Forest", "Inn", "Castle"]
        userApproval = False
        while userApproval != True:
            availableWeapons = WeaponPile().getRandomWeapon()
            hero = Hero(availableWeapons)
            print("Your character is " + hero.char.name + "\nEquipped with a " + hero.GetWeapon().name + " that does " + str(hero.GetWeapon().lowDamage) + "-" + str(hero.GetWeapon().highDamage) + " damage.")
            userText = input("Do you approve of this character: ")
            if userText is "Y" or userText is "y" or userText is "Yes":
                userApproval = True

        while True:
            print("\nLocations: ")
            counter = 1
            for i in locations:
                print( str(counter) + ". " + i)
                counter+=1
            userChoice = input("Where would you like to go: ")
            if int(userChoice) is 1:
                Tavern(hero)
            if int(userChoice) is 2:
                Shop(hero)
            if int(userChoice) is 3:
                forest = Forest()
                forest.entry(hero)
            if int(userChoice) is 4:
                hotel = Inn(hero)
            if int(userChoice) is 5:
                Castle(hero)
            input()



gameboard = World()