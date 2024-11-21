from modelos import Producto

class GestorInventario:
    """
    Clase para gestionar el inventario de productos
    """
    def __init__(self):
        """
        Inicializa un gestor de inventario vacío
        """
        self.productos = []
    
    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario
        
        Parámetros:
        - producto: Instancia de Producto a añadir
        """
        self.productos.append(producto)
        print(f"Producto {producto.nombre} añadido al inventario.")
    
    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario
        """
        print("\n--- INVENTARIO ACTUAL ---")
        if not self.productos:
            print("El inventario está vacío.")
            return
        
        for producto in self.productos:
            print(producto)
    
    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre
        
        Parámetros:
        - nombre: Nombre del producto a buscar
        
        Retorna:
        - Producto encontrado o None
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def realizar_compra(self, nombre, cantidad):
        """
        Simula la compra de un producto
        
        Parámetros:
        - nombre: Nombre del producto
        - cantidad: Cantidad a comprar
        """
        producto = self.buscar_producto(nombre)
        if producto:
            if producto.cantidad >= cantidad:
                producto.disminuir_stock(cantidad)
                total = producto.precio * cantidad
                print(f"Compra realizada. Total: ${total:.2f}")
            else:
                print(f"Error: Stock insuficiente de {nombre}")
        else:
            print(f"Producto {nombre} no encontrado.")
    
    def realizar_reposicion(self, nombre, cantidad):
        """
        Simula la reposición de stock de un producto
        
        Parámetros:
        - nombre: Nombre del producto
        - cantidad: Cantidad a reponer
        """
        producto = self.buscar_producto(nombre)
        if producto:
            producto.aumentar_stock(cantidad)
        else:
            print(f"Producto {nombre} no encontrado.")