from NPC import NPC
from Weapon import weapon_pile


class Inn():
    def __init__(self, hero):
        print("You walk into the Inn and see the friendly innkeeper.")
        print("You are currently missing " +  str(hero.char.max_health - hero.char.current_health) + " health points.")
        self.inn_decision(hero)

    def inn_decision(self, hero):
        inn_keeper = NPC(weapon_pile().get_random_weapon())
        inn_choices = ["Sleep for the night", "Leave"]
        counter = 1
        for i in inn_choices:
            print(str(counter) + ". " + i)
            counter += 1
        inn_decision = input("Your decision: ")
        if int(inn_decision) is 1:
            print(hero.char.health_display())
            if hero.char.max_health - hero.char.current_health == 0:
                print("It will cost you 5 gold.")
            else:
                print("It will cost you " + str((hero.char.max_health - hero.char.current_health) * 2) + " gold.")
            if hero.char.money >= (hero.char.max_health - hero.char.current_health) * 2 or hero.char.money >= 5:
                sleep_yn = input("Would you like to stay the night: ")
                if sleep_yn.upper() is "Y":
                    if hero.char.max_health - hero.char.current_health == 0:
                        hero.char.decrease_money(5)
                    else:
                        hero.char.decrease_money((hero.char.max_health - hero.char.current_health) * 2)
                        hero.char.current_health = hero.char.max_health
                    print("The " + hero.char.name + " walks upstairs to the rented room, and sleeps for the night.")
            else:
                print("The innkeeper looks at you with a furrowed brow and says \"Sorry, it appears you don't have enough gold.\"")

        print(hero.char.name + " leaves the inn.")