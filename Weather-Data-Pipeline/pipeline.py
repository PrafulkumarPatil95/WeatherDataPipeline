from scripts.extract import fetch_weather_data
from scripts.transform import transform_data
from scripts.load import load_data_to_db

def run_pipeline(api_key, city):
    """
    Runs the complete ETL pipeline: Extract, Transform, Load.
    """
    # Step 1: Extract
    print("Starting the pipeline...")
    raw_data = fetch_weather_data(api_key, city)
    if not raw_data:
        print("Pipeline stopped: Failed to fetch weather data.")
        return

    # Step 2: Transform
    transformed_data = transform_data(raw_data)
    print("Transformed Data:", transformed_data)

    # Step 3: Load
    load_data_to_db(transformed_data)
    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    api_key = "15a850fbfa7a371ffffebbb7db8d7a57"  # Replace with your actual API key
    city = "Mumbai"
    run_pipeline(api_key, city)
