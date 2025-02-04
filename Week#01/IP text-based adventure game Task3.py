# INTERNSHIP PAKISTAN
# Task_3
# Develop a text-based adventure game where user can navigate through different rooms and make choices.

def start_game():
    print("Welcome to the Haunted House Adventure!")
    print("You find yourself in a dark, eerie house with only one objective: Escape!")
    print("You can choose to explore different rooms to find the exit.")
    print("Type 'help' anytime to see your options.\n")
    first_room()

def first_room():
    print("\nYou are in the living room. There's a door to the north and a door to the east.")
    choice = input("What would you like to do? (north/east): ").lower()

    if choice == 'north':
        kitchen()
    elif choice == 'east':
        library()
    elif choice == 'help':
        print("Options: north, east")
        first_room()
    else:
        print("Invalid choice. Try again.")
        first_room()

def kitchen():
    print("\nYou are in the kitchen. There's a strange noise coming from the pantry.")
    choice = input("What would you like to do? (investigate/back): ").lower()

    if choice == 'investigate':
        print("A ghost appears and scares you back to the living room!")
        first_room()
    elif choice == 'back':
        print("You go back to the living room.")
        first_room()
    elif choice == 'help':
        print("Options: investigate, back")
        kitchen()
    else:
        print("Invalid choice. Try again.")
        kitchen()

def library():
    print("\nYou are in the library. There's a door to the north and a door to the south.")
    choice = input("What would you like to do? (north/south/back): ").lower()

    if choice == 'north':
        secret_room()
    elif choice == 'south':
        print("You go back to the living room.")
        first_room()
    elif choice == 'back':
        print("You go back to the living room.")
        first_room()
    elif choice == 'help':
        print("Options: north, south, back")
        library()
    else:
        print("Invalid choice. Try again.")
        library()

def secret_room():
    print("\nYou have entered a secret room with a treasure chest and a door to the east.")
    choice = input("What would you like to do? (open/east/back): ").lower()

    if choice == 'open':
        print("Congratulations! You found a key to escape the house.")
        print("You win!")
    elif choice == 'east':
        print("You walk through the door and find yourself back in the library.")
        library()
    elif choice == 'back':
        print("You go back to the library.")
        library()
    elif choice == 'help':
        print("Options: open, east, back")
        secret_room()
    else:
        print("Invalid choice. Try again.")
        secret_room()

# Start the game
start_game()
