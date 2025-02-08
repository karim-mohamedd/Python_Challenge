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

def find_Highest_Bidder(bidding_Dictionary):
    winner = ""
    Highest_Bid = 0
    for bidder in bidding_Dictionary:
        bid = bidding_Dictionary[bidder]
        if bid > Highest_Bid:
            Highest_Bid = bid
            winner = bidder
    print(f"The winner is {winner} with bid of: ${Highest_Bid}")


Continue_bidding = True
bids = {}
while Continue_bidding:
    name = input("What is your name: ")
    price = int(input("What is your bid: $ "))
    bids[name] = price
    while True:    
        Should_Continue = input("Are there any other bidders (Y, N): ")
        if Should_Continue in ["Y","N"]:
            break
        print("Invalid, Please enter Y or N")
    if Should_Continue == "N":
        Continue_bidding = False
        find_Highest_Bidder(bids)
    elif Should_Continue == "Y":
        print("\n" * 20)
        continue


# def find_Highest_Bidder(bidding_Dictionary):
#     winner = ""
#     Highest_Bid = 0
#     for bidder in bidding_Dictionary:
#         bid = bidding_Dictionary[bidder]
#         if bid > Highest_Bid:
#             Highest_Bid = bid
#             winner = bidder
#     print(f"The winner is {winner} with a bid of: ${Highest_Bid}")

# Continue_bidding = True
# bids = {}

# while Continue_bidding:
#     name = input("What is your name: ")
    
#     while True:
#         try:
#             price = int(input("What is your bid: $ "))
#             if price < 0:
#                 print("Bid amount must be a positive number.")
#             else:
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

#     bids[name] = price    

#     while True:
#         Should_Continue = input("Are there any other bidders? (Y/N): ").strip().upper()
#         if Should_Continue in ["Y", "N"]:
#             break
#         print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

#     if Should_Continue == "N":
#         Continue_bidding = False
#         find_Highest_Bidder(bids)
#     elif Should_Continue == "Y":
#         print("\n" * 20)

       


