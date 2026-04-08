import sqlite3
import pandas as pd
import os

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "weather_data.db")

# Reports folder path
REPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "reports", "weather_report.txt")


def generate_report():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("SELECT * FROM weather_data", conn)

    print("\n WEATHER REPORT")
    print("======================")

    avg_temp = round(df["temperature"].mean(), 2)
    max_temp = df["temperature"].max()
    min_temp = df["temperature"].min()
    

    print("\n Average Temperature:", avg_temp)
    print(" Maximum Temperature:", max_temp)
    print("Minimum Temperature:", min_temp)
    print("\n Highest Temperature Record:")
    print(df.loc[df["temperature"].idxmax()])

    # ✅ SAVE REPORT TO FILE
    with open(REPORT_PATH, "w") as f:
        f.write("WEATHER REPORT\n")
        f.write("====================\n")
        f.write(f"Average Temperature: {avg_temp}\n")
        f.write(f"Max Temperature: {max_temp}\n")
        f.write(f"Min Temperature: {min_temp}\n")

    conn.close()
    print("\n Report saved in 'reports/weather_report.txt'")


if __name__ == "__main__":
    generate_report()

