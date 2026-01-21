class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        if len(self.students) == 0:
            return 0
        
        total = 0
        for student in self.students:
            total += student.score
        
        return total / len(self.students)


gradebook = Gradebook()

gradebook.add_student(Student("Alice", 85))
gradebook.add_student(Student("BOb",90))
gradebook.add_student(Student("Charlie", 80))



print("Class Average:", gradebook.get_average())