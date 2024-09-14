import numpy as np
import pandas as pd
import json
import tkinter as tk

from gui import WordleFeedbackGUI, wordle_feedback_gui
from entropy import entropy_calculation
from pruning import pruning
from best_guess import find_best_guess
from gui import wordle_feedback_gui

# Open the JSON file for reading
with open('/Users/soosgabor/Library/Mobile Documents/com~apple~CloudDocs/05_Programming/01_Wordle/initial_entropies.json', 'r') as file:
    INITIAL_ENTROPIES = json.load(file)

FIRST_GUESS = next(iter(INITIAL_ENTROPIES.keys()))
MAIN_WORDS_LIST = list(INITIAL_ENTROPIES.keys())

def wordle_solver(wordlist, secret_word=None):
    guess_count = 0
    solved = False
    feedback = ''
    possible_words_dict = {word: list(word) for word in MAIN_WORDS_LIST}
    
    print("Starting Wordle Solver!")
    
    # Initialize the GUI
    root = tk.Tk()
    gui = WordleFeedbackGUI(root)

    # Step 1: Use the fixed first guess for the first round
    best_guess = FIRST_GUESS  # Fixed first guess
    
    while not solved and guess_count < 6:
        if guess_count == 0:
            print(f"First Guess: {best_guess}")
        else:
            # Recalculate entropy after pruning and choose the best guess
            entropy_values = {word: entropy_calculation(word, wordlist, feedback) for word in possible_words_dict.keys()}
            best_guess = max(entropy_values, key=entropy_values.get)
            print(f"Guess {guess_count + 1}: {best_guess}")

        # Update the GUI with the current best guess
        gui.update_guess(best_guess)
        gui.add_feedback_row()

        # Run the GUI event loop and wait for feedback
        root.mainloop()

        # Collect feedback from the GUI
        feedback = gui.get_feedback()  # Get the feedback from the GUI
        print(f"User feedback: {feedback}")

        guess_count += 1

        if feedback == ['🟩', '🟩', '🟩', '🟩', '🟩']:
            print(f"Solved in {guess_count} guesses! The word is {best_guess}.")
            solved = True
            break

        # Step 3: Prune the word list based on feedback
        possible_words_dict = pruning(possible_words_dict, best_guess, feedback)

    # Close the GUI window after the game is over
    gui.close()

    if not solved:
        print("Game over! Couldn't solve the Wordle in 6 tries.")

wordle_solver(MAIN_WORDS_LIST)
