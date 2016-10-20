g1=input("what is your math letter grade?")
g2=input("what is your science letter grade?")
g3=input("what is your history letter grade?")
g4=input("what is your no hw elective letter grade?")
g5=input("what is your PE letter grade?")
g6=input("what is your english letter grade?")
g7=input("what is your language letter grade?")

def calcPoints(grade):
    if grade=="a":
        return 4.0
    if grade=="b":
        return 3.0
    if grade=="c":
        return 2.0
    if grade=="d":
        return 1.0
    else :
        return 0.0
def calcGPA():
    GPA= (
        calcPoints(g1) + calcPoints(g2)+calcPoints(g3)+calcPoints(g4)+calcPoints(g5)+calcPoints(g6)+calcPoints(g7))/7
    print("Your GPA is {:.2f}".format(GPA))
calcGPA()
