Algoritmo figuras_geometricas
	Definir op, lado, base, altura, diagonalmem, diagonalmay, radio, perimetro, apotema, area, basmen, basmay Como Real
	Escribir "Calculadora de Áreas de Figuras Geométricas"
	Escribir "Seleccione una figura:"
	Escribir "1) Área de un Cuadrado"
	Escribir "2) Área de un Triángulo"
	Escribir "3) Área de un Círculo"
	Escribir "4) Área de un Rectángulo"
	Escribir "5) Área de un Rombo"
	Escribir "6) Área de un Romboide"
	Escribir "7) Área de un Trapecio"
	Escribir "8) Área de un Pentágono"
	Escribir "9) Salir"
	Leer op
	si op ==1 Entonces
		Escribir "ingrese la base del cuadrado:"
		Leer lado
		area <- lado*lado
		Escribir "el área del cuadrado es:", area
	SiNo
		si op ==2 Entonces
			Escribir "ingrese la altura del triángulo:"
			leer altura
			Escribir "ingrese la base del triángulo:"
			leer base 
			area <- (base*altura)/2
			Escribir "el área del triangulo es: ",area
		SiNo
			si op ==3 Entonces
				Escribir "ingrese la altura del rectángulo:"
				leer altura
				Escribir "ingrese la base del rectángulo:"
				leer base 
				area <- base*altura
				Escribir "el área del rectángulo es: ",area
			SiNo
				si op ==4 Entonces
					Escribir "ingrese la diagonal mayor del rombo:"
					leer diagonalmay
					Escribir "ingrese la diagonal menor del rombo:"
					leer diagonalmem
					area <- (diagonalmay*diagonalmem)/2
					Escribir "el área del rombo es: ",area
				SiNo
					si op ==5 Entonces
						Escribir "ingrese la altura del romboide:"
						leer altura
						Escribir "ingrese la base del romboide:"
						leer base 
						area <- base*altura
						Escribir "el área del romboide es: ",area
					SiNo
						si op ==6 Entonces
							Escribir "ingrese la base mayor del trapecio:"
							leer basmay
							Escribir "ingrese la base menor del trapecio:"
							leer basmen
							area <- ((basmay+basmen)*altura)/2
							Escribir "el área del trapecio es: ",area
						SiNo
							si op ==7 Entonces
								Escribir "ingrese el perímetro del pentágono:"
								leer perimetro
								Escribir "ingrese el apotema del pentágono:"
								leer apotema
								area <- (perimetro*apotema)/2
								Escribir "el área del pentágono es: ",area
							SiNo
								si op ==8 Entonces
									Escribir "ingrese el radio del círculo:"
									leer radio
									area <- (pi*(radio^2))
									Escribir "el área del circulo es: ",area
								SiNo
									si op ==9 Entonces
										Escribir "Saliendo del programa"
									SiNo
										Escribir "Opción no valida"
									FinSi	
								FinSi	
							FinSi	
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi	
FinAlgoritmo
