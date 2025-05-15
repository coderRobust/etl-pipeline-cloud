# 🛠️ ETL Pipeline with Cloud-Ready Integration

Simple Python ETL pipeline using Pandas and SQLAlchemy. Easily extendable to AWS S3, Azure Blob, PostgreSQL, BigQuery, etc.

## Features
- Extracts CSV files
- Cleans and transforms data
- Loads into SQLite (can swap for cloud DBs)

## Run Instructions

### 1. Prepare CSV
Put your CSV file in the `data/` folder as `sales_data.csv`.

### 2. Install dependencies
bash
pip install -r requirements.txt
3. Run the ETL Pipeline

python etl/pipeline.py
4. Verify the DB
Check etl_pipeline.db for the loaded table.