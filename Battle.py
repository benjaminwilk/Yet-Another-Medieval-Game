
class Battle(object):
    def __init__(self, hero, enemy):
        #EnemyC = EnemyCreation()
        #enemyValue = EnemyC.enemyCreation(availableWeapons)
        self.fightPrefix(hero, enemy)
        self.fightLoop(hero, enemy)

    # def Fight(self):
    #     availableWeapons = WeaponPile().getWeapons()
    #     self.fightLoop(self.heroCreation(availableWeapons), self.enemyCreation(availableWeapons))

    def prefixHeroDisplay(self, hero):
        print(hero.weaponDisplay())
        print(hero.healthDisplay())

    def prefixEnemyDisplay(self, enemy):
        print(enemy.weaponDisplay())
        print(enemy.healthDisplay())

    def fightPrefix(self, hero, enemy):
        print("You find yourself in pitched combat with a " + enemy.Name + "!")
        self.prefixHeroDisplay(hero)
        self.prefixEnemyDisplay(enemy)
        input()

    def fightLoop(self, hero, enemy):
        while enemy.alive() and hero.alive():
            damageGivenToEnemy = hero.Weapon.dispenseDamage()
            print(hero.attack(damageGivenToEnemy))
            enemy.decreaseHealth(damageGivenToEnemy)
            input()
            damageGivenToYou = enemy.Weapon.dispenseDamage()
            print(enemy.attack(damageGivenToYou))
            hero.decreaseHealth(damageGivenToYou)
            input()
            print(hero.healthDisplay())
            print(enemy.healthDisplay())
            input()
            self.endingCheck(hero, enemy)

    def endingCheck(self, hero, enemy):
        if enemy.currentHealth <= 0 and hero.currentHealth <= 0:
            quit("Both you and your enemy collapse; both of you have been killed!")
        elif enemy.currentHealth <= 0:
            print("The " + enemy.Name + " throws down its " + enemy.Weapon.name + ", and collapses to the ground; you have defeated " + enemy.Name + "!")
        elif hero.currentHealth <= 0:
            quit("The " + hero.Name + "'s vision goes black, and can't stand anymore; " + hero.Name + " has been defeated!")