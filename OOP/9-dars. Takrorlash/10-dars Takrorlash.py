# class Person:
#     def __init__(self,age , name , year):
#         self.age = age
#         self.name = name
#         self.year = year
#
#     @property
#     def person(self):
#         return self.age ,self.name , self.year
#
#
#     def Get_info(self,new_year):
#         self.name = new_year.capitalize()
#
#
#
#
# object = Person(15,"Diyorbek",2008)
# object.Get_info("abdulmajid")
# print(object.person)





# class Person:
#     def __init__(self,age , name) :
#         self.age = age
#         self.name = name
#
#     def get_info(self):
#         return self.age,self.name
# class Person1(Person):
#     def __init__(self,age, name, year):
#         super().__init__(age,name)
#         self.year = year
#
#     @property
#     def get_info(self):
#         return  self.year ,self.name,self.age
#
# Shaxs = Person1(22,"diyorbek",2008)
# print(Shaxs.get_info)


from abc import ABC, abstractmethod


class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")


class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")


# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

# object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))
