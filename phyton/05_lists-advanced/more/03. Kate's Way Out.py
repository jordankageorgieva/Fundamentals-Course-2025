rows = int(input())

k_in = False
number_of_moves = 0
way_out = False
way_out_g = False
for _ in range(rows):
    line = input()
    curr_steps = 0
    curr_steps_lst= []
    if line != '':
        for i in line:
            if i != "#":
                if i == ' ':
                    curr_steps += 1
                elif i == 'k':
                    k_in = True
                    number_of_moves += 1
                    way_out_g = True
            else:
                curr_steps_lst.append(curr_steps)
                curr_steps = 0
        # print(curr_steps_lst)
        # print(k_in)
        # print(way_out_g)
        if curr_steps_lst and max(curr_steps_lst) == 0 and k_in:
            way_out_g = False
        elif curr_steps_lst and  max(curr_steps_lst) > 0 and k_in:
            way_out = True
            number_of_moves += max(curr_steps_lst)


if not way_out_g:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {number_of_moves} moves")