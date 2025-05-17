str1 = input()
str2 = input()

if len(str1) != len(str2):
    print("strings could not be mutated because they are with different lengths")
elif str1 != str2:
    #  we make string mutation only when they are difference
    new_str = ""
    for index in range(len(str1)):
        # print(index)
        # print(str2[:index+1])
        # print(str1[index +1:])
        curr_str = str2[:index+1] + str1[index +1:]
        if curr_str != new_str:
            new_str = curr_str
            print(curr_str)