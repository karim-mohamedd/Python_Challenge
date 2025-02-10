import random
# Function to display the logo
def print_logo():
    logo = """                                                                                                                                        

     _  _            _                ___                _              ___                
    | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
    | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
    |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
                                                            |___/                       
                            welcome to number guessing game !!
    """
    print(logo)

# Function to generate random number between 0 and 100
def generate_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

#Function to get the difficulty
def get_difficulty():
    """Asks the user to choose difficulty and returns the number of attempts."""
    while True:
        difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid input! Please type 'easy' or 'hard'.")

#Function for the logic of the game
def play_game():
    """Runs the number guessing game."""
    print_logo()
    number = generate_number()
    print("I'm thinking of a number between 1 and 100... 🤔")

    lives = get_difficulty()

    while lives > 0:
        print(f"\nYou have {lives} attempts remaining. Good luck! 🍀")
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100.")
                continue

            if guess == number:
                print(f"🎉 Good job! You guessed the right number {number}.")
                return
            elif guess < number:
                print("⬆️ Too low, try again.")
            else:
                print("⬇️ Too high, try again.")

            lives -= 1

        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    print(f"\n💀 You ran out of attempts! The correct number was {number}. Better luck next time!")

# Start the game
play_game()
