class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return self.name, self.age, self.address

    def change_student(self, *new) -> None:
        self.name = new[0]
        self.age = new[1]
        self.address = new[2]


name = input("Ismingizni kiriting:")
age = input("Yoshingizni kiriting:")
address = input("Manzilingizni kiriting:")


student1 = Student(name, 15, "Namangan Region")
student2 = Student("Muhtasar", 14, "Namangan Region")
print("          After")
print(*student1.get_info())
print(*student2.get_info())
new_name = input("O'zgartirmoqchi bo'lgan ismingzini kiriting:")
new_age = input("O'zgartirmoqchi bo'lgan yoshingizni kiriting:")
new_address = input("O'zgartirmoqchi bo'lgan manzilingizni kiriting:")
student1.change_student(new_name, new_age, new_address)
student1.change_student("-----", 14, "Tashkent Region")
print("          Before")
print(*student1.get_info())
print(*student2.get_info())
