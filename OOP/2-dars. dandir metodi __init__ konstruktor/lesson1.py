class Person:
    def __init__(self, first_name, last_name, year, age):
        self.name = first_name
        self.surname = last_name
        self.yil = year
        self.yosh = age

    def malumot(self):
        return f"""
Shaxsning ismi : {self.name}
Shaxsning familiyasi : {self.surname}
Shaxsning tug'ilgan yili : {self.yil}
Shaxsning  yoshi : {self.yosh}
        """


person1 = Person("Abdulmajid", "Mirmakhmudov", 2008, 15)
person2 = Person("Muhtasar", "Izzatullayeva", 2009, 14)
person3 = Person("Rosulhon", "Abdullajanov", 2008, 15)
person4 = Person("Diyor", "To'rabekov", 2008, 15)
print(person1.malumot())
print("------------------------------------------")
print(person2.malumot())
print("------------------------------------------")
print(person3.malumot())
print("------------------------------------------")
print(person4.malumot())

