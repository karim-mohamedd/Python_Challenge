import random
print('''
         playing card - card games - Blackjack
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
''')

#number 10 is repeated to represent the queen and other cards equal to 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# ask user to play
play = input("Do you want to play game of blackjack (y/n): ")
my_cards = []
computer_cards = []
complete = True
first_card = input("enter 'y' to pick your first card: ")
if first_card == "y":
    my_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    print(f"your card is : {my_cards[0]}")
else:
    print("Invalid you can not bet !")
    complete = False
while complete:
    do_u_want_card = input("Do you want another card (y/n): ")
    if do_u_want_card == "y":
        my_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        print(f"your card is {my_cards[-1]}")
        print("===================================================")
        print(f"your cards are {my_cards}")
        print(f"Computer first card is {computer_cards[0]}")
        if sum(my_cards) > 21:
            print("Bust , You lost the game !!")
            complete = False
    elif do_u_want_card == "n":
        complete = False
        if sum(computer_cards) > 21 or sum(my_cards) > sum(computer_cards):
            print(f"Your cards are {my_cards}")
            print(f"Computer Cards are {computer_cards}")
            print("================================================")
            print("Congrats, You won!! 🎉")
        elif sum(my_cards) < sum(computer_cards):
            print(f"Your cards are {my_cards}")
            print(f"Computer Cards are {computer_cards}")
            print("================================================")
            print("Computer won! You lost 😢")
        else:
            print("It is a Draw !!")
    else:
        print("Invalid Please enter 'y' or 'n' ")
        continue



    
