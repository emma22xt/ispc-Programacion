import mysql.connector
midb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="stratocaster333",
 database="Proyectointegradorv01"
)
print(midb)

cursor=midb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

cursor.execute("SELECT * FROM dispositivos")