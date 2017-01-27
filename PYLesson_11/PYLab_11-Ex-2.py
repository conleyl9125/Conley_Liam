import math
class Distance:
    #Constructor:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.xO = int(x1)
        self.yO = int(y1)
        self.xT = int(x2)
        self.yT = int(y2)
        distance = 0

    #modifier:
    def setValues(self, x1="", y1="", x2="", y2=""):
        self.xO = int(x1)
        self.yO = int(y1)
        self.xT = int(x2)
        self.yT = int(y2)
        distance = 0
        

    #Accessor:
    def getMPH(self):
        distance = math.sqrt((self.xT-self.xO)*(self.xT-self.xO)+(self.yT-self.yO)*(self.yO-self.yT));
        return distance
    
    #main:
def main():
    x1 = input("imput a value for x1")
    x2 = input("imput another value for x2")
    y1 = input("imput another value for y1")
    y2 = input("imput another value for y2")
    dist = Distance(x1, y1, x2, y2)
    print(dist.getMPH())
    
main()
