#se inmportan las librerias segun el nombre de cada definicion
#FROM: se refiera a el codigo o la apliacion donde esta cada funcion
from interfaz import *
from figuras import *
#funcion principal
opcion = 0
while opcion != 9:
    op = menu()
    formas_geometricas = opcion_seleccionada(op)
    if formas_geometricas == 1:
    #area cuadrado
        lado = solicitar_cuadrado()
        area = area_cuadrado(lado)
        print(f"El area del cuadrado es: {area} metros cuadrados")
    elif formas_geometricas == 2:
    #area triangulo
        base,altura = solicitar_triangulo()
        area = area_triangulo(base,altura)
        print(f"El area del triangulo es: {area} metros cuadrados")
    elif formas_geometricas == 3:
    #area circulo
        radio = solicitar_circulo()
        area = area_circulo(radio)
        print (f"El area del circulo es: {area} metros cuadrados")
    elif formas_geometricas == 4:
    #area pentagono
        nlados,lonlados,apotema = solicitar_pentagono ()
        area = area_pentagono(nlados,lonlados,apotema)
        print (f"El area del pentagono es: {area} metros cuadrados")
    elif formas_geometricas == 5:
    #area trapecio
        Baselarga,basecorta,alturap = solicitar_trapecio ()
        area = area_trapecio(Baselarga,basecorta,alturap)
        print (f"El area del trapecio es: {area} metros cuadrados")
    elif formas_geometricas == 6:
    #area Romboide
        baser,alturar = solicitar_romboide ()
        area = area_romboide(baser,alturar)
        print (f"El area del romboide es de: {area} metros cuadrados")
    elif formas_geometricas == 7:
    #area Rombo
        diametroM,diametrom = solicitar_rombo ()
        area = area_rombo (diametroM,diametrom)
        print (f"El area del rombo es: {area} metros cuadrados")
    elif formas_geometricas == 8:
        baset,alturat = solicitar_rectangulo ()
        area = area_rectangulo (baset,alturat)
        print (f"El area del rectangulo es: {area} metros cuadrados")
    elif formas_geometricas == 9:
        break
    else:
        print ("Opcion incorrecta, digite una opcion entre el 1 y el 9")