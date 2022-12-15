"""
 * Reto #23
 * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
 * Fecha publicación enunciado: 07/06/22
 * Fecha publicación resolución: 13/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común
 * múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

# Usamos la funcion de conjuntos del reto anterior
def conjuntos(array1: list, array2: list, comunes: bool):
    new_array = []
    if comunes:
        for element in array1:
            if element in array2:
                new_array.append(element)
    else:
        for element in array1:
            if element not in array2:
                new_array.append(element)
        for element in array2:
            if element not in array1:
                new_array.append(element)
    return new_array


def MCD(num1, num2):
    array1 = []
    temp1 = num1
    while temp1 > 1:
        for i in range(2, num1+1):
            if temp1 % i == 0:
                array1.append(i)
                temp1 /= i
                break
    array2 = []
    temp2 = num2
    while temp2 > 1:
        for i in range(2, num2 + 1):
            if temp2 % i == 0:
                array2.append(i)
                temp2 /= i
                break
    mcd = 1
    for factor in conjuntos(array1, array2, True):
        mcd *= factor
    return mcd


def MCM(num1, num2):
    return int(num1 * num2 / MCD(num1, num2))


print(MCD(0, 27))
print(MCM(10, 55))
