import requests

def fetch_weather_data(api_key, city):
    """
    Fetch weather data from OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}K")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description']}")
        return data  # Return the raw data
    else:
        print(f"Failed to fetch weather data. Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None  # Return None in case of failure

if __name__ == "__main__":
    api_key = "15a850fbfa7a371ffffebbb7db8d7a57"  # Replace with your actual API key
    city = "Chicago"
    raw_data = fetch_weather_data(api_key, city)
    print("Raw Data:", raw_data)
