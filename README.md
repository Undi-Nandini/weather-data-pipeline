# Weather Data Pipeline System

##  Overview
This project implements an end-to-end ETL pipeline that extracts real-time weather data from the OpenWeatherMap API, processes it, and stores it in a SQLite database.

## Features
- API integration using OpenWeatherMap
- ETL pipeline (Extract, Transform, Load)
- Data validation and error handling
- SQLite database storage
- Monitoring system
- Reporting system

## Tech Stack
- Python
- SQLite
- Pandas
- Requests

## How to Run
1. Add API key in api_client.py
2. Run database setup:
   python src/database.py
3. Run ETL pipeline:
   python src/etl_pipeline.py
4. Generate report:
   python src/reporter.py

## Output
- Weather data stored in database
- Reports saved in /reports folder
- Logs monitored

## Future Improvements
- Real-time dashboard
- Alert system
- Cloud deployment