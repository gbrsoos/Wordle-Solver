import tkinter as tk

class WordleFeedbackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Feedback")
        self.feedback = ['⬜'] * 5  # Initial feedback: all grey
        self.buttons = []
        self.guess_label = None

        # Create a frame for feedback rows
        self.feedback_frame = tk.Frame(root)
        self.feedback_frame.pack(pady=10)

        # Create a label for the guessed word
        self.guess_label = tk.Label(root, text="", font=("Arial", 16))
        self.guess_label.pack()

        # Create a submit button to confirm feedback
        self.submit_button = tk.Button(root, text="Submit Feedback", command=self.submit_feedback)
        self.submit_button.pack(pady=10)

        self.feedback_data = []

    def update_guess(self, guess):
        if self.guess_label:
            self.guess_label.config(text=f"Guess: {guess}")

    def add_feedback_row(self):
        # Create buttons for each letter in the guessed word
        self.feedback = ['⬜'] * 5  # Reset feedback for new guess
        self.buttons = []
        for i in range(5):
            button = tk.Button(self.feedback_frame, text=self.feedback[i], font=("Arial", 24), width=4, command=lambda i=i: self.cycle_feedback(i))
            button.grid(row=len(self.feedback_data), column=i)
            self.buttons.append(button)
        self.feedback_data.append(self.feedback)

    def cycle_feedback(self, i):
        """Cycle through ⬜, 🟨, and 🟩 when the button is clicked."""
        feedback_states = ['⬜', '🟨', '🟩']
        current_state = feedback_states.index(self.feedback[i])
        self.feedback[i] = feedback_states[(current_state + 1) % 3]
        self.buttons[i].config(text=self.feedback[i])

    def submit_feedback(self):
        """Return the feedback and close the GUI."""
        self.root.quit()  # Closes the window after submission

    def get_feedback(self):
        """Retrieve the feedback from the GUI."""
        return self.feedback

    def close(self):
        """Properly close the GUI."""
        self.root.destroy()

def wordle_feedback_gui(gui, best_guess):
    """Update the existing GUI window with a new row for each best guess."""
    gui.add_feedback_row(best_guess)  # Add a new feedback row for each guess
    gui.root.update()  # Update the same window without reopening

    # Check if the window was closed manually
    if gui.closed:
        return None  # Indicate that the user closed the window

    return gui.get_latest_feedback()