from api_client import fetch_weather
from validators import validate_weather
import sqlite3
import os
import datetime

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "weather_data.db")


def run_pipeline():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cities = ["Mumbai", "Delhi", "Chennai"]

    for city in cities:

        print(f"\nFetching data for {city}...")

        data = fetch_weather(city)

        # Skip if API failed
        if not validate_weather(data):
            print(f" Invalid data for {city},skipping...")
            continue

        try:
            # Insert city if not exists
            cursor.execute(
                "INSERT OR IGNORE INTO cities(city_name) VALUES(?)",
                (city,)
            )

            # Get city_id
            cursor.execute(
                "SELECT city_id FROM cities WHERE city_name=?",
                (city,)
            )
            city_id = cursor.fetchone()[0]

            # Insert weather data
            cursor.execute("""
            INSERT INTO weather_data
            (city_id, timestamp, temperature, humidity, pressure, wind_speed, condition)
            VALUES (?, datetime('now'), ?, ?, ?, ?, ?)
            """,
            (
                city_id,
                data["temperature"],
                data["humidity"],
                data["pressure"],
                data["wind_speed"],
                data["condition"]
            ))

        
            print(f"{city} inserted at {datetime.datetime.now()}")

        except Exception as e:
            print(f" Error inserting {city}: {e}")

    conn.commit()
    conn.close()
    print("\n ETL Pipeline completed successfully!")


# Run pipeline
if __name__ == "__main__":
    run_pipeline()