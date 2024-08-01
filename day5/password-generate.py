import random
no=['1','2','3','4','5','6','7','8','9','0']
spcl=['@','#','$',"%",'*','?']
print("!!welcome to password generator!!\n")
name=input("your name: ")
length=int(input("no of letters u want in your pass from your name: "))
spclLength=int(input("no of spcl characters you want in your pass form this :"))
noLength=int(input("no of number you want in your pass form this: "))
passwordList=[]

for char in range(0,length):
    passwordList.append(random.choice(name))
for char in range(0,spclLength):
    passwordList.append(random.choice(spcl))
for char in range(0,noLength):
    passwordList.append(random.choice(no))
random.shuffle(passwordList)
#one brute method 
# password=""
# for i in passwordList:
#     password+=i
#using library fucnction
password=""
print(f"your password is {password.join(passwordList)}")

