text = input()
new_text = ''
for i in range(len(text)):
    new_text += chr(ord(text[i]) + 3)

print(new_text)