import tkinter as tk
from tkinter import ttk

class WordleFeedbackGUI:
    def __init__(self, root, guess):
        self.root = root
        self.root.title("Wordle Feedback")
        self.feedback = ['⬜'] * 5  # Initial feedback: all grey
        self.comboboxes = []
        self.guess = guess

        # Create a label for the guessed word
        guess_label = tk.Label(root, text=f"Guess: {guess}", font=("Arial", 16))
        guess_label.grid(row=0, column=0, columnspan=5)

        # Create comboboxes for each letter in the guessed word to select feedback
        for i in range(5):
            combobox = ttk.Combobox(root, values=['⬜', '🟨', '🟩'], font=("Arial", 16), width=3)
            combobox.grid(row=1, column=i)
            combobox.current(0)  # Set the default value to grey
            self.comboboxes.append(combobox)

        # Create a submit button to confirm feedback
        submit_button = tk.Button(root, text="Submit Feedback", command=self.submit_feedback)
        submit_button.grid(row=2, column=0, columnspan=5)

    def submit_feedback(self):
        """Gather feedback and close the GUI."""
        self.feedback = [combobox.get() for combobox in self.comboboxes]
        print(f"Submitted Feedback: {''.join(self.feedback)}")
        self.root.quit()  # Closes the window after submission


def wordle_feedback_gui(guess):
    root = tk.Tk()
    gui = WordleFeedbackGUI(root, guess)
    root.mainloop()  # Runs the GUI
    return ''.join(gui.feedback)
