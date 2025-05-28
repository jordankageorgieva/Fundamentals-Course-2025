# containing the animals separated by a comma and a single space ", " ex. sheep, sheep, wolf
string = input()

list_string = string.split(",")
# print(list_string)

is_wolf_last = False
count = 0
wolf = 0
sheep = 0
while count <= len(list_string) -1:
    if count == len(list_string) -1 and list_string[count].strip() == 'wolf':
        is_wolf_last = True
    elif list_string[count].strip() == 'wolf':
        wolf +=1
    elif list_string[count].strip() == 'sheep':
        sheep += 1

    count += 1

if is_wolf_last:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
