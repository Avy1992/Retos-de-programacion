"""
 * MÁQUINA EXPENDEDORA
 * Fecha publicación enunciado: 11/07/22
 * Fecha publicación resolución: 18/07/22
 * Dificultad: MEDIA
 *
 * Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección del producto.
 * - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor
 *   número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje
 *   y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

dict_productos = {
    # CODIGO : (PRODUCTO, PRECIO)
    1 : ("Agua",50),
    2 : ("Coca-Cola", 100),
    3 : ("Cerveza", 155),
    5 : ("Pizza", 200),
    10 : ("Donut", 75)
}
coins_change = {200 : 0, 100: 0, 50 : 0, 10 : 0, 5 : 0}
coins = [200, 100, 50, 10, 5]

def buy(code: int, money: int):  #el dinero en centimos
    if code not in dict_productos.keys():
        print("Ese producto no existe")
        return
    if money < dict_productos[code][1] :
        print("Dinero insuficiente para ese producto")
        return
    change = money - dict_productos[code][1]
    for coin in coins:
        coins_change[coin] = int(change/coin)
        change = change % coin
    print(f"Usted ha comprado {dict_productos[code][0]} por {dict_productos[code][1]} centimos. Ha pagado {money}. Su cambio sera:")
    print('\n'.join([f"{coins_change[coins[i]]} monedas de {coins[i]}" for i in range(len(coins))]))

buy(5,525)