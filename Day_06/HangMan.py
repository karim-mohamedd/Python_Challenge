import random

# Step 1: Word List
word_list = ["lion", "cow", "tiger", "fish", "donkey", "monkey", "fox"]
secret_word = random.choice(word_list)

# Printing the placeholders for the word
the_word = "_" * len(secret_word)
print(the_word)

# Variables to track the game state
correct_letters = []
Game_Over = False

# Step 2: Game Loop
while not Game_Over:
    guess = input("Guess a letter: ").lower()

    # Validate the input (only one character, and must be alphabetical)
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    # Display updates for the guessed letter
    display = ""

    # Loop through the secret word and build the updated display
    for index, char in enumerate(secret_word):
        if char == guess:  # Correct guess
            display += char
            if char not in correct_letters:
                correct_letters.append(char)
        elif char in correct_letters:  # Already correctly guessed letters
            display += char
        else:  # Placeholder for unguessed letters
            display += "_"

    print(display)

    # Check if the player has won
    if "_" not in display:
        print("You Won!")
        Game_Over = True

     