l=float(input("What is the length in feet?"))
w=float(input("What is the width in feet?"))
perim=0
length=l
width=w
def calcPerim(length, width):
    global l, w, perim
    perim=(2*l+2*w)

calcPerim(length, width)
print(perim)



num1=float(input("What is your first number?"))
num2=float(input("What is your second number?"))
num3=float(input("What is your third number?"))
average=((num1+num2+num3)/3)
def calcAve():
    global num1, num2,num3, average
    ((num1+num2+num3)/3)
print(average)



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



r=float(input("What is the radius of your circle?"))
area = 0
def circle():
    global r, area
    area = 3.14*r*r
    
circle()
print(area)
