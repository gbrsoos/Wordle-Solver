# Wordle-Solver

This project is a solver for the New York Times' famous daily game, Wordle (https://www.nytimes.com/games/wordle/index.html).
The idea is coming from the popular YouTube channel, 3Blue1Brown (https://www.youtube.com/watch?v=v68zYyaEmEA&t=228s). The purpose of this project was to recreate the output without looking into his code.

Wordle solver is an entropy-based solution that suggests optimal words for input based on the game's feedback. 

## Building steps

1. Initial word entropies has been calculated after the initial dataset was filtered to the 5-letter words (https://www.kaggle.com/datasets/rtatman/english-word-frequency)
2. A feedback function was built, which serves as a bridge between the original game and the code. Using this, the user can determine the colored brackets that are shown by the game.
3. The pruning function is responsible for updating the pool of possible words in each iteration after the feedback has been prompted.
4. The entropy calculation function then uses the pool of remaining words to calculate which words provides the most information, and then the program suggests that word as the next input in the game.
5. A minimal GUI has been also built by tkinter, which displays the suggested word by the program, and a clickable interface to input the most recent feedback.
6. There is also an executable, which can be used to start the program using a Mac device.

## Way of using:

The most practical way to use the program is the following:
1. Fork the repository
2. In your terminal, navigate to the folder using 'cd'
3. type 'python main.py' and wait for the program to run
