from datos import *
from matriz import *
def main():
    while True:
        # Mostrar menú
        mostrar_menu()
        
        # Solicitar opción al usuario
        try:
            opcion = input("Seleccione una opción (1-2): ").strip()
            
            if opcion == '1':
                # Solicitar dimensiones de la matriz
                filas, columnas = solicitar_dimensiones()
                
                # Solicitar temperatura crítica
                temp_critica = solicitar_temperatura_critica()
                
                # Generar matriz de temperaturas
                matriz_temperaturas = generar_matriz_temperaturas(filas, columnas)
                
                # Detectar temperaturas críticas
                ubicaciones_criticas = detectar_temperaturas_criticas(matriz_temperaturas, temp_critica)
                
                # Calcular estadísticas
                estadisticas = calcular_estadisticas(matriz_temperaturas)
                
                # Imprimir informe
                imprimir_informe_sensores(matriz_temperaturas, ubicaciones_criticas, estadisticas)
            
            elif opcion == '2':
                print("Saliendo del programa. ¡Hasta luego!")
                break
            
            else:
                print("Opción no válida. Por favor, seleccione 1 o 2.")
        
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

# Ejecutar la simulación
if __name__ == "__main__":
    main()