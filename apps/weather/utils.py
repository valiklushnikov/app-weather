from datetime import timedelta


def localize_sun_times(sunrise, sunset, tz_offset):
    offset = timedelta(seconds=tz_offset)
    sunrise_local = sunrise + offset
    sunset_local = sunset + offset
    return sunrise_local, sunset_local
