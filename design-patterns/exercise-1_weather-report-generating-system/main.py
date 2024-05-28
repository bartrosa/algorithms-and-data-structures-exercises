from reports.report_factory import ReportFactory
from api.api import fetch_weather

def main():
    city = input("Enter the city name: ")
    format_type = input("Enter the report format (text/json/html): ")

    weather_data = fetch_weather(city)
    if weather_data:
        report = ReportFactory.get_report(format_type)
        print(report.generate_report(weather_data))
    else:
        print("Error fetching weather data")

if __name__ == "__main__":
    main()
