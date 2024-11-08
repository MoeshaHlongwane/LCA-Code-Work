squared_numbers = [num ** 2 for num in list_of_numbers]
print("Squared Numbers:", squared_numbers)

def square(numbers):
    return [num ** 2 for num in numbers]

squared_numbers = square(list_of_numbers)
print("Squared Numbers:", squared_numbers)

sum_of_numbers = sum(list_of_numbers)
average_of_numbers = sum_of_numbers / len(list_of_numbers)

print("Sum:", sum_of_numbers)
print("Average:", average_of_numbers)

# List of numbers from 1 to 5
list_of_numbers = [1, 2, 3, 4, 5]

# Create a new list with each number squared
squared_numbers = [num ** 2 for num in list_of_numbers]
print("Squared Numbers:", squared_numbers)

# Find the sum and average of the original numbers
sum_of_numbers = sum(list_of_numbers)
average_of_numbers = sum_of_numbers / len(list_of_numbers)

# Print the results
print("Sum:", sum_of_numbers)
print("Average:", average_of_numbers)
