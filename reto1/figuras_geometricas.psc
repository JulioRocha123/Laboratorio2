Algoritmo figuras_geometricas
	Definir op, lado, base, altura, diagonalmem, diagonalmay, radio, perimetro, apotema, area, basmen, basmay Como Real
	Escribir "Calculadora de �reas de Figuras Geom�tricas"
	Escribir "Seleccione una figura:"
	Escribir "1) �rea de un Cuadrado"
	Escribir "2) �rea de un Tri�ngulo"
	Escribir "3) �rea de un C�rculo"
	Escribir "4) �rea de un Rect�ngulo"
	Escribir "5) �rea de un Rombo"
	Escribir "6) �rea de un Romboide"
	Escribir "7) �rea de un Trapecio"
	Escribir "8) �rea de un Pent�gono"
	Escribir "9) Salir"
	Leer op
	si op ==1 Entonces
		Escribir "ingrese la base del cuadrado:"
		Leer lado
		area <- lado*lado
		Escribir "el �rea del cuadrado es:", area
	SiNo
		si op ==2 Entonces
			Escribir "ingrese la altura del tri�ngulo:"
			leer altura
			Escribir "ingrese la base del tri�ngulo:"
			leer base 
			area <- (base*altura)/2
			Escribir "el �rea del triangulo es: ",area
		SiNo
			si op ==3 Entonces
				Escribir "ingrese la altura del rect�ngulo:"
				leer altura
				Escribir "ingrese la base del rect�ngulo:"
				leer base 
				area <- base*altura
				Escribir "el �rea del rect�ngulo es: ",area
			SiNo
				si op ==4 Entonces
					Escribir "ingrese la diagonal mayor del rombo:"
					leer diagonalmay
					Escribir "ingrese la diagonal menor del rombo:"
					leer diagonalmem
					area <- (diagonalmay*diagonalmem)/2
					Escribir "el �rea del rombo es: ",area
				SiNo
					si op ==5 Entonces
						Escribir "ingrese la altura del romboide:"
						leer altura
						Escribir "ingrese la base del romboide:"
						leer base 
						area <- base*altura
						Escribir "el �rea del romboide es: ",area
					SiNo
						si op ==6 Entonces
							Escribir "ingrese la base mayor del trapecio:"
							leer basmay
							Escribir "ingrese la base menor del trapecio:"
							leer basmen
							area <- ((basmay+basmen)*altura)/2
							Escribir "el �rea del trapecio es: ",area
						SiNo
							si op ==7 Entonces
								Escribir "ingrese el per�metro del pent�gono:"
								leer perimetro
								Escribir "ingrese el apotema del pent�gono:"
								leer apotema
								area <- (perimetro*apotema)/2
								Escribir "el �rea del pent�gono es: ",area
							SiNo
								si op ==8 Entonces
									Escribir "ingrese el radio del c�rculo:"
									leer radio
									area <- (pi*(radio^2))
									Escribir "el �rea del circulo es: ",area
								SiNo
									si op ==9 Entonces
										Escribir "Saliendo del programa"
									SiNo
										Escribir "Opci�n no valida"
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
