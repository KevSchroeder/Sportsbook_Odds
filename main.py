import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="12345", port="5433")

cur = conn.cursor()

query = f"""--sql
CREATE TABLE IF NOT EXISTS person (
id INT PRIMARY KEY,
age INT);
"""

cur.execute(query)

conn.commit()

cur.close()
conn.close()