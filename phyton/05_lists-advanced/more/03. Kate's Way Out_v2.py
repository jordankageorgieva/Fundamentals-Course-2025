rows = int(input())

maze = []
kate_row = 0
kate_col = 0
for indx in range(rows):
    line = input()
    maze.append(line)
    for i in range(len(line)):
        if line[i] == 'k':
            kate_row = indx
            kate_col = i

print(maze)
empty_space = 0
steps_on_row = []
for row_indx in range(len(maze)):
#     empty space upper space
    row = maze[row_indx]
    list_possible_steps_on_1_row = []
    count_steps_on_the_row = 0
    for element_indx in range(len(row)):
        element = row[element_indx]
        if element != "#":
            if element == ' ':
                count_steps_on_the_row += 1
            elif element == 'k':
                list_possible_steps_on_1_row.append("k")
                count_steps_on_the_row += 1
        else:
            count_steps_on_the_row = 0
            list_possible_steps_on_1_row.append(count_steps_on_the_row)


    print(list_possible_steps_on_1_row)
    steps_on_row.append(list_possible_steps_on_1_row)

print(kate_row)
print(kate_col)