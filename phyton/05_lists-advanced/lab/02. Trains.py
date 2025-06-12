wagons= int(input())
list_passangers =[0] * wagons

command_data = input()

while command_data != 'End':
    # unbox
    command_data_list = command_data.split(' ')
    if command_data_list[0] == 'add':
        list_passangers[-1] += int(command_data_list[1])
    elif command_data_list[0] == 'insert':
        list_passangers[int(command_data_list[1])] += int(command_data_list[2])
    elif command_data_list[0] == 'leave':
        list_passangers[int(command_data_list[1])] -= int(command_data_list[2])

    command_data = input()


print(list_passangers)