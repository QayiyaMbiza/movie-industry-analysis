import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

database = r"C:\Users\bongo\OneDrive\Desktop\GitHub\Movie Analysis\Database\movie_industry.db"

connection = sqlite3.connect(database)

movies = pd.read_sql(
    """
    SELECT
        name,
        budget,
        gross,
        profit,
        ROI
    FROM movies
    WHERE budget > 0
      AND gross > 0;
    """,
    connection
)

plt.figure(figsize=(12,7))

plt.scatter(
    movies["budget"],
    movies["gross"],
    alpha=0.6
)

plt.xscale("log")
plt.yscale("log")

plt.title("Movie Budget vs Box Office Revenue")

plt.xlabel("Production Budget (Log Scale)")

plt.ylabel("Gross Revenue (Log Scale)")

plt.grid(True)

plt.show()

import numpy as np

log_budget = np.log10(movies["budget"])
log_gross = np.log10(movies["gross"])

m, b = np.polyfit(log_budget, log_gross, 1)

plt.figure(figsize=(12,7))

plt.scatter(
    movies["budget"],
    movies["gross"],
    alpha=0.5,
    label="Movies"
)

plt.plot(
    movies["budget"],
    10 ** (m * log_budget + b),
    linewidth=2,
    label="Trend"
)

plt.xscale("log")
plt.yscale("log")

plt.title("Relationship Between Production Budget and Box Office Revenue")

plt.xlabel("Production Budget (USD, Log Scale)")
plt.ylabel("Gross Revenue (USD, Log Scale)")

plt.legend()

plt.grid(True)

plt.show()

correlation = movies["budget"].corr(movies["gross"])

print(f"Correlation: {correlation:.3f}")