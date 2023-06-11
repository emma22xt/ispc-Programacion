import conexion

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Conexion(host="localhost", user="root", password="Noah2016", database="proyecto_integrador_1")

# Conectar a la base de datos
conexion_bd.connect()

conexion_bd.ingresar_dispositivo_iot(modelo=1234, numero_serie="748923723", direccion_instalacion="av.mayo 2145 cordoba", fecha_instalacion="2021-09-15")

# Leer los propietarios desde la tabla
dispositivos_iot = conexion_bd.leer_dispositivos_iot()
for dispositivos in dispositivos_iot:
    print(dispositivos)

print("Fin tabla dispositivos")

# Desconectar de la base de datos
conexion_bd.disconnect()