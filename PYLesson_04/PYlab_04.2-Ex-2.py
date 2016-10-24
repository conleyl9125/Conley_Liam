num1=float(input("What is your first number?"))
num2=float(input("What is your second number?"))
num3=float(input("What is your third number?"))

def average(n1,n2,n3):
    return((n1+n2+n3)/3)
print("The average of your three numbers is",average(num1,num2,num3), "")
