import wx

from Castle import Castle
from Forest import Forest
from Hero import Hero
from Inn import Inn
from Shop import Shop
from Tavern import Tavern
from Weapon import Weapon


class World():
    def main(self):
        self.mainPane()


    def mainPane(self):
        locations = ["Tavern", "Shop", "Forest", "Inn", "Castle"]
        character_approval = False
        while character_approval != True:
            hero = Hero(Weapon().generate_weapon())
            print("Your character is " + hero.char.name + "\nEquipped with a " + hero.get_weapon().name + " that does " + str(hero.get_weapon().low_damage) + "-" + str(hero.get_weapon().high_damage) + " damage.")
            char_generation = input("Do you approve of this character: ")
            if "Y" in char_generation.upper():
                character_approval = True

        while True:
            print("\nLocations: ")
            counter = 1
            for i in locations:
                print( str(counter) + ". " + i)
                counter += 1
            location_choice = input("Where would you like to go: ")
            if int(location_choice) is 1:
                Tavern(hero)
            if int(location_choice) is 2:
                Shop(hero)
            if int(location_choice) is 3:
                forest = Forest()
                forest.entry(hero)
            if int(location_choice) is 4:
                hotel = Inn(hero)
            if int(location_choice) is 5:
                Castle(hero)
            input()



gameboard = World.main()