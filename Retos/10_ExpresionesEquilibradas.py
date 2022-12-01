"""
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión
 * están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

import re

def isBalanced(string):
   # simbolos = re.findall(r'[\[\]\(\)\{\}]',string)
    parentesis_dict = {'(':0, ')':0, '[':0, ']':0, '{':0, '}':0}
    for simbolo in string:
        if simbolo in parentesis_dict.keys():
            parentesis_dict[simbolo]+=1
    return (parentesis_dict['(']==parentesis_dict[')'] and parentesis_dict['[']==parentesis_dict[']'] and parentesis_dict['{']==parentesis_dict['}'])

print(isBalanced("{a + b [c] * (2x2)}}}}"))
print(isBalanced("{ [ a * ( c + d ) ] - 5 }"))