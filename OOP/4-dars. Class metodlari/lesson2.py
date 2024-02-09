class Talaba:
    university_name = "University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, name):
        print(Talaba.university_name)
        Talaba.university_name = name


user = Talaba("Abdulmajid", 14)

Talaba.university_name = "PDP University"
print(Talaba.university_name)
