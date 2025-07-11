string = input()
digits = []
letters = []
characters = []
for index in range(len(string)):
    if string[index].isdigit():
        digits.append(string[index])
    elif string[index].isalpha():
        letters.append(string[index])
    else:
        characters.append(string[index])

print("".join(digits))
print("".join(letters))
print("".join(characters))