import random
xAndO=[]

for i in range(0,4):
    xAndO.append([])
    for j in range(0,4):
        switch=random.randint(0,1)
        if switch==1:
            xAndO[i].append("X")
        else:
            xAndO[i].append("O")
for i in xAndO:
    output=""
    for value in xAndO:
        output += "\n"
        for piece in value:
            output+=str(piece) + "\t"
            
print(output)

