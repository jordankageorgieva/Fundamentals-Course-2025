def password_validator(password:str) ->list:
    messages = []
    if len(password) < 6 or len(password) > 10:
        messages.append("Password must be between 6 and 10 characters")
    if len([letter for letter in password if not letter.isdigit() and not letter.isalpha()]) > 0 :
        messages.append("Password must consist only of letters and digits")
    if len([letter for letter in password if letter.isdigit()]) < 2 :
        messages.append("Password must have at least 2 digits")
    if messages == []:
        messages.append("Password is valid")
    return messages

password_input = input()
messages = password_validator(password_input)
for message in messages:
    print(message)