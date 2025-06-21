sequence_of_targets =  [int(element) for element in input().split(' ')]
command = input()

while command != "End":
    com, index, value = command.split(" ")
    index = int(index)
    value = int(value)
    if com == 'Shoot':
        # print(index)
        # print(value)
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets[index] -= value
            # print(sequence_of_targets)
            # print(sequence_of_targets[index])
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.remove(sequence_of_targets[index])
    elif com == 'Add':
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif com == 'Strike':
        # There will never be a case when the "Strike" command would empty the whole sequence
        if not(0 <= index + value < len(sequence_of_targets)) or not(0 <= index - value < len(sequence_of_targets)):
                print("Strike missed!")
        else:
            for index in range(index + value, index - value -1, -1):
                sequence_of_targets.pop(index)
    # print(sequence_of_targets)
    command = input()

# print(sequence_of_targets)
if sequence_of_targets:
    print("|".join([str(el) for el in sequence_of_targets]))