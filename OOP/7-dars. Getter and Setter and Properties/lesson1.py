class Student:
    def __init__(self, name, age, region):
        self.name = name
        self.age = age
        self.region = region

    def get_region(self):
        return self.region


student1 = Student("AbdulMajid", 15, "Nam")
print(student1.get_region())
