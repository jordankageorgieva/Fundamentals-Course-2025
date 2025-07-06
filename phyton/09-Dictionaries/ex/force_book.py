command = input()
force = {}
while command != "Lumpawaroo":
    # print(force)
    if "|" in command:
        group, user = command.split(" | ")
        if user not in force.keys():
            force[user] = group
    elif "->" in command:
        user, group = command.split(" -> ")
        if user not in force.keys():
            print(f"{user} joins the {group} side!")
        elif user in force.keys() and force[user] != group :
            print(f"{user} joins the {group} side!")
            #     remove the user and when we added it to be last in the dict order
            force.pop(user)
        force[user] = group
    command = input()
# print(force)
# gropus = set()
gropus = []
for value in force.values():
    # gropus.add(value)
    if value not in gropus:
        gropus.append(value)
for value in gropus:
    count_keys = 0
    list_users= []
    for user, cur_value in force.items():
        if cur_value == value:
            count_keys += 1
            list_users.append(user)
    print(f"Side: {value}, Members: {count_keys}")
    print("\n".join(["! " +str(item) for item in list_users]))
