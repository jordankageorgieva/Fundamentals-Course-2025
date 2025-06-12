to_do = input()
list_to_do = []
while to_do != 'End':
    # to_do_split = to_do.split('-')
    list_to_do.append(to_do)
    to_do = input()

# sort list
# sorted_lst = sorted(list_to_do, key=lambda task: int(task.split('-')[0]))
sorted_lst = sorted(list_to_do, key=lambda task: int(task.split('-')[0]))
# remove numbers
cleaned_lst = [element.split('-')[1] for element in sorted_lst]
print(cleaned_lst)
