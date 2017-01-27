import random
class User:
    #Constructor
    def __init__(self, price, category, manufacturer, name = ""):
        self.Price = price
        self.UPC = random.randint(100000000, 1000000000)
      
    #accessor
    def getPrice(self):
        return self.price
    def getCategory(self):
        return self.category
    def getManufacturer(self):
        return self.lName
    def getName(self):
        return self.userID
    def __str__(self):
        return "Customer Info...\nPrice: " + self.price + \
                           "\nCategory: " + self.category + \
                           "\nName: " + self.name + \
                           "\nMaunfacturer: " + str(self.maunfacturer)

def main():
    maufacturer=input("What is the manufacturer?")
    name=input("What is the name?")

    
main()
