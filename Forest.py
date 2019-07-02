import random

#from Battle import Battle
#from main import EnemyCreation
from Battle import Battle
from Enemy import Enemy
from Weapon import weapon_pile


class Forest(object):
    def __init__(self):
        self.plotter = [1,0]
        self.entry_count = 1

    def entry(self, hero):
        print("You find yourself in a clearing, looking at an entry to a forest.")
        input()
        entryFight = random.randrange(0, 100)
        if entryFight >= 90:
            print("You see a creature guarding the entrance, it wants to fight!")
            guard_creature = Enemy(weapon_pile().get_random_weapon())
          #  storeWeapons = WeaponPile().getWeapons()
          #  guardCreature = guardCreature.enemyCreation(storeWeapons)
            Battle(hero, guard_creature)
        self.wandering_overview(hero)

    def forest_descriptors(self):
        forestDescription = ["You fin"]

    def wandering_overview(self, hero):
        directions = ["north", "south", "east", "west", "Go Back to Town"]

        while self.is_plotter_zeroed() == False:
            print("What direction would you like to go: ")
            counter = 1
            for dir in directions:
                print(str(counter) + ". " + dir)
                counter += 1
            dir_choice = input("Your choice: ")
          #      self.entryCount += 1
            if dir_choice == "north" or dir_choice.upper() == "N":
                self.plotter[0] += 1
            if dir_choice == "south" or dir_choice.upper() == "S":
                self.plotter[0] -= 1
            if dir_choice == "east" or dir_choice.upper() == "E":
                self.plotter[1] += 1
            if dir_choice == "west" or dir_choice.upper() == "W":
                self.plotter[1] -= 1
            if "town" in dir_choice:
                self.plotter[0] = 0
                self.plotter[1] = 0

            deepness_range = random.randrange(self.plotter[0] * self.plotter[1], 100)
       #     print("Deepness Range: " + str(deepnessRange))
            if deepness_range > 50:
                available_weapons = weapon_pile().get_random_weapon()
          #      enemy = Enemy(availableWeapons)
                print("As " + hero.char.name + " comes to a clearing")
                Battle(hero, Enemy(available_weapons))

        if self.is_plotter_zeroed() == True:
            user_leave = input("Are you sure you want to leave the forest?: ")
            if str(user_leave) is "N" or str(user_leave) is "N":
                self.plotter[0] += 1
                print( hero.Name + " walks back into the forest.")
            else:
                print(hero.Name + " walks out of the forest, towards the town")

    def is_plotter_zeroed(self):
        if self.plotter[0] == 0 and self.plotter[1] == 0:
            return True
        else:
            return False