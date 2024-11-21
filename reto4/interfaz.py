def mostrar_menu_principal():
    """
    Muestra el menú principal del sistema de gestión de inventario
    """
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Realizar Compra")
    print("4. Reponer Stock")
    print("5. Salir")

from modelos import Producto
from inventario import GestorInventario

def main():
    # Crear gestor de inventario
    gestor = GestorInventario()
    
    # Productos iniciales
    productos_iniciales = [
        Producto("Laptop", 1200.00, 10),
        Producto("Smartphone", 600.00, 25),
        Producto("Tablet", 350.00, 15)
    ]
    
    # Agregar productos iniciales
    for producto in productos_iniciales:
        gestor.agregar_producto(producto)
    
    # Bucle principal del menú
    while True:
        mostrar_menu_principal()
        
        try:
            opcion = input("Seleccione una opción (1-5): ").strip()
            
            if opcion == '1':
                # Agregar nuevo producto
                nombre = input("Ingrese nombre del producto: ")
                precio = float(input("Ingrese precio del producto: "))
                cantidad = int(input("Ingrese cantidad inicial: "))
                
                nuevo_producto = Producto(nombre, precio, cantidad)
                gestor.agregar_producto(nuevo_producto)
            
            elif opcion == '2':
                # Mostrar inventario
                gestor.mostrar_inventario()
            
            elif opcion == '3':
                # Realizar compra
                nombre = input("Ingrese nombre del producto a comprar: ")
                cantidad = int(input("Ingrese cantidad a comprar: "))
                gestor.realizar_compra(nombre, cantidad)
            
            elif opcion == '4':
                # Reponer stock
                nombre = input("Ingrese nombre del producto a reponer: ")
                cantidad = int(input("Ingrese cantidad a reponer: "))
                gestor.realizar_reposicion(nombre, cantidad)
            
            elif opcion == '5':
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            
            else:
                print("Opción no válida. Intente nuevamente.")
        
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()