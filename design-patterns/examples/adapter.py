class EuropeanCar:
    def charge_with_european_socket(self) -> str:
        return "Charging with European socket"

class AmericanCar:
    def charge_with_american_socket(self) -> str:
        return "Charging with American socket"

class CarCharger:
    def charge(self) -> str:
        pass

class EuropeanCarAdapter(CarCharger):
    def __init__(self, european_car: EuropeanCar) -> None:
        self._european_car = european_car

    def charge(self) -> str:
        return self._european_car.charge_with_european_socket()

class AmericanCarAdapter(CarCharger):
    def __init__(self, american_car: AmericanCar) -> None:
        self._american_car = american_car

    def charge(self) -> str:
        return self._american_car.charge_with_american_socket()

def client_code(car_charger: CarCharger) -> None:
    print(car_charger.charge())

if __name__ == "__main__":
    european_car = EuropeanCar()
    american_car = AmericanCar()

    european_car_adapter = EuropeanCarAdapter(european_car)
    american_car_adapter = AmericanCarAdapter(american_car)

    print("Client: Charging European car:")
    client_code(european_car_adapter)

    print("\nClient: Charging American car:")
    client_code(american_car_adapter)
