####
####write a code take dict of three student name and their marks in 3 exams
# and the funcuthion retrun list of student name that
# the average of their exams markes is >=78 and use formatting to formate  the output





def student_info(students):
   return [student for student, marks in students.items() if sum(marks)/len(marks)>=78 ]

student_marks={"reem":[90,95,100],
      "abdo":[95,99,87],
      "omer":[50,30,77]}
print("The List Of Student Name That Get High Marks",student_info(student_marks))
high_scores=student_info(student_marks)
if high_scores:
    print("Hight Scores With Average >= 78")
    for student in high_scores:
        average_marks=sum(student_marks[student])/len(student_marks[student])
        print(f"{student}: Average Mark = {average_marks:.2f}")
    else:
        print("_______________________________________")