class Car:
    def __init__(self, model, brand, color, year, price):
        self.model = model
        self.brand = brand
        self.color = color
        self.year = year
        self.price = price

    def get_info(self):
        return f"Model : {self.model}\nBrand : {self.brand}\nColor : {self.color}\nYear : {self.year}\nPrice : {self.price}"

    def change_year(self, new_year):
        self.year = new_year


car1 = Car("Damas", "Uz Auto Motors", "White", 1998, 9_800)
car1.change_year(2024)
print(car1.get_info())
