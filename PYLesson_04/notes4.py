def method1(thing):
    return thing

def thingPrint(thing):
    print("method1 returns the thing",method1(thing))

thing=Tp MTB
thingPrint(thing)

num=3
num2=4
sum=0

def mkSum():
    global sum, num, num2
    sum=num+num2

def numPrint():
    global sum, num, num2
    print(num,"plus",num2,"equals", sum)

mkSum()
numPrint()
