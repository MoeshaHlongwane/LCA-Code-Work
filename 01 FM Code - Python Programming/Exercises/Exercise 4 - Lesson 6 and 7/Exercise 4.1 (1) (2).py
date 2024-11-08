#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.
# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.


def check_attendance(list_of_names , list_of_absentees):
    absent_students = [name for name in list_of_names if name in list_of_absentees]
    return absent_students

results = check_attendance(["Alice", "Bob", "Charlie", "David"], ["Bob", "David"] )
print(results)
  
#------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.
# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.


def calculate_average_grade(average_dic):   
#You can access the key and value inside the dictionary by using the .key() function and .value()f function.
    sum_of_grades = int(sum(average_dic.values())) #Calculating the sum of the grade
    number_students = len(average_dic.values()) #Calculating the average by using the len() function. 
    return sum_of_grades/number_students
    
results= (calculate_average_grade({"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}))
print(f"Average grade", results)
  
#------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.
from math_operations import add, multiply
def operation_selector(operation):
    
    # Return the appropriate function based on the operation
    if operation == "add":
        return add
    elif operation == "multiply":
        return multiply
    else:
        raise ValueError("Invalid operation. Please use 'add' or 'multiply'.")

# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
add_function = operation_selector("add")
print("Addition:", add_function(4, 6))  

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.
multiply_function = operation_selector("multiply")
print("Multiplication:", multiply_function(3, 7)) 

#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)

# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}

# TODO: Use a for loop to print each item and its quantity in stock.

for items in grocery_inventory:
    print(items + " - " + str(grocery_inventory[items]))
# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).
sum_of_items = sum(grocery_inventory.values())
print(f"You have", sum_of_items, "items in stock. ")

#------------------------------------------------------------------------------------
# Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# TODO: Ask the user to input their PIN.
# TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
# TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".
# TODO: Use a while loop to implement the retry system.

def pin():
    correct_pin = "1234"
    attempts = 3
    while attempts > 0:  
        user_pin = input("Please enter your pin. ")

        if user_pin == correct_pin:
                print ("Access Granted. ")   
                break         
        else:
            attempts -=1
            if attempts > 0:
             print(f"You have {attempts} attempts left, please enter correct pin")
            else:
                 print("Access Denied. You have exhausted all attempts.")
pin()                  


#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System

# TODO: Create a list with 10 random assignment scores (between 0 and 100).
# TODO: Use a for loop to calculate the total score.
# TODO: Calculate and print the average score for the class.
# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.

import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]

# TODO: Calculate total and average scores.
# Ask the user to input the total loan amount.
loan_amount = float(input("Enter the total loan amount: "))

# Ask the user to input their monthly repayment amount.
monthly_payment = float(input("Enter your monthly payment amount: "))

# Use a while loop to simulate the repayment process.
while loan_amount > 0:
    # Subtract the monthly payment from the loan amount.
    loan_amount -= monthly_payment

    # Check if the loan amount is less than 0 to avoid negative values.
    if loan_amount < 0:
        loan_amount = 0

    # Print the remaining loan amount.
    print(f"Remaining loan amount: R{loan_amount:.2f}")

# When the loan is fully paid off, print a congratulatory message.
print("Congratulations! Your loan is fully paid off.")



#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)

# TODO: Create a list with the names of 20 participants.
# TODO: Use the random module to select 5 random participants.
# TODO: Print the names of the selected team members.
import random

# List of participants.
participants = ["Person1", "Person2", "Person3","Person4", "Person5", 
                "Person6", "Person7", "Person8", "Person9", "Person10",
                "Person11", "Person12", "Person13", "Person14", "Person15",
                "Person16", "Person17", "Person18", "Person19" , "Person20"]

# TODO: Randomly select 5 people from the participants list.
random_people = random.sample(participants, 5)
print("Selected team members:", random_people)


#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""

# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.
# TODO: Ask the user to input the distance they walked, ran, and cycled today.
# Import the custom 'fitness_tracker' module.
import fitness_tracker

# Ask the user to input the distance they walked, ran, and cycled today.
distance_walked = float(input("Enter the distance you walked today (in km): "))
distance_ran = float(input("Enter the distance you ran today (in km): "))
distance_cycled = float(input("Enter the distance you cycled today (in km): "))

# Calculate and print the total calories burned for each activity.
calories_walked = fitness_tracker.walk_calories(distance_walked)
calories_ran = fitness_tracker.run_calories(distance_ran)
calories_cycled = fitness_tracker.cycle_calories(distance_cycled)

print(f"Calories burned from walking: {calories_walked} kcal")
print(f"Calories burned from running: {calories_ran} kcal")
print(f"Calories burned from cycling: {calories_cycled} kcal")

# Sum and print the total calories burned for the day.
total_calories = calories_walked + calories_ran + calories_cycled

#TODO: Sum and print the total calories burned for the day.
# fitness_tracker.py
print(f"Total calories burned today: {total_calories} kcal")

#------------------------------------------------------------------------------------
# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# TODO: Ask the user to input the total loan amount.
# TODO: Ask the user to input their monthly repayment amount.
# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
# TODO: Print the remaining loan amount after each payment.
# TODO: When the loan is fully paid off, print a congratulatory message.

loan_amount = float(input("Enter the total loan amount: "))
monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate the repayment process.

# Ask the user to input their monthly repayment amount.
monthly_payment = float(input("Enter your monthly payment amount: "))

# Use a while loop to simulate the repayment process.
while loan_amount > 0:
    # Subtract the monthly payment from the loan amount.
    loan_amount -= monthly_payment

    # Check if the loan amount is less than 0 to avoid negative values.
    if loan_amount < 0:
        loan_amount = 0

    # Print the remaining loan amount.
    print(f"Remaining loan amount: R{loan_amount:.2f}")

# When the loan is fully paid off, print a congratulatory message.
print("Congratulations! Your loan is fully paid off.")
