import emoji
print("welcome to new treasure hunt \U0001f600")
start=input("do you want to play(y/n): ")
if start=="y":
    path=input("tell the path\nleft or right: ")
    if path=="left":
        print(f"welcome to riverside \U0001F929")
        leftPath=input("tell the no from below options\n1.use boat\n2.swim: ")
        if leftPath=="1":
            print("sadly you die \U0001FAE3")
        else:
            print("you crossed the river \U0001FAE5")
            treasure=input("tell the path\nleft or right: ")
            if treasure=="left":
                print("death!!\U0001FAE3")
            else:
                print("congratulationss!! \U0001F973\nyou find the treasure")
    else:
        print("welcoem to iceland!\U0001F976")
        leftPath=input("tell the no from below options\n1.use ski\n2.spikeboot: ")
        if leftPath=="2":
            print("sadly you die \U0001FAE3")
        else:
            print("you crossed the iceland \U0001FAE5")
            treasure=input("tell the path\nleft or right: ")
            if treasure=="left":
                print("death!!\U0001FAE3")
            else:
                print("congratulationss!! \U0001F973\nyou find the treasure")
else:
    print("thank you !!")
