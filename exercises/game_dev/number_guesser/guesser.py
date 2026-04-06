"""
File: guesser.py
Author: Cody Gilbert
Date: 04/05/2026

Description:
    
    Guesser class definition - Contains variables and methods
    to execute a number guessing game where the computer
    tries to guess the user's chosen number.

"""

class Guesser:
# Creates Guesser object with instance variables

    def __init__(self, low, high):
   
        self._low = low
        self._high = high

        self._midpoint = 0
        self._response = None

    def __repr__(self):
    # Returns formatted string for debugging

        return (
                f"Guesser(low={self._low}, high={self._high})"
                f"Current guess: {self._midpoint}"
            )

    def welcome(self):
        print(
                "Welcome to my number guessing game!"
                f"Pick a number between {self._low} and {self._high}!"
                )
   
    def get_current_guess(self):
    # Calculates and returns midpoint of current range

        return (self._low + self._high) // 2

    def lower(self):
    # Assigns new upper bound
        self._high = self._midpoint

    def higher(self):
    # Assigns new lower bound
        self.low = self.midpoint
