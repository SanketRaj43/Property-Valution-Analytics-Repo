📌**Project Overview**
This project addresses the Real Estate Valuation Risk by resolving the "pricing anxiety" between buyers and sellers. Using a dataset of 1,460 residential records, our team performs a deep Exploratory Data Analysis (EDA) to assess whether properties are correctly priced or undervalued.

The core of this project is a Persistent Data Layer built on Postgres, allowing for scalable analysis of 79 features over 4 years of historical data.

🛠 **Tech Stack**
Database: Postgres (Relational Storage & Schema Management)

Language: Python 3.x (Pandas, SQLAlchemy, Psycopg2)

Testing: Great Expectations (Data Quality & Validation)

Visualization: Matplotlib, Seaborn, Tableau

🏗 **System Architecture & Workflow**
As a system designed for a team of four, the repository follows a modular structure to ensure strategic and financial control.

Data Ingestion: Raw Kaggle data is validated and loaded into Postgres.

Cleaning & Validation: Automated scripts handle missing values and "Anomalies".

Exploratory Data Analysis:

Univariate: Analyzing Sale Price and Overall Quality.

Bivariate: Correlating physical features with ROI.

Spatial: Neighborhood-based price distribution.

Insights Synthesis: Translating patterns into Business Value (e.g., higher realized sale prices).

📊 **The EDA Framework**
The system performs EDA through these engineering-led steps:

Data Profiling: Mapping the 79 features into Postgres schemas.

Quality Gates: Identifying outliers that deviate from expected market value.

Correlation Heatmaps: Identifying drivers of house size, type, and renovation history.

Seasonality Detection: Identifying peak months and festival seasons from the 4-year history.

🚀 **How to Run**
Setup Database: Initialize a Postgres DB named property_valuation_db.

Configure: Update config/config.yaml with your Postgres credentials.

Ingest Data: Run python src/ingestion.py to populate the tables.

Explore: Use the notebooks/ directory to run the team's specific analyses.

**Business Value Delivered**
Higher Margins: By identifying undervalued assets.

Improved Liquidity: By understanding the best time to sell (Seasonality).

Competitive Advantage: Data-backed geographic expansion strategy.
