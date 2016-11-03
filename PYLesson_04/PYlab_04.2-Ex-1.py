l=float(input("What is the length in feet?"))

w=float(input("What is the width in feet?"))

def calcPerim(le,wi):
    return((le+wi)*2)

print("Your rectangle is", calcPerim(l,w) ,"ft around.")
