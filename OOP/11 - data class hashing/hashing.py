from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int


    def __hash__(self):
        return hash((self.name,self.age))

person = Person("Alice",51)
person1 = Person("Alice",44)

print(hash(person))
print(hash(person1))

emp = Person("Jamshid",21)
print(emp)
