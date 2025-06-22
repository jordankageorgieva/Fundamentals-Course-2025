commands = input()

message = []
while commands != 'end':
    commands = commands.split(" ")
    if commands[0] == 'Chat':
        msg = commands[1]
        message.append(msg)
        # print(message)
    elif commands[0] == 'Delete':
        msg = commands[1]
        if msg in message:
            index = message.index(msg)
            message.pop(index)
        # print(message)
    elif commands[0] == 'Edit':
        msg = commands[1]
        new_msg = commands[2]
        index = message.index(msg)
        if msg in message:
            message[index] = new_msg
        # print(message)
    elif commands[0] == 'Pin':
        msg = commands[1]
        if msg in message:
            index = message.index(msg)
            message.pop(index)
            message.append(msg)
        # print(message)
    elif commands[0] == 'Spam':
        for index in range(1, len(commands)):
            message.append(commands[index])
        # print(message)
    commands = input()

for index in range(len(message)):
    print(message[index])