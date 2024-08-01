import random
test_seed=random.random()
random.seed(test_seed)
names=input("enter your names separated by comma: ")
all=names.split(",")
print(f"the contributors are {all}")
randomStr=all[random.randint(0,len(all)-1)]
#we can use random.choice(all)
print(f"the person going to pay is {randomStr}")