"""
/* Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100."""
# Un numero es primo si solo es divisible por 1 y por él mismo

def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
def primes_to_100():
    for i in range(2,101):
        if is_prime(i):
            print(i)

print(is_prime(int(input("Introduce un número paracomprobar si es primo:"))))
primes_to_100()