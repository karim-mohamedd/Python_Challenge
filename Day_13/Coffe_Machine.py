from Menu import MENU
from Resources_for_day import resources

profit = 0
# Checking the resources
def is_enough(order_ingredients):
    enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            enough = False
    return enough

def coins():
    print("Please insert the coins ")
    total = int(input("How many Quarters: ")) * 0.25
    total += int(input("How many dimes: "))   * 0.10
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total

def Transaction(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your {change} change")
        global profit 
        profit += drink_cost
        return True
    else:
        print("sorry! that's not enough money😒. Money refunded ")
        return False

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}☕")


def coffee_machine():
    is_on = True
    while is_on:
        coffee = input("What would you like? (espresso/latte/cappuccino):​ " )
        if coffee == "off":
            is_on = False
            print("Thank You")
        elif coffee == "report":
            print(f"water: {resources['water']}ml")
            print(f"milk: {resources['milk']}ml")
            print(f"coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[coffee]
            if is_enough(drink["ingredients"]):
                payment = coins()
                if Transaction(payment, drink['cost']):
                    make_coffee(coffee, drink["ingredients"])

coffee_machine()       