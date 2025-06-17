username = input()
command = input()
while command != 'Registration':
    command_lst = command.split(" ")
    if command_lst[0] == 'Letters':
        # "Letters {Lower/Upper}"
        if command_lst[1] == 'Lower':
            username = username.lower()
        else:
            username = username.upper()
        print(username)
    elif command_lst[0] == 'Reverse':
        # Reverse {startIndex} {endIndex}
        startIndex = int(command_lst[1])
        endIndex = int(command_lst[2])
        if 0 <= startIndex <= endIndex < len(username):
            sub_username = username[startIndex: endIndex +1]
            print("".join(sub_username[::-1]))
    elif command_lst[0] == 'Substring':
        # Substring {substring}
        if command_lst[1] in username:
            username = username.replace(command_lst[1], "")
            print(f"{username}")
        else:
            print(f"The username {username} doesn't contain {command_lst[1]}.")
    elif command_lst[0] == "Replace":
        #     Replace {char}
        username = username.replace(command_lst[1], "-")
        print(username)
    elif command_lst[0] == "IsValid":
        # IsValid {char}
        if command_lst[1] in username:
            print("Valid username.")
        else:
            print(f"{command_lst[1]} must be contained in your username.")
    command = input()