from sqlalchemy import create_engine


def load_weather(df):

    engine = create_engine(
        "mysql+pymysql://shiva:1234@localhost/weather_db"
    )

    df.to_sql(
        "weather",
        engine,
        if_exists="append",
        index=False
    )

    print("Weather data loaded successfully")