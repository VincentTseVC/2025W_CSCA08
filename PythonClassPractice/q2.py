"""
QUESTION 2: Object Oriented Programming

8 marks, ~15 minutes

(a) Write a series of classes that satisfy the following specification.

A parking garage has an address (an arbitrary string), and zero or more vehicle
parked in it. Because of local laws a parking garage can host at most 1000
parking spots. If a vehicle tries to enter the parking garage that does not have
enough parking spots left, a NoParkingAvailableError is raised.

A vehicle can either be a truck or a car. Trucks are longer than cars and have
to park at an angle, taking up two parking spots at a time. Cars can park
normally and take up one parking spot in the parking garage.

Both trucks and cars have a make, colour and year in which they are built.

TODO: Write your code below here.

You may import any type of from "typing" for type contracts. No other import is
allowed.

Documentation are not required for the marking of this question; however, it may
help the TAs understand your code better.
"""

from __future__ import annotations

class NoParkingAvailableError(Exception):
    ...

class Garage:
    address: str
    spots: int
    vehicles: list[Vehicle]
    spots_taken: int

    def __init__(self, address: str, spots: int = 1000) -> None:
        self.address = address
        self.spots = spots
        self.vehicles = []
        self.spots_taken = 0

    def park(self, vehicle: Vehicle) -> None:

        # if isinstance(vehicle, Car):
        #     self.spots_taken += 2
        # elif isinstance(vehicle, Truck):
        #     self.spots_taken += 4

        if self.spots_taken + vehicle.spots_requried() > self.spots:
            raise NoParkingAvailableError

        self.spots_taken += vehicle.spots_requried()
        self.vehicles.append(vehicle)


class Vehicle:
    make: str
    colour: str
    year: int

    def __init__(self, make: str, colour: str, year: int) -> None:
        self.make = make
        self.colour = colour
        self.year = year

    def spots_requried(self) -> int:
        raise NotImplementedError


class Car(Vehicle):

    def spots_requried(self) -> int:
        return 2

class Truck(Vehicle):

    def spots_requried(self) -> int:
        return 4

class AirPlane(Vehicle):

    def spots_requried(self) -> int:
        return 30



"""
(b) Write code in the __main__ block below to perform the following.

- Create a new parking garage.
- Write a loop and add 400 trucks and 199 cars to the parking garage.
- Ask the user for a year, make and colour of a car and instantiate a new
  object with these attributes.
- Add the newly created car to the parking garage with the following
  considerations:
  - If this raises a NoParkingAvailableError, print "Sorry, No parking" without
    crashing the program.
"""

if __name__ == "__main__":

    # TODO: write your main-block code below here
    parking_lot = Garage("123 street")

    for _ in range(400):
        parking_lot.park(Truck("Tsla", "Grey", 2023))

    for _ in range(199):
        parking_lot.park(Car("Benz", 'red', 2022))



    try:
        parking_lot.park(Car("Toyota", 'grey', 1990))
    except NoParkingAvailableError:
        print("Sorry, No parking")
