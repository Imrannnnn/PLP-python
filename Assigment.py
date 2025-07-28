"""
Create a simple Python program that asks the user to input two numbers and a mathematical 
operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15. """

num1 = input("Enter your first Number: ")
num2 = input("Enter your second Number: ")
Symbol = input("enter your Symbol '+, -, /, *': ")

if Symbol == '+':
    result = int(num1) + int(num2)
elif Symbol == '-':
    result  = int(num1) - int(num2)
elif Symbol == '*':
    result = int(num1) * int(num2)
elif Symbol == '/':
    result = int(num1) / int(num2)
else: 
    result = "Invalid Operation"

print(f"{int(num1)} {Symbol} {int(num2)} = {int(result)}")