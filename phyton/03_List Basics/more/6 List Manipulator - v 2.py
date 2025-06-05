initial_list = input().split(" ")

list_integer = list(map(int, initial_list))

command = input()
while command != "end":
    current_command = command.split(" ")

    if current_command[0] == "exchange":
        if len(list_integer) > int(current_command[1]) >= 0:
            list_one = []
            list_two = []
            for index_one in range(0, int(current_command[1]) + 1):
                list_one.append(list_integer[index_one])
            for index_two in range(int(current_command[1]) + 1, len(list_integer)):
                list_two.append(list_integer[index_two])
            list_integer = list_two + list_one
        else:
            print("Invalid index")

    elif current_command[0] == "max":
        if current_command[1] == "even":
            even_num_max = []
            for num_max_even in list_integer:
                if num_max_even % 2 == 0:
                    even_num_max.append(num_max_even)
            if not even_num_max:
                print("No matches")
            else:
                max_even_num = max(even_num_max)
                for max_integer_even in range(len(list_integer) - 1, -1, -1):
                    if list_integer[max_integer_even] == max_even_num:
                        print(max_integer_even)
                        break
        elif current_command[1] == "odd":
            odd_num_max = []
            for num_max_odd in list_integer:
                if num_max_odd % 2 != 0:
                    odd_num_max.append(num_max_odd)
            if not odd_num_max:
                print("No matches")
            else:
                max_odd_num = max(odd_num_max)
                for max_integer_odd in range(len(list_integer) - 1, -1, -1):
                    if list_integer[max_integer_odd] == max_odd_num:
                        print(max_integer_odd)
                        break
    elif current_command[0] == "min":
        if current_command[1] == "even":
            even_num_min = []
            for num_min_even in list_integer:
                if num_min_even % 2 == 0:
                    even_num_min.append(num_min_even)
            if not even_num_min:
                print("No matches")
            else:
                min_even_num = min(even_num_min)
                for min_integer_even in range(len(list_integer) - 1, -1, -1):
                    if list_integer[min_integer_even] == min_even_num:
                        print(min_integer_even)
                        break
        elif current_command[1] == "odd":
            odd_num_min = []
            for num_min_odd in list_integer:
                if num_min_odd % 2 != 0:
                    odd_num_min.append(num_min_odd)
            if not odd_num_min:
                print("No matches")
            else:
                min_odd_num = min(odd_num_min)
                for min_integer_odd in range(len(list_integer) - 1, -1, -1):
                    if list_integer[min_integer_odd] == min_odd_num:
                        print(min_integer_odd)
                        break
    elif current_command[0] == "first":
        counter = int(current_command[1])
        if counter > len(list_integer):
            print("Invalid count")
        else:
            if current_command[2] == "even":
                even_num_first = []
                for num_first_even in list_integer:
                    if num_first_even % 2 == 0:
                        even_num_first.append(num_first_even)
                        counter -= 1
                        if counter == 0:
                            break
                if not even_num_first:
                    print("[]")
                else:
                    print(even_num_first)
            elif current_command[2] == "odd":
                odd_num_first = []
                for num_first_odd in list_integer:
                    if num_first_odd % 2 != 0:
                        odd_num_first.append(num_first_odd)
                        counter -= 1
                        if counter == 0:
                            break
                if not odd_num_first:
                    print("[]")
                else:
                    print(odd_num_first)
    elif current_command[0] == "last":
        counter = int(current_command[1])
        if counter > len(list_integer):
            print("Invalid count")
        else:
            if current_command[2] == "even":
                even_num_last = []
                for last_num_even in range(len(list_integer) - 1, -1, -1):
                    if list_integer[last_num_even] % 2 == 0:
                        even_num_last.insert(0, list_integer[last_num_even])
                        counter -= 1
                        if counter == 0:
                            break
                if not even_num_last:
                    print("[]")
                else:
                    print(even_num_last)
            elif current_command[2] == "odd":
                odd_num_last = []
                for last_num_odd in range(len(list_integer) - 1, -1, -1):
                    if list_integer[last_num_odd] % 2 != 0:
                        odd_num_last.insert(0, list_integer[last_num_odd])
                        counter -= 1
                        if counter == 0:
                            break
                if not odd_num_last:
                    print("[]")
                else:
                    print(odd_num_last)
    command = input()

print(list_integer)