n=float(input("What is the side length of your cube?"))
area=0

def calcSurf():
    global n,area
    area=(6*n*6*n)

def surfPrint():
    global area
    print(area)

calcSurf()
surfPrint()
