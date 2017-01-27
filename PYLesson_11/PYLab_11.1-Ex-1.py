class Car:
#Constructor
    def __init__(self, p, i, e, t):
        self.paint=p
        self.interior=i
        self.engine=e
        self.tires=t

#Modifier
    def setValues(self, p, i, e, t):
        self.paint=p
        self.interior=i
        self.engine=e
        self.tires=t

#Accessor
    def getDist(self):
        return self.p
    def getHours(self):
        return self.i
    def getMins(self):
        return self.e
    def getMins(self):
        return self.t

def main():
    paint=input("What type of interior would you like?")
    interior=input("What interior would you like?")
    engine=input("What kind of engine would you like")
    tires=input("What kind of tires would you like")
    print("paint:", paint, "interior:", interior, "engine:", engine, "tires:", tires)

main()
