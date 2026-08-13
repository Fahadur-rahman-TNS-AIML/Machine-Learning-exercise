student1 = (101, "Arun", "CSE", 8.5)
student2 = (102, "Rahul", "ECE", 7.8)
student3 = (103, "John", "CSE", 9.2)
student4 = (104, "David", "IT", 8.1)
student5 = (105, "Sam", "CSE", 9.5)
student6 = (106, "Peter", "MECH", 7.5)

students = [student1, student2, student3, student4, student5, student6]

highest = students[0]
total = 0

for student in students:
    total = total + student[3]

    if student[3] > highest[3]:
        highest = student

print("Highest CGPA student:", highest)

print("CSE Students:")

for student in students:
    if student[2] == "CSE":
        print(student)

average = total / 6

print("Average CGPA:", average)

students.sort(key=lambda x: x[3], reverse=True)

print("Students by CGPA:")

for student in students:
    print(student)
