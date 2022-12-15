"""
 * Reto #20
 * PARANDO EL TIEMPO
 * Fecha publicación enunciado: 16/05/22
 * Fecha publicación resolución: 23/05/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la
 * ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.
"""

import asyncio
import time

async def suma_con_delay(num1: int, num2: int, delay: int):
    start = time.time()
    sum=num2+num1
    await asyncio.sleep(delay)
    end = time.time()
    print(f"Se ha tardado en realizar la suma {num1}+{num2}={sum}: {end-start} segundos")

async def main():
    await asyncio.gather(
        suma_con_delay(5, 10, 5),
        suma_con_delay(2, 10, 2),
        suma_con_delay(1, 1 ,5)
    )

start = time.time()
asyncio.run(main())
end = time.time()
print(f"Se ha tardado en total {end-start} segundos")