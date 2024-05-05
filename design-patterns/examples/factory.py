from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()


class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()


def vehicle_client(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    print(vehicle.drive())


if __name__ == "__main__":
    car_factory = CarFactory()
    bike_factory = BikeFactory()
    vehicle_client(car_factory)
    vehicle_client(bike_factory)
