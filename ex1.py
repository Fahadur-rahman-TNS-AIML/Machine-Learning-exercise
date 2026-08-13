marks = [78, 45, 89, 92, 56, 78, 65, 89, 100, 45, 72, 84, 91, 56, 88]

unique = []

for mark in marks:
    if mark not in unique:
        unique.append(mark)

print("Unique marks:", unique)

unique.sort(reverse=True)

print("Descending order:", unique)

print("Top 3 marks:", unique[0], unique[1], unique[2])

total = 0

for mark in unique:
    total = total + mark

average = total / len(unique)

print("Average:", average)

count = 0

for mark in marks:
    if mark > average:
        count = count + 1

print("Students above average:", count)
