sequence = [int(num) for num in input().split(" ")]

command = input()

while command != "end":
    command_list = command.split(" ")
    if command_list[0] == "swap":
        sequence[int(command_list[1])], sequence[int(command_list[2])] = sequence[int(command_list[2])], sequence[int(command_list[1])]
    elif command_list[0] == "multiply":
        sequence[int(command_list[1])] = sequence[int(command_list[1])] * sequence[int(command_list[2])]
    elif command_list[0] == "decrease":
        sequence = [(num-1) for num in sequence]

    command = input()

print(", ".join([str(num) for num in sequence]))
