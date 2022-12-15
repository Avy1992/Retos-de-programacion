"""
 * Reto #22
 * CONJUNTOS
 * Fecha publicación enunciado: 01/06/22
 * Fecha publicación resolución: 07/06/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def conjuntos(array1: list, array2: list, comunes: bool):
    new_array=[]
    if comunes:
        for element in array1:
            if element in array2 and element not in new_array:
                new_array.append(element)
    else:
        for element in array1:
            if element not in array2:
                new_array.append(element)
        for element in array2:
            if element not in array1:
                new_array.append(element)
    return new_array

print(conjuntos([1, 2, 3, 3, 4], [2, 2, 3, 3, 3, 4, 6], True))
print(conjuntos([1, 2, 3, 3, 4], [2, 2, 3, 3, 3, 4, 6], False))