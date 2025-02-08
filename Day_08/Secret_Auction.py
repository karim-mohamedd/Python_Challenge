print("===================== Welcome to Secret Auction Program =====================")
print('''                ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ 
      ''')
z = True

while z:
    x = input("What is your name: ")
    y = int(input("Whats is your Bid price: "))
    dictt = {x : y}
    Finish = input("are there any other bidders ? Y, N: ")
    if Finish == "Y":
        continue
    elif Finish == "N" or "n":
        for x in dictt:
            print(x)
            z = False
    else:
        print("Invalid input please enter Y, N")



  

       
