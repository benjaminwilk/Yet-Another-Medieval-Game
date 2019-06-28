import random

from Battle import Battle


class Castle():
    def __init__(self, hero):
        print("You walk up to the castle")
        if random.randrange(0, 100) > 90:
            print("The guards determine you're a threat, and want to fight!")
            guardCreature = EnemyCreation()
            guardCreature = guardCreature.enemyCreation()
            Battle(hero, guardCreature)
        else:
            print("The guards stand stoically; watching your every move, as you move inside.")
        self.guardSpeak(hero)

    def guardSpeak(self, hero):
        print("A guard stops you in your tracks and says; \"We don't let just anyone speak with the king.\"\nWhy are you here?");
        castleOptions = ["Ask for title", "Attack King", "Leave"]
        if str(castleOptions) == "title" or str(castleOptions) == "ask":
            print("Title receive")
        if str(castleOptions) == "attack" or str(castleOptions) == "king":
            areYouSure = input("Are you sure you want to do this?  This is a death sentence!: ")
            if str(areYouSure) == "y" or str(areYouSure) == "yes":
                print("Fighting the guards and eventual king")
                #Battle(hero, )