class Person:
    def __init__(self, name, year, age=0):
        self.name = name
        self.year = year
        self.age = age



    def malumot(self):
        return f"""
Shaxsning Ismi : {self.name}
Shaxsning Tug'ilgan yili : {self.year}
Shaxsning Yoshi : {2023 - self.year}
        """


person1 = Person("Abdulmajid", 2008)
print(person1.malumot())
