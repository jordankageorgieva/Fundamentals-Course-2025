elements = [element for element in input().split(" ")]


elements_dic = {}
for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    elements_dic[key] = value

print(elements_dic)