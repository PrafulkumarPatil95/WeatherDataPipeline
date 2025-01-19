# Weather Data Pipeline

Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline to process weather data. It fetches real-time weather data from the OpenWeatherMap API, processes the data (e.g., temperature conversion), and stores it in a SQLite database for further analysis.

Features

	•	Extract: Fetch real-time weather data from the OpenWeatherMap API.
	•	Transform: Clean and standardize the data, converting temperatures from Kelvin to Celsius.
	•	Load: Store the transformed data in a SQLite database.
	•	Multiple Cities: Supports processing weather data for multiple cities.
	•	Error Handling: Robust handling of API errors and invalid inputs.

Project Structure

Weather-Data-Pipeline/
├── scripts/
│   ├── extract.py        # Extracts weather data from OpenWeatherMap API
│   ├── transform.py      # Transforms raw data into a cleaned format
│   ├── load.py           # Loads data into a SQLite database
├── pipeline.py           # Orchestrates the entire ETL process
├── weather_data.db       # SQLite database for storing weather data
├── requirements.txt      # Python dependencies
├── .gitignore            # Excludes unnecessary files from Git
└── README.md             # Documentation for the project

How to Run the Project

1. Clone the Repository

git clone https://github.com/PrafulkumarPatil95/WeatherDataPipeline.git
cd Weather-Data-Pipeline

2. Install Dependencies

Install the required Python libraries:

pip install -r requirements.txt

3. Run the Pipeline

Execute the ETL pipeline:

python pipeline.py

4. Query the Database

You can query the SQLite database to analyze the stored weather data:

sqlite3 weather_data.db

Example SQL Query:

SELECT * FROM weather;

Requirements

	•	Python 3.8 or later
	•	An active API key from OpenWeatherMap
	•	Dependencies listed in requirements.txt:
	•	requests
	•	sqlite3

Example Output

Console Output:

Processing weather data for Chicago...
Weather in Chicago:
Temperature: 3.15°C
Humidity: 65%
Condition: Clear sky
Data for Chicago loaded successfully into the database.

Processing weather data for London...
Weather in London:
Temperature: 10.45°C
Humidity: 70%
Condition: Overcast clouds
Data for London loaded successfully into the database.

ETL pipeline completed successfully.

Database Query:

sqlite> SELECT * FROM weather;
Chicago|3.15|65|Clear sky
London|10.45|70|Overcast clouds

Future Enhancements

	•	Add support for scheduled runs using cron jobs or Airflow.
	•	Implement data visualization using Matplotlib or Tableau.
	•	Deploy the pipeline to the cloud for real-time processing.

Contributing

If you’d like to contribute to this project:
	1.	Fork the repository.
	2.	Create a feature branch:

git checkout -b feature-name


	3.	Commit your changes and push:

git commit -m "Add new feature"
git push origin feature-name


	4.	Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Prafulkumar Patil
	•	GitHub: @PrafulkumarPatil95

