# simple calculator v1.0

# 1- input first number 
firstNumber = int(input("Enter the first number: "))

# 2- input operation type
operationType = input('Enter the operator do you want: ')

# 3- input second number 
secondNumber = int(input("Enter the second number: "))

# 4- print the result
if operationType == "+": 
     print ("The result =",firstNumber + secondNumber)
elif operationType == "-":
     print ("The result =", firstNumber - secondNumber)
elif operationType == "*":
     print ("The result =", firstNumber * secondNumber)
elif operationType == "/":
     print ("The result =", firstNumber / secondNumber)
else:
     print("the operator you entered not valid")

     
     
