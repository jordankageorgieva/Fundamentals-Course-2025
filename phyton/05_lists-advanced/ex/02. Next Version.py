current_version = input().split(".")
current_version_digit = "".join(current_version)
current_version_digit_new = int(current_version_digit) + 1
print(".".join(str(current_version_digit_new)))
