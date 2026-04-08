import requests


API_KEY = "ed7516871cbe0dd80625caf91a679998"


def fetch_weather(city):

    url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("API RESPONSE:", data)

    if "main" not in data or "weather" not in data:
        print(f"Skipping {city} due to API error")
        return None

    weather = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],   
        "wind_speed": data["wind"]["speed"],    
        "condition": data["weather"][0]["description"]
    }

    return weather
if __name__ == "__main__":
    result = fetch_weather("Mumbai")
    print("\nProcessed Data:\n", result)