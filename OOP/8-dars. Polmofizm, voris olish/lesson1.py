class Chevrolet:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color


chevrolet1 = Chevrolet("Matiz", "Chevrolet", "white")


class BMW(Chevrolet):
    def __init__(self, km, price):
        super(Chevrolet).__init__(name, model, color)
        self.km = km
        self.price = price


bmw1 = BMW(45_000, )
