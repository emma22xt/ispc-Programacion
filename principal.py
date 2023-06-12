import conexion

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Conexion(host="localhost", user="root", password="stratocaster333", database="Proyectointegradorv01")

# Conectar a la base de datos
conexion_bd.connect()

conexion_bd.ingresar_dispositivo_iot(id=101, modelo=4762, numero_serie="748923723", estado= "Operativo")

# Leer los propietarios desde la tabla
dispositivos_iot = conexion_bd.leer_dispositivos_iot()
for dispositivos in dispositivos_iot:
    print(dispositivos)

print("Fin tabla dispositivos")

# Desconectar de la base de datos
conexion_bd.disconnect()