import json
from reports.abstract_report import WeatherReport

class JSONReport(WeatherReport):
    def generate_report(self, data):
        return json.dumps(data, indent=4)
