# INTERNSHIP PAKISTAN
# WEEK 3 : File Handling And Basic Automation 
# Task #1: Text File Analyzer
# Develop a script that reads a textt file and provides stats like word count, line count, and the most frequent words.

# Open the text file in read mode
file_name = input("Enter the name of the text file (with extension): ")
with open(file_name, 'r') as file:
    # Read the contents of the file
    text = file.read()

# Initializing counters
line_count = 0
word_count = 0
word_frequency = {}

# Split the text into lines
lines = text.splitlines()

# Looping through each line to count lines and words
for line in lines:
    line_count += 1  # Count the lines
    words = line.split()  # Split the line into words
    word_count += len(words)  # Count the words in the line

    # Count the frequency of each word
    for word in words:
        word = word.lower()  # Convert the word to lowercase to handle case-insensitive counting
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

# Find the most frequent word
most_frequent_word = max(word_frequency, key=word_frequency.get)

# Display the statistics
print("\nText File Statistics:")
print(f"Total Lines: {line_count}")
print(f"Total Words: {word_count}")
print(f"Most Frequent Word: '{most_frequent_word}' (appears {word_frequency[most_frequent_word]} times)")
