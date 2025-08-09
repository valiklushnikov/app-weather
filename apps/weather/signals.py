from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import WeatherStatus


@receiver(post_migrate)
def populate_weather_status(sender, **kwargs):
    if sender.name != "apps.weather":
        return
    data = [
        {"name": "Clear", "image_path": "images/weather_status/clear.webp"},
        {"name": "Clouds", "image_path": "images/weather_status/clouds.png"},
        {"name": "Rain", "image_path": "images/weather_status/rain.png"},
        {"name": "Snow", "image_path": "images/weather_status/snow.png"},
        {"name": "Drizzle", "image_path": "images/weather_status/drizzle.png"},
        {
            "name": "Thunderstorm",
            "image_path": "images/weather_status/thunderstorm.png",
        },
        {"name": "Haze", "image_path": "images/weather_status/haze.png"},
    ]
    for item in data:
        WeatherStatus.objects.update_or_create(
            name=item["name"], defaults={"image_path": item["image_path"]}
        )
