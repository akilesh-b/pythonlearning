import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rathin8248.",
    database="fetch_db"
)

cursor = conn.cursor()

query = "SELECT * FROM employees"

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()