from data import MENU
initial={
    "milk":200,
    "water":300,
    "coffee":100,
}

def coin_calc(q,n,d,p,name):
    q=q*0.25
    n=n*0.05
    d=d*0.1
    p=p*0.01
    total=q+n+d+p
    if name["cost"]==total:
        return True
    elif name["cost"]<total:
        print(f"here is your change ${round(total-name["cost"],2)}")
        return True
    else:
        print("insufficient coin. your coins are refunded")
        return False

def check_ingredients(name):
    i_wat=initial["water"]
    i_cof=initial["coffee"]
    i_mil=initial["milk"]
    wat=name["water"]
    cof=name["coffee"]
    mil=name["milk"]
    if initial["water"]>=wat and  initial["coffee"]>=cof and initial["milk"]>=mil:
        initial["water"]=i_wat-wat
        initial["milk"]=i_mil-mil
        initial["coffee"]=i_cof-cof
        return True
    else:
        print("not enough ingredients..your coins are refunded😞")
        return False

def cont():
    again=input("do you want to buy again(y/n): ")
    if again=='y':
        return True
    else:
        return False

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
        user=input("what you want?\nespresso=$1.5\nlatte=$2.5\ncappuccino=$3.0\n-> ")
        if user=='espresso':
            print("insert some coins: ")
            q=float(input("how many quarters: "))
            n=float(input("how many nickel: "))
            d=float(input("how many dimes: "))
            p=float(input("how many pennies: "))
            check= coin_calc(q,n,d,p,MENU["espresso"])
            if check==True:
                if check_ingredients(MENU["espresso"]["ingredients"]):
                    print("here is your coffee:☕️")
                    isContinue=cont()
                else:
                    isContinue=cont()
            else:
                isContinue=cont()
        elif user=='latte':
            print("insert some coins: ")
            q=float(input("how many quarters: "))
            n=float(input("how many nickel: "))
            d=float(input("how many dimes: "))
            p=float(input("how many pennies: "))
            check= coin_calc(q,n,d,p,MENU["latte"])
            if check==True:
                if check_ingredients(MENU["latte"]["ingredients"]):
                    print("here is your latte:🧋")
                    isContinue=cont()
                else:
                    isContinue=cont()
            else:
                isContinue=cont()
        elif user=='cappuccino':
            print("insert some coins: ")
            q=float(input("how many quarters: "))
            n=float(input("how many nickel: "))
            d=float(input("how many dimes: "))
            p=float(input("how many pennies: "))
            check= coin_calc(q,n,d,p,MENU["cappuccino"])
            if check==True:
                if check_ingredients(MENU["cappuccino"]["ingredients"]):
                    print("here is your cappuccino:🍹")
                    isContinue=cont()
                else:
                    isContinue=cont()
            else:
                isContinue=cont()
        elif user=='report':
            print(f"water:{initial["water"]}ml\nmilk:{initial["milk"]}ml\ncoffee:{initial["coffee"]}gm\n")
        else:
            print("not in the menu!!😁")
