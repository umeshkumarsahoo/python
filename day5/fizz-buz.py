p=int(input("the number uptowhich you want to continue the game"))+1
for i in range(1,p):
    if i%5==0 and i%3==0:
        print("fizz-buzz\n")
    elif i%3==0:
        print("fizz\n")
    elif i%5==0:
        print("buzz\n")
    else:
        print(f"{i}\n")
