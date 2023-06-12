cursor=midb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)