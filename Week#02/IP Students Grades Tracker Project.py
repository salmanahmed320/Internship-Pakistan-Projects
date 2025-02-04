# INTERNSHIP PAKISTAN
# Week 2: Introdiction To Data Structures 
# Project_Task # Task#3: Students Grades Tracker
# Develop script to manage students grades, including adding grades, calculating averages, and detemining letter grades.

# Initialize an empty dictionary to store student grades
grades_tracker = {}
1
# Infinite loop to keep the grades tracker running
while True:
    # Display menu options
    print("\nStudent Grades Tracker Menu:")
    print("1. Add Student Grades")
    print("2. View Student Grades")
    print("3. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1/2/3): ")

    # Add grades for a student
    if choice == '1':
        student_name = input("Enter the student's name: ")

        # Taking grades as input from the user and converting them to a list of integers
        grades_input = input(f"Enter grades for {student_name} separated by spaces: ")
        grades_list = list(map(int, grades_input.split()))

        # Adding the student's grades to the dictionary
        grades_tracker[student_name] = grades_list
        print(f"Grades for {student_name} added successfully.")

    # View all student grades, averages, and letter grades
    elif choice == '2':
        if grades_tracker:
            print("\nStudent Grades:")
            for student, grades_list in grades_tracker.items():
                # Calculate the average grade
                average_grade = sum(grades_list) / len(grades_list)

                # Determine the letter grade
                if average_grade >= 90:
                    letter_grade = 'A'
                elif average_grade >= 80:
                    letter_grade = 'B'
                elif average_grade >= 70:
                    letter_grade = 'C'
                elif average_grade >= 60:
                    letter_grade = 'D'
                else:
                    letter_grade = 'F'

                print(f"{student}: Grades = {grades_list}, Average = {average_grade:.2f}, Letter Grade = {letter_grade}")
        else:
            print("No student grades available.")

    # Exit the program
    elif choice == '3':
        print("Exiting the student grades tracker. Goodbye!")
        break

    # Handle invalid input
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
