# it creates all string letter into a list
# numbers="goobhi"
# number=[i for i in numbers]
# print(number)

#can be changed and copied to another list
# numbers=[1,2,3]
# number=[n*2+1 for n in numbers]
# print(numbers)
# print(number)

#searching common strings from both file and creating a new list // list comprehension
with open("file1.txt") as file1:
    file_1=file1.readlines()
with open("file2.txt") as file2:
    file_2=file2.readlines()
common_list=[int(num) for num in file_1 if num in file_2]
print(common_list)
