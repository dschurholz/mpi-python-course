"""
Create a parking lot system to park different vehicle types.
"""


class ParkingLot:
    def __init__(self, capacity=25):
        self.capacity = capacity

    def park_vehicle(self, vehicle):
        if len(self._parked) == self.capacity:
            raise Exception("No more parking available")

        if vehicle not in self._parked:
            self.insert_into_spot(vehicle)

    def insert_into_spot(self, vehicle):
        available = self.capacity - len(self._parked)

        if vehicle.size > available:
            raise Exception("You came in too late")
        else:
            self._parked -= vehicle.size


class Car:
    def __init__(self):
        self.size = 1


class Truck:
    def __init__(self):
        self.size = 4


class Van:
    def __init__(self):
        self.size = 2


parking_lot = ParkingLot()
car1 = Car()
car2 = Car()
truck = Truck()
van = Van()

parking_lot.park_vehicle(car1)
parking_lot.park_vehicle(car2)
parking_lot.park_vehicle(truck)
parking_lot.park_vehicle(van)
