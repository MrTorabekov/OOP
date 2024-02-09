date = {
}
while True:
    choose_section = int(input(f"""
    1. Register
    2. Login
    Please Choose...."""))
    if choose_section == 1:

        print("Ro'yhatdan o'tish uchun quyidagilarni to'ldiring!")


        class Register:
            def __init__(self, username, password, email, name):
                self.username = username
                self.password = password
                self.email = email
                self.name = name


        name = input("Name kiriting:")
        email = input("Email kiriting:")
        username = input("Username kiriting:")
        password = input("Password kiriting:")
        person1 = Register(username, password, email, name)
        date.setdefault("username", person1.username)
        date.setdefault("password", person1.password)
        date.setdefault("email", person1.email)
        date.setdefault("name", person1.name)

    elif choose_section == 2:

        class Login:
            def __init__(self, username2, password2):
                self.username = username2
                self.password = password2


        username2 = input("Username kiriting:")
        password2 = input("Password kiriting:")

        if date["username"] in username2 and date["password"] in password2:
            print(f"Xush kelibsiz {username2} Muvafaqqiyatli ✅")
            quit()
        else:
            print("Nimadir xato ketdi ? ❌")
            quit()

    else:
        quit()
