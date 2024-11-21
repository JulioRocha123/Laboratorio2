def solicitar_dimensiones():
    """
    Solicita al usuario las dimensiones de la matriz de sensores
    
    Retorna:
    - Tupla con número de filas y columnas
    """
    while True:
        try:
            filas = int(input("Ingrese el número de filas de la matriz de sensores: "))
            columnas = int(input("Ingrese el número de columnas de la matriz de sensores: "))
            
            # Validar dimensiones
            if filas > 0 and columnas > 0:
                return filas, columnas
            else:
                print("Error: Las dimensiones deben ser números positivos.")
        
        except ValueError:
            print("Error: Por favor, ingrese números enteros válidos.")
def solicitar_temperatura_critica():
    """
    Solicita al usuario el umbral de temperatura crítica
    
    Retorna:
    - Temperatura crítica
    """
    while True:
        try:
            temp_critica = float(input("Ingrese el umbral de temperatura crítica (°C): "))
            
            # Validar temperatura crítica
            if temp_critica > 0:
                return temp_critica
            else:
                print("Error: La temperatura debe ser un número positivo.")
        
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def mostrar_menu():
    """
    Muestra el menú principal de opciones
    """
    print("\n--- Simulador de Red de Sensores ---")
    print("1. Generar Temperaturas")
    print("2. Salir")