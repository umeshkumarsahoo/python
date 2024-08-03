print('''
                  _   _
                 | | (_)
  __ _ _   _  ___| |_ _  ___  _ __
 / _` | | | |/ __| __| |/ _ \| '_ \
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|
 ''')

print("\nwelcome!!")

#inputs
isContinue=True

def find_max(user):
    max=user[0]["bid"]
    max_bid=user[0]
    for i in user:
        if max<=i["bid"]:
            max=i["bid"]
            max_bid=i
    return max_bid




while isContinue:
    user_log=[]
    name=input("please enter your name: ")
    bid_amount=int(input("please enter your bid amount: "))
    name_log={
        "name":name,
        "bid":bid_amount,
    }
    user_log.append(name_log)
    ctn= input("any other one here to bid (y/n): ")
    if ctn=="y":
        isContinue=True
    else:
        isContinue=False
        max=find_max(user_log)
        print(f"maximum bid is done by {max["name"]} and the bid amount is {max["bid"]}")
