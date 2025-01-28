import random
word_list = ["lion","caw","tiger","fish","donkey","monkey","fox"]
secret_word = random.choice(word_list)
print(secret_word)

#printing the placeholders for the word
the_word = "_" * len(secret_word)
print(the_word)
#--------------------------------------
guess = input("Guess the letter\n")

display = ""
for char in secret_word:
    if char == guess:
        display += guess
    else:
        display += "_"
print(display)

     