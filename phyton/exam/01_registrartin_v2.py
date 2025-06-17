username = input()

while True:
    command = input()
    if command == "Registration":
        break

    tokens = command.split()

    if tokens[0] == "Letters":
        if tokens[1] == "Lower":
            username = username.lower()
        elif tokens[1] == "Upper":
            username = username.upper()
        print(username)

    elif tokens[0] == "Reverse":
        start = int(tokens[1])
        end = int(tokens[2])
        if 0 <= start <= end < len(username):
            substring = username[start:end+1]
            print(substring[::-1])
        # If invalid, do nothing (skip)

    elif tokens[0] == "Substring":
        substring = tokens[1]
        if substring in username:
            username = username.replace(substring, '', 1)
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif tokens[0] == "Replace":
        char = tokens[1]
        username = username.replace(char, '-')
        print(username)

    elif tokens[0] == "IsValid":
        char = tokens[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")
