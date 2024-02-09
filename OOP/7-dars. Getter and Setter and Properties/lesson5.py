class Student:
    def __init__(self, name, surname, yonalish):
        self.name = name
        self.surname = surname
        self.yonalish = yonalish

    def student_info(self):
        return f"Ismi : {self.name}\nFamiliya : {self.surname}\nYo'nalish : {self.yonalish}"

    def student_change(self, new_name, new_surname, new_yonalish):
        self.name = new_name
        self.surname = new_surname
        self.yonalish = new_yonalish


student1 = Student("Abdulmajid", "Mirmakhmudov", "Front-end Developer")
print(f"Before : \n      \n{student1.student_info()}")
print(student1.student_change("Muhtasar", "Izzatullayeva", "Back-end Developer"))
print(f"After : \n      \n{student1.student_info()}")
print(student1.student_change("erg", "vbb", "Back-end Developer"))

print(f"After : \n      \n{student1.student_info()}")
