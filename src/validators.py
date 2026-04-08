def validate_weather(data):

    if data is None:
        return False

    # Temperature range check
    if not (-50 < data["temperature"] < 60):
        return False

    # Humidity check
    if not (0 <= data["humidity"] <= 100):
        return False

    return True