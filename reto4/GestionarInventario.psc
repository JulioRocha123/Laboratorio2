Algoritmo GestionarInventario
	Definir opcion, cantidad_a_comprar, cantidad_a_vender Como Entero
	Definir stock Como Entero
	stock <- 0
	Repetir
		Escribir '1. Comprar producto, 2. Vender producto, 0. Salir:'
		Leer opcion
		Según opcion Hacer
	1:
		Escribir 'Ingrese la cantidad a comprar:'
		Leer cantidad_a_comprar
		stock <- stock+cantidad_a_comprar
		Escribir 'Compra realizada. Stock actual: ', stock
	2:
		Escribir 'Ingrese la cantidad a vender:'
		Leer cantidad_a_vender
		Si cantidad_a_vender<=stock Entonces
			stock <- stock-cantidad_a_vender
			Escribir 'Venta realizada. Stock actual: ', stock
		SiNo
			Escribir 'No hay suficiente stock para la venta.'
		FinSi
	0:
		Escribir 'Saliendo del sistema.'
	De Otro Modo:
		Escribir 'Opción inválida.'
FinSegún
Hasta Que opcion=0
FinAlgoritmo