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

def play_game(user_choose):
    pass

def info_game():
    pass

def exit_game():
    pass