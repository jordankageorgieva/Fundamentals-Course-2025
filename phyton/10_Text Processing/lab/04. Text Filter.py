bans = input().split(", ")
text = input()
for ban in bans:
    new_ban = len(ban) * "*"
    text = text.replace(ban, new_ban)

print(text)