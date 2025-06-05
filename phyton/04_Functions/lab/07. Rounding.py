def round_input_numbers(numbers: str):
    numbers_list = numbers.split(" ")
    numbers_list_as_int = [float(num) for num in numbers_list]
    return_numbers_list = [round(number) for number in numbers_list_as_int]
    return return_numbers_list


numbers = input()

print(round_input_numbers(numbers))
