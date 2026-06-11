import pandas as pd
from datetime import datetime


def transform_weather(data):

    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": datetime.now()
    }

    return pd.DataFrame([weather])