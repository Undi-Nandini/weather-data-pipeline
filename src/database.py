import sqlite3
import os

# Create database folder path
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "weather_data.db")

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Cities table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities(
        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name TEXT UNIQUE
    )
    """)

    # Weather data table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data(
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        timestamp TEXT,
        temperature REAL,
        humidity INTEGER,
        pressure REAL,
        wind_speed REAL,
        condition TEXT,
        FOREIGN KEY(city_id) REFERENCES cities(city_id)
    )
    """)

    conn.commit()
    conn.close()

# Run automatically
if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully!")