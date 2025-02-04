# INTERNSHIP PAKISTAN
# WEEK#04 : Quiz Application Development 
# Objective: Develop a Quiz Application in python that allows users to take quizzes with multiple choice questions. The application will include score tracking, question categorization, and a timer for each quiz.

# *************************************** QUIZ APPLICATION 2 ********************************************************
# Build this application a web-based GUI Quiz Application gpt 
# updated version of the Quiz Application
# Version v2.0
# GUI Based

import tkinter as tk
from tkinter import messagebox
import time
import random
   
# Quiz data with 10 questions for each category
quiz_data = {
    "Science": [
        {"question": "What is the chemical symbol for water?", "choices": ["H2O", "CO2", "O2", "H2"], "answer": "H2O"},
        {"question": "What planet is known as the Red Planet?", "choices": ["Mars", "Jupiter", "Venus", "Saturn"], "answer": "Mars"},
        {"question": "What gas do plants absorb from the atmosphere?", "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
        {"question": "What is the hardest natural substance on Earth?", "choices": ["Iron", "Diamond", "Gold", "Silver"], "answer": "Diamond"},
        {"question": "What is the atomic number of carbon?", "choices": ["6", "12", "14", "16"], "answer": "6"},
        {"question": "What part of the plant conducts photosynthesis?", "choices": ["Root", "Leaf", "Stem", "Flower"], "answer": "Leaf"},
        {"question": "What is the speed of light?", "choices": ["300,000 km/s", "150,000 km/s", "400,000 km/s", "500,000 km/s"], "answer": "300,000 km/s"},
        {"question": "What is the boiling point of water?", "choices": ["90°C", "100°C", "110°C", "120°C"], "answer": "100°C"},
        {"question": "Which planet has the most moons?", "choices": ["Earth", "Saturn", "Jupiter", "Mars"], "answer": "Jupiter"},
        {"question": "What gas do humans need to breathe?", "choices": ["Oxygen", "Carbon Dioxide", "Helium", "Nitrogen"], "answer": "Oxygen"}
    ],
    "History": [


        {"question": "Who was the first Prime Minister of Pakistan?", "choices": ["Liaquat Ali Khan", "Muhammad Ali Jinnah", "Zulfiqar Ali Bhutto", "Benazir Bhutto"], "answer": "Liaquat Ali Khan"},
        {"question": "In which year did Pakistan become an independent country?", "choices": ["1940", "1947", "1952", "1958"], "answer": "1947"},
        {"question": "Which city was the capital of Pakistan before Islamabad?", "choices": ["Karachi", "Lahore", "Peshawar", "Quetta"], "answer": "Karachi"},
        {"question": "When did the Indo-Pak war over Kashmir take place?", "choices": ["1948", "1965", "1971", "1999"], "answer": "1965"},
        {"question": "Who presented the Objectives Resolution in Pakistan’s Constituent Assembly?", "choices": ["Liaquat Ali Khan", "Muhammad Ali Jinnah", "Allama Iqbal", "Ayub Khan"], "answer": "Liaquat Ali Khan"},
        {"question": "What is the official language of Pakistan?", "choices": ["Punjabi", "Sindhi", "Urdu", "English"], "answer": "Urdu"},
        {"question": "When did Pakistan become a nuclear power?", "choices": ["1990", "1998", "2001", "2005"], "answer": "1998"},
        {"question": "Which document was passed in 1973, forming the basis of Pakistan's current constitution?","choices": ["The Constitution of Pakistan", "The Objectives Resolution", "The 1973 Constitution", "The Pakistan Act"], "answer": "The 1973 Constitution"},
        {"question": "Who was Pakistan’s first female Prime Minister?", "choices": ["Benazir Bhutto", "Fatima Jinnah", "Asma Jahangir", "Hina Rabbani Khar"], "answer": "Benazir Bhutto"},
        {"question": "Which Pakistani leader gave the famous speech 'You are free to go to your temples'?", "choices": ["Muhammad Ali Jinnah", "Liaquat Ali Khan", "Zulfikar Ali Bhutto", "Ayub Khan"], "answer": "Muhammad Ali Jinnah"},
        # {"question": "Who was the first president of the United States?", "choices": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "answer": "George Washington"},
        # {"question": "In which year did World War II end?", "choices": ["1942", "1945", "1948", "1950"], "answer": "1945"},
        # {"question": "Who discovered America?", "choices": ["Christopher Columbus", "Vasco da Gama", "Marco Polo", "Ferdinand Magellan"], "answer": "Christopher Columbus"},
        # {"question": "What was the name of the ship on which the Pilgrims traveled to America?", "choices": ["Mayflower", "Santa Maria", "Victoria", "Endeavour"], "answer": "Mayflower"},
        # {"question": "Which war was fought between the North and South regions of the United States?", "choices": ["World War I", "World War II", "Civil War", "Revolutionary War"], "answer": "Civil War"},
        # {"question": "Who was the British Prime Minister during World War II?", "choices": ["Winston Churchill", "Neville Chamberlain", "Margaret Thatcher", "Tony Blair"], "answer": "Winston Churchill"},
        # {"question": "What ancient civilization built the pyramids?", "choices": ["Romans", "Aztecs", "Egyptians", "Mayans"], "answer": "Egyptians"},
        # {"question": "Who was the first emperor of Rome?", "choices": ["Julius Caesar", "Augustus", "Nero", "Tiberius"], "answer": "Augustus"},
        # {"question": "In which year did the Berlin Wall fall?", "choices": ["1980", "1985", "1989", "1991"], "answer": "1989"},
        # {"question": "Who was the leader of the Soviet Union during the Cuban Missile Crisis?", "choices": ["Nikita Khrushchev", "Joseph Stalin", "Leonid Brezhnev", "Mikhail Gorbachev"], "answer": "Nikita Khrushchev"}
    ],
    "General Knowledge": [
        {"question": "Which country is the largest by land area?", "choices": ["Russia", "Canada", "China", "USA"], "answer": "Russia"},
        {"question": "What is the capital of Japan?", "choices": ["Beijing", "Seoul", "Tokyo", "Osaka"], "answer": "Tokyo"},
        {"question": "What is the tallest mountain in the world?", "choices": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"], "answer": "Mount Everest"},
        {"question": "What is the largest ocean?", "choices": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
        {"question": "Who invented the telephone?", "choices": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Isaac Newton"], "answer": "Alexander Graham Bell"},
        {"question": "What currency is used in Japan?", "choices": ["Yen", "Won", "Dollar", "Euro"], "answer": "Yen"},
        {"question": "What is the longest river in the world?", "choices": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
        {"question": "What is the smallest country in the world?", "choices": ["Monaco", "Malta", "Vatican City", "San Marino"], "answer": "Vatican City"},
        {"question": "Who is the author of 'Harry Potter'?", "choices": ["J.K. Rowling", "Stephen King", "J.R.R. Tolkien", "George R.R. Martin"], "answer": "J.K. Rowling"},
        {"question": "Which is the largest desert in the world?", "choices": ["Sahara", "Arabian", "Gobi", "Kalahari"], "answer": "Sahara"}
    ]
}

# Initialize application window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("400x400")

# Global variables
score = 0
question_index = 0
selected_category = ""
total_questions = 10
time_limit = 30  # seconds per question
question_timer = None

# Function to load next question
def load_question():
    global question_index, question_timer
    
    # If all questions are answered, display the final score
    if question_index >= total_questions:
        messagebox.showinfo("Quiz Finished", f"Your final score: {score}/{total_questions}")
        root.quit()
        return
    
    # Display question and choices
    question_data = quiz_data[selected_category][question_index]
    question_label.config(text=f"Q{question_index + 1}: {question_data['question']}")
    
    for i, choice in enumerate(question_data["choices"]):
        choice_buttons[i].config(text=choice, command=lambda c=choice: check_answer(c))
    
    question_index += 1
    start_timer()

# Function to check the answer
def check_answer(choice):
    global score
    
    correct_answer = quiz_data[selected_category][question_index - 1]["answer"]
    if choice == correct_answer:
        score += 1
    stop_timer()
    load_question()

# Timer function
def start_timer():
    global time_limit, question_timer
    if time_limit > 0:
        timer_label.config(text=f"Time left: {time_limit}s")
        time_limit -= 1
        question_timer = root.after(1000, start_timer)  # Call start_timer every 1 second
    else:
        messagebox.showinfo("Time's up", "Time is up for this question!")
        stop_timer()
        load_question()

# Stop the timer
def stop_timer():
    global question_timer, time_limit
    if question_timer:
        root.after_cancel(question_timer)
        time_limit = 30

# Function to start the quiz
def start_quiz(category):
    global selected_category, question_index, score
    selected_category = category
    question_index = 0
    score = 0
    welcome_frame.pack_forget()
    quiz_frame.pack()
    load_question()

# Welcome Frame
welcome_frame = tk.Frame(root)
welcome_frame.pack()

welcome_label = tk.Label(welcome_frame, text="Welcome to the Quiz Application!", font=("Helvetica", 16))
welcome_label.pack(pady=10)

category_label = tk.Label(welcome_frame, text="Select a category:", font=("Helvetica", 12))
category_label.pack(pady=10)

categories = ["Science", "History", "General Knowledge"]
for category in categories:
    category_button = tk.Button(welcome_frame, text=category, command=lambda c=category: start_quiz(c))
    category_button.pack(pady=5)

# Quiz Frame
quiz_frame = tk.Frame(root)

question_label = tk.Label(quiz_frame, text="", font=("Helvetica", 14), wraplength=300)
question_label.pack(pady=10)

choice_buttons = [tk.Button(quiz_frame, text="", font=("Helvetica", 12)) for _ in range(4)]
for btn in choice_buttons:
    btn.pack(pady=5)

timer_label = tk.Label(quiz_frame, text="", font=("Helvetica", 12))
timer_label.pack(pady=10)

root.mainloop()
