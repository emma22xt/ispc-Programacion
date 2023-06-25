import mysql.connector
midb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Prueba!123",
 database="proyectointegradorv01"
)
print(midb)

cursor=midb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)