from dataclasses import dataclass,field
# @dataclass
# class employee:
#     # type hinting
#     name:str
#     emp_id:str
#     age: int
#     city: str
#
#
# emp1 = employee("Diyorbek","123diyorbek",15,"Tashkent")
#
# emp2 = employee("Abdulmajid","1234",15,"Tashkent")
#
# emp3 = employee("Ahmad","5678",15,"Turkey")
#
# print(emp1)
# print(emp2)
# print(emp3)






# @dataclass
# class Autosalon:
#     nomi: str
#     brend: str
#     km : int
#     yil: int
#     color:str = field(default="Black",init=True)
#
#
# obj = Autosalon("BMW","BMW X5",10 , 2024)
# print(obj)



# from dataclasses import dataclass, field
#
#
# @dataclass
# class Person:
#     # type hinting
#     name: str
#     age: int
#     address: str
#     city: str = field(default="The City", init=True)
#
#
# odam = Person("Akbar", 45, "Tashkent")
# print(odam.city)
