class Teacher():
    school_name = "Hamstring Highschool"
    current_id = 1
    def __init__(self, name, subject):
        self.id = Teacher.current_id
        self.name = name
        self.subject = subject
        Teacher.current_id += 1

teacher1 = Teacher("Sam", "Math")
teacher2 = Teacher("John", "English")
teacher3 = Teacher("Lily", "History")

teachers = [teacher1, teacher2, teacher3]

for teacher in teachers:
    print(f"{teacher.school_name} {teacher.id} {teacher.name} {teacher.subject}")
