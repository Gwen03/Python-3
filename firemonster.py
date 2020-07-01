print("You have found the fire monster, your location is (1,1).")

print('Type 1 to attack, 2 to heal')

#monster stats
import random
fhealth = random.randint(9,16)
fattack = random.randint(2,6)
fmhealth = fhealth
fmattack = fattack

#player stats
import main
phealth = main.health
pheal = main.heal
pattack = main.attack
#player = {'attack': main.attack, 'heal': main.heal, 'health': main.health}

#monster = {'attack': fma, 'health': fmh}
game_running = True

while game_running == True:

    
    player_choice = input()

    if player_choice == '1':
        print ("Attack")
        fmhealth = fmhealth - pattack
        phealth = phealth - fmattack
        print("Your health:", phealth)
        print("Monster health:", fmhealth)
    if player_choice == '2':
        print("Heal")
        phealth = phealth + pheal
        print("Your health:", phealth)
        
       

    if fmhealth <= 0:
        print("You have beat fire monster.")
        game_running = False
    if phealth <= 0:
        print ("You lost to fire monster.")
        game_running = False
    
  


