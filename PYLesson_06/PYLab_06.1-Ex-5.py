finish=int(input("Enter a number that the pattern will end at"))
x=int(input("Enter a number that the pattern will increase by"))

def printPattern():
    for i in range(0,int(finish/x),1):
        print((1+i)*x)
printPattern()

