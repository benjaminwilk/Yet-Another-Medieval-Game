


class Inn():
    def __init__(self, hero):
        print("You walk into the Inn and see the friendly innkeeper.")
        print("You are currently missing " +  str(hero.maxHealth - hero.currentHealth) + " health points.")
        from main import NPCCreation
        innKeeper = NPCCreation()
        innKeeper = innKeeper.NPCCreation()
        innChoices = ["Sleep for the night", "Leave"]
        for i in innChoices:
            print(i)
        innDecision = input("Your decision: ")
        if int(innDecision) is 1:
            hero.currentHealth = hero.maxHealth
            print(hero.healthDisplay())
