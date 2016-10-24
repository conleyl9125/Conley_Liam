def interst(pr,ra,nu,ti):
    return((p*((1+(r/n))**(n*t)))/(t*12))

print("This is a interest calculator for a loan")
r=float(input("What is your interest rate?"))
p=float(input("What is your principal?"))
n=float(input("How many times has the loan compounded per year?"))
t=float(input("What is the life of the loan in years?"))

print("your monthly payment is: ", "{:5.2f}".format(interst(p,r,n,t)))
