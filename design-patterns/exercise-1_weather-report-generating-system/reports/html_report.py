from reports.abstract_report import WeatherReport

class HTMLReport(WeatherReport):
    def generate_report(self, data):
        report = f"<html><body><h1>Weather Report for {data['name']}</h1>"
        report += f"<p>Temperature: {data['main']['temp']}°C</p>"
        report += f"<p>Weather: {data['weather'][0]['description']}</p>"
        report += f"<p>Humidity: {data['main']['humidity']}%</p>"
        report += f"<p>Wind Speed: {data['wind']['speed']} m/s</p>"
        report += "</body></html>"
        return report
