"""
 * Reto #26
 * CUADRADO Y TRIÁNGULO 2D
 * Fecha publicación enunciado: 27/06/22
 * Fecha publicación resolución: 07/07/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
"""


base = '* '
base_void = '  '


def draw_square(size: int, solid: bool):

    for i in range(size):
        row = ''
        if i == 0 or i == size-1:
            row = size * base
        else:
            if solid == False:
                row = base + (size-2)*base_void + base
            else:
                row = size * base
        print(row)

draw_square(6,False)
print()

def draw_inverted_triangle(size: int, solid: bool):
    for i in range(size,0,-1):
        if solid is True or i == 1 or i == size:
            print(base*i)
        else:
            print((base + base_void*(i-2) + base))

draw_inverted_triangle(6, True)
print()


def draw_triangle(size: int, solid: bool):
    for i in range(1,size+1):
        if solid is True or i == 1 or i == size:
            print(base*i)
        else:
            print((base + base_void*(i-2) + base))

draw_triangle(6, True)
print()

def draw_centered_triangle(size: int, solid: bool):
    for i in range(size):
        if solid == True or i == 0 or i == size - 1:
            print(' ' * (size-i) + base * (i+1) + ' ' * (size-i))
        else:
            print(' ' * (size-i) + base + base_void * (i-1) + base + ' ' * (size-i))

draw_centered_triangle(6,False)
print()

def draw_centered_inverted_triangle(size: int, solid: bool):
    for i in range(size):
        if solid==True or i == 0 or i == size-1:
            print(' '*i + base*(size-i) + ' '*i)
        else:
            print(' '*i + base + base_void*(size-i-2) + base + ' '*i)

draw_centered_inverted_triangle(6, False)

