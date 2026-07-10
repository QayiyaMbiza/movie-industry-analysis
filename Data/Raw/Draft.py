# Movie Industry Analysis

# Import Libraries
import os
from pathlib import Path

import pandas as pd
import numpy as np
import sqlite3

# File Paths
raw = r"C:\Users\bongo\OneDrive\Desktop\GitHub\Movie Analysis\Data\Raw\movies.csv\movies.csv"
clean = r"C:\Users\bongo\OneDrive\Desktop\GitHub\Movie Analysis\Data\Clean"

# Create Clean Directory
os.makedirs(clean, exist_ok=True)

print("=*" * 60)
print("Movie Industry Analysis - ETL")
print("=*" * 60)

# Extraction of data
movies = pd.read_csv(raw)

print(f"\nRows  : {movies.shape[0]:,}")
print(f"Columns: {movies.shape[1]:,}")

print("\nData successfully loaded into a pandas DataFrame.")

# Saving the cleaned data to the clean dataset.

clean_file = os.path.join(clean, "cleaned_movies.csv")

movies.to_csv(clean_file, index=False)

print("\nClean data saved successfully to:", clean_file)


# Initial Data Exploration
print("\n" + "=" * 60)
print("Initial Data Exploration")
print("=" * 60)

print("\nFirst 5 rows of the dataset:")
print(movies.head())

print("\nLast 5 rows of the dataset:")
print(movies.tail())

print("\nDataset Dimensions:")
print(f"Rows: {movies.shape[0]:,}")
print(f"Columns: {movies.shape[1]:,}")

print("\nColumn Names:")
print(movies.columns.tolist())

print("\nData Types:")
print(movies.dtypes)

print("\nSummary Statistics:")
print(movies.describe(include='all'))

print("\nMissing Values:")
print(movies.isnull().sum())

print("\nDuplicate Records:")
duplicates = movies.duplicated().sum()

print("\nDuplicate Records")
if duplicates > 0:
    print(movies[movies.duplicated()])
else:
    print("No duplicate records found.")

# Initial Quality Report
print("\n" + "=" * 60)
print("INITIAL DATA QUALITY REPORT")
print("=" * 60)

quality_report = pd.DataFrame({

    "Metric": [
        "Rows",
        "Columns",
        "Missing Values",
        "Duplicate Records"
    ],

    "Value": [
        movies.shape[0],
        movies.shape[1],
        movies.isna().sum().sum(),
        duplicates
    ]

})

print(quality_report)


# SQLite Database
DATABASE_FOLDER = r"C:\Users\bongo\OneDrive\Desktop\GitHub\Movie Analysis\Database"

os.makedirs(DATABASE_FOLDER, exist_ok=True)

database_path = os.path.join(DATABASE_FOLDER, "movie_industry.db")

connection = sqlite3.connect(database_path)

print("\nSQLite database created successfully.")

# Load clean dataset into SQLite
movies.to_sql(
    name="movies",
    con=connection,
    if_exists="replace",
    index=False
)

print("Clean dataset successfully loaded into SQLite.")

cursor = connection.cursor()


#Verify Row Count in the Database
cursor.execute("""
SELECT COUNT(*)
FROM movies;
""")

row_count = cursor.fetchone()[0]

print(f"\nRows loaded into SQLite: {row_count:,}")

#Verify the number of columns in the database
cursor.execute("""
PRAGMA table_info(movies);
""")

columns = cursor.fetchall()

print(f"Columns in database: {len(columns)}")

#Display Column Names
print("\nDatabase Columns")

for column in columns:
    print(column[1])

#Test Query 1
print("\nFirst Five Movies")

query = """
SELECT *
FROM movies
LIMIT 5;
"""

print(pd.read_sql(query, connection))

#Test Query 2
query = """
SELECT
    COUNT(*) AS TotalMovies,
    AVG(gross) AS AverageRevenue,
    MAX(gross) AS HighestRevenue
FROM movies;
"""

print("\nSummary Statistics")

print(pd.read_sql(query, connection))