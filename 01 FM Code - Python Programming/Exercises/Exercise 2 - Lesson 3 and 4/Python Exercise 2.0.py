# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 0
x += 3
# TODO: Multiply y by 2 using the *= operator
y = 1
y *= 2 
# TODO: Divide x by y and store the result in a variable called 'result'
results = x / y
# TODO: Print the value of 'result'
print(results)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = int(input("What is your number for a? ")) 
b = int(input("What is your number for b? "))
if a > b: 
    print("True")
else:
    print("False")

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)

if b % 2 == 0: 
            print("Even")
else:
       print("Odd")
      
# TODO: Create a condition that checks if c is less than or equal to a
c = int(input("What is the number for c? "))
if c <= a:
       print("True")
else:
       print("False")
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

final_condition = True
if a > b or b % 2 == 0 and c <= a:
       print(final_condition)
else:
       print("False")
# TODO: Print the value of 'final_condition'

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("Enter score between 1 until 100 "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score in range(90, 101):
       print("A")
elif score in range(80, 90):
       print("B")
elif score in range(70, 80):
       print("C")
elif score in range(60, 70):
       print("D")
elif score in range(0, 60):
       print("Sorry you failed, F")
else:
       print("invalid, enter score between 0 - 100")      
# TODO: Print the grade for the given score
print(f"score:", {score})
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Please input number 1. "))
num2 = float(input("Please input number 2. "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Please input an operation (+, -, *, /) ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2

if operation == "+": 
       results = num1 + num2
elif operation == "-":
       results = num1 + num2
elif operation == "*":
       results = num1 * num2
elif operation == "/" and num2 == 0:
       print("invalid")
elif operation == "/":
       results = num1/num2 

# TODO: Handle the case of division by zero
     
#TODO: Print the result of the operation
print(results)