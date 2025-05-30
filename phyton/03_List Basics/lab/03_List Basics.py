n = int(input())
word = input()

data_list = []

for _ in range(n):
    data_list.append(input())

print(data_list)

for element in data_list:
    if word not in element:  # <- махаме елемента, в който думата я няма.
        data_list.remove(element)

print(data_list)
