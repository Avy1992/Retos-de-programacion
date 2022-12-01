"""
 * Reto #15
 * ¿CUÁNTOS DÍAS?
 * Fecha publicación enunciado: 11/04/22
 * Fecha publicación resolución: 18/04/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""

from datetime import  datetime

def days(date1, date2):
    try:
        datetime.strptime(date1,"%d/%m/%Y")
        datetime.strptime(date2, "%d/%m/%Y")
    except:
        print("Formato de fecha incorrecto")
        pass
    fecha1=datetime.strptime(date1,"%d/%m/%Y")
    fecha2=datetime.strptime(date2,"%d/%m/%Y")
    if fecha1>fecha2:
        return (fecha1-fecha2).days
    else:
        return (fecha2-fecha1).days


print(days('12/12/1995', '01/01/2012'))
print(days("18/5/2022", "29/04/2022"))