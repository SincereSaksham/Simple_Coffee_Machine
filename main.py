from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


cf = CoffeeMaker()
menu = Menu()
mm = MoneyMachine()


def main():
    while True:
        options = menu.get_items()
        choice = input(f"Enter your choice: {options} ")
        if choice == "report":
            cf.report()
            mm.report()
        elif choice == "espresso":
            drink = menu.find_drink(choice)
            flag = cf.is_resource_sufficient(drink)
            if flag:
                if mm.make_payment(drink.cost):
                    cf.make_coffee(drink)

        elif choice == "latte":
            drink = menu.find_drink(choice)
            flag = cf.is_resource_sufficient(drink)
            if flag == True:
                if mm.make_payment(drink.cost):
                    cf.make_coffee(drink)

        elif choice == "cappuccino":
            drink = menu.find_drink(choice)
            flag = cf.is_resource_sufficient(drink)
            if flag:
                if mm.make_payment(drink.cost):
                    cf.make_coffee(drink)
        else:
            break


main()
