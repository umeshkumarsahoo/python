import random
from game_data import data
from art import logo
from art import vs
main_data=data
main_logo=logo

def data_print(log):
    print(f"{log['name']},{log['description']},{log['country']}")

def check_ans(first,second):
    if first>second:
        return True
    else:
        return False

print (f"{logo}")
play=input("you want to play the game(y/n): ")
if play=='y':
    isContinue=True
    while isContinue:
            isScore=True
            score=0
            while isScore:
                    a=random.choice(main_data)
                    b=random.choice(main_data)
                    if a==b:
                        b=random.choice(main_data)
                    print(f"current score is {score}\n")
                    print("compare a:")
                    data_print(a)
                    print(f"{vs}")
                    print("compare b:")
                    data_print(b)
                    ans=input("who has more follower type (a/b): ")
                    if ans=='a':
                        if check_ans(a['follower_count'],b['follower_count']):
                            score+=1
                            isScore=True
                        else:
                            print(f"wrong guess!!. total score is {score}")
                            isScore=False
                            isEqual=False
                            cont=input("do you want to try again(y/n): ")
                            if cont=='y':
                                isContinue=True
                            else:
                                isContinue=False
                    elif ans=='b':
                        if check_ans(b['follower_count'],a['follower_count']):
                            score+=1
                            isScore=True
                        else:
                            print(f"wrong guess!!. total score is {score}")
                            isScore=False
                            isEqual=False
                            cont=input("do you want to try again(y/n): ")
                            if cont=='y':
                                isContinue=True
                            else:
                                isContinue=False
