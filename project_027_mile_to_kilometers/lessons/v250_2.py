class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # Doesn't give error if not passed
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

my_car = Car(make="Subaru")
print(my_car.make)
print(my_car.model)
