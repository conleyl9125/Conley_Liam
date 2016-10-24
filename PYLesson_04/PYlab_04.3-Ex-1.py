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
