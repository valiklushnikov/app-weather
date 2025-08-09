from django.contrib import admin

from .models import WeatherStatus, SearchHistory


@admin.register(WeatherStatus)
class WeatherStatusAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "image_path",
    )


@admin.register(SearchHistory)
class WeatherStatusAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "weather_status",
        "city",
        "temperature",
        "description",
        "search_date",
    )
