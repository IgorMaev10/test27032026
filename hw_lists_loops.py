numbers = [-8, 16, 1.5, 3, 5, 0]
biggest_number = max(numbers)
print(biggest_number)
smallest_number = min(numbers)
print(smallest_number)
summed_numbers = sum(numbers)
print(summed_numbers)

grades = [1, 12, 11, 10, 7, 6]
average = sum(grades) / len(grades)
print(average)
for grade in grades:
    if grade > average:
        print(grade)
