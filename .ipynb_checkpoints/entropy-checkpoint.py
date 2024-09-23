import pandas as pd
import numpy as np
import random

def entropy_calculation(guess, possible_words, feedback_from_user):
    # Dictionary to store how often each feedback pattern appears
    feedback_patterns = {}

    # Iterate over all possible words and use the manually provided feedback
    for word in possible_words:
        feedback = tuple(feedback_from_user)  # Feedback provided by user (tuple for hashability)
        if feedback not in feedback_patterns:
            feedback_patterns[feedback] = 1
        else:
            feedback_patterns[feedback] += 1
    
    # Calculate entropy and track pattern contributions
    total_possible = len(possible_words)
    entropy = 0
    pattern_contributions = {}

    for feedback, count in feedback_patterns.items():
        prob = count / total_possible
        entropy_contribution = -prob * np.log2(prob)
        entropy += entropy_contribution
        # Store the contribution of each feedback pattern
        pattern_contributions[feedback] = entropy_contribution
    
    return entropy, pattern_contributions
