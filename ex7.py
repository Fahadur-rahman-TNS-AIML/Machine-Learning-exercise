club_a = {"Arun", "Rahul", "John", "David"}
club_b = {"Rahul", "John", "Sam", "Peter"}
club_c = {"John", "Sam", "David", "Alex"}

common = club_a & club_b & club_c

print("Common to all clubs:", common)

all_students = club_a | club_b | club_c

print("Students belonging to exactly one club:")

for student in all_students:

    count = 0

    if student in club_a:
        count = count + 1

    if student in club_b:
        count = count + 1

    if student in club_c:
        count = count + 1

    if count == 1:
        print(student)

print("Students belonging to at least two clubs:")

for student in all_students:

    count = 0

    if student in club_a:
        count = count + 1

    if student in club_b:
        count = count + 1

    if student in club_c:
        count = count + 1

    if count >= 2:
        print(student)

print("Total unique students:", len(all_students))
