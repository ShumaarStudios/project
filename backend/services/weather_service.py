import requests

class WeatherService:
    @staticmethod
    def get_weather_data(location):
        api_key = 'your_weather_api_key'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        response = requests.get(url)
        return response.json()
