def printf (food, price):
    print("*{:<16}   {:10.2f}".format(food, price))

food1 =input(print("What did you order first"))
price1 =float(input(print("How much did it cost?")))

food2 =input(print("What did you order next?"))
price2 =float(input(print("How much did it cost?")))
                  
food3 =input(print("What did you order last?"))
price3 =float(input(print("How much did it cost?")))


printf(food1, price1)
printf(food2, price2)
printf(food3, price3)

print("\n")

food4 = "Subtotal"
price4 = price1+price2+price3

printf (food4, price4)


food5 = "Tax"
price5 = 0.63

printf (food5, price5)

food6 = "Total"
price6 = 0.63+price4

printf (food6, price6)
