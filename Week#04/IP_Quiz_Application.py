# INTERNSHIP PAKISTAN
# WEEK#04 : Quiz Application Development 
# Objective: Develop a Quiz Application in python that allows users to take quizzes with multiple choice questions. The application will include score tracking, question categorization, and a timer for each quiz.

# *************************************** QUIZ APPLICATION ********************************************************
# Version v1.0
# Console Based

import time
import json

# Quiz data with multiple categories and questions
quiz_data = {
    "Science": [
        {"question": "What is the chemical symbol for water?", "choices": ["H2O", "CO2", "O2", "H2"], "answer": "H2O"},
        {"question": "What planet is known as the Red Planet?", "choices": ["Mars", "Jupiter", "Venus", "Saturn"], "answer": "Mars"}
    ],
    "History": [
        {"question": "Who was the first president of the United States?", "choices": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "answer": "George Washington"},
        {"question": "In which year did World War II end?", "choices": ["1942", "1945", "1948", "1950"], "answer": "1945"}
    ],
    "General Knowledge": [
        {"question": "Which country is the largest by land area?", "choices": ["Russia", "Canada", "China", "USA"], "answer": "Russia"},
        {"question": "What is the capital of Japan?", "choices": ["Beijing", "Seoul", "Tokyo", "Osaka"], "answer": "Tokyo"}
    ]
}

# To store user scores and performance history
scores_file = "quiz_scores.json"

# Function to save the score to a file
def save_score(username, category, score, total_questions):
    try:
        with open(scores_file, "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = {}
    
    if username not in scores:
        scores[username] = []
    
    scores[username].append({"category": category, "score": score, "total_questions": total_questions})

    with open(scores_file, "w") as file:
        json.dump(scores, file)

# Function to view past scores
def view_scores(username):
    try:
        with open(scores_file, "r") as file:
            scores = json.load(file)
        if username in scores:
            print(f"\n{username}'s Score History:")
            for record in scores[username]:
                print(f"Category: {record['category']}, Score: {record['score']}/{record['total_questions']}")
        else:
            print(f"\nNo score history found for {username}.")
    except FileNotFoundError:
        print(f"\nNo score history found for {username}.")

# Quiz logic
def start_quiz(username):
    print("\nAvailable categories:")
    for category in quiz_data:
        print(f"- {category}")

    category = input("\nChoose a category: ").title()
    if category not in quiz_data:
        print("Invalid category! Exiting...")
        return

    print("\nYou have 15 seconds to answer each question.")
    time.sleep(1)
    
    score = 0
    total_questions = len(quiz_data[category])

    for question_data in quiz_data[category]:
        print("\n" + question_data["question"])
        for i, choice in enumerate(question_data["choices"], 1):
            print(f"{i}. {choice}")

        start_time = time.time()
        try:
            answer = input("Enter the number of your answer (1/2/3/4): ")
            if time.time() - start_time > 15:
                print("Time's up! Moving to the next question.")
            elif question_data["choices"][int(answer) - 1] == question_data["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        except:
            print("Invalid input or timeout!")

    # Save the score and show final results
    save_score(username, category, score, total_questions)
    print(f"\nQuiz finished! Your score: {score}/{total_questions}")
    view_scores(username)

# Main application loop
def main():
    print("Welcome to the Quiz Application!")
    username = input("Please enter your name: ").capitalize()

    while True:
        print("\n1. Take a Quiz")
        print("2. View Past Scores")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            start_quiz(username)
        elif choice == "2":
            view_scores(username)
        elif choice == "3":
            print("Thank you for using the Quiz Application!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
