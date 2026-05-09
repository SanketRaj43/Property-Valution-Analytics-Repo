import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

def get_database_connection():
    """Establish a connection to the PostgreSQL database using environment variables."""
    try:
        # Load environment variables from .env file
        load_dotenv()

        # Get database connection parameters from environment variables
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')

        # Create the database connection string
        connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

        # Create and return the SQLAlchemy engine
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None