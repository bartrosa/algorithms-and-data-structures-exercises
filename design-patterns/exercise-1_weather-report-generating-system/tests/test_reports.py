import pytest
from reports.text_report import TextReport
from reports.json_report import JSONReport
from reports.html_report import HTMLReport

@pytest.fixture
def weather_data():
    return {
        "name": "London",
        "main": {"temp": 15, "humidity": 80},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 3.5}
    }

def test_text_report(weather_data):
    report = TextReport()
    expected_report = (
        "Weather Report for London:\n"
        "Temperature: 15°C\n"
        "Weather: clear sky\n"
        "Humidity: 80%\n"
        "Wind Speed: 3.5 m/s\n"
    )
    assert report.generate_report(weather_data) == expected_report

def test_json_report(weather_data):
    report = JSONReport()
    import json
    expected_report = json.dumps(weather_data, indent=4)
    assert report.generate_report(weather_data) == expected_report

def test_html_report(weather_data):
    report = HTMLReport()
    expected_report = (
        "<html><body><h1>Weather Report for London</h1>"
        "<p>Temperature: 15°C</p>"
        "<p>Weather: clear sky</p>"
        "<p>Humidity: 80%</p>"
        "<p>Wind Speed: 3.5 m/s</p>"
        "</body></html>"
    )
    assert report.generate_report(weather_data) == expected_report
