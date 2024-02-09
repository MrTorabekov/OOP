class Student:
    def __init__(self, first_name):
        first_name = first_name

    @staticmethod
    def katta(*name):
        for i in name:
            print(*i.title()) 


student1 = Student("Xasan")
print(student1.katta("abdulmajid"))
