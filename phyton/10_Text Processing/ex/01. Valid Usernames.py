usernames = input().split(", ")
valid_username = []
for name in usernames:

    if len(name) < 3 or len(name) > 16:
        continue

    is_name_not_correct = False
    for i in range(len(name)):
        if not name[i].isalpha() and not name[i].isdigit() and not name[i] == '-' and not name[i] == '_':
            is_name_not_correct = True
            break
    if is_name_not_correct:
        continue

    if " " in name:
        continue

    valid_username.append(name)

print("\n".join(valid_username))