import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://user:password@localhost/farmers_website')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'your_google_api_key')
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'your_weather_api_key')
