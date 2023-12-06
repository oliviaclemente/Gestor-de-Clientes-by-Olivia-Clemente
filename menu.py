
import os

def iniciar():
    while True:
        os.system('clear')
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Listar clientes ")
        print("[2] Buscar cliente ")
        print("[3] Añadir cliente ")
        print("[4] Modificar cliente ")
        print("[5] Borrar cliente ")
        print("[6] Cerrar el Manager ")
        print("========================")
        opcion = input("> ")
        os.system('clear')
        if opcion == '1':
            print("Listando los clientes...\n")
            print('Opcion 1') # Add this line
        if opcion == '2':
            print("Buscando un cliente...\n")
            print('Opcion 2') # Add this line
        if opcion == '3':
            print("Añadiendo un cliente...\n")
            print('Opcion 3') # Add this line
        if opcion == '4':
            print("Modificando un cliente...\n")
            print('Opcion 4') # Add this line
        if opcion == '5':
            print("Borrando un cliente...\n")
            print('Opcion 5') # Add this line
        if opcion == '6':
            print("Saliendo...\n")
            break
        input("\nPresiona ENTER para continuar...")


# Leer el DNI del cliente (2 ints y 1 char)
def leer_dni():
    while True:
        try:
            dni = int(input("DNI (2 ints y 1 char): "))
            if 1000000 > dni > 99999999:
                raise ValueError
        except ValueError:
            logger.error("El DNI no es válido.")
        else:
            return dni

# Validar el campo DNI
def validar_dni(dni):
    if len(str(dni)) == 8:
        logger.debug(f"El DNI {dni} es válido.")
        return True
    else:
        logger.debug(f"El DNI {dni} no es válido.")
        return False

# Añadir un cliente
def crear_cliente():
    dni = leer_dni()
    nombre = input("Nombre (de 2 a 30 chars): ").capitalize()
    apellido = input("Apellido (de 2 a 30 chars): ").capitalize()
    logger.debug(f"Se ha creado el cliente {dni}.")
    return dni, nombre, apellido

# Buscar un cliente
def buscar_cliente(dni):
    for cliente in db.Clientes.lista:
        if cliente.dni == dni:
            logger.debug(f"El cliente {dni} ha sido encontrado.")
            return cliente

# Modificar un cliente
def modificar_cliente(dni):
    cliente = buscar_cliente(dni)
    if cliente:
        nombre = input(f"Nombre (de 2 a 30 chars) [{cliente.nombre}]: ").capitalize()
        apellido = input(f"Apellido (de 2 a 30 chars) [{cliente.apellido}]: ").capitalize()
        logger.debug(f"Se ha modificado el cliente {dni}.")
        return dni, nombre, apellido
    else:
        logger.error("Cliente no encontrado.")
