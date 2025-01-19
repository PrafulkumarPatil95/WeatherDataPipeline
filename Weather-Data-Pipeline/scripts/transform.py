def transform_data(raw_data):
    """
    Transforms raw weather data into a cleaned format for loading into a database.
    """
    transformed_data = {
        "city": raw_data["name"],
        "temperature": round(raw_data["main"]["temp"] - 273.15, 2),  # Convert Kelvin to Celsius
        "humidity": raw_data["main"]["humidity"],
        "weather": raw_data["weather"][0]["description"].capitalize()  # Capitalize the description
    }
    return transformed_data

if __name__ == "__main__":
    # Example raw data from the API
    sample_raw_data = {
        "name": "London",
        "main": {"temp": 293.15, "humidity": 65},
        "weather": [{"description": "clear sky"}]
    }
    transformed_data = transform_data(sample_raw_data)
    print("Transformed Data:", transformed_data)
