import mysql.connector

class Conexion:
    def __init__(self, host, user, password, database):
        self.host = "stratocaster333"
        self.user = "root"
        self.password = "stratocaster333"
        self.database = "Proyectointegradorv01"
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión")

    def leer_dispositivos_iot(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM dispositivos"
            cursor.execute(query)
            propietarios = cursor.fetchall()
            cursor.close()
            return propietarios
        else:
            print("No hay conexión a la base de datos")

    def ingresar_dispositivo_iot(self, id, modelo, numero_serie, estado):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "INSERT INTO dispositivos (id, modelo, numero_serie, estado) VALUES (%s, %s, %s, %s)"
            values = ("12","Sensor de movimiento t1", "1357" ,"operativo",)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Datos insertados correctamente")
        else:
            print("No hay conexión a la base de datos")