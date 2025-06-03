raw_cards_data_list = input().split(" ")
count_faro_shuffles = int(input())


faro_list = raw_cards_data_list
for number in range(1, count_faro_shuffles + 1):
    middle = len(raw_cards_data_list) // 2
    first_list = faro_list[:middle]
    second_list = faro_list[middle:]
    faro_list = []
    for index in range(middle):
        # in faro
        faro_list.append(first_list[index])
        faro_list.append(second_list[index])
    # print(f"{number} - faro_list {faro_list}")
# print(first_list)
# print(second_list)
print(faro_list)