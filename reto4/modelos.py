class Producto:
    """
    Clase para representar un producto en el inventario
    """
    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un nuevo producto
        
        Parámetros:
        - nombre: Nombre del producto
        - precio: Precio unitario del producto
        - cantidad: Cantidad inicial en stock
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def aumentar_stock(self, cantidad):
        """
        Aumenta la cantidad de productos en stock
        
        Parámetros:
        - cantidad: Número de unidades a añadir
        """
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Stock de {self.nombre} aumentado. Nuevo stock: {self.cantidad}")
        else:
            print("La cantidad a añadir debe ser positiva.")
    
    def disminuir_stock(self, cantidad):
        """
        Disminuye la cantidad de productos en stock
        
        Parámetros:
        - cantidad: Número de unidades a retirar
        """
        if 0 < cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Stock de {self.nombre} reducido. Nuevo stock: {self.cantidad}")
        else:
            print(f"Error: No hay suficiente stock de {self.nombre}")
    
    def __str__(self):
        """
        Representación en cadena del producto
        """
        return (f"Producto: {self.nombre} | "
                f"Precio: ${self.precio:.2f} | "
                f"Stock: {self.cantidad} unidades")
