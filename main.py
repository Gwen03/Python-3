print("Welcome to my first text game, written in python.")

print("Please name your character")
username = input()
print("Welcome to Drugland, " + username + ".")

print("Feel free to explore the world. What would you like to do?")
print("Please use only lowercase letters and no punctation.")
print("For examples on what you can do, type 'helpme'.")
print("To exit game, type 'exit'.")

gameon = True

#starting inventory
crackamount = 0
methamount = 0

#starting coordinates
x = 0
y = 0

#player stats
import random
health = random.randint(9,16)
attack = random.randint(1,5)
heal = random.randint(1,5)

while gameon == True:

    #keywords
    keywords = ("buy", "crack", "meth", "helpme", "exit", "inventory", "coordinates", "w", "a", "s", "d")
    choose = input()
    actionwords = choose.split()

    #inventory
    def inventory():
        print ("You have this much crack:", crackamount )
        print("You have this much meth:", methamount )

    #coordinates
    def cod():
        print("Your location is", x , ",", y,)

    #basic world actions
    for word in actionwords:
        if word in keywords: 
            #use this if making sure it works
            #print("200")
            checkingword = word #idk why this is needed, should go figure this out
            
            if checkingword == "helpme":
                print(
                    "To buy drugs, type 'buy', followed by the drugs you want to buy. For example, 'buy crack'."
                )
            if checkingword == "exit":
                gameon = False
            if checkingword == "inventory":
                inventory()
            if checkingword == "coordinates":
                cod()
            #moving charcter
            if checkingword == "w":
                y = y + 1
            if checkingword == "s":
                y = y - 1
            if checkingword == "a":
                x = x - 1
            if checkingword == "d":
                x = x + 1

            if checkingword == "crack":
                print("You bought crack.")
                crackamount = crackamount + 1

            if checkingword == "meth":
                print("You bought meth.")
                methamount = methamount + 1
            
       #linear storylines
        #firemonster
        if x == 1 & y == 1:
            import firemonster
print("You have exited the game, have a good day!")