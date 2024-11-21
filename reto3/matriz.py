from datos import *
import random

def generar_matriz_temperaturas(filas, columnas, temp_min=20, temp_max=100):
    """
    Genera una matriz de temperaturas utilizando random.uniform()
    
    Parámetros:
    - filas: Número de filas en la matriz de sensores
    - columnas: Número de columnas en la matriz de sensores
    - temp_min: Temperatura mínima (por defecto 20°C)
    - temp_max: Temperatura máxima (por defecto 100°C)
    
    Retorna:
    - Matriz de temperaturas como lista de listas
    """
    # Establece la semilla para reproducibilidad aleatoria
    random.seed(random.randint(1, 1000))
    
    # Genera matriz de temperaturas aleatorias
    matriz = []
    for _ in range(filas):
        fila = [round(random.uniform(temp_min, temp_max), 2) for _ in range(columnas)]
        matriz.append(fila)
    
    return matriz

def detectar_temperaturas_criticas(matriz, temp_critica=80):
    """
    Detecta ubicaciones de sensores con temperaturas críticas
    
    Parámetros:
    - matriz: Matriz de temperaturas
    - temp_critica: Umbral de temperatura crítica (por defecto 80°C)
    
    Retorna:
    - Lista de tuplas con ubicaciones de sensores críticos
    """
    ubicaciones_criticas = []
    
    # Recorre la matriz con bucle for anidado
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > temp_critica:
                ubicaciones_criticas.append((i, j, matriz[i][j]))
    
    return ubicaciones_criticas

def calcular_estadisticas(matriz):
    """
    Calcula estadísticas básicas de la matriz de temperaturas
    
    Parámetros:
    - matriz: Matriz de temperaturas
    
    Retorna:
    - Diccionario con estadísticas
    """
    # Acumula temperaturas en una lista plana
    temperaturas_planas = [temp for fila in matriz for temp in fila]
    
    return {
        'promedio': round(sum(temperaturas_planas) / len(temperaturas_planas), 2),
        'maximo': max(temperaturas_planas),
        'minimo': min(temperaturas_planas)
    }

def imprimir_informe_sensores(matriz, ubicaciones_criticas, estadisticas):
    """
    Imprime un informe detallado de la simulación de la red de sensores
    """
    print("\n--- Informe de Red de Sensores ---")
    
    # Imprimir matriz de temperaturas
    print("Matriz de Temperaturas:")
    for fila in matriz:
        print(" ".join(f"{temp:6.2f}" for temp in fila))
    
    print("\nUbicaciones con Temperaturas Críticas:")
    if ubicaciones_criticas:
        for ubicacion in ubicaciones_criticas:
            print(f"Sensor [Fila {ubicacion[0]}][Columna {ubicacion[1]}]: {ubicacion[2]:.2f}°C")
    else:
        print("No se encontraron temperaturas críticas.")
    
    print("\nEstadísticas:")
    print(f"Total de sensores críticos: {len(ubicaciones_criticas)}")
    print(f"Temperatura promedio: {estadisticas['promedio']}°C")
    print(f"Temperatura máxima: {estadisticas['maximo']}°C")
    print(f"Temperatura mínima: {estadisticas['minimo']}°C")