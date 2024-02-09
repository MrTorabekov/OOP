class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, name):
        print(Student.school_name)
        Student.school_name = name


jasur = Student("Jasur", 14)
Student.change_school("PDP School")
print(Student.school_name)
