import random
class User:
   def __init__(self, fName, lName, avat = ""):
       self.firstName = fName
       self.lastName = lName
       self.avatar = avat
       self.userID = random.randint(0, 1000000)

    #modifier
   def setAvatar(self, avat):
      self.avatar = avat
      return avat
      
    #accessor
   def getAvatar(self):
      return self.avatar
   
   def getfName(self):
      return self.firstName
   def getlName(self):
      return self.lastName
   def getID(self):
        return self.userID
   def __str__(self):
      return "Customer Info...\nFirst Name: " + self.firstName + \
                           "\nLast Name: " + self.lastName + \
                           "\nAvatar: " + self.avatar + \
                           "\nUser ID#: " + str(self.userID)
   
def main():
   fName=input("What is you first name?")
   lName=input("What is your last name?")
   yon=input("Whould you like to use a public avatar? (yes/no)?")
      
   if yon=="no":
      user1 = User(fName, lName)
   else:
      avat=input("What is your avatar name?")
      user1 = User(fName, lName, avat)
         
   print(user1)
main()
