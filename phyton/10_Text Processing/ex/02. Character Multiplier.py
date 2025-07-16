name_1, name_2 = input().split(" ")

sum = 0
if len(name_1) < len(name_2):
    for i in range(len(name_1)):
        sum += ord(name_1[i]) * ord(name_2[i])
    for i in range(len(name_1), len(name_2)):
        sum += ord(name_2[i])
elif len(name_2) < len(name_1):
    for i in range(len(name_2)):
        sum += ord(name_1[i]) * ord(name_2[i])
    for i in range(len(name_2), len(name_1)):
        sum += ord(name_1[i])
else:
    for i in range(len(name_2)):
        sum += ord(name_1[i]) * ord(name_2[i])

print(sum)
# print(ord('a'))