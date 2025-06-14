numbers_sequence = list(map(int, input().split(", ")))

max_number = max(numbers_sequence)
max_number_groups = (max_number - 1) // 10 + 1

for group in range(1, max_number_groups + 1):
    upper = group * 10
    lower = upper - 10
    group_numbers = [num for num in numbers_sequence if lower < num <= upper]
    print(f"Group of {upper}'s: {sorted(group_numbers)}")
    # print(f"Group of {upper}'s: ")