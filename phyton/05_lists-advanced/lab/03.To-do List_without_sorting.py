notes = [0] * 10
while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    priority = int(tokens[0]) -1
    # print(f"priority : {priority}")
    note = tokens [1]
    # print(f"note : {note}")
    # print(notes)
    notes.pop(priority)
    # data are inserted according the index == priority
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)