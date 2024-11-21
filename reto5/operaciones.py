from collections import deque
from banco import CuentaBancaria
def procesar_cliente(cliente):
    while True:
        print(f"\nOperaciones para {cliente.titular}:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar saldo")
        print("4. Finalizar")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            print(cliente.depositar(cantidad))
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            print(cliente.retirar(cantidad))
        elif opcion == "3":
            print(cliente.consultar_saldo())
        elif opcion == "4":
            print(f"Finalizando operaciones para {cliente.titular}.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_cliente(cola_clientes, registro_clientes):
    nombre = input("Ingrese el nombre del cliente: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    nuevo_cliente = CuentaBancaria(nombre, saldo_inicial)
    cola_clientes.append(nuevo_cliente)
    registro_clientes.append(nuevo_cliente)
    print(f"Cliente {nombre} agregado exitosamente.")

def mostrar_clientes(registro_clientes):
    if registro_clientes:
        print("\nClientes registrados:")
        for cliente in registro_clientes:
            print(f"- {cliente.titular}, Saldo: ${cliente.saldo:.2f}")
    else:
        print("No hay clientes registrados.")

def seleccionar_cliente(registro_clientes):
    if not registro_clientes:
        print("No hay clientes registrados.")
        return
    nombre = input("Ingrese el nombre del cliente que desea seleccionar: ")
    for cliente in registro_clientes:
        if cliente.titular.lower() == nombre.lower():
            print(f"Cliente {cliente.titular} encontrado. Puede realizar operaciones:")
            procesar_cliente(cliente)
            return
    print(f"No se encontró un cliente con el nombre: {nombre}")
