"""/*
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo."""
import re

def area(poligono, base, altura=0):
    try:
        poligono = poligono.lower()
    except:
        return "Poligono no valido"
    if poligono == 'triangulo':
        print('Triangulo')
        return base*altura/2
    elif poligono == 'cuadrado':
        print('Cuadrado')
        return base*base
    elif poligono == 'rectangulo':
        print('Rectangulo')
        return base*altura
    else:
        return "poligono no valido"


print(area('Triangulo',10, 5))
print(area('rectangulo', 10, 12))
print(area('cuadrado', 10))
print(area(123, 12, 5))
