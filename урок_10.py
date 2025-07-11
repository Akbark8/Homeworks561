class Car:
    # инициализатор
    def __init__(self, model, year):
        # свойства, атрибуты, поля
        self.model = model
        self.year = year
        self.fined = False

    def drive_to_location(self, location):
        print(f"Car {self.model} driving to {location}")

class Truck(Car):
    pass

truck_man = Truck("MAN", 2019)
print("Model", truck_man.model, "Year", truck_man.year, "fined", truck_man.fined)