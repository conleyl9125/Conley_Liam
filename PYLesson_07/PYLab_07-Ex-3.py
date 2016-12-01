number=int(input("Please enter a multiple digit number"))
num = number
rev=0
def getReverse():
    global num, rev
    while num > 0:
        rev *= 10
        rev += num % 10
        num = (int(num / 10))
getReverse()
print(number, "reversed is", rev)
