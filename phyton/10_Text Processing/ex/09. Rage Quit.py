text = input()
elements = []

alfa_text = []
digit_text = []
for index in range(len(text)):
    if text[index] not in elements:
        elements.append(text[index])
    if not text[index].isdigit():
        alfa_text.append(text[index])
        digit_text.append("_")
    elif text[index].isdigit():
        digit_text.append(text[index])
        alfa_text.append("_")

# print(alfa_text)
# print(digit_text)
new_text = ''
append_text = ''
append_digit = ''
for index in range(len(alfa_text)):
    if alfa_text[index] != '_':
        append_text += alfa_text[index].upper()
    else:
        append_digit += digit_text[index]

    if index == (len(digit_text) -1) or (digit_text[index+1] == '_' and alfa_text[index] == '_') :
        new_text += append_text * int(append_digit)
        append_text = ''
        append_digit = ''

alfa_text_set = {element.upper() for element in alfa_text if element != "_"}
# print(alfa_text_set)
print(f"Unique symbols used: {len(alfa_text_set)}")
print(new_text)
