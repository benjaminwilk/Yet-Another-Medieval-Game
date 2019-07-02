import random

from Battle import Battle
from Enemy import Enemy
from Weapon import weapon_pile


class Castle():
    def __init__(self, hero):
        print("You walk up to the castle")
        if random.randrange(0, 100) > 90:
            print("The guards determine you're a threat, and want to fight!")
            guard_greature = Enemy(weapon_pile().get_random_weapon())
            Battle(hero, guard_greature)
        else:
            print("The guards stand stoically; watching your every move, as you move inside.")
        self.guard_speak(hero)

    def guard_speak(self, hero):
        print("A guard stops you in your tracks and says; \"We don't let just anyone speak with the king.\"\nWhy are you here?");
        castle_options = ["Ask for title increase", "Attack King", "Leave"]
        counter = 1
        for co in castle_options:
            print(str(counter) + ". " + co)
            counter += 1
        user_co = input("What would you like to do: ")
        if int(user_co) == 1:
            self.increase_title(hero)
        if int(user_co) == 2:
            are_you_sure = input("Are you sure you want to do this?  This is a death sentence!: ")
            if str(are_you_sure).upper() == "Y":
                print("Fighting the guards and eventual king")
                guard_one = Enemy(weapon_pile().get_random_weapon())
                Battle(hero, guard_one)
                Battle(hero, guard_one)
                Battle(hero, guard_one)
        print(hero.char.name + " leave the castle.")

    def increase_title(self, hero):
        title_multiplier = 500
        self.current_title = 0
        title_list = ["Nobody", "Baron", "Viscount", "Earl", "Marquis", "Sovereign Prince", "Duke", "Prince", "Crown Prince", "Arch Duke", "King", "Emperor"]
        self.current_title = title_list.index(hero.title)

        print(hero.char.name + "'s current title: " + hero.title)
        print("To increase your title from " + hero.title + " to " + title_list[self.current_title + 1] + " will cost " + str((self.current_title + 1) * title_multiplier) + " gold.")
        if hero.char.money < (self.current_title + 1) * title_multiplier:
            print("The guard raises his nose and says \"Looks like you can't afford this, peasant...\"")
            input()
        else:
            user_increase = input("Do you accept this title increase: ")
            if "y" in user_increase:
                hero.decrease_money((self.current_title + 1) * title_multiplier)
                hero.change_title(title_list[self.current_title + 1])
                print("The guard with a disinterested look on his face says \"Congratulations, you are offically a " + hero.title + "\".")