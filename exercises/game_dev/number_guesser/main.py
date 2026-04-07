"""
File: main.py
Author: Cody Gilbert
Date: 04/05/2026

Description:
    Main progam - Controls implements game loop and
        user interactions.
"""
from guesser import Guesser

def play(object):
# Defines game logic

    play = True
    while play:
    # Outer loop - repeats until user opts out

        print("Welcome to my number guessing game!")
        print(f"Pick a number between 1 and 100!")
        input("\nWhen you're ready, press Enter to begin...")

        still_guessing = True

        while still_guessing:
        # Inner loop - repeats until guess is correct

            guess = object.get_current_guess()
            response = input(f"Is it {guess}? (h/l/c): ")
            if response == 'c':
                print("I knew it!")
                still_guessing = False
            elif response == 'h':
                object.higher()
            elif response == 'l':
                object.lower()
            else:
                print("Invalid response. Please enter h, l or c")

        if input("\nPlay again? (y/n): ").lower() == 'y':
            object.reset()
        else:
            print("Thanks for playing!")
            play = False

def main():
    game = Guesser(1, 100)
    play(game)

    
if __name__ == "__main__":
    main()
