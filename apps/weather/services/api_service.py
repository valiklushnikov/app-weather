from abc import ABC, abstractmethod
import requests
import os



class WeatherAPI(ABC):
    BASE_URL = ""
    API_KEY = ""

    def __init__(self, city) -> None:
        self.city = city
        self._data = None

    @abstractmethod
    def _get_data(self):
        pass


class OpenWeatherMapError(Exception):
    pass


class OpenWeatherMapAPI(WeatherAPI):
    def __init__(self, city) -> None:
        self.BASE_URL = os.environ.get("OPENWEATHER_URL")
        self.API_KEY = os.environ.get("OPENWEATHER_API_KEY")
        if not self.BASE_URL:
            raise OpenWeatherMapError("OPENWEATHER_URL environment variable not set.")
        if not self.API_KEY:
            raise OpenWeatherMapError("OPENWEATHER_API_KEY environment variable not set.")
        super().__init__(city)

    def _get_data(self) -> dict:
        try:
            response = requests.get(
                self.BASE_URL,
                params={"q": self.city, "appid": self.API_KEY, "units": "metric"},
            )
            data = response.json()
            if data.get("cod") != 200:
                raise OpenWeatherMapError(f"{data.get('message', 'Unknown error')}")
            return data
        except requests.RequestException as e:
            raise OpenWeatherMapError(e)
        except OpenWeatherMapError as e:
            raise ValueError(e)
        return {}

    @property
    def data(self) -> dict:
        if self._data is None:
            self._data = self._get_data()
        return self._data
