
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self,vehicle_type ,year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


vehicle_type = "car"

year  = input("Enter the car year: ")
make  = input("Enter the car make: ")
model = input("Enter the car model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof  = input("Enter the type of roof (solid or sun roof): ")

my_car = Automobile(vehicle_type, year, make, model, doors, roof)

print("Vehicle Type:", my_car.vehicle_type)
print("Year:", my_car.year)
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Number of Doors:", my_car.doors)
print("Type of Roof:", my_car.roof)
