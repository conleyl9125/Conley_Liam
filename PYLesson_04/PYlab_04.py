

def interst(pr,ra,nu,ti):
    return((p*((1+(r/n))**(n*t)))/(t*12))

print("This is a interest calculator for a loan")
r=float(input("What is your interest rate?"))
p=float(input("What is your principal?"))
n=float(input("How many times has the loan compounded per year?"))
t=float(input("What is the life of the loan in years?"))

print("your monthly payment is: ", "{:5.2f}".format(interst(p,r,n,t)))

def printf (food, price):
    print("*{:<16}   {:10.2f}".format(food, price))

food1 =input(print("What did you order first"))
price1 =float(input(print("How much did it cost?")))

food2 =input(print("What did you order next?"))
price2 =float(input(print("How much did it cost?")))
                  
food3 =input(print("What did you order last?"))
price3 =float(input(print("How much did it cost?")))


printf(food1, price1)
printf(food2, price2)
printf(food3, price3)

print("\n")

food4 = "Subtotal"
price4 = price1+price2+price3

printf (food4, price4)


food5 = "Tax"
price5 = 0.63

printf (food5, price5)

food6 = "Total"
price6 = 0.63+price4

printf (food6, price6)


print("\n")

def printd (thing1, thing2):
    print("*{:<15}{:10.10}*".format(thing1, thing2))

thing1=input(print("What school do you go to?"))
thing2=input(print("What year are you going?"))

thing3=input(print("What is your first name?"))
thing4=input(print("What is your last name"))

thing5=input(print("Are you a student or a teacher?"))
thing6=input(print("What class are you in?"))

print("*"*27)

printd(thing1, thing2)
printd(thing3, thing4)
printd(thing5, thing6)
                
print("*"*27)








