
print('''

█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄''')

print("welcome!!(„• ֊ •„)")
number=float()
#operation
def operation(first,second,operator):
    """
    it carries out the operation taking operator and user_data
    """
    if operator=='+':
        return round(first+second,2)
    elif operator=='-':
        return round(first-second,2)
    elif operator=='*':
        return round(first*second,2)
    elif operator=='/':
        return round(first/second,2)
    else:
        return False



#inputs
isContinue=True
while isContinue:
    if not number:
        first_var=float(input("write the number: "))
        operator=input("write the operator from this \n1. +\n2. - \n3. *\n4. /\n")
        second_var=float(input("write the number: "))
        ans=operation(first_var,second_var,operator)
        if not ans:
            print("invalid operator")
        else:
            print(f"\n{first_var}{operator}{second_var}={ans}")
    else:
        first_var=number
        operator=input("write the operator from this \n1. +\n2. - \n3. *\n4. /\n")
        second_var=float(input("write the number: "))
        ans=operation(first_var,second_var,operator)
        if not ans:
            print("invalid operator")
        else:
            print(f"\n{first_var}{operator}{second_var}={ans}")
    a=input("do you want to :\ncontinue with previous ans(y)\ncontinue with new inputs(n)\nyou want to cancel the operation(ac) ")
    if a=='y':
        number=ans
        isContinue=True
    elif a=='n':
        number=float()
        isContinue=True
    else:
        isContinue=False
