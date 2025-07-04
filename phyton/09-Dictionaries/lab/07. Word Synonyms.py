synonym_sum = int(input())
synonym_dict = {}
for _ in range(synonym_sum):
    key = input()
    synonym = input()
    if key not in synonym_dict:
        synonym_dict[key] = synonym
    else:
        synonym_dict[key] = str(synonym_dict.get(key)) + ", " + synonym

# print(synonym_dict)
print("\n".join([data +" - " + synonym_dict.get(data) for data in synonym_dict]))