class Light:
    def turn_on(self) -> None:
        print("The light is on")
    
    def turn_off(self) -> None:
        print("The light is off")

class AirConditioner:
    def turn_on(self) -> None:
        print("The air conditioner is on")
    
    def turn_off(self) -> None:
        print("The air conditioner is off")
    
    def set_temperature(self, temperature: float) -> None:
        print(f"The temperature is set to {temperature} degrees")

class SecuritySystem:
    def arm(self) -> None:
        print("The security system is armed")
    
    def disarm(self) -> None:
        print("The security system is disarmed")

class SmartHomeFacade:
    def __init__(self) -> None:
        self._light = Light()
        self._air_conditioner = AirConditioner()
        self._security_system = SecuritySystem()

    def leave_home(self) -> None:
        print("Leaving home...")
        self._light.turn_off()
        self._air_conditioner.turn_off()
        self._security_system.arm()

    def arrive_home(self) -> None:
        print("Arriving home...")
        self._light.turn_on()
        self._air_conditioner.turn_on()
        self._air_conditioner.set_temperature(22)
        self._security_system.disarm()

def client_code(facade: SmartHomeFacade) -> None:
    facade.leave_home()
    print("\n")
    facade.arrive_home()

if __name__ == "__main__":
    facade = SmartHomeFacade()
    client_code(facade)
