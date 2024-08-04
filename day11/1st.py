import random
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_log=[]
compt_log=[]


def check(logs):
    sum=0
    for i in logs:
        sum+=i
    if sum>=21:
        return False
    else:
        return True

def check_score(log):
    print(f"score is {sum(log)}")
    print(f"your cards are {user_log}")


def check_winner(log1,log2):
    sum1=sum(log1)
    sum2=sum(log2)
    if sum1>sum2:
        print(f"user wins😎 with these cards{log1}and sum is{sum1}")
        print(f"computer LOSE🥺 with these cards{log2}and sum is {sum2}")
    elif sum1<sum2:
        print(f"user LOSE🥺 with these cards{log1}and sum is{sum1}")
        print(f"computer wins😎 with these cards{log2}and sum is {sum2}")
    else:
        print(f"user LOSE🥺 with these cards{log1}and sum is{sum1}")
        print(f"computer wins😎 with these cards{log2}and sum is {sum2}")
        print("draw")

isPlay=True
print(f"{logo}")
while isPlay:
    play=input("you want to play the game (y/n): ")
    if  play=='y':
        user_log.clear()
        compt_log.clear()
        user_log.append(random.choice(cards))
        user_log.append(random.choice(cards))
        check_score(user_log)
        compt_log.append(random.choice(cards))
        print(f"computer 1st card is {compt_log}")
        compt_log.append(random.choice(cards))
        if not check(user_log):
            print(f"you LOSE🥺..as you have cards {user_log}")
        elif not check(compt_log):
            print(f"you wins😎..as you compt cards {compt_log}")
        else:
            draw=True
            while draw==True:
                pick=input("you want to draw cards(y/n):")
                if pick=='y':
                    user_log.append(random.choice(cards))
                    check_score(user_log)
                    if not check(user_log):
                        print(f"you LOSE🥺..as you have cards {user_log} and sum of your card is {sum(user_log)}")
                        draw=False
                    else:
                        draw=True
                else:
                    check_winner(user_log,compt_log)
                    draw=False
    else:
        isPlay=False
