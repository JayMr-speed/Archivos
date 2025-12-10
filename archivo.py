
import os

archivo = "registros.txt"

def crear_archivo():

    if not os.path.exists(archivo):
        with open(archivo, "w") as f:
            print("Archivo creado exitosamente.")
    else:
        print("El archivo ya existe.")

def guardar_registros():
    nombre = input("nombre: ")
    matricula = input("matrícula: ")
    correo = input("correo: ")
    telefono = input("teléfono: ")

    with open(archivo, "a") as f:
        f.write(f"NOMBRE: {nombre}\n")
        f.write(f"MATRÍCULA: {matricula}\n")
        f.write(f"CORREO: {correo}\n")
        f.write(f"TELÉFONO: {telefono}\n")
        f.write("\n")  # Separador entre registros

    print("Registro guardado exitosamente.")

def leer_registro():
    archivo = open("JMR.txt", "r")
    print(archivo.read())



def actualizar_nombre():
    nombre_buscar = input("Ingrese el nombre que desea actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")

    with open("JMR.txt", "r") as f:
        lineas = f.readlines()

    with open("JMR.txt", "w") as f:
        for linea in lineas:
            if linea.startswith("NOMBRE:") and nombre_buscar in linea:
                f.write(f"NOMBRE: {nuevo_nombre}\n")
            else:
                f.write(linea)

    print("Nombre actualizado exitosamente.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear archivo")
        print("2. Guardar registros")
        print("3. Leer archivo")
        print("4. Actualizar nombre")
        print("5. Cerrar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            guardar_registros()
        elif opcion == "3":
            leer_registro()
        elif opcion == "4":
            actualizar_nombre()
        elif opcion == "5":
            print("Programa cerrado.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar menú principal
menu()
