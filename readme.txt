# Weather API ETL Pipeline

## Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline that fetches live weather data from the OpenWeather API, transforms the JSON response into a structured format, and loads it into a MySQL database for storage and analysis.

---

## Tech Stack

- Python
- Requests
- Pandas
- MySQL
- SQLAlchemy
- PyMySQL
- Jupyter Notebook
- VS Code

---

## Project Workflow

Weather API
↓
Extract
↓
Transform
↓
Load
↓
MySQL

---

## Project Structure

weather_api_de/

├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── notebook/
│   └── test_api.ipynb
│
├── sql/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

---

## ETL Process

### Extract

- Connects to OpenWeather API
- Fetches real-time weather data
- Returns raw JSON response

### Transform

Extracts required fields:

- City
- Temperature
- Humidity
- Pressure
- Wind Speed
- Timestamp

Converts JSON into a Pandas DataFrame.

### Load

- Connects to MySQL using SQLAlchemy
- Loads transformed data into the weather table
- Uses append mode to store historical weather records

---

## Sample Output

| city | temperature | humidity | pressure | wind_speed | timestamp |
|------|-------------|----------|----------|------------|------------|
| Bengaluru | 28.3 | 62 | 1011 | 14.7 | 2026-06-11 |

---

## Key Concepts Learned

- ETL Pipeline Design
- API Integration
- JSON Processing
- Data Transformation
- MySQL Integration
- SQLAlchemy Engine
- Append vs Replace Loading
- Timestamp Tracking
- Schema Evolution
- Automation using main.py

---

## How To Run

### Install Dependencies

```bash
pip install -r requirements.txt