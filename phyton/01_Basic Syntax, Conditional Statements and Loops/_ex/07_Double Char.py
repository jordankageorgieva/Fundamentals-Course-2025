str_in = input()
while str_in != "End":
    if str_in != "SoftUni":
        for index in range(len(str_in)):
            new_str = str_in[index] + str_in[index]
            print(new_str, end="")

        print()
    str_in = input()


