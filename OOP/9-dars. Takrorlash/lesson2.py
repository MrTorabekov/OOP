class Shaxs:

    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def get_info(self):
        print(self.name, self.surname, self.age, self.gender)


class Student(Shaxs):

    def __init__(self, name, surname, age, passport, gender):
        super().__init__(name, surname, age, gender)
        self.passport = passport

    @property
    def get_info(self):
        return f"Ismi : {self.name}\nFamiliya : {self.surname}\nYoshi : {self.age}\nGender : {self.gender}"


student1 = Student("Abdulmajid", "Mirmakhmudov", 15, "None", "Male")
student2 = Student("Muhtasar", "Izzatullayeva", 14, "None", "Female")
print(student1.get_info)
print("--------------------------------------------------------------------")
print(student2.get_info)
