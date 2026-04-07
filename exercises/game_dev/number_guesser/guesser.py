"""
File: guesser.py
Author: Cody Gilbert
Date: 04/05/2026

Description:

    Guesser class definition - Contains variables and methods
    to execute a binary search for a number guessing game.

"""

class Guesser:

    def __init__(self, low, high):
    # Creates Guesser object with instance variables

        # Stores initial range
        self._start_low = low
        self._start_high = high

        self.reset()

    def reset(self):
    # Resets game to initial state

        self._low = self._start_low
        self._high = self._start_high
        self._guess = self.get_current_guess()

    def __repr__(self):
        # Returns formatted string for debugging

        return f"Guesser(low={self._low}, high={self._high}, guess={self._guess})"

    def get_current_guess(self):
    # Calculates and returns midpoint of current range
        self._guess = (self._low + self._high) // 2
        return self._guess 

    def lower(self):
    # Assigns new upper bound

        self._high = self._guess - 1

    def higher(self):
    # Assigns new lower bound

        self._low = self._guess + 1

