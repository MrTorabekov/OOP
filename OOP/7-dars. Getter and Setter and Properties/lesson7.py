class Personal:
    def __init__(self, first_name, username, age):
        self.first_name = first_name
        self.username = username
        self.age = age

    @property
    def full_date(self):
        return f"Ismingiz : {self.first_name}\nUsernamingiz : {self.username}\nYoshingiz : {self.age}"

    @full_date.setter
    def full_date(self, *new):
        self.first_name = new[0]
        self.username = new[1]
        self.age = new[2]


first_name = input("Ismingizni kiriting :")
while len(first_name) > 15:
    print("Ismingiz maximium 15 ta harfdan iborat bo'lishi kerak!")
    first_name = input("Ismingizni kiriting :")

username = input("Username kiriting :")
while not "@" in username:
    print("Usernameda kamida 1 ta (@) bo'lishi kerak!")
    username = input("Username kiriting :")

age = int(input("Yoshingizni kiriting :"))

while age > 24:
    print("Siz ro'yhatdan o'tishingiz uchun 24 yoki undan kichik yoshda bo'lishingiz mumkin!")
    age = int(input("Yoshingizni kiriting :"))

person1 = Personal(first_name, username, age)
print(person1.full_date)
