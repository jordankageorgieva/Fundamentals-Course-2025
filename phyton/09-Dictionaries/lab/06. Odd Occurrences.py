input_data = input().split(" ")
occurrences = {}
for data in input_data:
    data = data.lower()
    if data in occurrences:
        current_value = occurrences.get(data)
        occurrences[data] = current_value + 1
    else:
        occurrences[data] = 1

# print(occurrences)
print(" ".join([data for data in occurrences if occurrences.get(data) % 2 != 0]))
