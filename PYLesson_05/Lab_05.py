import random
playerRoll=random.randint(1,6)
compRoll=random.randint(1,6)

def rollDice(player, comp):
    print("Your roll is", playerRoll)
    print("The computer's roll is", compRoll)
rollDice(playerRoll, compRoll)

if playerRoll>compRoll:
    print("You win!")
if compRoll>playerRoll:
    print("The computer wins")


