# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["Apple", "pear", "Orange", "Strawberry"]
# TODO: Add a fruit to the end of the list
fruits.append("Tomato")

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "Kiwi")

# TODO: Remove a fruit from the list
fruits.remove("pear")

# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
list_of_numbers = [1,2,3,4,5]

# TODO: Create a new list with each number squared
# attempt 1, however it didnt return the square numbers as a list.
# for new_list in list_of_numbers: 
#     results = int(new_list **2)
#     print (results)

def square(num):
    return [num ** 2 for num in list_of_numbers]
print(square(list_of_numbers))

# TODO: Find the sum and average of the original numbers
# TODO: Print the results

sum_of_numbers = sum(list_of_numbers) #Using the sum function to get the sum of the list 
print(sum_of_numbers)
avg_of_numbers = sum_of_numbers/len(list_of_numbers) # Use the len() function to get return or get the number of element inside the list. 
print(avg_of_numbers)  

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_and_states = {"Botswana": "Gaborone", "Uganda": "Kampala",
                         "Zimbabwe": "Harare", "Zimbabwe": "Harare"
                         }
# TODO: Add a new country-capital pair
countries_and_states["China"] = "Beijing"

# TODO: Update the capital of an existing country
countries_and_states ["Zimbabwe"] ="HARARE"

# TODO: Remove a country-capital pair
del countries_and_states["China"] #Used the delete function

# TODO: Print the modified dictionary
print(countries_and_states)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruits_dic = {"Apple": "Gold", "Banana": "Yellow", "Peach": "Red", "Kiwi": "Green"}
# TODO: Print all the fruits (keys)
for fruit in fruits_dic:
    print (fruit)
# TODO: Print all the colors (values)
for fruit in fruits_dic:
    print(fruits_dic[fruit])

# TODO: Print each fruit and its color
for fruit in fruits_dic:
    print(fruit + " " + fruits_dic[fruit])

# TODO: Check if a fruit is in the dictionary and print its color
User_selection = input("Please guess my favorite fruit in the dictionary! ")
if fruit in fruits_dic:
    print(fruits_dic[fruit])
else:
    print("Fruit is not in the dictionary. ")
