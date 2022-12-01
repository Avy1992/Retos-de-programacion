"""
 * Reto #12
 * ¿ES UN PALÍNDROMO?
 * Fecha publicación enunciado: 21/03/22
 * Fecha publicación resolución: 28/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean)
 * según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""

import re
from unidecode import unidecode
def palindromo(string: str):
    no_spaces=re.sub(r'[,.\-?! ]','', string.lower())
    #print(no_spaces)
    for i in range(len(no_spaces)):
        #print(no_spaces[i]+' ' + no_spaces[-1-i])
        if unidecode(no_spaces[i])!=unidecode(no_spaces[-i-1]):
            return False
    return True
print(palindromo('Aa lleva al oso la avellana.'))
print(palindromo('Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida'))