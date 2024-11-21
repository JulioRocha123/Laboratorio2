from collections import deque
from operaciones import *

def simular_banco():
    cola_clientes = deque()
    registro_clientes = []
    while True:
        print("\nMenú del Banco:")
        print("1. Agregar cliente")
        print("2. Procesar cliente de la cola")
        print("3. Mostrar clientes registrados")
        print("4. Seleccionar cliente por nombre")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente(cola_clientes, registro_clientes)
        elif opcion == "2":
            if cola_clientes:
                cliente = cola_clientes.popleft()
                procesar_cliente(cliente)
            else:
                print("No hay clientes en la cola.")
        elif opcion == "3":
            mostrar_clientes(registro_clientes)
        elif opcion == "4":
            seleccionar_cliente(registro_clientes)
        elif opcion == "5":
            print("Cerrando el simulador de banco. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    simular_banco()
