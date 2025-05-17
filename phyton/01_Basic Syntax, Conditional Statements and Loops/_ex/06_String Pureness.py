n = int(input())

for index in range (n):
    in_string = input()
    if "," in in_string or "." in in_string or "_" in in_string:
        print(f"{in_string} is not pure!")
    else :
        print(f"{in_string} is pure.")

