import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database='hello_areum'
)

cursor = mydb.cursor()
query = ("select * from users")

cursor.execute(query)

print(cursor)

for ddd in cursor:
  print(ddd)
