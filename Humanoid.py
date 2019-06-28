from Body import Body
import random

class Humanoid(object):
    def heroCreation(self, passedWeapon, maxHealth):
        self.char = Body(self.generateHero(), passedWeapon, maxHealth, maxHealth)
        return self.char

    def enemyCreation(self, passedWeapon, maxHealth):
        self.char = Body(self.generateEnemy(), passedWeapon, maxHealth, maxHealth)
        return self.char

    def npcCreation(self, passedWeapon, maxHealth):
        self.char = Body(self.generateNPC(), passedWeapon, maxHealth, maxHealth)
        return self.char

    def generateEnemy(self):
        enemyTypes = ["Gremlin", "Ogre", "Thief", "Dragon", "Kobold", "Dark Knight", "Ghoul", "Satyr", "Gnoll"]
        return random.choice(enemyTypes)

    def generateHero(self):
        heroPrefix = ["Human", "Elf", "Halfling", "Dwarf", "Lizard person"]
        heroTypes = ["Paladin", "Knight", "Mage", "Rogue", "Priest", "Hunter", "Assassin", "Warlock"]
        return random.choice(heroTypes)

    def generateNPC(self):
        npcTypes = ["Shopkeep", "Guard", "Barkeep", "Stable boy"]
        return random.choice(npcTypes)

    def attack(self, damageAmount):
        return self.char.Name + " uses its " + self.char.Weapon.name + " to attack and dispenses " + str(damageAmount) + " damage."

    def generateHealth(self):
#        if "Human" in self.char.Name:


        return random.randrange(1, 25)


class HeroCreation():
    def heroCreation(self, availableWeapons):
        heroC = Humanoid()
        healthValue = heroC.generateHealth()
        return heroC.heroCreation(random.choice(availableWeapons), healthValue)

class EnemyCreation():
    def enemyCreation(self, availableWeapons):
        enemy = Humanoid()
        healthValue = enemy.generateHealth()
        return enemy.enemyCreation(random.choice(availableWeapons), healthValue)

class NPCCreation():
    def NPCCreation(self, availableWeapons):
        npc = Humanoid()
        healthValue = npc.generateHealth()
        return npc.npcCreation(random.choice(availableWeapons), healthValue)
