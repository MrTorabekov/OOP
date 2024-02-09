class Car:
    model = ""
    colour = ""
    engine = ""
    year = ""
    fuel = ""
    price = ""

    def malumot(self):
        return f"""
        Avtomobil modeli : {self.model}
        Avtomobil rangi : {self.colour}
        Avtomobil dvigiteli : {self.engine}
        Avtomobil yoqilg'i sarfi : {self.fuel}
        Avtomobil ishlab chiqarilgan yili : {self.year}
        Avtomobil narxi : {self.price}
        """


car1 = Car()
car1.model = "Chevrolet Malibu XL"
car1.colour = "Black"
car1.engine = "Unknown"
car1.year = 2023
car1.fuel = "Unknown"
car1.price = "40000 $"

car2 = Car()
car2.model = "Chevrolet Nexia 2 Premier"
car2.colour = "White"
car2.engine = "Unknown"
car2.year = 2013
car2.fuel = "1.6L"
car2.price = "5000 $"

print(car1.malumot())

print(
    "-----------------------------------------------------------------\n-----------------------------------------------------------------")
print(car2.malumot())
