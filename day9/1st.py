student_mark={
    "harry":81,
    "style":92,
    "lomu":32,
    "chomu":89
}
student_grade={}
for name in student_mark:
    if student_mark[name]<30:
        student_grade[name]= "f-grade"
    elif student_mark[name]<40:
        student_grade[name]="e-grade"
    elif student_mark[name]<50:
        student_grade[name]="d-grade"
    elif student_mark[name]<60:
        student_grade[name]="c-grade"
    elif student_mark[name]<70:
        student_grade[name]="b-grade"
    elif student_mark[name]<80:
        student_grade[name]="a-grade"
    else:
        student_grade[name]="o*-garde"
print(f"{student_grade}")
