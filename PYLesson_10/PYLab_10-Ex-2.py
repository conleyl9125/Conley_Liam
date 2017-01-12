go=input("please enter 16 strings")

spList = go.split(" ")

print(spList)

wordsList=[]
spot=0

print("\n2D Grid Pattern...")
for i in range(0,4):
    output = ""
    wordsList.append([])
    for j in range(0,4):
        wordsList[i].append(spList[spot])
        spot += 1
        output += wordsList[i][j] + " "
    print(output)
