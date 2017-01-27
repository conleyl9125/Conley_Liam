class MilesPerHour:
#Constructor
    def __init__(self, distance = 0, hours = 0, minutes = 0):
        self.distance=distance
        self.hours=hours
        self.minutes=minutes
        mph=0

#Modifier
    def setValues(self,distance, hours, minutes):
        self.distance=distance
        self.hours=hours
        self.minutes=minutes

#Accessor
    def getDist(self):
        return self.distance
    def getHours(self):
        return self.hours
    def getMins(self):
        return self.minutes
    def getMPH(self):
        self.mph=self.distance / (self.hours + self.minutes / 60)
        return self.mph

    def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + \
                           "\nLast Name: " + self.lastName + \
                           "\nAvatar: " + self.avatar + \
                           "\nUser ID#: " + str(self.userID)

def main():
    distance=float(input("Distance?"))
    hours=float(input("Hours?"))
    minutes=float(input("Minutes"))
    mlph = MilesPerHour(distance,hours,minutes)
    print(user1.__str__())

main()
