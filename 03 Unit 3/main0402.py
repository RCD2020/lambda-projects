""" This module implements an increment function and a Car class, very epic! """
# Prints documentation
# python3 -m pydoc main0402

# Writes the documentation to an html file
# python3 -m pydoc -w main0402

def inc(n):
    return n + 1

class Car:
    """ Class for creating car objects. """

    def __init__(self, make, model, year, mileage=0):
        """ Initializing attributes """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self):
        """ Drives the car """
        print(f"Driving the {self.make} {self.model}...")

    def set_mileage(self, new_mileage):
        """ Sets the mileage """
        self.mileage = new_mileage

    def get_gas(self):
        """ Gets the gas """
        print(f"Filling up the {self.make} {self.model} with gas...")