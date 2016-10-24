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
