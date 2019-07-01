from NPC import NPC
from WeaponPile import WeaponPile


class Inn():
    def __init__(self, hero):
        print("You walk into the Inn and see the friendly innkeeper.")
        print("You are currently missing " +  str(hero.char.maxHealth - hero.char.currentHealth) + " health points.")
        innKeeper = NPC(WeaponPile().generateWeapons())
        innChoices = ["Sleep for the night", "Leave"]
        counter = 1
        for i in innChoices:
            print(str(counter) + ". " + i)
            counter += 1
        innDecision = input("Your decision: ")
        if int(innDecision) is 1:
            print(hero.char.healthDisplay())
            if hero.char.maxHealth - hero.char.currentHealth == 0:
                print("It will cost you 5 gold.")
            else:
                print("It will cost you " + str((hero.char.maxHealth - hero.char.currentHealth) * 2) + " gold.")
            if hero.char.money >= (hero.char.maxHealth - hero.char.currentHealth) * 2 or hero.char.money >= 5:
                sleepYN = input("Would you like to stay the night: ")
                if sleepYN is "y" or sleepYN is "Y":
                    if hero.char.maxHealth - hero.char.currentHealth == 0:
                        hero.char.decreaseMoney(5)
                    else:
                        hero.char.decreaseMoney((hero.char.maxHealth - hero.char.currentHealth) * 2)
                        hero.char.currentHealth = hero.char.maxHealth
                    print("The " + hero.char.name + " walks upstairs to the rented room, and sleeps for the night.")
            else:
                print("The innkeeper looks at you with a furrowed brow and says \"Sorry, it appears you don't have enough gold.\"")