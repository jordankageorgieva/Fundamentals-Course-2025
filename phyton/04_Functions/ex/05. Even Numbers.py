def even_numbers(sequence_of_numbers: str) -> list:
    sequence_of_numbers = sequence_of_numbers.split(" ")
    sequence_of_numbers_list = [int(d) for d in sequence_of_numbers]
    sequence_of_numbers_list = list(filter(lambda x: x % 2 == 0, sequence_of_numbers_list))
    return sequence_of_numbers_list


input_numbers = input()
print(even_numbers(input_numbers))
