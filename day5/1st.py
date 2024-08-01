student=input("enter the student heights , and give comma:\n").split(",")
sum=count=0
for n in student:
    sum+=float(n)
    count+=1
avg=round(sum/count,2)
print(f"average is {avg}")


