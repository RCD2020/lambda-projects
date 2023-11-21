"""Module that iplements a Car and Electric Car class"""

"""Car Class"""


class Car:

    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self):
        print(f"Driving the {self.make} {self.model}...")

    def set_mileage(self, new_mileage):
        self.mileage = new_mileage

    def get_gas(self):
        print(f"Filling up the {self.make} {self.model} with gas...")


"""Electric Car Class"""


class ElectricCar(Car):

    def __init__(self, make, model, year, battery_size=100, mileage=0):
        super().__init__(make, model, year, mileage=mileage)
        self.battery_size = battery_size

    def get_gas(self):
        print("You stupid idiot! I take electricity, not gas! Get that vile liquid away from me!")

# auto style using 'autopep8 --in-place --aggressive --aggressive lambda30/oop_example.py' in terminal