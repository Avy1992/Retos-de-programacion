"""
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y
 * dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""

import re

def morse(texto):
    nat_to_morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                         'h': '....',
                         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                         'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                         'x': '-..-',
                         'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                         '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '----'
                         }
    morse_to_nat = {x:y for y,x in nat_to_morse_dict.items()}
    nat_to_morse_dict[' ']='  '

    new_text = ''
    if re.match(r'[a-zA-Z0-9]', texto):
        for word in texto.split(' '):
            for character in word:
                new_text=new_text+nat_to_morse_dict[character]+' '
            new_text+=' '
    else:
        for word in re.split('  ', texto):
            for character in word.split(' '):
                new_text=new_text+morse_to_nat[character]
            new_text+=' '
    return new_text


print(morse('..-. --.  -.. ..-. --.  - ....  -.--'))
print(morse('fg dfg th y'))
# ..-. --.  -.. ..-. --.  - ....  -.--
# fg dfg th y