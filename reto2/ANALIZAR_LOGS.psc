Algoritmo ANALIZAR_LOGS
	Dimensionar usuarios(100)
	Dimensionar accesos(100)
	total_usuarios <- 0
	encontrado <- FALSO
	Para i<-1 Hasta total_usuarios Hacer
		Si usuarios[i]=nombre Entonces
			accesos[i] <- accesos[i]+1
			encontrado <- VERDADERO
		FinSi
	FinPara
	Si  NO encontrado Entonces
		total_usuarios <- total_usuarios+1
		usuarios[total_usuarios] <- nombre
		accesos[total_usuarios] <- 1
	FinSi
	Escribir 'Resultados de accesos por usuario:'
	Para i<-1 Hasta total_usuarios Hacer
		Escribir usuarios[i], ' - ', accesos[i], ' accesos'
	FinPara
FinAlgoritmo
