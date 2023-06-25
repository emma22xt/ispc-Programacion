import mysql.connector
from datetime import datetime

fecha_str = "2023-06-22"
fecha = datetime.strptime(fecha_str, "%Y-%m-%d")


class Conexion:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
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

    def leer_dispositivos(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM dispositivos"
            cursor.execute(query)
            dispositivos = cursor.fetchall()
            cursor.close()
            return dispositivos
        else:
            print("No hay conexión a la base de datos")

    def ingresar_dispositivos(self, modelo, numero_serie, estado):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "INSERT INTO dispositivos (modelo, numero_serie, estado) VALUES (%s, %s, %s)"
            values = (modelo, numero_serie, estado)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Datos insertados correctamente")
        else:
            print("No hay conexión a la base de datos")
                    
    def actualizar_dispositivo(self, modelo_nuevo, numero_serie_nuevo, estado_nuevo, id_dispositivo):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "UPDATE dispositivos SET modelo = %s, numero_serie = %s, estado = %s WHERE id = %s"
            values = (modelo_nuevo, numero_serie_nuevo, estado_nuevo, id_dispositivo)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Dispositivo actualizado correctamente")
        else:
            print("No hay conexión a la base de datos")
    
    def leer_instalaciones(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM instalaciones"
            cursor.execute(query)
            instalaciones = cursor.fetchall()
            cursor.close()
            return instalaciones
        else:
            print("No hay conexión a la base de datos")

    def ingresar_instalacion(self, dispositivo_id, direccion_instalacion, fecha_instalacion, coordenadas):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "INSERT INTO instalaciones (dispositivo_id, direccion_instalacion, fecha_instalacion, coordenadas) VALUES (%s, %s, %s, %s)"
            values = (dispositivo_id, direccion_instalacion, fecha_instalacion, coordenadas)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Instalación insertada correctamente")
        else:
            print("No hay conexión a la base de datos")
                    
    def actualizar_instalacion(self, dispositivo_id, direccion_instalacion, fecha_instalacion, coordenadas):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "UPDATE instalaciones SET direccion_instalacion = %s, fecha_instalacion = %s, coordenadas = %s WHERE id = %s"
            values = (dispositivo_id, direccion_instalacion, fecha_instalacion, coordenadas)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Instalación actualizada correctamente")
        else:
            print("No hay conexión a la base de datos")

