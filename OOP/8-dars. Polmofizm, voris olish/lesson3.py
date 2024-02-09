class Auto:

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def get_info(self):
        print(self.name, self.model, self.color)


class Car(Auto):

    def __init__(self, name, model, color, speed, year, km):
        self.name_ = name
        super().__init__(name, model, color)
        self.model = model
        self.speed = speed
        self.year = year
        self.km = km

    @property
    def get_info(self):
        return f"Nomi : {self.name}\nModeli : {self.model}\nTezligi : {self.speed}\nChiqarilgan yili : {self.year}\nProbeg : {self.km}"


car1 = Car("BMW", "X5", "white", 320, 2023, 0)
print(car1.get_info)
