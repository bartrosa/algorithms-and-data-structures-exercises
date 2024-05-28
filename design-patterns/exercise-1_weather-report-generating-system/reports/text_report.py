from reports.abstract_report import WeatherReport

class TextReport(WeatherReport):
    def generate_report(self, data):
        report = f"Weather Report for {data['name']}:\n"
        report += f"Temperature: {data['main']['temp']}°C\n"
        report += f"Weather: {data['weather'][0]['description']}\n"
        report += f"Humidity: {data['main']['humidity']}%\n"
        report += f"Wind Speed: {data['wind']['speed']} m/s\n"
        return report
