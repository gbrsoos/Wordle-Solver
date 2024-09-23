import numpy as np
import pandas as pd

def pruning(words, guess, feedback):

    #Creating a hashmap to pair feedback squares for all 5 letters for evaluation
    hashmap = {}

    grey_letters=[]
    yellow_letters = []
    green_letters=[]

    for index in range(5):    
        hashmap.update({index: list()})
        hashmap[index].append(guess[index])
        hashmap[index].append(feedback[index])

    #GREEN
    #Keeping words with green letter(s) match
    has_green = any(square == '🟩' for letter, square in hashmap.values()) #Flag for the presence of '🟩'

    if has_green:
        for index, (letter, square) in hashmap.items():
            if square == '🟩':
                green_index = index
                green_letter = letter

                #Collect words to be pruned (if the letter in the suggested place is not the expected one)
                words_to_prune_green = [index for index, word in words.items() 
                                if word[green_index] != green_letter]

                #Remove the words after iteration
                for index in words_to_prune_green:
                    words.pop(index)
    
    #YELLOW
    #Sorting words based on yellow feedback(s)
    has_yellow = any(square == '🟨' for letter, square in hashmap.values()) #Flag for the presence of '🟨'

    if has_yellow:
        yellow_letters = []

        for index, (letter, square) in hashmap.items():
            if square == '🟨':
                yellow_index = index
                yellow_letter = letter
                yellow_letters.append(yellow_letter)

                #Collect words to be pruned (if the letter in the yellow places are the same letters
                #or if the word does not contain the letter of interest)
                words_to_prune_notinplace = [index for index, word in words.items()
                                if word[yellow_index] == yellow_letter]
                words_to_prune_noletter = [index for index, word in words.items()
                                if yellow_letter not in word]

                #Remove the words after iteration
                for index in words_to_prune_notinplace + words_to_prune_noletter:
                    words.pop(index)

    #GREY
    #Sorting words based on grey feedback(s)
    has_grey = any(square == '⬜' for letter, square in hashmap.values()) #Flag for the presence of '⬜'

    if has_grey:
        for index, (letter, square) in hashmap.items():
            if square == '⬜':
                grey_index = index
                grey_letter = letter

                #Collect words to be pruned (if the word has the letter labeled grey AND is not present among yellow letters)
                words_to_prune_grey = [index for index, word in words.items()
                                if grey_letter in word and grey_letter not in yellow_letters]
                
                #Remove the words after iteration
                for index in words_to_prune_grey:
                    words.pop(index)
        
    return words

"""
with open('/Users/soosgabor/Library/Mobile Documents/com~apple~CloudDocs/05_Programming/01_Wordle/initial_entropies.json', 'r') as file:
    INITIAL_ENTROPIES = json.load(file)

FIRST_GUESS = next(iter(INITIAL_ENTROPIES.keys()))
MAIN_WORDS_LIST = list(INITIAL_ENTROPIES.keys())
possible_words_dict = {word: list(word) for word in MAIN_WORDS_LIST}

pruning(possible_words_dict, 'rates', ['🟨', '🟩' ,'⬜', '⬜', '🟨'])
"""

