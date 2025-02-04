# INTERNSHIP PAKISTAN
# Week 2: Introdiction To Data Structures 
# Task#1: List Manipulation
# Objective: write/build a script in pyhton that takes a list of numbers.....

# Taking a list of numbers as input from the user
numbers = input("Enter a list of numbers separated by spaces: ")

# Converting the input string into a list of integers
numbers_list = list(map(int, numbers.split()))

# Display the original list
print("Original list:", numbers_list)

# Sorting the list
sorted_numbers = sorted(numbers_list)
print("Sorted list:", sorted_numbers)

# Finding the largest number
largest_number = max(numbers_list)
print("Largest number:", largest_number)

# Finding the smallest number
smallest_number = min(numbers_list)
print("Smallest number:", smallest_number)

# Calculating the sum of all numbers
total_sum = sum(numbers_list)
print("Sum of all numbers:", total_sum)
