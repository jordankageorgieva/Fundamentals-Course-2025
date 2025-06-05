data_input = input()
# data normalization
data_list = [int(data) for data in data_input.split(' ')]
# print(data_list)

# list manipulation
command = input()


def exchange():
    global index, data_list
    # data split
    exchange, index = command.split(' ')
    index = int(index)
    if 0 <= index < len(data_list):
        list_1 = data_list[:index]
        list_2 = data_list[index:]
        data_list = list_2 + list_1
        print(data_list)
    else:
        print("Invalid index")


def max_data_extraction():
    global even, even_numbers, index, odd_numbers
    # data split
    max_, even = command.split(' ')
    if even == 'even':
        even_numbers = [int(number) for number in data_list if number % 2 == 0]
        if even_numbers:
            max_number = max(even_numbers)
            index = data_list.index(max_number)
            print(index)
        else:
            print("No matches")
    elif even == 'odd':
        odd_numbers = [number for number in data_list if number % 2 != 0]
        if odd_numbers:
            max_odd = max(odd_numbers)
            index = data_list.index(max_odd)
            print(index)
        else:
            print("No matches")


def min_data_extraction():
    global even, even_numbers, index, odd_numbers
    # data split
    min_, even = command.split(' ')
    if even == 'even':
        even_numbers = [int(number) for number in data_list if number % 2 == 0]
        if even_numbers:
            min_number = min(even_numbers)
            index = data_list.index(min_number)
            print(index)
        else:
            print("No matches")
    elif even == 'odd':
        odd_numbers = [number for number in data_list if number % 2 != 0]
        if odd_numbers:
            min_odd = max(odd_numbers)
            index = data_list.index(min_odd)
            print(index)
        else:
            print("No matches")


while command != 'end':
    # print(command)
    # data
    if 'exchange' in command:
        exchange()
    elif 'max' in command:
        max_data_extraction()
    elif 'min' in command:
        min_data_extraction()
    elif 'first' in command:
        # data split
        first, count, even = command.split(' ')
        count = int(count)

        if even == 'even':
            even_numbers = [int(number) for number in data_list if number % 2 == 0]
            if count > len(even_numbers):
                print("Invalid count")
            else:
                #print count even numbers
                list_even_numbers = even_numbers[:count]
                print(list_even_numbers)
        elif even == 'odd':
            odd_numbers = [int(number) for number in data_list if number % 2 != 0]
            if count > len(odd_numbers):
                print("Invalid count")
            else:
                 # print count even numbers
                list_odd_numbers = odd_numbers[:count]
                print(list_odd_numbers)

    elif 'last' in command:
        # data split
        last, count, even = command.split(' ')
        count = int(count)

        if even == 'even':
            even_numbers = [int(number) for number in data_list if number % 2 == 0]
            if count > len(even_numbers):
                print("Invalid count")
            else:
                 #print count even numbers
                list_even_numbers = even_numbers[count:]
                print(list_even_numbers)

        elif even == 'odd':
            odd_numbers = [int(number) for number in data_list if number % 2 != 0]
            if count > len(odd_numbers):
                print("Invalid count")
            else:
                # print count even numbers
                list_odd_numbers = odd_numbers[count:]
                print(list_odd_numbers )
    command = input()
