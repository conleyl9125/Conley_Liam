
item1=input("What was your first item?")
itemP1=float(input("How much did it cost?"))
item2=input("What was your second item?")
itemP2=float(input("How much did it cost?"))
item3=input("What was your third item?")
itemP3=float(input("How much did it cost?"))
item4=input("What was your fourth item?")
itemP4=float(input("How much did it cost?"))

def formatr(item, price):
    print("{:<10}\t{:12.2f}".format(item,price))

subTotal=itemP1+itemP2+itemP3+itemP4
discount=0.15
tax=0.8*subTotal
if subTotal>2000:
    global total
    total=subTotal*discount+tax
if subTotal<2000:
    global total
    total=subTotal+tax
print("<<<<<<<< Receipt >>>>>>>>")
formatr(item1,itemP1)
formatr(item2,itemP2)
formatr(item3,itemP3)
formatr(item4,itemP4)
formatr("Subtotal ", subTotal)
formatr("Total", total)
print("Thank you!")
