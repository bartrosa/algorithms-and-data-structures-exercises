from abc import ABC, abstractmethod

class WeatherReport(ABC):
    @abstractmethod
    def generate_report(self, data):
        pass
