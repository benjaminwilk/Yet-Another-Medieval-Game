import random

from Battle import Battle
from Enemy import Enemy
from WeaponPile import WeaponPile


class Castle():
    def __init__(self, hero):
        print("You walk up to the castle")
        if random.randrange(0, 100) > 90:
            print("The guards determine you're a threat, and want to fight!")
            guardCreature = Enemy(WeaponPile().getRandomWeapon())
            Battle(hero, guardCreature)
        else:
            print("The guards stand stoically; watching your every move, as you move inside.")
        self.guardSpeak(hero)

    def guardSpeak(self, hero):
        print("A guard stops you in your tracks and says; \"We don't let just anyone speak with the king.\"\nWhy are you here?");
        castleOptions = ["Ask for title increase", "Attack King", "Leave"]
        counter = 1
        for co in castleOptions:
            print(str(counter) + ". " + co)
            counter += 1
        userCO = input("What would you like to do: ")
        if int(userCO) == 1:
            self.increaseTitle(hero)
        if int(userCO) == 2:
            areYouSure = input("Are you sure you want to do this?  This is a death sentence!: ")
            if str(areYouSure) == "y" or str(areYouSure) == "yes":
                print("Fighting the guards and eventual king")
                guardOne = Enemy(WeaponPile().getRandomWeapon())
                Battle(hero, guardOne)
                Battle(hero, guardOne)
                Battle(hero, guardOne)

    def increaseTitle(self, hero):
        titleMultiplier = 500
        self.currentTitle = 0
        titleList = ["Nobody", "Baron", "Viscount", "Earl", "Marquis", "Sovereign Prince", "Duke", "Prince", "Crown Prince", "Arch Duke", "King", "Emperor"]
        self.currentTitle = titleList.index(hero.title)

        print(hero.char.name + "'s current title: " + hero.title)
        print("To increase your title from " + hero.title + " to " + titleList[self.currentTitle + 1] + " will cost " + str((self.currentTitle + 1) * titleMultiplier) + " gold.")
        if hero.char.money < (self.currentTitle + 1) * titleMultiplier:
            print("The guard raises his nose and says \"Looks like you can't afford this, peasant...\"")
            input()
        else:
            userIncrease = input("Do you accept this title increase: ")
            if "yes" in userIncrease or "y" in userIncrease:
                hero.decreaseMoney((self.currentTitle + 1) * titleMultiplier)
                hero.changeTitle(titleList[self.currentTitle + 1])
                print("The guard with a disinterested look on his face says \"Congratulations, you are offically a " + hero.title + "\".")
        print("You leave the castle.")