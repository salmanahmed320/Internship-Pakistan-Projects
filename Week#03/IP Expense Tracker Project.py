# INTERNSHIP PAKISTAN
# WEEK 3 : File Handling And Basic Automation 
# Task #3 PROJECT TASK: EXPENSE TRACKER
# Build a script to track daily expenses, categorize them and generate a summary report.

import csv
from collections import defaultdict
# Initialize an empty dictionary to store expenses
expenses = defaultdict(lambda: defaultdict(float))
# Read expense data from CSV file
with open('sample expenses data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date = row['date']
        category = row['category']
        amount = float(row['amount'])
        expenses[date][category] += amount
# Generate and display the summary report
print("Expense Summary Report:")
for date, categories in expenses.items():
    print(f"\nDate: {date}")
    for category, total in categories.items():
        print(f"  {category}: ${total:.2f}")
