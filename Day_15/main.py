from coffee_maker import *
from menu import *
from money_machine import *


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} ? : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # notice that find drink method is returning MenuItem object if found, so drink var is MenuItem Object
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

