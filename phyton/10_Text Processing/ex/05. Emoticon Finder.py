text = input()
emoticon = []
for i in range(len(text)):
    if text[i] == ":":
        emoticon.append(text[i] + text[i+1])
print("\n".join(emoticon))