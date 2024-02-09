class Car:
    km = 10_200

    def __new__(cls, model, color, km=0):
        avto = super(Car, cls).__new__(cls)
        avto.model = model
        avto.color = color
        return avto

    @classmethod
    def update_km(cls, new_km):
        Car.km = new_km


car1 = Car("Chevrolet", "White")
car1.update_km(10_200_1)
print(f"{car1.model}\n{car1.color}\n{car1.km:,}")
