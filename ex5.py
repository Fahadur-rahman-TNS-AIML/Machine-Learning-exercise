students = {
    "Arun": 95,
    "Rahul": 82,
    "John": 68,
    "David": 55,
    "Sam": 91,
    "Peter": 73
}

topper = ""
lowest = ""
total = 0

for name in students:
    total = total + students[name]

    if topper == "":
        topper = name
    elif students[name] > students[topper]:
        topper = name

    if lowest == "":
        lowest = name
    elif students[name] < students[lowest]:
        lowest = name

average = total / 6

print("Topper:", topper)
print("Lowest scorer:", lowest)
print("Average:", average)

print("Grades:")

for name in students:

    mark = students[name]

    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "D"

    print(name, mark, grade)
