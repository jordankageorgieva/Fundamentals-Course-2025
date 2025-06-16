sequence_int = list(map(int, input().split(' ')))
# print(sequence_int)

sum_pokemon = 0
while len(sequence_int) > 0:
    index = int(input())

    if index < 0:
        element = sequence_int.pop(0)
        sequence_int.insert(0, sequence_int[-1])
    elif index >= len(sequence_int):
        element = sequence_int.pop(len(sequence_int)-1)
        # print(element)
        sequence_int.append(sequence_int[0])
        # print(sequence_int)
    else:
        element = sequence_int.pop(index)
    sum_pokemon += element
    for i in range(len(sequence_int)):
        if sequence_int[i] > element:
            sequence_int[i] -= element
        else:
            sequence_int[i] += element
    # print(sequence_int)
print(sum_pokemon)