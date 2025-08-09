from .api_service import OpenWeatherMapAPI
from apps.weather.validation_schema import WeatherValidator
from apps.weather.utils import localize_sun_times
from apps.weather.models import WeatherStatus


def fetch_weather_data(city):
    response = OpenWeatherMapAPI(city)
    data = WeatherValidator(**response.data)

    sunrise, sunset = localize_sun_times(
        data.sys.sunrise, data.sys.sunset, data.timezone
    )

    return {
        "city": data.name,
        "temperature": data.main.temp,
        "temp_min": data.main.temp_min,
        "temp_max": data.main.temp_max,
        "feels_like": data.main.feels_like,
        "humidity": data.main.humidity,
        "pressure": data.main.pressure,
        "wind_speed": data.wind.speed,
        "sunrise": sunrise,
        "sunset": sunset,
        "description": data.weather[0].description,
        "weather_status": WeatherStatus.objects.filter(
            name=data.weather[0].main
        ).first(),
    }
