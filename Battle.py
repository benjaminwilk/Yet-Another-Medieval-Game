
class Battle(object):
    surrender = False

    def __init__(self, hero, enemy):
        self.fightPrefix(hero, enemy)
        self.fightLoop(hero, enemy)

    def prefixHeroDisplay(self, hero):
        print(hero.char.weaponDisplay())
        print(hero.char.healthDisplay())

    def prefixEnemyDisplay(self, enemy):
        print(enemy.char.weaponDisplay())
        print(enemy.char.healthDisplay())

    def fightPrefix(self, hero, enemy):
        print("You find yourself in pitched combat with a " + enemy.char.name + "!")
        input()
        self.prefixHeroDisplay(hero)
        self.prefixEnemyDisplay(enemy)
        input()

    def userFightChoice(self, enemy):
        fightChoices = ["Fight", "Run Away"]
        print("What would you like to do: ")
        counter = 1
        for fc in fightChoices:
            print(str(counter) + ". " + fc)
            counter += 1
        ufc = input("Your choice: ")
        if isinstance(enemy, list):
            for en in enemy:
                print (en)

        if int(ufc) is 1:
            print("Who would you like to target: ")

            return False
        if int(ufc) is 2:
            return True


    def fightLoop(self, hero, enemy):
        self.surrender = False
        while self.surrender != True:# or (enemy.char.alive() == True and hero.char.alive() == True):
            self.surrender = self.userFightChoice(enemy)
            print(self.surrender)
            if self.surrender is False:
                damageGivenToEnemy = hero.GetWeapon().dispenseDamage()
                print(hero.char.attack(damageGivenToEnemy))
                enemy.char.decreaseHealth(damageGivenToEnemy)
                input()
                damageGivenToYou = enemy.GetWeapon().dispenseDamage()
                print(enemy.char.attack(damageGivenToYou))
                hero.char.decreaseHealth(damageGivenToYou)
                input()
                print(hero.char.healthDisplay())
                print(enemy.char.healthDisplay())
                input()
                self.endingCheck(hero, enemy)
            else:
                print(hero.char.name + " starts running away from the fight!")
                input()


    def endingCheck(self, hero, enemy):
        if enemy.char.currentHealth <= 0 and hero.char.currentHealth <= 0:
            quit("Both you and your enemy collapse; both of you have been killed!")
        elif enemy.char.currentHealth <= 0:
            print("The " + enemy.char.name + " throws down its " + enemy.GetWeapon().name + ", and collapses to the ground; you have defeated " + enemy.char.name + "!")
            hero.increaseKills()
            input()
            self.looting(hero,enemy)
        elif hero.char.currentHealth <= 0:
            quit("The " + hero.char.name + "'s vision goes black, and can't stand anymore; " + hero.char.name + " has been defeated!")

    def looting(self, hero, enemy):
        if enemy.char.money > 0:
            print("You find on the struck down the " + enemy.char.name + ", it has " + str(enemy.char.money) + " gold.")
            hero.char.increaseMoney(enemy.char.money)
            print("You pocket the money.")
        print("You find on the struck down " + enemy.char.name + ", a " + enemy.GetWeapon().name + ".  It's damage rating is " + str(enemy.GetWeapon().lowDamage) + "-" + str(enemy.GetWeapon().highDamage))
        userSwap = input("Would you like to swap your " + hero.GetWeapon().name + " for a " + enemy.GetWeapon().name + "?: ")
        if "y" in userSwap or "Y" in userSwap:
            hero.GetWeapon().upgradeWeapon(enemy.GetWeapon().name)