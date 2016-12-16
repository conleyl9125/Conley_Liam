import random
numbers=[]
output = ""
for i in range(1,10):
    numbers.append(random.randint(1,100))
    output+= str(numbers[i-1]) + " "
    


def average(numbers):
    average=0
    for i in numbers:
        average+= i
    average/=10
    return average

average(numbers)

print("numbers...")
print(output)
print("")
print("The average of the above numbers is..." , average(numbers) )
