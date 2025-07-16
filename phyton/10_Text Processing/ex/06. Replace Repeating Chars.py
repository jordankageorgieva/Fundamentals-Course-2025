text = input()
new_text = ''
for i in range(len(text)):
    if i+1 < len(text) and text[i] == text[i+1]:
        continue
    else:
        new_text += text[i]
print(new_text)