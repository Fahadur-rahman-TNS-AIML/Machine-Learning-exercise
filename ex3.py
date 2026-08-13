employee1 = ("E101", "John", 45000)
employee2 = ("E102", "David", 52000)
employee3 = ("E103", "Rahul", 38000)
employee4 = ("E104", "Arun", 60000)
employee5 = ("E105", "Peter", 48000)
employee6 = ("E106", "Sam", 55000)

employees = [employee1, employee2, employee3, employee4, employee5, employee6]

highest = employees[0]
lowest = employees[0]

total = 0

for employee in employees:
    total = total + employee[2]

    if employee[2] > highest[2]:
        highest = employee

    if employee[2] < lowest[2]:
        lowest = employee

average = total / 6

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees above average:")

for employee in employees:
    if employee[2] > average:
        print(employee)
