n = int(input())
numbers = list()
filter_numbers = list()

for _ in range(n):
    data = int(input())
    numbers.append(data)

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filter_numbers.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filter_numbers.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filter_numbers.append(number)
elif command == "positive":
    for number in numbers:
        if number > 0:
            filter_numbers.append(number)

print(filter_numbers)