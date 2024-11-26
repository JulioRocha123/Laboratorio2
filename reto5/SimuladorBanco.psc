Algoritmo SimuladorBanco
	
	Definir saldo, cantidad, opcion Como Entero
	
	saldo <- 1000
	
	Repetir
		Escribir "Saldo actual: ", saldo
		Escribir "1. Depositar, 2. Retirar, 3. Consultar saldo, 0. Salir"
		Leer opcion
		
		Según opcion Hacer
	Caso 1:
		Escribir "Ingrese cantidad a depositar:"
		Leer cantidad
		saldo <- saldo + cantidad
		Escribir "Depósito realizado. Saldo actual: ", saldo
	Caso 2:
		Escribir "Ingrese cantidad a retirar:"
		Leer cantidad
		Si cantidad <= saldo Entonces
			saldo <- saldo - cantidad
			Escribir "Retiro realizado. Saldo actual: ", saldo
		Sino
			Escribir "Saldo insuficiente para realizar el retiro."
		FinSi
	Caso 3:
		Escribir "El saldo actual es: ", saldo
	Caso 0:
		Escribir "Saliendo del sistema."
	De Otro Modo:
		Escribir "Opción no válida."
FinSegún
Hasta Que opcion = 0
FinAlgoritmo