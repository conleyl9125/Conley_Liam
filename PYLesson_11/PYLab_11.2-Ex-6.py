import random
class Item:
    #Constructor
    def __init__(self, price, category, manufa, UPC, name = ""):
        self.Name = name
        self.Manufa = manufa
        self.Price = price
        self.Category = category
        self.UPC = random.randint(100000000, 1000000000)

    #Modifier
    def setValues(self, price, category, manufa, UPC, name = ""):
        self.Name = name
        self.Manufa = manufa
        self.Price = price
        self.Category = category
        self.UPC = random.randint(100000000, 1000000000)
      
    #accessor
    def getPrice(self):
        return self.Price
    def getCategory(self):
        return self.Category
    def getManufacturer(self):
        return self.Manufa
    def getName(self):
        return self.Name
    def getUPC(self):
        return self.UPC
    def __str__(self):
        return "Customer Info...\nPrice: " + self.Price + \
                           "\nCategory: " + self.Category + \
                           "\nName: " + self.Name + \
                           "\nMaunfacturer: " + str(self.Manufa)

def main():
    manufa=input("What is the manufacturer?")
    name=input("What is the name?")
    yon=input("Will you be entering price and category information? (y/n)")
    
    if yon=="n":
        item1 = Item(category, manufa)
    else:
        price=input("What do you want the price to be?")
        category=input("What is the category?")
        item1 = Item(category, manufa, name, category, price)
    print(item1)
main()
