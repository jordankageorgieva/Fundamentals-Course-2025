import re
secret_message = input().split(" ")

decoded_words = []
for message in secret_message:
    match = re.match(r"(\d+)([a-zA-Z]+)", message)
    if match:
        digits, letters = match.groups()
        letters_list = [let for let in letters]
        if len(letters) > 1 :
            letters_list[0], letters_list[len(letters) -1] = letters_list[len(letters) -1], letters_list[0]
        decoded_words.append(chr(int(digits)) + "".join(letters_list))

print(" ".join(decoded_words))