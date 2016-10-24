w=float(input("How much do you wiegh in pounds?"))
h=float(input("How tall are you in inches?"))
BMI=0

def calcBMI():
    global BMI

    BMI=703*(w/(h*h))
calcBMI()

def healthy():
    if BMI<18.5:
        print("You are underweight")
    if 25>BMI>18.5:
        print("You are normal")
    if 29.9>BMI>25:
        print("You are overweight")
    if 34.9>BMI>29.9:
        print("You are obese")
    if 39.9>BMI>35:
        print("You are very obese")
    if BMI>39.9:
        print("You are morbidly obese")
healthy()
print("Your BMI",BMI)

