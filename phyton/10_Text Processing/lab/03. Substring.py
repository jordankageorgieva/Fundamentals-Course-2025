line_1 = input()
line_2 = input()
no_match = True

end_result = ''
while no_match:
    if line_1 in line_2:
        line_2 = line_2.split(line_1)
        line_2 = ''.join(line_2)
        # print(line_2)
    else:
        end_result = line_2
        no_match = False

print(end_result)