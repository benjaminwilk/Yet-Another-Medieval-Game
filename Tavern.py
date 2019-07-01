class Tavern():
    def __init__(self, hero):
        print(hero.char.name + " walks into the tavern, it's dark and smoky.")
        print("You make your way to the bar.")
        input()
        print("The barkeep says \"What will it be?\"")
        barOptions = ["Get a drink", "Hear rumors", "Leave"]
        print("Options:")
        counter = 1
        for bo in barOptions:
            print(str(counter) + ". " + bo)
            counter += 1
        UserBO = input("Your choice: ")
        if int(UserBO) is 1:
            print("Serve drink")
        if int(UserBO) is 2:
            print("Hear rumors")
