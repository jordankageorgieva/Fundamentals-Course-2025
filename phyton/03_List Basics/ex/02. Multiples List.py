factor = int(input("Enter the factor: "))
count = int(input("Enter how many multiples: "))

list_count_to_factor = []
for number in range(1, count + 1):
    list_count_to_factor.append(number * factor)


# list_count_to_factor = [factor * i for i in range(1, count + 1)]

print(list_count_to_factor)