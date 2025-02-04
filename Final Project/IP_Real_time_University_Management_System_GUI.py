# INTERNSHIP PAKISTAN
# FINAL_PROJECT 
# ***************************** Real-Time University Management System (UMS) GUI Based ************************************************
# Version v1.1
# GUI Based

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('university_management_system.db')
c = conn.cursor()

# Create tables
def create_tables():
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    address TEXT,
                    grade TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    credits INTEGER
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS faculty (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    subject TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    course_id INTEGER,
                    status TEXT,
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (course_id) REFERENCES courses(id)
                )''')

    conn.commit()

# Insert sample data
def insert_sample_data():
    sample_students = [
        ('John Doe', '123 Street', 'A'),
        ('Jane Smith', '456 Avenue', 'B'),
        ('David Johnson', '789 Road', 'A'),
        ('Sarah Miller', '101 Highway', 'C'),
        ('Michael Brown', '102 Blvd', 'B'),
        ('Emma White', '103 St', 'A'),
        ('James Davis', '104 St', 'C'),
        ('Olivia Wilson', '105 St', 'B')
    ]

    sample_courses = [
        ('Mathematics', 3),
        ('Physics', 4),
        ('Chemistry', 4),
        ('English', 2),
        ('History', 3),
        ('Computer Science', 4),
        ('Biology', 4),
        ('Economics', 3)
    ]

    sample_faculty = [
        ('Dr. Smith', 'Mathematics'),
        ('Dr. Johnson', 'Physics'),
        ('Dr. Miller', 'Chemistry'),
        ('Dr. Brown', 'English'),
        ('Dr. White', 'History'),
        ('Dr. Davis', 'Computer Science'),
        ('Dr. Wilson', 'Biology'),
        ('Dr. Taylor', 'Economics')
    ]

    sample_attendance = [
        (1, 1, 'Present'),
        (2, 1, 'Absent'),
        (3, 2, 'Present'),
        (4, 2, 'Absent'),
        (5, 3, 'Present'),
        (6, 3, 'Absent'),
        (7, 4, 'Present'),
        (8, 4, 'Absent')
    ]

    c.executemany("INSERT INTO students (name, address, grade) VALUES (?, ?, ?)", sample_students)
    c.executemany("INSERT INTO courses (name, credits) VALUES (?, ?)", sample_courses)
    c.executemany("INSERT INTO faculty (name, subject) VALUES (?, ?)", sample_faculty)
    c.executemany("INSERT INTO attendance (student_id, course_id, status) VALUES (?, ?, ?)", sample_attendance)

    conn.commit()

# GUI Code
def add_student():
    name = student_name_entry.get()
    address = student_address_entry.get()
    grade = student_grade_entry.get()

    if name and address and grade:
        c.execute("INSERT INTO students (name, address, grade) VALUES (?, ?, ?)", (name, address, grade))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully")
    else:
        messagebox.showerror("Error", "All fields are required")

def view_students():
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    display_data(students, "Students")

def add_course():
    name = course_name_entry.get()
    credits = course_credits_entry.get()

    if name and credits:
        c.execute("INSERT INTO courses (name, credits) VALUES (?, ?)", (name, credits))
        conn.commit()
        messagebox.showinfo("Success", "Course added successfully")
    else:
        messagebox.showerror("Error", "All fields are required")

def view_courses():
    c.execute("SELECT * FROM courses")
    courses = c.fetchall()
    display_data(courses, "Courses")

def add_faculty():
    name = faculty_name_entry.get()
    subject = faculty_subject_entry.get()

    if name and subject:
        c.execute("INSERT INTO faculty (name, subject) VALUES (?, ?)", (name, subject))
        conn.commit()
        messagebox.showinfo("Success", "Faculty added successfully")
    else:
        messagebox.showerror("Error", "All fields are required")

def view_faculty():
    c.execute("SELECT * FROM faculty")
    faculty = c.fetchall()
    display_data(faculty, "Faculty")

def add_attendance():
    student_id = attendance_student_id_entry.get()
    course_id = attendance_course_id_entry.get()
    status = attendance_status_entry.get()

    if student_id and course_id and status:
        c.execute("INSERT INTO attendance (student_id, course_id, status) VALUES (?, ?, ?)", (student_id, course_id, status))
        conn.commit()
        messagebox.showinfo("Success", "Attendance added successfully")
    else:
        messagebox.showerror("Error", "All fields are required")

def view_attendance():
    c.execute("SELECT * FROM attendance")
    attendance = c.fetchall()
    display_data(attendance, "Attendance")

def display_data(data, title):
    top = tk.Toplevel()
    top.title(title)

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            tk.Label(top, text=str(value), borderwidth=1).grid(row=i, column=j)

# GUI Setup
root = tk.Tk()
root.title("University Management System")
root.geometry("700x600")  # Set the window size to be larger

# Student Management Section
tk.Label(root, text="Student Name:").grid(row=0, column=0)
student_name_entry = tk.Entry(root)
student_name_entry.grid(row=0, column=1)

tk.Label(root, text="Address:").grid(row=1, column=0)
student_address_entry = tk.Entry(root)
student_address_entry.grid(row=1, column=1)

tk.Label(root, text="Grade:").grid(row=2, column=0)
student_grade_entry = tk.Entry(root)
student_grade_entry.grid(row=2, column=1)

tk.Button(root, text="Add Student", command=add_student).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="View Students", command=view_students).grid(row=4, column=0, columnspan=2)

# Course Management Section
tk.Label(root, text="Course Name:").grid(row=5, column=0)
course_name_entry = tk.Entry(root)
course_name_entry.grid(row=5, column=1)

tk.Label(root, text="Credits:").grid(row=6, column=0)
course_credits_entry = tk.Entry(root)
course_credits_entry.grid(row=6, column=1)

tk.Button(root, text="Add Course", command=add_course).grid(row=7, column=0, columnspan=2)
tk.Button(root, text="View Courses", command=view_courses).grid(row=8, column=0, columnspan=2)

# Faculty Management Section
tk.Label(root, text="Faculty Name:").grid(row=9, column=0)
faculty_name_entry = tk.Entry(root)
faculty_name_entry.grid(row=9, column=1)

tk.Label(root, text="Subject:").grid(row=10, column=0)
faculty_subject_entry = tk.Entry(root)
faculty_subject_entry.grid(row=10, column=1)

tk.Button(root, text="Add Faculty", command=add_faculty).grid(row=11, column=0, columnspan=2)
tk.Button(root, text="View Faculty", command=view_faculty).grid(row=12, column=0, columnspan=2)

# Attendance Management Section
tk.Label(root, text="Student ID:").grid(row=13, column=0)
attendance_student_id_entry = tk.Entry(root)
attendance_student_id_entry.grid(row=13, column=1)

tk.Label(root, text="Course ID:").grid(row=14, column=0)
attendance_course_id_entry = tk.Entry(root)
attendance_course_id_entry.grid(row=14, column=1)

tk.Label(root, text="Status:").grid(row=15, column=0)
attendance_status_entry = tk.Entry(root)
attendance_status_entry.grid(row=15, column=1)

tk.Button(root, text="Add Attendance", command=add_attendance).grid(row=16, column=0, columnspan=2)
tk.Button(root, text="View Attendance", command=view_attendance).grid(row=17, column=0, columnspan=2)

# Initialize database and insert sample data
create_tables()
insert_sample_data()

root.mainloop()

# Close the connection when the program ends
conn.close()

