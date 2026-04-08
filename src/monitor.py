import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "weather_data.db")

def show_status():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # total records
    cursor.execute("SELECT COUNT(*) FROM weather_data")
    total = cursor.fetchone()[0]

    # total cities
    cursor.execute("SELECT COUNT(*) FROM cities")
    cities = cursor.fetchone()[0]

    print("\nPIPELINE STATUS")
    print("----------------------")
    print(f"Total Records: {total}")
    print(f"Total Cities: {cities}")

    conn.close()


if __name__ == "__main__":
    show_status()