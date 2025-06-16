# lst = ['Ivo', 'Johny', 'Tony', 'Bony', 'Mony']
# print(lst[0:3])
# lst2 = ['IvoJohnyTony', 'Bony', 'Mony']
# print(lst2[3:4])
# # print(lst[3:5])
# number = 6
# print(number / 3)
element = 'qrstuvwxyz'
partitions = 3
step =  int(len(element) % partitions)
print(step)
lst = [element[index:index + step] for index in range(0, partitions -1)]
print(element[len(element) - 2:])
print(lst + [element[len(element) - 2:]])
# for index in range(0, len(text), 2):
#     print(text[index: index +2])

test = ['abc', 'def', 'ghi']
print(test[0:2])
print(test[2])