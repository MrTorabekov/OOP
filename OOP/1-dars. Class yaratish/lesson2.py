class Car:
    name: ""
    color: ""
    year: ""
    price: ""

    def malumot(self):
        return f" Model : {self.name} \n Rangi : {self.color} \n Ishlab chiqarilgan yili : {self.year} \n Narxi : {self.price}"


malibu = Car()
malibu.name = "Chevrolet Malibu"
malibu.color = "Qora"
malibu.year = 2022
malibu.price = 30000


print(malibu.malumot())
