numbers_sequence = list(map(int, input().split(", ")))

max_number = max(numbers_sequence)
max_number_groups = (max_number - 1) // 10 + 1
# print(max_number_groups)
# create groups

#  we could work with the max possible data list - found data will be removed and add to the new data list

for group in range (1, max_number_groups + 1):
    group_numbers = []
    index = len(numbers_sequence)
    while index >= 1:
        # print(group_numbers)
        # print(f"index + {index}")
        # print(numbers_sequence[index -1])
        if (group -1) * 10 < numbers_sequence[index -1]  <= group * 10:
            group_numbers.append(numbers_sequence[index -1])
            numbers_sequence.remove(numbers_sequence[index -1])
        index -= 1
    group_numbers.reverse()
    print(f"Group of {group * 10}'s: {group_numbers}")