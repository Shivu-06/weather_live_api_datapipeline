# 🌦️ Weather API ETL Pipeline

An end-to-end **Data Engineering project** that extracts real-time weather data from the OpenWeather API, transforms JSON responses into structured data using Python and Pandas, and loads the results into MySQL for storage and analysis.

## 📌 Project Overview

This project demonstrates how to build a simple ETL pipeline using real-world API data.

The pipeline retrieves weather information for Bengaluru, processes the response into a structured tabular format, and stores the resulting records in a MySQL database.

### 🔄 Pipeline Architecture

```text
OpenWeather API
       |
       v
    EXTRACT
  Python Requests
       |
       v
   TRANSFORM
 Python + Pandas
       |
       v
      LOAD
 SQLAlchemy + PyMySQL
       |
       v
   MySQL Database
```

## 🛠️ Tech Stack

| Category              | Technologies              |
| --------------------- | ------------------------- |
| Programming Language  | Python                    |
| Data Source           | OpenWeather API           |
| API Integration       | Requests                  |
| Data Transformation   | Pandas                    |
| Database              | MySQL                     |
| Database Connectivity | SQLAlchemy, PyMySQL       |
| Development Tools     | VS Code, Jupyter Notebook |
| Version Control       | Git, GitHub               |

## ⚙️ ETL Workflow

### 1. Extract — API Ingestion

* Connects to the OpenWeather API.
* Requests current weather information for Bengaluru.
* Retrieves the API response in JSON format.
* Uses a configurable API key.

### 2. Transform — Data Processing

* Extracts relevant weather attributes from the JSON response.
* Converts the extracted information into a Pandas DataFrame.
* Structures the data for database storage.

**Fields processed:**

* City
* Temperature
* Humidity
* Atmospheric pressure
* Wind speed
* Timestamp

### 3. Load — Database Storage

* Connects to MySQL using SQLAlchemy and PyMySQL.
* Loads the transformed DataFrame into a database table.
* Uses append mode to retain weather records from multiple pipeline runs.

This design provides a foundation for collecting historical weather observations over time.

## 📁 Project Structure

```text
weather_live_api_datapipeline/
│
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
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install the following before running the project:

* Python
* MySQL Server
* An OpenWeather API key

### 1. Clone the Repository

```bash
git clone https://github.com/Shivu-06/weather_live_api_datapipeline.git
cd weather_live_api_datapipeline
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Credentials

The current `main.py` imports `API_KEY` from a `config` module. Configure the API key and database connection settings before running the pipeline.

**Security:** Never commit API keys, database passwords, or other credentials to GitHub. Keep them in a local configuration file excluded through `.gitignore`, or use environment variables.

### 5. Configure MySQL

Ensure MySQL is running and that the database connection settings used by `src/load.py` match your local environment.

Create the target database and table if they are not created automatically by your loading code.

### 6. Run the Pipeline

```bash
python main.py
```

The script runs the extraction, transformation, and loading functions in sequence.

> **Note:** The setup steps assume your local configuration and MySQL database are correctly configured. Verify the connection settings and target table before running the pipeline.

## 📊 Example Output

The pipeline is designed to produce structured records similar to the following:

| city      | temperature | humidity | pressure | wind_speed | timestamp         |
| --------- | ----------: | -------: | -------: | ---------: | ----------------- |
| Bengaluru |        28.3 |       62 |     1011 |       14.7 | Example timestamp |

*Illustrative example only; actual values depend on the API response and execution time.*

## 🧠 Key Data Engineering Concepts

* ETL pipeline design
* REST API integration
* JSON data extraction
* Data transformation using Pandas
* Relational database loading
* SQLAlchemy database connectivity
* Historical data collection using append mode
* Modular Python project structure
* Configuration and credential management

## 🔮 Potential Future Improvements

* Schedule recurring pipeline executions.
* Add logging and exception handling.
* Implement API retry logic and request timeouts.
* Add data validation before database loading.
* Move credentials to environment variables.
* Containerize the pipeline using Docker.
* Build a dashboard to visualize historical weather trends.

These are potential extensions, not features claimed to be implemented in the current version.

## 👨‍💻 Author

**Shiva Kumar**

Aspiring Data Engineer focused on Python, SQL, ETL pipelines, Azure Data Engineering, and distributed data processing.

* GitHub: https://github.com/Shivu-06

---

⭐ If you find this project useful, feel free to explore the repository and its implementation.
