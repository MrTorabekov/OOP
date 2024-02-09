from dataclasses import dataclass


@dataclass
class Users:
    name: str
    username: str
    email: str
    password: str
    role: str

    @property
    def get_hash(self):
        return hash(self.password)


user1 = Users("John", "@john", "john@gmail.com", "john45", "Admin")
user2 = Users("ali", "@john", "john@gmail.com", "john45", "Xodim")
user3 = Users("alibek", "@john", "ali@gmail.com", "john45", "Manager")
user4 = Users("guli", "@john", "guli@gmail.com", "john45", "HR")


print(user1.get_hash)
print(user2.get_hash)
print(user3.get_hash)
print(user4.get_hash)












# from data import *

user: list = [user1.get_hash, user2.get_hash, user3,user4]
for x in user:
    print(x)
