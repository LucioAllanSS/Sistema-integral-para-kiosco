from math import prod
from operator import index
from os import system
from turtle import clear
Banco = 0
Stock = []
Ventas = [Banco]
Compras = [Banco]

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
        func_Stock()
    elif entrada == 2:
        func_Ventas()
    elif entrada == 3:
        PProvedores()
    elif entrada == 4:
        PClientes()
    else:
        system("cls")
        Main()

def buscar(Item, Lista):
    for i in Lista:
        if Item == i[0]:
            return i
    

def func_Stock():
    print("Control de Stock")
    print(Stock)
    print("Porfavor, seleccione en el menu textual que desea hacer:")
    print("1. Volver a Inicio")
    print("2. Agregar Productos")
    print("3. Quitar Productos")

    entrada = int(input())

    if entrada == 1:
        system("cls")
        Main()
    elif entrada == 2:
        print("Ingrese el producto que desea agregar o actualizar")
        producto = input()
        index = buscar(producto, Stock)
        if index != None:
            print("si")
            print("Ingrese la cantidad en stock")
            cantidad = input()
            Stock[Stock.index(index)] = [producto, int(cantidad)]
            system("cls")
            func_Stock()
        else:
            print("Ingrese la cantidad en stock")
            cantidad = input()
            Stock.append([producto, int(cantidad)])
            system("cls")
            func_Stock()
    elif entrada == 3:
        producto = input()
        index = buscar(producto, Stock)
        Stock.pop(Stock.index(index))
        system("cls")
        func_Stock()

def func_Ventas():
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