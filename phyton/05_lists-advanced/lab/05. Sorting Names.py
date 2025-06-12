names = input()
names_lst = names.split(", ")
names_lst = sorted(names_lst, key= lambda name: (-1 * len(name), name))

# for name in names_lst:
#     print(len(name))

print(names_lst)