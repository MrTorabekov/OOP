class Person:
    first_name = "Xadicha"

    def __init__(self, address, age):
        self.address = address
        self.age = age

    @classmethod
    def change_name(cls, name):
        print(Person.first_name)
        Person.first_name = name
        return name


User = Person("Tashkent", 15)
# print(User.first_name)
print(User.change_name("GuliAsal"))
