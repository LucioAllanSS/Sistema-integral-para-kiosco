
from os import system
from turtle import clear


def Main():
    print("Bienvenido al Programa Kiosco.")
    print("Porfavor, introduzca en el menu textual que desea hacer:")
    print("1. Control de Stock")
    print("2. Control de Ventas")
    print("3. Pedidos a proveedores")
    print("4. Pedidos a clientes")
    print("(Indique el numero del menu que desea abrir y pulse enter)")
    
    entrada = int(input())
    system("cls")

    if entrada == 1:
        Stock()
    elif entrada == 2:
        Ventas()
    elif entrada == 3:
        PProvedores()
    elif entrada == 4:
        PClientes()

def Stock():
    print("Control de Stock")
    print("Porfavor, seleccione en el menu textual que desea hacer:")
    print("1. Volver a Inicio")

    entrada = int(input())
    system("cls")

    if entrada == 1:
        Main()

def Ventas():
    print("Control de Ventas")
    print("Porfavor, seleccione en el menu textual que desea hacer:")
    print("1. Volver a Inicio")

    entrada = int(input())
    system("cls")

    if entrada == 1:
        Main()

def PProvedores():
    print("Pedidos a Proveedores")
    print("Porfavor, seleccione en el menu textual que desea hacer:")
    print("1. Volver a Inicio")

    entrada = int(input())
    system("cls")

    if entrada == 1:
        Main()

def PClientes():
    print("Pedidos de Clientes")
    print("Porfavor, seleccione en el menu textual que desea hacer:")
    print("1. Volver a Inicio")

    entrada = int(input())
    system("cls")

    if entrada == 1:
        Main()

Main()