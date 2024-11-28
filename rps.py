# This game was built using GitHub Copilot, but notably the code
# matches this website's version almost identically:
#   https://realpython.com/python-rock-paper-scissors/

import random

# This Loop allows the user to play repeatedly until the decide not to
while True:
    # Ask the user for their throw
    user_action = input("Enter throw (rock, paper, scissors): ").lower()

    # Randomly choose the AI's action
    ai_action = random.choice(["rock", "paper", "scissors"])

    # Print the result of the throw
    print(f"\nYou chose {user_action}, AI chose {ai_action}.\n")

    # Determine the winner based on the choices
    if user_action == ai_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if ai_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if ai_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if ai_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Invalid input! Please enter rock, paper, or scissors.")

    play_game_again = input("Do you want to play the game again? (yes/no): ").lower()

    if play_game_again != "yes":
        print("Thanks for playing!")
        break

