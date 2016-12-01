number=int(input("Please enter a number"))

def sumDigits(num):
    summ = 0
    while num > 0:
        summ += num%10
        num= int(num/10)
    return summ
        
print("The sum of the digits in ", number , "is" , sumDigits(number))
