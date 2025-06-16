import math

strings_lst = input().split(" ")
command = input()

out_lst = []
while command != "3:1":
    command_lst = command.split(" ")
    # print(' '.join(strings_lst))
    if command_lst[0] == 'merge':
        begin = int(command_lst[1])
        end = int(command_lst[2])
        # if begin > end:
        #     continue
        if begin < 0:
            begin = 0
        if end > len(strings_lst):
            end = len(strings_lst)
        # str_new = strings_lst[begin:end]
        str_new = strings_lst[begin:end +1]
        str_new = "".join(str_new)
        # out_lst.append(str_new)
        # print(str_new)
        if str_new != '':
            if begin == 0 :
                strings_lst = [str_new] + strings_lst[end +1:]
            else:
                strings_lst = strings_lst[:begin] + [str_new] + strings_lst[end +1:]
    elif command_lst[0] == 'divide':
        index = int(command_lst[1])
        partitions = int(command_lst[2])
        element = strings_lst[index]
        del strings_lst[index]
        if partitions > 0:
            if len(element) % partitions == 0:
                step = int(len(element) / partitions)
                begin_lst = strings_lst[:index]
                end_lst = strings_lst[index + 1:]
                for index in range(0, len(element), step):
                    begin_lst.append(element[index: index + step])
                strings_lst = begin_lst + end_lst

            else:
                step = math.floor(len(element) / partitions)
                begin_lst = strings_lst[:index]
                end_lst = strings_lst[index + 1:]
                index = 0
                for i in range(0, partitions-1):
                    begin_lst.append(element[index: index + step])
                    index += step
                else:
                    begin_lst.append(element[index:])
                strings_lst = begin_lst + end_lst

    command = input()



print(' '.join(strings_lst))