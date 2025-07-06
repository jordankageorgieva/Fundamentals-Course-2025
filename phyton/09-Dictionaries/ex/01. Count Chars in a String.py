text = input()
text_dict = {}
for index in range(0, len(text)):
    if text[index] != " " :
        if text[index] not in text_dict:
            text_dict[text[index]] = 0

        text_dict[text[index]] += 1

print("\n".join([key + " -> "+ str(value) for key, value in text_dict.items()]))