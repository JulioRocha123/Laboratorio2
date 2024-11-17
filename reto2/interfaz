from datos import *
while True:
    try:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            # Registrar hora de entrada
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            nombre_usuario = nombre_usuario.capitalize()
            hora_entrada = input("Ingrese la hora de entrada (formato HH:MM): ")
            # Crear un registro inicial con la hora de entrada
            logs.append([nombre_usuario, hora_entrada, None])  # None para la hora de salida

        elif opcion == "2":
            # Registrar hora de salida
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            nombre_usuario = nombre_usuario.capitalize()
            registro = buscar_usuario(nombre_usuario)
            if registro:
                hora_salida = input("Ingrese la hora de salida (formato HH:MM): ")
                registro[2] = hora_salida  # Actualizar la hora de salida
            else:
                print(f"No se encontró un registro activo para el usuario '{nombre_usuario}'.")

        elif opcion == "3":
            # Mostrar resultados
            if not logs:
                print("No hay registros para mostrar.")
            else:
                print("\n--- Resultados ---")
                usuarios = {}
                for registro in logs:
                    nombre_usuario = registro[0]
                    if nombre_usuario in usuarios:
                        usuarios[nombre_usuario] += 1
                    else:
                        usuarios[nombre_usuario] = 1

                # Mostrar resultados
                for usuario, accesos in usuarios.items():
                    print(f"Usuario: {usuario}, Número de accesos: {accesos}")

        elif opcion == "4":
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Ingrese un valor numerico.")
    except ValueError:
        print (f"Ingrese un valor numerico")