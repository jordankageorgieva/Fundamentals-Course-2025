n = int(input())

student_academy = {}
for index in range(n):
    name = input()
    grade = float(input())
    if name in student_academy.keys():
        student_academy[name] = (student_academy[name] + grade)/2
    else:
        student_academy[name] = grade

for name, averageGrade in student_academy.items():
    if averageGrade >= 4.5:
        print(f"{name} -> {averageGrade:.02f}")
