"""
 * Reto #14
 * ¿ES UN NÚMERO DE ARMSTRONG?
 * Fecha publicación enunciado: 04/04/22
 * Fecha publicación resolución: 11/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también
 * llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
"""

def numArmstrong(number):
    num_cifras=0
    cifras=[]
    number2=number
    while number2>0:
        cifras.append(number2%10)
        num_cifras+=1
        number2=int(number2/10)
    for numero in cifras:
        number2+=numero**num_cifras
    return number==number2

print(numArmstrong(372))