import tkinter as tk

class WordleFeedbackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Feedback")
        self.feedback_ready = False
        
        # Label for Best Guess
        self.best_guess_label = tk.Label(root, text="Best Guess: ", font=("Arial", 16))
        self.best_guess_label.grid(row=0, column=0, columnspan=5, pady=(10, 5))
        
        # Label and Listbox for Top 10 Words
        self.top_words_label = tk.Label(root, text="Top 10 Words by Entropy", font=("Arial", 14))
        self.top_words_label.grid(row=1, column=0, columnspan=5)

        self.top_words_listbox = tk.Listbox(root, width=50, height=10)
        self.top_words_listbox.grid(row=2, column=0, columnspan=5, pady=10)

        # Initialize feedback squares (one row)
        self.feedback_squares = []
        self.create_feedback_squares()

        # Add a submit button
        submit_button = tk.Button(root, text="Submit Feedback", command=self.submit_feedback)
        submit_button.grid(row=4, column=0, columnspan=5)

    def create_feedback_squares(self):
        """Create a single row of feedback squares."""
        row = tk.Frame(self.root)
        row.grid(row=3, column=0, columnspan=5, pady=10)

        for i in range(5):
            button = tk.Button(row, text='⬜', font=("Arial", 24), width=4, command=lambda i=i: self.cycle_feedback(i))
            button.grid(row=0, column=i)
            self.feedback_squares.append(button)

    def update_top_words(self, top_words):
        """Update the top 10 words list."""
        self.top_words_listbox.delete(0, tk.END)  # Clear current list
        for word in top_words:
            self.top_words_listbox.insert(tk.END, word)

    def update_guess(self, guess):
        """Update the displayed best guess in the GUI."""
        self.best_guess_label.config(text=f"Best Guess: {guess}")

    def cycle_feedback(self, index):
        """Cycle through grey, yellow, and green colors for a square."""
        feedback_states = ['⬜', '🟨', '🟩']  # Grey, Yellow, Green
        current_state = self.feedback_squares[index].cget("text")  # Get current button text
        
        # Determine the new state
        if current_state == '⬜':
            new_state = '🟨'  # Change from Grey to Yellow
        elif current_state == '🟨':
            new_state = '🟩'  # Change from Yellow to Green
        else:
            new_state = '⬜'  # Change from Green back to Grey

        self.feedback_squares[index].config(text=new_state)  # Update the button text

    def get_feedback(self):
        """Return the feedback from the GUI."""
        return [button.cget("text") for button in self.feedback_squares]

    def submit_feedback(self):
        """Signal that feedback is ready and close the GUI."""
        self.feedback_ready = True
        self.root.quit()  # Close the GUI

# Example usage:
# root = tk.Tk()
# gui = WordleFeedbackGUI(root)
# root.mainloop()

def wordle_feedback_gui(gui, best_guess):
    """Update the existing GUI window with a new row for each best guess."""
    gui.add_feedback_row(best_guess)  # Add a new feedback row for each guess
    gui.root.update()  # Update the same window without reopening

    # Check if the window was closed manually
    if gui.closed:
        return None  # Indicate that the user closed the window

    return gui.get_latest_feedback()
