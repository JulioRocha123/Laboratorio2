Algoritmo Simulacion_Red_Sensores
	Escribir 'Generando la matriz de temperaturas'
	Leer n, m
	Dimensionar matriz(n,m)
	Para i<-1 Hasta n Hacer
		Para j<-1 Hasta m Hacer
			matriz[i,j]<-Aleatorio(0,100)
		FinPara
	FinPara
	Escribir 'Verificando temperaturas críticas...'
	Según n Hacer
De Otro Modo:
	Para i<-1 Hasta n Hacer
		Para j<-1 Hasta m Hacer
			Si matriz[i,j]>80 Entonces
				Escribir 'Temperatura crítica detectada en posición (', i, ',', j, '): ', matriz[i,j], '°C'
			FinSi
		FinPara
	FinPara
FinSegún
FinAlgoritmo