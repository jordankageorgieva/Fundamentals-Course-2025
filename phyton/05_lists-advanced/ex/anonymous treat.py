import math
input_data = input().split(" ")

command = input()
while command != '3:1':
    data_command = command.split(" ")
    print(input_data)
    if data_command[0] == 'merge':
        # begin = int(data_command[1])
        # end = int(data_command[2])
        begin = max(0, min(int(data_command[1]), len(input_data)))
        end = max(begin, min(int(data_command[2]), len(input_data)))
        print(begin)
        print(end)
        # merge data to be in list form
        if begin != end :
            extract_data = [''.join(input_data[begin: end])]
            #  create new input_data
            input_data = input_data[:begin] + extract_data + input_data[end:]
    elif data_command[0] == 'divide':
        index = int(data_command[1])
        partitions = int(data_command[2])
    #     get element to divide
        element = input_data.pop(index)
        step = len(element) // partitions
        if len(element) % partitions == 0:
    #         equals part
            element_to_partitions = [element[i: i + step] for i in range(0, len(element)-1, step)]
    #         insert
            input_data = input_data[:index] + element_to_partitions + input_data[index:]
        else:
            step = math.floor(len(element) / partitions)
            begin_lst = input_data[:index]
            end_lst = input_data[index + 1:]
            j = 0
            for i in range(0, partitions - 1):
                begin_lst.append(element[j: j + step])
                j += step
            else:
                begin_lst.append(element[index:])
            input_data = begin_lst + end_lst
    command = input()


print(' '.join(input_data))