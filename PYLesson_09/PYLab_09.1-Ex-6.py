math=(input("please give a math equation"))
equation = math.split()
output= ""
print(output)
for i in range(0,len(equation),1):
    output += equation[i]
i = 0
while i < len(equation):
    if i < len(equation) and (equation[i]=="*" or equation[i] == "/"):
        if equation[i] == "*":
            equation[i] = int(equation[i-1])* int(equation[i+1])
            equation.pop(i+1)
            equation.pop(i-1)
        elif equation[i] == "/":
            equation[i] = int(equation[i-1]) / int(equation[i+1])
            equation.pop(i+1)
            equation.pop(i-1)
    i+=1
i=0
while i<(len(equation)-1):
    if i<(len(equation)-1) and (equation[i]== "+" or equation[i] == "-"):
        if equation[i]=="+":
            equation[i] = int(equation[i-1]) + int(equation[i+1])
        elif equation[i] == "-":
            equation[i] = int(equation[i-1])+ int(equation[i+1])
        equation.pop(i+1)
        equation.pop(i-1)
    i+=1
print(equation)

