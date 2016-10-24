r=float(input("What is the radius of your circle?"))
area = 0
def circle():
    global r, area
    area = 3.14*r*r
    
circle()
print(area)
