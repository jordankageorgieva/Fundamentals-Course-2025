special_numbers = [int(number) for number in input().split(" ")]
number_remove = int(input())

# sort the numbers
special_numbers_sorted = special_numbers.copy()
special_numbers_sorted.sort(reverse=True)
# print(special_numbers_sorted)

for index in range(0, number_remove):
    elemnt = special_numbers_sorted.pop()
    special_numbers.remove(elemnt)

output = ', '.join(str(num) for num in special_numbers)
print(output)