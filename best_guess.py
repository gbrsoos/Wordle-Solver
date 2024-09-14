import numpy as np
import pandas as pd

def find_best_guess(word_entropy_dict):
    best_guess = next(iter(word_entropy_dict.keys()))

    return best_guess