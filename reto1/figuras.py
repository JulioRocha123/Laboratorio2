#se importa la libreria math
import math

#Datos Cuadrados
def area_cuadrado(lado):
    """
    l = lado del cuadrado
    A = l*l
    """
    area = lado * lado
    return area

#Datos Triangulo
def area_triangulo(base,altura):
    """
    b = base | a = altura | A =
    A = (b*a) / 2
    """
    area = (base * altura) / 2
    return area

#Datos Circulo
def area_circulo(radio):
    """
    r = radio
    A = pi*(r**2)
    """
    area = (math.pi *(radio**2))
    return area

#Datos Pentagono
def area_pentagono(nlados,lonlados,apotema):
    """
    P = pelimetro | a = apotema | n = numero de lados | l = longitud de los lados
    A = (P*a)/2
    P = n * l
    """
    pelimetro = nlados * lonlados
    area = (pelimetro * apotema) / 2
    return (area)

#Datos Trapecio
def area_trapecio (Baselarga,basecorta,alturap):
    """
    B = base larga | b = base corta | h = altura maxima
    A = ((B + b)/2) h
    """
    area = ((Baselarga + basecorta)/2) * alturap
    return (area)

def area_romboide (baser,alturar):
    """
    b = base | h altura
    A = b * h
    """
    area = (baser * alturar)
    return (area)

def area_rombo (diametroM,diametrom):
    """
    D = diametro mayor | d = diametro menor
    A = (D * d)
    """
    area = (diametroM*diametrom)/2
    return (area)

def area_rectangulo (baset,alturat):
    """
    b = base | a = altura
    A = b * a
    """
    area = baset * alturat
    return (area)

def validador ():
    while True:
        try:
            continue
        except ValueError:
            print (f"¡Error!, ingrese un valor numerico")