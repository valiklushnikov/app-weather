from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from .forms import SearchForm
from apps.weather.services.api_service import OpenWeatherMapError
from apps.weather.services.weather_service import fetch_weather_data
from .models import SearchHistory


@login_required
def home(request):
    weather = None
    search_history = None
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            user = request.user
            try:
                weather_data = fetch_weather_data(city)
                weather = SearchHistory.objects.create(user=user, **weather_data)
                search_history = SearchHistory.objects.select_related(
                    "weather_status"
                ).filter(user=user)[:10]
                form = SearchForm()
            except (ValueError, OpenWeatherMapError) as e:
                messages.error(request, e)
    else:
        form = SearchForm()
    return render(
        request,
        "weather/includes/home.html",
        {"form": form, "weather": weather, "history": search_history, "is_home": True},
    )
