initial_lessons = input().split(", ")

command = input()
while command != 'course start':
    data = command.split(":")
    action = data[0]
    lesson_title = data[1]

    if action == 'Add':
        if lesson_title not in initial_lessons:
            initial_lessons.append(lesson_title)

    elif action == 'Insert':
        index = int(data[2])
        if lesson_title not in initial_lessons and 0 <= index < len(initial_lessons):
            initial_lessons.insert(index, lesson_title)

    elif action == 'Remove':
        if lesson_title in initial_lessons:
            initial_lessons.remove(lesson_title)
        if lesson_title + "-Exercise" in initial_lessons:
            initial_lessons.remove(lesson_title + "-Exercise")

    elif action == 'Swap':
        lesson2 = data[2]
        if lesson_title in initial_lessons and lesson2 in initial_lessons:
            i, j = initial_lessons.index(lesson_title), initial_lessons.index(lesson2)
            initial_lessons[i], initial_lessons[j] = initial_lessons[j], initial_lessons[i]

            # Swap Exercises if they exist
            lesson1_ex = lesson_title + "-Exercise"
            lesson2_ex = lesson2 + "-Exercise"

            if lesson1_ex in initial_lessons:
                initial_lessons.remove(lesson1_ex)
                initial_lessons.insert(initial_lessons.index(lesson_title) + 1, lesson1_ex)

            if lesson2_ex in initial_lessons:
                initial_lessons.remove(lesson2_ex)
                initial_lessons.insert(initial_lessons.index(lesson2) + 1, lesson2_ex)

    elif action == 'Exercise':
        exercise = lesson_title + "-Exercise"
        if lesson_title in initial_lessons:
            if exercise not in initial_lessons:
                idx = initial_lessons.index(lesson_title)
                initial_lessons.insert(idx + 1, exercise)
        else:
            initial_lessons.append(lesson_title)
            initial_lessons.append(exercise)

    command = input()

for idx, lesson in enumerate(initial_lessons, 1):
    print(f"{idx}.{lesson}")
