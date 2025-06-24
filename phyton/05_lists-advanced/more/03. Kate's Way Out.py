rows = int(input())

k_in = False
number_of_moves = 0
way_out = False
way_out_g = False
for _ in range(rows):
    line = input()
    curr_steps = 0
    for i in line:
        if i != "#":
            if i == ' ':
                curr_steps += 1
            elif i == 'k':
                k_in = True
                number_of_moves += 1
                way_out_g = True
    # print(curr_steps)
    # print(k_in)
    # print(way_out_g)
    if curr_steps == 0 and k_in:
        way_out_g = False
    elif curr_steps > 0 and k_in:
        way_out = True
        number_of_moves += curr_steps


if not way_out_g:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {number_of_moves} moves")