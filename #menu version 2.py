#menu version 2
import conexion
from datetime import datetime
def mostrar_menu():
    print("========================== MENU ==========================")
    print("¡Elija una opcion ingresando el numero correspondiente!")
    print("1_ Dispositivos")
    print("2_ Instalaciones")
    print("3_ Salir")
    print("=========================================================")

def mostrar_menu_dispositivos():
    print("#################### MENU DISPOSITIVOS ##################")
    print("1_ Actualizar dispositivo")
    print("2_ Insertar un nuevo dispositivo")
    print("#########################################################")

def mostrar_menu_instalaciones():
    print("******************** MENU INSTALACIONES *****************")
    print("1_ Actualizar instalación")
    print("2_ Insertar una nueva instalación")
    print("*********************************************************")

def actualizar_dispositivo():
    # Pedir datos del dispositivo a actualizar
    id_dispositivo = int(input("Ingrese el ID del dispositivo a actualizar: "))
    modelo_nuevo = str(input("Ingrese el nombre del nuevo modelo de dispositivo: ")) 
    numero_serie_nuevo = str(input("Ingrese el numero de serie del nuevo dispositivo: "))
    estado_nuevo = str(input("Ingrese el estado del dispositivo por ej: Operativo / No Operativo:  "))

    # Crear una instancia del conector de base de datos
    conexion_bd = conexion.Conexion(host="localhost", user="root", password="Talleres1999", database="proyecto_integrador_1")

    # Conectar a la base de datos
    conexion_bd.connect()

    # Actualizar el dispositivo en la base de datos
    conexion_bd.actualizar_dispositivo(modelo_nuevo, numero_serie_nuevo, estado_nuevo, id_dispositivo)

    # Desconectar de la base de datos
    conexion_bd.disconnect()

    print("Dispositivo actualizado correctamente")
    

def ingresar_dispositivo():
    # Pedir datos del nuevo dispositivo
    modelo = str(input("Ingrese el modelo del nuevo dispositivo: "))
    numero_serie = str(input("Ingrese el número de serie del nuevo dispositivo: "))
    estado = str(input("Ingrese el estado del nuevo dispositivo: "))

    # Crear una instancia del conector de base de datos
    conexion_bd = conexion.Conexion(host="localhost", user="root", password="Talleres1999", database="proyecto_integrador_1")

    # Conectar a la base de datos
    conexion_bd.connect()

    # Insertar el dispositivo en la base de datos
    conexion_bd.insertar_dispositivo(modelo, numero_serie, estado)

    # Desconectar de la base de datos
    conexion_bd.disconnect()

    print("Dispositivo insertado correctamente")
    
def ingresar_instalacion():
    #pedir datos de la instalacion a ingresar
    dispositivo_id = int (input("Ingrese el ID de la instalación: "))
    direccion_instalacion =str (input("Ingrese la dirección de la instalación: "))
    fecha_instalacion= int (input("Ingrese la nueva fecha de la instalación (AAAA-MM-DD): "))
    coordenadas = int (input("Ingrese las nuevas coordenadas de la instalación: "))

    # Crear una instancia del conector de base de datos
    conexion_bd = conexion.Conexion(host="localhost", user="root", password="Prueba!123", database="proyectointegradorv01")

    # Conectar a la base de datos
    conexion_bd.connect()

    # Actualizar la instalación en la base de datos
    conexion_bd.ingresar_instalacion(dispositivo_id, direccion_instalacion, fecha_instalacion, coordenadas)

    # Desconectar de la base de datos
    conexion_bd.disconnect()

    print("Instalación actualizada correctamente")
    
def actualizar_instalacion():
    # Pedir datos de la instalación a actualizar
    dispositivo_id = int(input("Ingrese el ID de la instalación a actualizar: "))
    direccion_instalacion = input("Ingrese la nueva dirección de la instalación: ")
    fecha_instalacion= input("Ingrese la nueva fecha de la instalación (AAAA-MM-DD): ")
    coordenadas = input("Ingrese las nuevas coordenadas de la instalación: ")

    # Crear una instancia del conector de base de datos
    conexion_bd = conexion.Conexion(host="localhost", user="root", password="Prueba!123", database="proyectointegradorv01")

    # Conectar a la base de datos
    conexion_bd.connect()

    # Actualizar la instalación en la base de datos
    conexion_bd.actualizar_instalacion(dispositivo_id, direccion_instalacion, fecha_instalacion, coordenadas)

    # Desconectar de la base de datos
    conexion_bd.disconnect()

    print("Instalación actualizada correctamente")
    
# Mostrar el menú y solicitar la opción al usuario
mostrar_menu()

opcion_menu =int (input("Ingrese la opción deseada: "))

if opcion_menu == 1:
    # Opción de dispositivos
    mostrar_menu_dispositivos()
    opcion_dispositivos = input("Ingrese la opción deseada: ")
    if opcion_dispositivos == "1":
        actualizar_dispositivo()
    elif opcion_dispositivos == "2":
        ingresar_dispositivo()
    else:
        print("Opción no válida")

elif opcion_menu == 2:
    # Opción de instalaciones
    mostrar_menu_instalaciones()
    opcion_instalaciones = input("Ingrese la opción deseada: ")
    if opcion_instalaciones == "1":
        actualizar_instalacion()
    elif opcion_instalaciones == "2":
        ingresar_instalacion()
    else:
        print("Opción no válida")

elif opcion_menu == 3:
    print("Hasta luego. ¡Gracias por utilizar el programa!")

else:
    print("Opción no válida")
