length=float(input("What is the length of the box?"))
width=float(input("What is the width of the box?"))
height=float(input("What is the height of the box?"))

def volCalc():
    global volumeCi
    volumeCi=(length*width*height)
volCalc()
def convert():
    global volumeCf
    volumeCf=volumeCi*0.000578704
convert()
print("The volume of your subwoofer is",volumeCf,"in cubic feet")

