sequence_of_targets =  [int(element) for element in input().split(' ')]
command = input()

count_of_shot_targets = 0
while command != "End":
    index = int(command)
    if 0 <= index < len(sequence_of_targets) :
        count_of_shot_targets += 1
        shot = sequence_of_targets[index]
        sequence_of_targets[index] = -1
        for ind in range(len(sequence_of_targets)):
            if index != ind:
                if sequence_of_targets[ind] != -1 and sequence_of_targets[ind] > shot:
                    sequence_of_targets[ind] -= shot
                elif sequence_of_targets[ind] != -1 and sequence_of_targets[ind] <= shot:
                    sequence_of_targets[ind] += shot
    # print(sequence_of_targets)
    command = input()

result = ' '.join([str(num) for num in sequence_of_targets])
print(f"Shot targets: {count_of_shot_targets} -> {result}")