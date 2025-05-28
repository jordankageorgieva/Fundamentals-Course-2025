in_string = input()

words_to_check = ["Sand", "Water", "Fish", "Sun"]

count = 0
for word in words_to_check:
    word = word.lower()
    # print(in_string.lower().count(word))
    if word in in_string.lower():
        count += in_string.lower().count(word)

print(count)