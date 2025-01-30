import requests

class MapService:
    @staticmethod
    def get_location_data(api_key, lat, lon):
        url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={api_key}"
        response = requests.get(url)
        return response.json()
