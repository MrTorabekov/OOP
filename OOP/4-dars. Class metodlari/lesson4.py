class Person:
    def __new__(cls, name, surname):
        full_name = super(Person, cls).__new__(cls)
        full_name.name = name
        full_name.surname = surname
        return full_name


person1 = Person("Abdulmajid", "Mirmakhmudov")
print(person1.name, person1.surname)
