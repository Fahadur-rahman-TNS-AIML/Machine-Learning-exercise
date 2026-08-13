numbers = [1, 2, 3, 4, 5]

k = int(input("Enter k: "))

for i in range(k):
    last = numbers[-1]

    for j in range(len(numbers) - 1, 0, -1):
        numbers[j] = numbers[j - 1]

    numbers[0] = last

print("Rotated list:", numbers)

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)

sum_value = numbers[0] + numbers[-1]

print("Sum of first and last:", sum_value)
