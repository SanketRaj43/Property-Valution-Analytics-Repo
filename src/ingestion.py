import os
import pandas as pd
from database import get_database_connection

def ingest_data(file_path):
    """Ingest data from a CSV file and store it in the PostgreSQL database."""
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Get the database connection
        engine = get_database_connection()
        if engine is None:
            print("Failed to connect to the database.")
            return

        # Ingest data into the database (replace 'properties' with your table name)
        df.to_sql('properties', con=engine, if_exists='replace', index=False)
        print("Data ingested successfully.")
    except Exception as e:
        print(f"Error ingesting data: {e}")

if __name__ == "__main__":
    # This is where you specify your actual file path
    file_path = "data/raw/Property_finder_set.csv"
    ingest_data(file_path)