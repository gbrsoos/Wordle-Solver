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
with open('data/initial_entropies.json', 'r') as file:
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
    print(f"First Guess: {best_guess}")
    gui.update_guess(best_guess)  # Display the first guess

    while not solved and guess_count < 6:
        guess_count += 1
        
        # Run the GUI event loop and wait for feedback
        root.mainloop()

        # Collect feedback from the GUI
        feedback = gui.get_feedback()
        # Get the current guess from the GUI after feedback
        current_guess = gui.best_guess_label.cget("text").replace("Best Guess: ", "")
        
        print(f"User feedback for guess {current_guess}: {feedback}")

        # Check if the guess was correct
        if feedback == ['🟩', '🟩', '🟩', '🟩', '🟩']:
            print(f"Solved in {guess_count} guesses! The word is {current_guess}.")
            solved = True
            break

        # Prune the word list based on feedback using the current guess
        possible_words_dict = pruning(possible_words_dict, current_guess, feedback)

        # Check if any possible words remain
        if not possible_words_dict:
            print("No possible words left after pruning. The game cannot continue.")
            break

        # Calculate entropy for remaining possible words
        entropy_values = {word: entropy_calculation(word, wordlist, feedback) for word in possible_words_dict.keys()}
        
        # Get the top 10 guesses based on entropy
        sorted_guesses = sorted(entropy_values.items(), key=lambda x: x[1], reverse=True)
        top_guesses = sorted_guesses[:10]  # Get the new top 10 words

        # Update the displayed best guess and the list of top words
        best_guess = top_guesses[0][0] if top_guesses else current_guess  # Fallback to current guess if no top guesses
        gui.update_guess(best_guess)
        gui.update_top_words([word for word, _ in top_guesses])

    if not solved:
        print("Game over! Couldn't solve the Wordle in 6 tries.")

    root.quit()  # Make sure to close the GUI when done

wordle_solver(MAIN_WORDS_LIST)
