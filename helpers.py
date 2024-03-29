# Import modules
import os
import platform

# Define function
def limpiar_pantalla():
    print("Limpiando pantalla...")
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Define function
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    if mensaje:
        print(mensaje)
    while True:
        texto = input("> ")
        print("DEBUG: El texto introducido tiene", len(texto), "caracteres.")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        
import re
def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    print("DNI correcto.")
    return True