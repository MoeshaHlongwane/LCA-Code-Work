# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("What is your name? ")
# TODO: Ask the user for their age and store it in a variable
age = input("How old are you? ")
# TODO: Print a greeting using the name and age variables
print("Hello " + name + " " + age )
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("What is the length of the rectangle? "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("What is the width of the rectangle? "))
# TODO: Calculate the area of the rectangle
area = length * width 
# TODO: Print the result
print(f"The area of your rectangle is: {area}cm**2")
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temperature_in_C = float(input("What is the temperature in Celsius? "))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
temperature_in_F = round((temperature_in_C * 9/5) + 32, 2)
# TODO: Print the result rounded to two decimal places
print(f"Your temperature is: {temperature_in_F}F") 