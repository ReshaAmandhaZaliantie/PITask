import math

numbers = []
while True:
    number = int(input("Enter a number (-1 to stop): "))
    if number == -1:
        break
    numbers.append(number)

sum_of_numbers = sum(numbers)
print("Sum of numbers:", sum_of_numbers)