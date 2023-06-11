import mysql.connector

class Conexion:
    def __init__(self, host, user, password, database):
        self.host = "localhost"
        self.user = "root"
        self.password = "Noah2016"
        self.database = "proyecto_integrador_1"
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
            query = "SELECT * FROM dispositivos_iot"
            cursor.execute(query)
            propietarios = cursor.fetchall()
            cursor.close()
            return propietarios
        else:
            print("No hay conexión a la base de datos")

    def ingresar_dispositivo_iot(self, modelo, numero_serie, direccion_instalacion, fecha_instalacion):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "INSERT INTO dispositivos_iot (modelo,numero_serie,direccion_instalacion, fecha_instalacion) VALUES (%s, %s, %s, %s)"
            values = (modelo, numero_serie, direccion_instalacion, fecha_instalacion)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Datos insertados correctamente")
        else:
            print("No hay conexión a la base de datos")