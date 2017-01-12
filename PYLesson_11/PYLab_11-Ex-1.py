class MilesPerHour:
    #Constructor
    def __init__(self, Xdistance, Xhours, Xminutes):
        self.distance=Xdistance
        self.hours=Xhours
        self.minutes=Xminutes
        mph=0

    #Modifier
    def setValues(self,Ydistance, Yhours, Yminutes):
        self.distance=Ydistance
        self.hours=Yhours
        self.minutes=Yminutes

    #Accessor
    def getDist():
        return distance
    def getHours():
        return hours
    def getMins():
        return minutes
    def getMPH():
        mph=distance / (hours + minutes / 60)
        return mph

def Main():
    distance
