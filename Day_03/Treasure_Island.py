print ('''                                   
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
 ''')
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______//______/
*******************************************************************************

''')

print("Now your mission is to find the treasure $$ ")

x = input("You are now in the middle of the island will you go left or right \n")

if x == "right":
    print("Fall into a hole, Game Over !!")
elif x == "left":
    y = input("now you are facing a sea will you swim or wait a boat \n")
    if y == "swim":
        print("you are attacked by shark , Game Over")
    if y == "wait":
        print("now you took the boat and arrived to nex area \n you are facing 3 doors red, yellow, blue choose one\n")
        y = input()
        if y == "red":
            print ("you are burned by fire , Game Over")
        if y == "blue":
            print("You are dead , Game Over !!")
        if y == "yellow":
            print("Good job you arrived to the treasure, You won")
        else:
            print("You are Dead !!")
    else:
        print("Game Over !!")
else:
    print("Game Over !!")



