from django.db import models
from django.contrib.auth import get_user_model
from django.templatetags.static import static


User = get_user_model()


class WeatherStatus(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def image_url(self):
        return static(self.image_path)

    class Meta:
        ordering = ("name",)
        verbose_name = "Weather Status"
        verbose_name_plural = "Weather Statuses"


class SearchHistory(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="search_history"
    )
    weather_status = models.ForeignKey(
        WeatherStatus, on_delete=models.CASCADE, related_name="searches"
    )
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    feels_like = models.FloatField()
    wind_speed = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    description = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Searching {self.city} by {self.user.email}"

    @property
    def temperature_fahrenheit(self):
        return round(self.temperature * 1.8) + 32

    class Meta:
        ordering = ("-search_date",)
        verbose_name = "Search History"
        verbose_name_plural = "Search Histories"
