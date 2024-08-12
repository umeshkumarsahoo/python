# dictionary comprehension
import random
names=["alex","carla","joe","joseph","loo","glitch","caroline","umesh"]
student_score={student:random.randint(50,101) for student in names}
passed={student:score for (student,score) in student_score.items() if score >=80 }
print(student_score)
print(passed)
