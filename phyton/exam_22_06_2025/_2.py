usernames = [name for name in input().split(", ")]
command = input()

blacklisted_names_count = 0
lost_names_count = 0
while command != 'Report':
    command_lst = command.split(" ")
    if command_lst[0] == 'Blacklist':
        name = command_lst[1]
        if name in usernames:
            index = usernames.index(name)
            usernames[index] = 'Blacklisted'
            print(f"{name} was blacklisted.")
            blacklisted_names_count += 1
            # print(usernames)
        else:
            print(f"{name} was not found.")
    elif command_lst[0] == 'Error':
        index = command_lst[1]
        index = int(index)
        if 0<= index < len(usernames):
            if usernames[index] != 'Blacklisted' and usernames[index] != 'Lost':
                print(f"{usernames[index]} was lost due to an error.")
                usernames[index] = 'Lost'
                lost_names_count +=1
    elif command_lst[0] == 'Change':
        index = command_lst[1]
        index = int(index)
        new_name = command_lst[2]
        if 0 <= index < len(usernames):
            current_name = usernames[index]
            usernames[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

    command = input()


print(f"Blacklisted names: {blacklisted_names_count}")
print(f"Lost names: {lost_names_count}")
print(" ".join(usernames))