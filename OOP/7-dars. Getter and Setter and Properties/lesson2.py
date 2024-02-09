class Car:
    def __init__(self, model, color, brand, price):
        self.model = model
        self.color = color
        self.brand = brand
        self.price = price

    def get_model(self):
        return f"Model : {self.model}"

    def full_info(self):
        return f"Model : {self.model}\nColor : {self.color}\nBrand : {self.brand}\nPrice : {self.price:,}"


car1 = Car("D A M A S", "White", "Uz Auto Motors", 9_545)
print(car1.get_model())
print(car1.full_info())
