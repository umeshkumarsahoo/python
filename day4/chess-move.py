list1=["🤖",'🤖',"🤖"]
list2=["🤖","🤖","🤖"]
list3=["🤖","🤖","🤖"]
map=[list1,list2,list3]
print(f"{list1}\n{list2}\n{list3}")
a=int(input("enter the row to step in:"))-1
b=int(input("enter the column to step in:"))-1
map[a][b]="👾"
print(f"{list1}\n{list2}\n{list3}")
