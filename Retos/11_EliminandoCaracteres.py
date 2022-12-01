"""
 * Reto #11
 * ELIMINANDO CARACTERES
 * Fecha publicación enunciado: 14/03/22
 * Fecha publicación resolución: 21/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima
 * otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""
def printNotCommon(string1, string2):
    str1=''
    str2=''
    for caracter in string1.lower():
        if caracter not in string2.lower():
            str1+=caracter
    print(str1)
    for caracter in string2.lower():
        if caracter not in string1.lower():
            str2+=caracter
    print(str2)
    return (str1,str2)

printNotCommon("Me gusta Java","Me gusta Kotlin")
