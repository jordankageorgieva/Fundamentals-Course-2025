name = '@smith'
is_name_not_correct = False
# for i in range(len(name)):
#     if not name[i].isalpha() and not name[i].isdigit() and not name[i] == '-' and not name[i] == '_':
#         is_name_not_correct = True
#         break
for i in range(len(name)):
    if not name[i].isalpha() and not name[i].isdigit() and not name[i] == '-' and not name[i] == '_':
        is_name_not_correct = True
        break
else:
    if is_name_not_correct:
        print(is_name_not_correct)

print(is_name_not_correct)