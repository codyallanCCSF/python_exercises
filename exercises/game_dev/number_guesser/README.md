# Guesser Project

## Description
The Guesser project consists of a Python class designed to facilitate a binary search guessing game. The `Guesser` class acts as a logic engine that manages numerical boundaries and calculates midpoints, while the `main.py` script handles all user input and output. This separation of concerns ensures the core logic remains independent of the user interface.

---

## File Structure
* **guesser.py**: Contains the `Guesser` class definition, including state management for the game range and methods for adjusting boundaries.
* **main.py**: The executable script that instantiates the `Guesser` object and runs the game loop, including welcome messages and replay functionality.

---

## Class Features

### Guesser Class
The class tracks a "low" and "high" value to perform a binary search.

* **Initial State**: Stores the original boundaries to allow for game resets without re-instantiation.
* **State Reset**: Reverts the active range to the starting parameters.
* **Boundary Adjustment**: Logic to increment the lower bound or decrement the upper bound based on user feedback, preventing infinite loops on adjacent numbers.
* **Representation**: A `__repr__` method provides a string format of the current object state for debugging purposes.

---

## Usage
To run the game, execute the main script from the terminal:

```bash
python main.py
