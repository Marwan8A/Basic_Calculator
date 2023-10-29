import math

num1 = input("Enter a number: ")
operation = input("Enter an operation: ")
num2 = input("Enter another number: ")
pi = math.pi
sqrt = math.sqrt

if operation == "+" and num1.isnumeric() == True and num2.isnumeric() == True:
    result = float(num1) + float(num2)
elif operation == "-" and num1.isnumeric() == True and num2.isnumeric() == True:
    result = float(num1) - float(num2)
elif operation == "x" or operation == "*" and num1.isnumeric() == True and num2.isnumeric() == True:
    result = float(num1) * float(num2)
elif operation == "/" and num1.isnumeric() == True and num2.isnumeric() == True:
    result = float(num1) / float(num2)
elif operation == "^" or operation == "**" and num1.isnumeric() == True and num2.isnumeric() == True:
    result = float(num1) ** float(num2)


print(str(num1) + " " + str(operation) + " " + str(num2) + " = " + str(int(result)))


