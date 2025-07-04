input_data = input()

course_dict = dict()
course = ''
while True :
    if ":" not in input_data:
        course = input_data
        break
    name, ID, course = input_data.split(":")
    course = str(course).lower().replace(" ", "_")
    if course in course_dict:
        # add current value to the existing ones
        current_value = course_dict.get(course) + [name, ID]
        course_dict[course] = list(current_value)
    else:
        # create new value
        course_dict[course] = [name, ID]

    input_data = input()

# print(course_dict)
if course in course_dict:
    students = course_dict.get(course)
    for index in range(0, len(students), 2):
        print(f"{students[index]} - {students[index+1]}")