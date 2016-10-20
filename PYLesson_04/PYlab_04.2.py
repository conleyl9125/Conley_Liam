l=float(input("What is the length in feet?"))

w=float(input("What is the width in feet?"))

def calcPerim(le,wi):
    return(le*wi)

print("Your rectangle is", calcPerim(l,w) ,"ft around.")


num1=float(input("What is your first number?"))
num2=float(input("What is your second number?"))
num3=float(input("What is your third number?"))

def average(n1,n2,n3):
    return((n1+n2+n3)/3)
print("The average of your three numbers is",average(num1,num2,num3), "")


n=float(input("What is the side length of your cube?"))

def calcSurf(n):
    return (6*n*6*n)

print("The surface area of your cube is",calcSurf(n), "")

r=float(input("What is the radius of your circle?"))
area = 0
def circle(r):
    return(3.14*r*r)
    area=3.14*r*r
    
print(circle(r))

