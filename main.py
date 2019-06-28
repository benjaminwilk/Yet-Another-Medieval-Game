import random

from Battle import Battle
from Body import Body
from Castle import Castle
from Forest import Forest
from Humanoid import Humanoid, HeroCreation
from Inn import Inn
from Shop import Shop
from Tavern import Tavern
from WeaponPile import WeaponPile

class World():
    def __init__(self):
        availableWeapons = WeaponPile().getWeapons()
        locations = ["Tavern", "Shop", "Forest", "Inn", "Castle"]
        userApproval = False
        while userApproval != True:
            hero = HeroCreation()
            hero = hero.heroCreation(availableWeapons)
            print(hero.healthDisplay())
            print("Your character is " + hero.Name + "\nEquipped with a " + hero.Weapon.name + " that does " + str(hero.Weapon.lowDamage) + "-" + str(hero.Weapon.highDamage) + " damage.")
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