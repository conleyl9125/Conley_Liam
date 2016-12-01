nu = int(input("Please enter a number"))
average = 0
digits = 0
def avDigits(number):
    global digits, average
    num = number
    while num > 0:
        digits += 1
        average += digits % 10
        num = int(num/10)
    average /= 10
avDigits(nu)
print("The average of the digits in", nu ,"is",average )
