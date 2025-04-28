# Heads and Tails Game

import random

def head_coin():
    print(r"""
      .-------.
     /         \
    |   HEADS   |
    |   (◕‿◕)   |
     \         /
      `-------`
    """)

def tail_coin():
    print(r"""
      .-------.
     /         \
    |   TAILS   |
    |   (≧◡≦)   |
     \         /
      `-------`
    """)

def main_text():
    print("\n\t\tWELCOME TO THE HEADS OR TAILS GAME!")

    print("1) PLAY!")
    print("2) INFO!")
    print("3) EXIT!")

    user_choose = input("Please select an option (1/2/3): ")

    return user_choose

def play_game():
    pc_choose = random.choice(["HEADS","TAILS"])
    if pc_choose == "HEADS":
        head_coin()
    else:
        tail_coin()

    print(f"YOU GOT: {pc_choose}\n")

def info_game():
    print("""
    === GAME INFO ===

    Flip a coin and guess: heads or tails.
    Let's see if luck is on your side!

    Press Enter to continue...
    """)
    input("-->")

def exit_game():
    print("Bye Bye...\n")
    quit()

while True:
    user_choice = main_text()

    if user_choice == "1":
        play_game()
    elif user_choice == "2":
        info_game()
    elif user_choice == "3":
        exit_game()
    else:
        print("Invalid choice, please try again.\n")