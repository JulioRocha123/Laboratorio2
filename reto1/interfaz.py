from figuras import *
def menu ():
    while True:
        try:
            print(" !!Menu¡¡ \n1) Cuadrado\n2) Triangulo\n3) Circulo\n4) Pentagono\n5) Trapecio\n6) Romboide\n7) Rombo\n8) Rectangulo\n9) Salir")
            op = int(input("Eliga una opcion: ")) 
            return op
        except ValueError:
            print (f"¡Error!, ingrese un valor numerico")
#definimos las variables de las formas geometricas
def opcion_seleccionada (op):
    cuadrado = 1
    triangulo = 2
    circulo = 3
    pentagono = 4
    trapecio = 5
    romboide = 6
    rombo = 7
    rectangulo = 8
    salir = 9
    if op == cuadrado:
        print (f"usted a elegido Cuadrado")       
        return cuadrado
    elif op == triangulo:
        print (f"Usted a elegido Triangulo")
        return triangulo
    elif op == circulo:
        print (f"Usted a elegido Circulo")
        return circulo
    elif op == pentagono:
        print (f"Usted a elegido Pentagono")
        return pentagono
    elif op == trapecio:
        print (f"Usted a elegido Trapecio")
        return trapecio
    elif op == romboide:
        print (f"Usted a elegido Romboide")
        return romboide
    elif op == rombo:
        print (f"Usted a elegido Rombo")
        return rombo
    elif op == rectangulo:
        print (f"Usted a elegido Rectangulo")
        return rectangulo
    elif op == 9:
        print (f"Usted esta saliendo de la claculadora de areas de figuras, feliz dia")
        return salir
    else:
        print (f"opcion no valida!!")

#solicitar datos
#cuadrado
def solicitar_cuadrado ():
    """
    Solicita el lado que va a ser un dato flotante
    """
    while True:
        try: 
            lado = float(input("Digite el lado: "))
            return lado
        except ValueError:
            print (f"¡¡Error!!, ingrese un valor numerico")

def solicitar_triangulo ():
    """
    Solicitar la base y la altura que va a ser un dato flotante
    """
    while True:
        try:
            base = float(input("Digita la base: "))
            altura = float(input("Digite la altura: "))
            return base,altura
        except ValueError:
            print (f"¡¡Error!!, ingrese un valor numerico") 

def solicitar_circulo ():
    """
    Solicita el radio que va a ser un dato flotante
    """
    radio = float(input("Digite el radio del circulo: "))
    return radio

def solicitar_pentagono ():
    """
    se le solicita el numero de lados, el apotema, 
    y la longitud de los lados del pentagono que van a ser tipos flotantes
    """
    nlados = float(input("Digite el numero de lados: "))
    lonlados = float(input("Digite la longitud de los lados: "))
    apotema = float(input("Digite el apotema del pentagono: "))
    return nlados,lonlados,apotema

def solicitar_trapecio ():
    """
    se le solicita el lado largo, el lado corto y la altura del pentagono
    """
    Baselarga = float(input("Digite el lado mas largo: "))
    basecorta = float(input("Digite el lado mas corto: "))
    alturap = float(input("Digite la altura: "))
    return Baselarga,basecorta,alturap

def solicitar_romboide ():
    """
    Se le solcita la base y la altura del romboide
    """
    baser = float(input("Digite la base: "))
    alturar = float(input("Digite la altura: "))
    return baser,alturar

def solicitar_rombo ():
    """
    Se le solicita el diametro mayor y el diametro menor
    """
    diametroM = float(input("Digite el diametro mayor: "))
    diametrom = float(input("Digite el diametro menor: "))
    return diametroM,diametrom

def solicitar_rectangulo ():
    """
    Se le solicita la base y la altura
    """
    baset = float(input("Digite la base: "))
    alturat = float(input("Digite la altura: "))
    return baset,alturat