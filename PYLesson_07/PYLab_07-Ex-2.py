number = int(input("Please enter a number"))
average = 0
digits = 0
def avDigits():
    global digits, average, number
    num = number
    while num > 0:
        digits += 1
        average += (num % 10)
        num = int(num/10)
    average = average/digits
avDigits()

print("The average of the digits in", number ,"is",average)
