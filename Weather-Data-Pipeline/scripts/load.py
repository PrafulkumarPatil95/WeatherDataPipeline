import sqlite3

def load_data_to_db(data, db_name="weather_data.db"):
    """
    Loads transformed weather data into a SQLite database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the weather table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            weather TEXT
        )
    """)

    # Insert the transformed data
    cursor.execute("""
        INSERT INTO weather (city, temperature, humidity, weather) 
        VALUES (?, ?, ?, ?)
    """, (data["city"], data["temperature"], data["humidity"], data["weather"]))
    conn.commit()
    conn.close()
    print(f"Data for {data['city']} loaded successfully into the database.")

if __name__ == "__main__":
    # Example transformed data
    sample_data = {
        "city": "London",
        "temperature": 20.0,
        "humidity": 65,
        "weather": "Clear"
    }
    load_data_to_db(sample_data)
