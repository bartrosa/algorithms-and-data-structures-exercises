import pytest
from api.api import fetch_weather

@pytest.mark.parametrize("city,expected", [
    ("London", True),
    ("NonExistentCity", False)
])
def test_fetch_weather(monkeypatch, city, expected):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_get(*args, **kwargs):
        if args[0].endswith("London"):
            return MockResponse({"name": "London", "main": {"temp": 15}}, 200)
        return MockResponse(None, 404)

    monkeypatch.setattr("requests.get", mock_get)
    
    result = fetch_weather(city)
    if expected:
        assert result is not None
        assert result["name"] == "London"
    else:
        assert result is None
