from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class Sedan(Car):
    def operation(self) -> str:
        return "Producing a Sedan"

class SUV(Car):
    def operation(self) -> str:
        return "Producing an SUV"

class CarFactory(ABC):
    @abstractmethod
    def factory_method(self) -> Car:
        pass
    
    def create_car(self) -> str:
        car = self.factory_method()
        result = f"CarFactory:The factory has created a car: {car.operation()}"
        return result

class SedanFactory(CarFactory):
    def factory_method(self) -> Car:
        return Sedan()

class SUVFactory(CarFactory):
    def factory_method(self) -> Car:
        return SUV()

def client_code(factory: CarFactory) -> None:
    print(f"Client:I'm not aware of the factory's class, but it still works.\n"
          f"{factory.create_car()}", end="")

if __name__ == "__main__":
    print("App: Launched with the SedanFactory.")
    client_code(SedanFactory())
    print("\n")

    print("App: Launched with the SUVFactory.")
    client_code(SUVFactory())
