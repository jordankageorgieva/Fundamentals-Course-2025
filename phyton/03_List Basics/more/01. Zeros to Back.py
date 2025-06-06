numbers = input()
numbers_split = numbers.split(",")
numbers_list = [int(num) for num in numbers_split]
# print(numbers_list)

zero_list = []
value_list = []
for index in range(len(numbers_list)):
    # print(numbers_list[index])
    if numbers_list[index] != 0:
        value_list.append(numbers_list[index])
    else:
        zero_list.append(numbers_list[index])

# print(value_list)
# print(zero_list)
print(value_list + zero_list)