text = input()

i = 0
step = 0
new_text = ''
strength = 0
while True:
    if i == len(text):
        break

    if text[i] == '>':
        strength += int(text[i+1])
        new_text += text[i]
    elif strength > 0 and text[i] != '>':
        strength -= 1
    else:
        new_text += text[i]
    i += 1
print(new_text)