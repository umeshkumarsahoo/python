import pandas
student_dict={
    "student":["jamie","oliver","umu"],
    "scores":[45,35,90]
}
data=pandas.DataFrame(student_dict)
print(data)
for (index,row) in data.iterrows():
    print(row.scores)
