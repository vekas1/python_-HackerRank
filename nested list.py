students = []
n = int(input())

for i in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = []
for student in students:
    grades.append(student[1])

unique_grades = sorted(set(grades))
second_lowest_grade = unique_grades[1]

names = []
for student in students:
    if student[1] == second_lowest_grade:
        names.append(student[0])

names.sort()

for name in names:
    print(name)
