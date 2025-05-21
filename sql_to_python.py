import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect(r"C:\Users\keanu\Desktop\Online_Intro\Python\sql_to_python\movies_portfolio.sqlite")

query = """
SELECT Genre, COUNT(*) AS genre_count
FROM [movie_analysis]
GROUP BY Genre
ORDER BY genre_count DESC;
"""

df = pd.read_sql_query(query, conn)
print(df)

plt.figure(figsize=(10, 6))
plt.bar(df['Genre'], df['genre_count'], color='orchid')
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.title("Genre Distribution of Movies")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

conn.close()
