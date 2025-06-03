gifts= [gift for gift in input().split(' ')]

read_input = True
while True:
    command = input()
    if command == 'No Money':
        break

    parts = command.split()
    action = parts[0]

    if 'OutOfStock' == action:
        gift = parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = None
        # print(gift)
    elif 'Required' == action:
        gift = parts[1]
        index = int(parts[2])
        # print(f" gift {gift} : index {index}")
        # print(f" gifts {gifts} ")
        if 0 <= index < len(gifts) :
            # print(int(index))
            # gifts.pop(int(index))
            # gifts.insert(int(index), gift)
            gifts[index] = gift  # Replace gift at the given index
        # print(gift)
    elif 'JustInCase' == action:
        gift = parts[1]
        # Replace the value of your last gift with this one.
        # gifts.pop()
        # gifts.append(gift)
        gifts[-1] = gift  # Replace the last gift




# output
# print(gifts)
# print(len(gifts))
# for index in range(len(gifts)):
#     if gifts[index] != None:
#         print(gifts[index], end=' ')
print(' '.join(g for g in gifts if g is not None))