import pandas as pd
import numpy as np

def wordle_feedback(secret_word, guessed_word):
    feedback=['⬜']*5 #Baseline feedback: 5 grey

    secret_word_list = list(secret_word)
    guessed_word_list = list(guessed_word)

    for i in range(5): #Checking for the perfect matches (🟩)
        if secret_word_list[i] == guessed_word_list[i]:
            feedback[i] = '🟩'
            secret_word_list[i] = None

    for i in range(5): #Checking for the half-matches (🟨)
        if guessed_word_list[i] in secret_word_list:
            feedback[i] = '🟨'
            secret_word_list[secret_word_list.index(guessed_word_list[i])] = None  # Mark the slot and the letter as used

    return ''.join(feedback)


wordle_feedback('stain', 'rates')


