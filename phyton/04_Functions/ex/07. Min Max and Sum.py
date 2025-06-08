def min_value(sequence_of_numbers: list) -> int:
    return min(sequence_of_numbers)


def max_value(sequence_of_numbers: list) -> int:
    return max(sequence_of_numbers)


def sum_value(sequence_of_numbers: list) -> int:
    return sum(sequence_of_numbers)


input_numbers = input()
sequence_of_numbers = input_numbers.split(" ")
sequence_of_numbers_list = [int(d) for d in sequence_of_numbers]
print(f"The minimum number is {min_value(sequence_of_numbers_list)}")
print(f"The maximum number is {max_value(sequence_of_numbers_list)}")
print(f"The sum number is: {sum_value(sequence_of_numbers_list)}")
