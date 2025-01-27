import random

# rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game = [rock, paper, scissors]

x = int(input("choose 0 for rock, 1 for paper, 2 for scissors\n"))
#validation
if x < 0 or x > 2:
    print("Invalid please choose 0 for rock, 1 for paper, 2 for scissors\n")
else:
    y = random.randint(0,2)

# Displaying the results
    print(f"Your Choice:\n{game[x]}")
    print(f"Computer's Choice:\n{game[y]}")

    if x == y:
        print("It is a Draw!")
    elif (x == 1 and y == 0) or (x == 2 and y == 1) or (x == 0 and y == 2):
        print("You Won!")
    else:
        print("You Lost!")