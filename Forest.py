import random

#from Battle import Battle
#from main import EnemyCreation
from Battle import Battle
from Enemy import Enemy
from WeaponPile import WeaponPile


class Forest(object):
    def __init__(self):
        self.plotter = [1,0]
        self.entryCount = 1

    def entry(self, hero):
        print("You find yourself in a clearing, looking at an entry to a forest.")
        input()
        entryFight = random.randrange(0, 100)
        if entryFight >= 90:
            print("You see a creature guarding the entrance, it wants to fight!")
            guardCreature = Enemy(WeaponPile.getRandomWeapon())
            storeWeapons = WeaponPile().getWeapons()
            guardCreature = guardCreature.enemyCreation(storeWeapons)
            Battle(hero, guardCreature)
        self.wanderingOverview(hero)

    def forestDescriptors(self):
        forestDescription = ["You fin"]

    def wanderingOverview(self, hero):
        directions = ["north", "south", "east", "west", "Go Back to Town"]

        while self.isPlotterZeroed() == False:
            print("What direction would you like to go: ")
            counter = 1
            for dir in directions:
                print(str(counter) + ". " + dir)
                counter += 1
            dirChoice = input("Your choice: ")
          #      self.entryCount += 1
            if dirChoice == "north" or dirChoice == "n" or dirChoice == "N":
                self.plotter[0] += 1
            if dirChoice == "south" or dirChoice == "s" or dirChoice == "S":
                self.plotter[0] -= 1
            if dirChoice == "east" or dirChoice == "e" or dirChoice == "E":
                self.plotter[1] += 1
            if dirChoice == "west" or dirChoice == "w" or dirChoice == "W":
                self.plotter[1] -= 1
            if "town" in dirChoice:
                self.plotter[0] = 0
                self.plotter[1] = 0

            deepnessRange = random.randrange(self.plotter[0] * self.plotter[1], 100)
       #     print("Deepness Range: " + str(deepnessRange))
            if deepnessRange > 50:
                availableWeapons = WeaponPile().getRandomWeapon()
          #      enemy = Enemy(availableWeapons)
                print("As " + hero.char.name + " comes to a clearing")
                Battle(hero, Enemy(availableWeapons))

        if self.isPlotterZeroed() == True:
            userLeave = input("Are you sure you want to leave the forest?: ")
            if str(userLeave) is "N" or str(userLeave) is "N":
                self.plotter[0] += 1
                print( hero.Name + " walks back into the forest.")
            else:
                print(hero.Name + " walks out of the forest, towards the town")

    def isPlotterZeroed(self):
        if self.plotter[0] == 0 and self.plotter[1] == 0:
            return True
        else:
            return False