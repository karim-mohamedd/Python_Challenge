import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Step 1: Word List
word_list = ["lion", "cow", "tiger", "fish", "donkey", "monkey", "fox"]
secret_word = random.choice(word_list)
lives = len(HANGMANPICS) - 1  # Total lives match the stages of HANGMANPICS

# Printing the placeholders for the word
the_word = "_" * len(secret_word)
print("Welcome to Hangman!")
print(the_word)

# Variables to track the game state
correct_letters = []
wrong_letters = []

# Step 2: Game Loop
while lives > 0:
    print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])  # Show current hangman state
    print(f"Lives left: {lives}")
    print(f"Current word: {' '.join(the_word)}")
    print(f"Wrong guesses: {', '.join(wrong_letters)}")

    guess = input("Guess a letter: ").lower()

    # Validate the input (only one character, and must be alphabetical)
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in correct_letters or guess in wrong_letters:
        print("You already guessed that letter. Try a different one.")
        continue

    # Check the guess
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
        correct_letters.append(guess)

        # Update the_word with the correctly guessed letter
        the_word = ''.join([char if char in correct_letters else '_' for char in secret_word])

        # Check if the player has won
        if "_" not in the_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
    else:
        print(f"Wrong guess! {guess} is not in the word.")
        wrong_letters.append(guess)
        lives -= 1

if lives == 0:
    print(HANGMANPICS[0])  # Final hangman state
    print(f"Game Over! The word was: {secret_word}")
