print("----------------- Welcome to tip calculator----------------")
bill = float(input("What was the total bill $ "))
tip = float(input("What percentage to tip "))
people = int(input("how many people to spilt the bill with "))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")
