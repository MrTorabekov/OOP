class Student:
    def __init__(self, Name, Surname, Year):
        self.Name = Name
        self.Surname = Surname
        self.Year = Year

    def student_info(self):
        return f"Ismi : {self.Name}\nFamiliya : {self.Surname}\nYear : {self.Year}"


student1 = Student("Abdulmajid", "Mirmakhmudov", 2008)
student2 = Student("Muhtasar", "Izzatullayeva", 2009)
student3 = Student("Rosulhon", "Abdullajanov", 2008)

print(f"{student1.student_info()}\n--------------------\n{student2.student_info()}\n-----------------\n{student3.student_info()}")

