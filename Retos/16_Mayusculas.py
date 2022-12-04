"""
 * Reto #16
 * EN MAYÚSCULA
 * Fecha publicación enunciado: 18/04/22
 * Fecha publicación resolución: 25/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def firstMayus(text: str):
    no_spaces = text.split(' ')
    for i in range(len(no_spaces)):
        no_spaces[i]=no_spaces[i][0].upper()+no_spaces[i][1:]

    return ' '.join(no_spaces)

print(firstMayus('no veas'))