# INTERNSHIP PAKISTAN
# FINAL_PROJECT 
# ******************************* Real-Time University Management System (UMS) ************************************************
# Version v1.0
# Console Based

import sqlite3
from datetime import datetime

# Create the database and tables
def create_database():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    # Create Students table
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 address TEXT,
                 course_id INTEGER
                 )''')

    # Create Courses table
    c.execute('''CREATE TABLE IF NOT EXISTS courses (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 course_name TEXT,
                 credits INTEGER
                 )''')

    # Create Faculty table
    c.execute('''CREATE TABLE IF NOT EXISTS faculty (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 subject TEXT
                 )''')

    # Create Grades table
    c.execute('''CREATE TABLE IF NOT EXISTS grades (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 student_id INTEGER,
                 course_id INTEGER,
                 grade TEXT,
                 FOREIGN KEY (student_id) REFERENCES students (id),
                 FOREIGN KEY (course_id) REFERENCES courses (id)
                 )''')

    # Create Attendance table
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 student_id INTEGER,
                 course_id INTEGER,
                 date TEXT,
                 status TEXT,
                 FOREIGN KEY (student_id) REFERENCES students (id),
                 FOREIGN KEY (course_id) REFERENCES courses (id)
                 )''')

    conn.commit()
    conn.close()


# Sample data for testing
def insert_sample_data():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    # Insert sample courses
    c.execute("INSERT INTO courses (course_name, credits) VALUES ('Mathematics', 3)")
    c.execute("INSERT INTO courses (course_name, credits) VALUES ('Physics', 4)")
    c.execute("INSERT INTO courses (course_name, credits) VALUES ('Computer Science', 3)")

    # Insert sample students
    c.execute("INSERT INTO students (name, address, course_id) VALUES ('John Doe', '123 Main St', 1)")
    c.execute("INSERT INTO students (name, address, course_id) VALUES ('Jane Smith', '456 Elm St', 2)")

    # Insert sample faculty
    c.execute("INSERT INTO faculty (name, subject) VALUES ('Dr. Alice', 'Mathematics')")
    c.execute("INSERT INTO faculty (name, subject) VALUES ('Dr. Bob', 'Physics')")

    conn.commit()
    conn.close()

# Function to add a student
def add_student():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    name = input("Enter student name: ")
    address = input("Enter student address: ")
    course_id = int(input("Enter course ID for enrollment: "))

    c.execute("INSERT INTO students (name, address, course_id) VALUES (?, ?, ?)", (name, address, course_id))

    conn.commit()
    conn.close()
    print("Student added successfully.")

# Function to update student information
def update_student():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    student_id = int(input("Enter student ID to update: "))
    new_address = input("Enter new address: ")
    new_course_id = int(input("Enter new course ID: "))

    c.execute("UPDATE students SET address = ?, course_id = ? WHERE id = ?", (new_address, new_course_id, student_id))

    conn.commit()
    conn.close()
    print("Student updated successfully.")

# Function to view all students
def view_students():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    c.execute("SELECT * FROM students")
    students = c.fetchall()

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Course ID: {student[3]}")

    conn.close()

# Function to add a course
def add_course():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    course_name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))

    c.execute("INSERT INTO courses (course_name, credits) VALUES (?, ?)", (course_name, credits))

    conn.commit()
    conn.close()
    print("Course added successfully.")

# Function to update course information
def update_course():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    course_id = int(input("Enter course ID to update: "))
    new_course_name = input("Enter new course name: ")
    new_credits = int(input("Enter new course credits: "))

    c.execute("UPDATE courses SET course_name = ?, credits = ? WHERE id = ?", (new_course_name, new_credits, course_id))

    conn.commit()
    conn.close()
    print("Course updated successfully.")

# Function to view all courses
def view_courses():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    c.execute("SELECT * FROM courses")
    courses = c.fetchall()

    for course in courses:
        print(f"ID: {course[0]}, Course Name: {course[1]}, Credits: {course[2]}")

    conn.close()

# Function to add a faculty member
def add_faculty():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    name = input("Enter faculty name: ")
    subject = input("Enter teaching subject: ")

    c.execute("INSERT INTO faculty (name, subject) VALUES (?, ?)", (name, subject))

    conn.commit()
    conn.close()
    print("Faculty member added successfully.")

# Function to view all faculty members
def view_faculty():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    c.execute("SELECT * FROM faculty")
    faculty = c.fetchall()

    for member in faculty:
        print(f"ID: {member[0]}, Name: {member[1]}, Subject: {member[2]}")

    conn.close()

# Function to record exam grades
def record_grade():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter Course ID: "))
    grade = input("Enter grade: ")

    c.execute("INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)", (student_id, course_id, grade))

    conn.commit()
    conn.close()
    print("Grade recorded successfully.")

# Function to view exam grades
def view_grades():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    student_id = int(input("Enter Student ID to view grades: "))

    c.execute("SELECT * FROM grades WHERE student_id = ?", (student_id,))
    grades = c.fetchall()

    if grades:
        for grade in grades:
            print(f"Course ID: {grade[2]}, Grade: {grade[3]}")
    else:
        print("No grades found for this student.")

    conn.close()

# Function to add attendance record
def add_attendance():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter Course ID: "))
    date = input("Enter date (YYYY-MM-DD): ")
    status = input("Enter attendance status (Present/Absent): ")

    c.execute("INSERT INTO attendance (student_id, course_id, date, status) VALUES (?, ?, ?, ?)", 
              (student_id, course_id, date, status))

    conn.commit()
    conn.close()
    print("Attendance added successfully.")

# Function to view attendance records
def view_attendance():
    conn = sqlite3.connect('university.db')
    c = conn.cursor()

    choice = input("View attendance by (1) Student ID or (2) Course ID? ")

    if choice == '1':
        student_id = int(input("Enter Student ID: "))
        c.execute("SELECT * FROM attendance WHERE student_id = ?", (student_id,))
        records = c.fetchall()

        if records:
            print(f"Attendance records for Student ID {student_id}:")
            for record in records:
                print(f"Date: {record[3]}, Status: {record[4]}")
        else:
            print("No attendance records found for this student.")

    elif choice == '2':
        course_id = int(input("Enter Course ID: "))
        c.execute("SELECT * FROM attendance WHERE course_id = ?", (course_id,))
        records = c.fetchall()

        if records:
            print(f"Attendance records for Course ID {course_id}:")
            for record in records:
                print(f"Student ID: {record[1]}, Date: {record[3]}, Status: {record[4]}")
        else:
            print("No attendance records found for this course.")

    else:
        print("Invalid choice.")

    conn.close()

# Main menu
def main():
    create_database()
    insert_sample_data()

    while True:
        print("\n=== University Management System ===")
        print("1. Add Student")
        print("2. Update Student")
        print("3. View Students")
        print("4. Add Course")
        print("5. Update Course")
        print("6. View Courses")
        print("7. Add Faculty")
        print("8. View Faculty")
        print("9. Record Exam Grade")
        print("10. View Exam Grades")
        print("11. Add Attendance")        # New option
        print("12. View Attendance")       # New option
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            view_students()
        elif choice == '4':
            add_course()
        elif choice == '5':
            update_course()
        elif choice == '6':
            view_courses()
        elif choice == '7':
            add_faculty()
        elif choice == '8':
            view_faculty()
        elif choice == '9':
            record_grade()
        elif choice == '10':
            view_grades()
        elif choice == '11':
            add_attendance()
        elif choice == '12':
            view_attendance()
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
