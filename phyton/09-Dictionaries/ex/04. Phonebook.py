command = input()
phonebook = {}
while True:
    if "-" not in command:
        break
    name, phone = command.split("-")
    phonebook[name] = phone
    command = input()

n = int(command)
for index in range(n):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
