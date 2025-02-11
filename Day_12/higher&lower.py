from Game_data import data
from art import logo, vs
import random

# Get random account from data
def get_random_acc():
    """Returns a random account from the dataset."""
    return random.choice(data)

# Format the account data
def format_data(account):
    """Formats account details into a readable string."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}."

# Check if the guess is correct
def check_answer(guess, a_follower, b_follower):
    """Returns True if the guess is correct, else False."""
    return (guess == "a" and a_follower > b_follower) or (guess == "b" and b_follower > a_follower)

def play():
    """Main game function."""
    print(logo)  # Print logo once at the start
    
    score = 0
    game_continue = True
    player_1 = get_random_acc()  # Start with a random player

    while game_continue:
        player_2 = get_random_acc()

        # Ensure player_1 and player_2 are not the same
        while player_1 == player_2:
            player_2 = get_random_acc()

        print(f"\nCompare A: {format_data(player_1)}")
        print(vs)
        print(f"Compare B: {format_data(player_2)}")

        # Take user input and convert it to lowercase
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower counts
        a_follower_count = player_1["follower_count"]
        b_follower_count = player_2["follower_count"]

        # Check if the user's guess is correct
        if check_answer(guess, a_follower_count, b_follower_count):
            score += 1
            print(f"You're right! Current score: {score}")
            player_1 = player_2  # Move player_2 to player_1 for the next round
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False  # End the game

play()
