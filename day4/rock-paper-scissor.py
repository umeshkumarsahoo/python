import random
test_seed=random.randint(1,100)
random.seed(test_seed)
p="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
q="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
r="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list=['rock','paper',"scissor"]
print("welcome to the game")
a=input("eneter your choice \n>rock\n>paper\n>scissor \n:")
print("your choice: ")
if a=='rock':
    print(p)
elif a=='paper':
    print(q)
else:
    print(r)
result=random.choice(list)
print("bot choice: ")
if result=='rock':
    print(p)
elif result=='paper':
    print(q)
else:
    print(r)
if a=='rock':
    if result=='rock':
        print("draw")
    elif result=='paper':
        print("you loose!")
    else:
        print("you win")
elif a=='paper':
    if result=='rock':
        print("you win!!")
    elif result=='paper':
        print("draw!")
    else:
        print("you loose")
else:
    if result=='rock':
        print("you loose")
    elif result=='paper':
        print("you win!")
    else:
        print("you draw")

    

