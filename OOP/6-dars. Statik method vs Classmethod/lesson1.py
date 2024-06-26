# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('Abdulmajid', 21)
person2 = Person.fromBirthYear('mayank', 2009)

print(person1.age)
print(person2.age)

# print the result
print(person1.isAdult(21))
print(person2.isAdult(32))
