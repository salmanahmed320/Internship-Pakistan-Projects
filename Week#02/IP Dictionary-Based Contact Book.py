# INTERNSHIP PAKISTAN
# Week 2: Introdiction To Data Structures 
# Task#2: Dictionary-based Contact book
# Objective: Create a contact book using a dictionary where user can add, delete, and view contacts.

# Initialize an empty dictionary to store contacts
contact_book = {}

# Infinite loop to keep the contact book running
while True:
    # Display menu options
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View All Contacts")
    print("4. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Add a new contact
    if choice == '1':
        name = input("Enter the contact name: ")
        phone = input("Enter the contact phone number: ")
        contact_book[name] = phone
        print(f"Contact {name} added successfully.")

    # Delete an existing contact
    elif choice == '2':
        name = input("Enter the contact name to delete: ")
        if name in contact_book:
            del contact_book[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found.")

    # View all contacts
    elif choice == '3':
        if contact_book:
            print("\nAll Contacts:")
            for name, phone in contact_book.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts available.")

    # Exit the program
    elif choice == '4':
        print("Exiting the contact book. Goodbye!")
        break

    # Handle invalid input
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
