class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return f"""
Name : {self.name}
Surname : {self.surname}
Age : {self.age}
        """


class Student(Human):
    def __init__(self, name, surname, age, student_id, address):
        super().__init__(name, surname, age)
        self.__student_id = student_id
        self.__address = address

    @property
    def get_info(self):
        return f"""
Name : {self.name}
Surname : {self.surname}
Age : {self.age}
Student_id : {self.student_id}
Address : {self.address}
        """


student1 = Student("Abdulmajid", "Mirmakhmudov", 15, 9860, "Namangan Region")
print(student1.get_info)
