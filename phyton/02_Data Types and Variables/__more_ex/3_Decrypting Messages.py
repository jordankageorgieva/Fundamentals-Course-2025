key = int(input())
line_numbers= int(input())

decrypt_message = ""
for index in range(line_numbers ):
    message = input()
    decrypt_message += chr(ord(message) + key)

print(decrypt_message)