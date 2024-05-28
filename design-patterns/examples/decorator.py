from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

class Coffee(Beverage):
    def cost(self) -> float:
        return 5.0

    def description(self) -> str:
        return "Coffee"

class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

class Milk(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 1.5

    def description(self) -> str:
        return f"{self._beverage.description()} + Milk"

class Sugar(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 0.5

    def description(self) -> str:
        return f"{self._beverage.description()} + Sugar"

def client_code(beverage: Beverage) -> None:
    print(f"Description: {beverage.description()}")
    print(f"Cost: {beverage.cost()}")

if __name__ == "__main__":
    coffee = Coffee()
    print("Client: I've got a plain coffee:")
    client_code(coffee)
    print("\n")

    coffee_with_milk = Milk(coffee)
    print("Client: Now I've got a coffee with milk:")
    client_code(coffee_with_milk)
    print("\n")

    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
    print("Client: Now I've got a coffee with milk and sugar:")
    client_code(coffee_with_milk_and_sugar)
