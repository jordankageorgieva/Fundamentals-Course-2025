def characters_in_range(char_1 : str, char_2 : str) -> str:

    char_list = []
    for index in range (ord(char_1) + 1, ord(char_2)):
        char_list.append(chr(index))

    return " ".join(char_list)

char_1 = input()
char_2 = input()

print(characters_in_range(char_1, char_2))