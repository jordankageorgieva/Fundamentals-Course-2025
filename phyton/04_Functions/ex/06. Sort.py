def sort(sequence_of_numbers: str) -> list:
    sequence_of_numbers = sequence_of_numbers.split(" ")
    sequence_of_numbers_list = [int(d) for d in sequence_of_numbers]
    sequence_of_numbers_list.sort()
    return sequence_of_numbers_list


input_numbers = input()
print(sort(input_numbers))