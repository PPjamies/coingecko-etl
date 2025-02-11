# **CoinGecko ETL**

A scheduled ETL workflow using Apache Airflow, Python, PostgreSQL, and Docker to fetch Bitcoin data from the CoinGecko
API, process it, and store it in a PostgreSQL database.

Tag: Data Engineering

## **Overview**

This ETL pipeline:

- Queries the CoinGecko API for Bitcoin data.
- Computes unavailable supply and issuance progress.
- Stores the processed data in a PostgreSQL database.
- Runs on a scheduled basis using Apache Airflow.

## **Tech Stack**

- Apache Airflow – Task scheduling & orchestration
- Python – Data processing
- PostgreSQL – Data storage
- Docker – Containerization

## **Setup**

Clone the repository:

```bash
git clone https://github.com/PPjamies/coingecko-etl.git 
cd coingecko-etl
 ```

Start the ETL pipeline using Docker Compose:

```bash
 docker-compose build && docker-compose up -d
 ```

Access the Airflow UI:
```http://localhost:8080```

Trigger the DAG to run the ETL process.

## **Future Improvements**

- Support for multiple cryptocurrencies.
- Data validation & error handling.
