data = input()

list_data = []
opposite_list_data = []

list_data = data.split(" ")
for data in list_data:
    # more phytonic is
    # opposite_data = -int(num)
    opposite_data = -1 * int(data)
    opposite_list_data.append(opposite_data)

print(opposite_list_data)