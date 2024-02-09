class Talaba:
    first_name = ""
    last_name = ""
    username = ""
    age = ""
    cource = ""

    def malumot(self):
        return f"Talabaning ismi : {self.first_name}\nTalabaning Familiyasi : {self.last_name}\nTalabaning usernamesi : {self.username}\nTalabaning yoshi : {self.age}\nTalaba o'qiydigan kurs turi : {self.cource}"


talaba1 = Talaba()
talaba1.first_name = "Abdulmajid"
talaba1.last_name = "Mirmakhmudov"
talaba1.username = "@mr.mirmakhmudov16112008"
talaba1.age = 15
talaba1.cource = "Back-end Programming"

talaba2 = Talaba()

talaba2.first_name = "Muhtasar"
talaba2.last_name = "Izzatullayeva"
talaba2.username = "@izzatullayeva08032008"
talaba2.age = 14
talaba2.cource = "Study school lessons"

print(talaba1.malumot())
print("-----------------------------------------------\n-----------------------------------------------")
print(talaba2.malumot())
