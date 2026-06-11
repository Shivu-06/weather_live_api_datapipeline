from config import API_KEY

from src.extract import get_weather
from src.transform import transform_weather
from src.load import load_weather

data = get_weather("Bangalore", API_KEY)

df = transform_weather(data)

load_weather(df)

print("Weather ETL Completed Successfully!")