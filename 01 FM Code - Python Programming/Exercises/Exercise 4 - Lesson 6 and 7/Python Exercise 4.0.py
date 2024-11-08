# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["Apple", "Pear", "Orange", "Banana"]
# TODO: Use a for loop to print each fruit in the list
for fruit in fruits: 
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
countdown = 6
while countdown > 1:
    countdown -= 1
    print (countdown)

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for square_numbers in range(0, 11):
    print(square_numbers * square_numbers)
    
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colours = ["Blue", "Purple","Yellow", "Red"]
# TODO: Use a for loop to select and print 3 random colors from the list
for random_colours in colours: 
    random_colours = random.choice(colours)
    print (random_colours)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
from math_operations import add, subtract, multiply, divide

results = subtract(3, 5)
results_2 = add(2,8)
results_3 = multiply(2,9)
results_4 = divide(3,0)
print(results)
print(results_2)
print(results_3)
print(results_4)

# TODO: Use a while loop to create a simple calculator
from math_operations import add, subtract, multiply, divide

def calculator():
    print("Simple Calculator")
    print("Type 'exit' to quit.")
    
    while True:
        # Get the operation from the user
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop
        
        if operation == "+":
            result = add(num1, num2)
            print(f"Result: {result}\n")
        
        elif operation == "-":
            result = subtract(num1, num2)
            print(f"Result: {result}\n")
        
        elif operation == "*":
            result = multiply(num1, num2)
            print(f"Result: {result}\n")
        
        elif operation == "/":

            result =divide(num1, num2)
            print(f"Result: {result}\n")
        
        else:
            print("Invalid operation. Please enter one of +, -, *, /.\n")

calculator()

