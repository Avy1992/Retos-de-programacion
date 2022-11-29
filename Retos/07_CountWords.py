"""
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y
 que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""
import re

def cuenta_palabras(texto: str):
    word_dict = {}
    word_list = re.split(r'[\W ]+',texto.lower())
    for word in word_list:
        if word not in word_dict.keys() and word!='':
            word_dict[word]=1
        elif word in word_dict:
            word_dict[word]+=1
    return word_dict
print(cuenta_palabras('Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).'))