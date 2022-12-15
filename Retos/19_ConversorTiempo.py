"""
 * Reto #19
 * CONVERSOR TIEMPO
 * Fecha publicación enunciado: 09/05/22
 * Fecha publicación resolución: 16/05/22
 * Dificultad: FACIL
 *
 * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
"""

def milisecs(days: int, hours: int, minutes: int, seconds: int):
    return seconds*1000+minutes*60*1000+hours*60*60*1000+days*24*60*60*1000

print(milisecs(200000000000,5,688,20))