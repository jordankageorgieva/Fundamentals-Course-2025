class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average = sum(self.grades) / len(self.grades)
        return f"{average:.02f}"

    def __repr__(self):
        average_grade = self.get_average_grade()
        studens = ", ".join(self.students)
        return f"The students in {self.name}: {studens}. Average grade: {average_grade}"

a_class = Class("11B")
a_class.add_student("Peter", 0.1)
a_class.add_student("George", 0.3)
a_class.add_student("Amy", 3.50)
print(a_class)
if 0.1 + 0.2 == 0.3:
    print(True)
else:
    print(False)
