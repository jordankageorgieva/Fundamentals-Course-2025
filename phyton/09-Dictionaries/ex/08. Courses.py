resource = input()
course = {}
while resource != 'end':
    name, registered_students = resource.split(" : ")
    if name not in course:
        course[name] = []
    list_students = course[name]
    if list_students == []:
        course[name] = [registered_students]
    else:
        students = list_students + [registered_students]
        course[name] = students
    resource = input()

for cource, students in course.items():
    print(f"{cource}: {len(students)}")
    for student in students:
        print(f"-- {student}")