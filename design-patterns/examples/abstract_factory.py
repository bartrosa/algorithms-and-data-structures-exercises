from abc import ABC, abstractmethod

class AbstractEngine(ABC):
    @abstractmethod
    def specification(self) -> str:
        pass

class AbstractTire(ABC):
    @abstractmethod
    def specification(self) -> str:
        pass

class SedanEngine(AbstractEngine):
    def specification(self) -> str:
        return "Engine for Sedan"

class SUVEngine(AbstractEngine):
    def specification(self) -> str:
        return "Engine for SUV"

class SedanTire(AbstractTire):
    def specification(self) -> str:
        return "Tire for Sedan"

class SUVTire(AbstractTire):
    def specification(self) -> str:
        return "Tire for SUV"

class AbstractCarFactory(ABC):
    @abstractmethod
    def create_engine(self) -> AbstractEngine:
        pass
    
    @abstractmethod
    def create_tire(self) -> AbstractTire:
        pass

class SedanFactory(AbstractCarFactory):
    def create_engine(self) -> AbstractEngine:
        return SedanEngine()

    def create_tire(self) -> AbstractTire:
        return SedanTire()

class SUVFactory(AbstractCarFactory):
    def create_engine(self) -> AbstractEngine:
        return SUVEngine()

    def create_tire(self) -> AbstractTire:
        return SUVTire()

def client_code(factory: AbstractCarFactory) -> None:
    engine = factory.create_engine()
    tire = factory.create_tire()

    print(f"Engine: {engine.specification()}")
    print(f"Tire: {tire.specification()}")

if __name__ == "__main__":
    print("Client: Testing client code with the Sedan factory:")
    client_code(SedanFactory())
    print("\n")

    print("Client: Testing the same client code with the SUV factory:")
    client_code(SUVFactory())
