import mysql.connector
midb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Noah2016",
 database="Proyecto_integrador_1"
)
print(midb)

cursor=midb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)