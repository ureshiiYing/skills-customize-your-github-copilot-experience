
# 🎮 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and random selection while creating an interactive word-guessing experience.

## 📝 Tasks

### 🛠️  Game Setup

#### Description
Create the initial setup for your Hangman game, including a list of possible words and logic to select one at random.

#### Requirements
Completed program should:

- Define a list of at least 5 possible words
- Randomly select one word for the player to guess
- Display a welcome message and instructions


### 🛠️  Gameplay Loop

#### Description
Implement the main game loop where the player guesses letters, and the game tracks progress and remaining attempts.

#### Requirements
Completed program should:

- Accept single-letter guesses from the player
- Show the current progress (e.g., _ a _ _ m a n)
- Track and display the number of incorrect guesses remaining
- End the game when the word is guessed or attempts run out
- Display a win or lose message at the end

Example output:
```text
Welcome to Hangman!
Word: _ _ _ _ _ _ _
Guesses left: 6
Guess a letter: a
Word: _ a _ _ _ a n
Guesses left: 5
...
Congratulations, you won!
```
