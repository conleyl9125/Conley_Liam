choice0=input("You find a broken down house. do you go inside? (yes/no)")
if choice0=="yes":
    choice2=input("you look around at the broken down interior, you see a tunnel leading down to the basement do you enter? (Yes/no)")
    if choice2=="yes":        
        choice4=input("you enter the basement. you see a monster, kill it? (yes/no)")
        if choice4=="yes":
            print("with what?... you die")
        else:
            print("you run away to live another day")
    else:
        choice6=input("you see a body on the ground. Do you touch it? (yes/no)")
        if choice6=="yes":
            print("it wakes and bites you...you die")
        else:
            print("officals come into the house and escort you out")
            
else:
    choice1=input("you are outside in an ash covered city. Do you (stay silent/call for help)")
    if choice1=="call for help":
        choice3=input("a zombie comes out the house. kill it? (yes/no)")
        if choice3=="yes":
            print("with what?...you die")
        else:
            print("you run away to live another day")
    else:
        choice5=input("you see a figure in the distance. do you go towards it? (yes/no)")
        if choice5=="yes":
            print("the figure turns out to be a monster. it sprints at you... you die")
        else:
            print("you run the other way and live another day")
