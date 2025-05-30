number = int(input())
word = input()

list_data = list()
for _ in range(number):
    data = input()
    list_data.append(data)

print(list_data)
# list_data_with_word = list()
# for data in list_data:
#     if word in data:
#         list_data_with_word.append(data)
# remove element
for index in range(len(list_data) -1, -1, -1):
    if word not in list_data[index]:
        list_data.pop(index)

print(list_data)