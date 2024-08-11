import csv
import pandas as pd
# with open("weather.csv") as data:
#     data_file=data.readlines()
#     print(data_file)
# with open("weather.csv") as data_file:
#     data=csv.reader(data_file)
#     for row in data:
#         if row[1]!="temp:":p
#             print(row[1])
# with open("weather.csv") as data:
#     data_list=pd.read_csv(data)
#     print(data_list)
#     print(round(data_list["temp:"].mean()))
#     print(data_list["temp:"].max())
squirrels=pd.read_csv("squirrel.csv")
Grey_color=len(squirrels[squirrels["Primary Fur Color"]=="Gray"])
Cinnamon_color=len(squirrels[squirrels["Primary Fur Color"]=="Cinnamon"])
data_dict={
        "fur_color":["Grey :","Cinnamon :"],
        "count":[Grey_color,Cinnamon_color]
    }
df=pd.DataFrame(data_dict)
df.to_csv("squirrel-color.csv")
