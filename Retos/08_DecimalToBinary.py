"""
 * Reto #8
 * DECIMAL A BINARIO
 * Fecha publicación enunciado: 18/02/22
 * Fecha publicación resolución: 02/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa se encargue de transformar un número decimal a binario
  sin utilizar funciones propias del lenguaje que lo hagan directamente.
 *
 """
def to_binary(number):
    num_binary = ''
    while number > 1 :
        num_binary=str(number%2)+num_binary
        number = int(number/2)
    num_binary=str(number) +num_binary
    return int(num_binary)
print(to_binary(222))