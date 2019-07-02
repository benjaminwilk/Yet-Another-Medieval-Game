
class Battle(object):
    surrender = False

    def __init__(self, hero, enemy):
        self.fight_prefix(hero, enemy)
        self.fight_loop(hero, enemy)

    def prefix_hero_display(self, hero):
        print(hero.char.weapon_display())
        print(hero.char.health_display())

    def prefix_enemy_display(self, enemy):
        print(enemy.char.weapon_display())
        print(enemy.char.health_display())

    def fight_prefix(self, hero, enemy):
        print("You find yourself in pitched combat with a " + enemy.char.name + "!")
        input()
        self.prefix_hero_display(hero)
        self.prefix_enemy_display(enemy)
        input()

    def user_fight_choice(self, enemy):
        fight_choices = ["Fight", "Run Away"]
        print("What would you like to do: ")
        counter = 1
        for fc in fight_choices:
            print(str(counter) + ". " + fc)
            counter += 1
        ufc = input("Your choice: ")
        if isinstance(enemy, list):
            for en in enemy:
                print (en)

        if int(ufc) is 1 or ufc is "":
            print("Who would you like to target: ")
            return False
        if int(ufc) is 2:
            return True

    def fight_loop(self, hero, enemy):
        self.surrender = False
        while self.surrender != True or enemy.char.alive() != False or hero.char.alive() != False:
            print("yeet")
            self.surrender = self.user_fight_choice(enemy)
            print(self.surrender)
            if self.surrender is False:
                damage_given_to_enemy = hero.get_weapon().dispense_damage()
                print(hero.char.attack(damage_given_to_enemy))
                enemy.char.decrease_health(damage_given_to_enemy)
                input()
                damage_given_to_you = enemy.get_weapon().dispense_damage()
                print(enemy.char.attack(damage_given_to_you))
                hero.char.decrease_health(damage_given_to_you)
                input()
                print(hero.char.health_display())
                print(enemy.char.health_display())
                input()
                self.ending_check(hero, enemy)
            else:
                print(hero.char.name + " starts running away from the fight!")
                input()

    def ending_check(self, hero, enemy):
        if enemy.char.current_health <= 0 and hero.char.current_health <= 0:
            print("Both you and your enemy collapse; both of you have been killed!")
            hero.statistics_readout()
            quit(1)
        elif enemy.char.current_health <= 0:
            print("The " + enemy.char.name + " throws down its " + enemy.get_weapon().name + ", and collapses to the ground; you have defeated " + enemy.char.name + "!")
            hero.increase_kills()
            input()
            self.looting(hero,enemy)
        elif hero.char.current_health <= 0:
            print("The " + hero.char.name + "'s vision goes black, and can't stand anymore; " + hero.char.name + " has been defeated!")
            hero.statistics_readout()
            quit(1)

    def looting(self, hero, enemy):
        if enemy.char.money > 0:
            print("You find on the struck down the " + enemy.char.name + ", it has " + str(enemy.char.money) + " gold.")
            hero.char.increase_money(enemy.char.money)
            print("You pocket the money.")
        print("You find on the struck down " + enemy.char.name + ", a " + enemy.get_weapon().name + ".  It's damage rating is " + str(enemy.get_weapon().low_damage) + "-" + str(enemy.get_weapon().high_damage))
        user_swap = input("Would you like to swap your " + hero.get_weapon().name + " for a " + enemy.get_weapon().name + "?: ")
        if "y" in user_swap or "Y" in user_swap:
            hero.get_weapon().upgrade_weapon(enemy.get_weapon().name)