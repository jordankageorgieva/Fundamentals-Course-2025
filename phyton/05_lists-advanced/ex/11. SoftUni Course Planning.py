initial_lessons = [lessons for lessons in input().split(", ")]


command = input()
while command != 'course start':
    lessons_data = command.split(":")
    print(f"in data = {lessons_data}")
    if lessons_data[0] == 'Add':
        initial_lessons.append(lessons_data[1])
    elif lessons_data[0] == 'Insert':
        if int(lessons_data[2]) > len(initial_lessons):
            initial_lessons.extend([0] * (int(lessons_data[2]) - len(initial_lessons) + 1))
        if lessons_data[1] not in initial_lessons:
            initial_lessons.insert(int(lessons_data[2]),lessons_data[1])
    elif lessons_data[0] == 'Remove':
        if lessons_data[1] in initial_lessons:
            initial_lessons.remove(lessons_data[1])
    elif lessons_data[0] == 'Swap':
        print(lessons_data[1])
        print(lessons_data[2])
        i, j = initial_lessons.index(lessons_data[1]), initial_lessons.index(lessons_data[2])
        print(f"j : {j}")
        if lessons_data[1]+"-Exercise" in initial_lessons or lessons_data[2]+"-Exercise" in initial_lessons:
            if lessons_data[2]+"-Exercise" in initial_lessons :
                initial_lessons[i], initial_lessons[j] = initial_lessons[j], initial_lessons[i]
                initial_lessons.insert(i+1, initial_lessons.pop(j+1))

        initial_lessons[i], initial_lessons[j] = initial_lessons[j], initial_lessons[i]
    elif lessons_data[0] == 'Exercise':
        if lessons_data[1] not in initial_lessons:
            initial_lessons.append(lessons_data[1])
            initial_lessons.append(lessons_data[1] + "-Exercise")
        print(lessons_data)
    print(initial_lessons)
    command = input()

print(initial_lessons)