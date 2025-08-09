from pydantic import BaseModel
from typing import List
from datetime import datetime


class SystemInfo(BaseModel):
    sunrise: datetime
    sunset: datetime


class WeatherDescription(BaseModel):
    main: str
    description: str


class WindInfo(BaseModel):
    speed: float


class MainInfo(BaseModel):
    temp: float
    temp_min: float
    temp_max: float
    feels_like: float
    humidity: float
    pressure: float


class WeatherValidator(BaseModel):
    weather: List[WeatherDescription]
    main: MainInfo
    wind: WindInfo
    sys: SystemInfo
    timezone: int
    name: str
