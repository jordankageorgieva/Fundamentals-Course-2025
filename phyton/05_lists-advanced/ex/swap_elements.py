lst = ['Methods', 'Lists', 'Arrays', 'Databases', 'Databases-Exercise']
# lst[1], lst[3:4:1] = lst[3:4:1], lst[1]
# lst.insert(2, lst.pop(4))
# print(lst[3:5])
print(lst[3:5:1])
lst[1], lst[3:5:1] = lst[3:5:1], lst[1]
print(lst)