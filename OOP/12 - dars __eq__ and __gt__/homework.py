# from dataclasses import dataclass,field
#
#
# @dataclass
# class User:
#     password:int
#     cart_id: int
#
#     def __hash__(self):
#         return hash((self.password,self.cart_id))
# obj = User(1234567,347976567)
# print(hash(obj))
#
#
#
#
#
#
#
# @dataclass
# class Person:
#     name:str
#     age:int
#     car_number:int and str
#     adress:str = field(init=False,default="Tashkent",repr=True)
#
# obj = Person("Diyorbek",15,"01 H 742 TA")
# print(obj)
#
#
#
#
#
#
# @dataclass
# class Car:
#     car_name: str
#     model: str
#     year: int
#     color: str = field(init=False, default="White", repr=True)
#     price: int = field(init=False, default=1000000, repr=True)
# obj = Car("BMW","BMW X5",2024)
# obj1 = Car("BMW","BMW X5",2023)
# print(obj == obj1)