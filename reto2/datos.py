# Lista para almacenar los registros de actividad
logs = []

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Registrar hora de entrada")
    print("2. Registrar hora de salida")
    print("3. Mostrar resultados")
    print("4. Salir")

def buscar_usuario(nombre):
    """Busca un registro en logs por el nombre del usuario."""
    for registro in logs:
        if registro[0] == nombre and registro[2] is None:  # Si no tiene salida registrada
            return registro
    return None