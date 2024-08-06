from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_money=MoneyMachine()
my_coffee=CoffeeMaker()
my_menu=Menu()


print('''
     )))
    (((
  +-----+
  |     |]
  `-----'   caffe terrace!!
___________
`---------'

      ''')

print("!welcome!")

start=input("you want to start the coffee machine(y/n): ")
isContinue=True
if start=='y':
    while isContinue:
        options=my_menu.get_items()
        choice=input(f"what you  want {options}: ")
        if choice=='off':
            isContinue=False
        elif choice=='report':
            my_coffee.report()
            my_money.report()
        else:
            drink=my_menu.find_drink(choice)
            if my_coffee.is_resource_sufficient(drink) and my_money.make_payment(drink.cost):
                my_coffee.make_coffee(drink)
