# Heads and Tails Game

import random

def head_coin():
    print("""
         ~~~~~~~~
       /\\         /\\
      /  \\       /  \\
     /    \\     /    \\
    |      |   |      |
    |  HEADS   |
     \\         /
      \\       /
       \\~~~~~/
     """)
def tail_coin():
    print("""
         ~~~~~~~~
       /\\         /\\
      /  \\       /  \\
     /    \\     /    \\
    |      |   |      |
    |  TAILS   |
     \\         /
      \\       /
       \\~~~~~/
     """)


def main_text():
    print("\t\tWELCOME TO THE HEADS OR TAILS GAME!")

    print("1) PLAY!")
    print("2) INFO!")
    print("3) EXIT!")

    user_choose = input("Please select an option (1/2/3): ")

    return user_choose

def play_game():
    pc_choose = random.choice(["heads","tails"])
    if pc_choose == "heads":
        head_coin()
    else:
        tail_coin()

def info_game():
    print("""
    === GAME INFO ===

    In this game, you test your luck!
    The computer flips a coin: heads or tails.
    Your task is to guess the outcome.

    Good luck and have fun!

    Press Enter to return to the menu...
    """)
    input("-->")
def exit_game():
    print("Bye Bye...")

