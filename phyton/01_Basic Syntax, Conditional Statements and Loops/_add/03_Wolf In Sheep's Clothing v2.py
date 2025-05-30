single_string_with_animals = input()
list_single_string_with_animals = single_string_with_animals.split(", ")
list_single_string_with_animals_new = []
for element in list_single_string_with_animals:
    list_single_string_with_animals_new.append(element.strip())
# print(list_single_string_with_animals[-1])
# print(list_single_string_with_animals_new)
if  'wolf' in list_single_string_with_animals_new:
    if list_single_string_with_animals_new[-1] == 'wolf':
        print("Please go away and stop eating my sheep")
    else:
        count_sheep = list_single_string_with_animals_new.count('sheep')
        print(f"Oi! Sheep number {count_sheep}! You are about to be eaten by a wolf!")
