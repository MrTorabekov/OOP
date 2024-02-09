class Shaxs:
    ism: ""
    familiya = ""
    yosh: ""
    yil: ""
    buyi: ""
    vazni: ""
    qon_guruhi: ""

    def malumot(self):
        return f"""
Shaxsning ismi : {self.ism} 
Shaxsning yoshi : {self.yosh}
Shaxsning tug'ilgan yili : {self.yil}
Shaxsning bo'yi : {self.buyi}
Shaxsning vazni : {self.vazni}
Shaxsning qon guruhi : {self.qon_guruhi}

"""


shaxs1 = Shaxs()

shaxs1.ism = "Abdulmajid"
shaxs1.yosh = 15
shaxs1.yil = 2008
shaxs1.buyi = 163
shaxs1.vazni = 56
shaxs1.qon_guruhi = 4

shaxs2 = Shaxs()

shaxs2.ism = "Muhtasar"
shaxs2.yosh = 14
shaxs2.yil = 2009
shaxs2.buyi = 154
shaxs2.vazni = "Unknown"
shaxs2.qon_guruhi = 1

print(shaxs1.malumot())
print(
    "-----------------------------------------------------------------\n-----------------------------------------------------------------")
print(shaxs2.malumot())
