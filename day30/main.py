# try:
#     file=open("a.txt")
# except:
#     file=open("a.txt","w")
# finally:
#     file.close()
# fruits=["apple","banana"]
# def make_pie(index):
#         try:
#             fruit=fruits[index]
#         except IndexError:
#             print("fruit pie have index error")
#         else:
#             print(fruit+"pie")
# make_pie(4)
import json
facebook_posts=[
    {'likes':0,'comments':21},
    {'likes':30,'comments':2},
    {'likes':90,'comments':2,'shares':80},
    {'comments':10,'shares':80}
]
total_likes=0

for post in facebook_posts:
    try:
        new_data={
        'likes':post['likes'],
        'comments':post['comments'],
        'shares':post['shares']
    }
        with open("a.json","w") as data:
            json.dump(new_data,data,indent=4)#to write in json file
        total_likes+=post['likes']
    except KeyError:
        pass


print(f"total_likes are {total_likes}")
