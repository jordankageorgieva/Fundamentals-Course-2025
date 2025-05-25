n = int(input())  # Number of lines

open_bracket_count = 0
balanced = True

for _ in range(n):
    line = input()

    if line == "(":
        open_bracket_count += 1
        if open_bracket_count > 1:  # Two consecutive opening brackets
            balanced = False
            break
    elif line == ")":
        if open_bracket_count == 0:  # Closing bracket without an opening one
            balanced = False
            break
        open_bracket_count -= 1
    # If it's a "Random string", we ignore it as per the problem description
    # It doesn't affect the bracket balance directly.

if open_bracket_count != 0:  # Unmatched opening brackets at the end
    balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")