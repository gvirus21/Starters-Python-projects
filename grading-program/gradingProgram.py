student_scores={
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
def grade_func(score):
    if 100>=score>=91:
        grade="Outstanding"
    elif 90>=score>=81:
        grade="Exceeds Expectations"
    elif 80>=score>=71:
        grade="Acceptable"
    else: grade="fail"
    return grade
student_grade={}

for student in student_scores:
    score=student_scores[student]
    student_grade[student]=grade_func(score)
print(student_grade)



