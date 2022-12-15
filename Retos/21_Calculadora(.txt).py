"""
 * Reto #21
 * CALCULADORA .TXT
 * Fecha publicación enunciado: 23/05/22
 * Fecha publicación resolución: 01/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
"""
supported_operators = ['+', '-', '*', '/']
def calculadora(filename):

    # Abrimos el archivo
    with open(filename,  "r") as file:

        # Leemos el archivo y almacenamos cada linea en una lista
        operations = [line.rstrip() for line in file.readlines()]
        # Creamos variable con el rango del for para modificarla en caso que el primer comando sea un operador
        rango = range(1, len(operations)-1)
        # Comprobamos que el primer comando sea un numero. Si es un operador, el primer numero sera 0
        try:
            total = float(operations[0])
        except:
            total=0
            rango = range(len(operations))
        for i in rango:
            try:
                float(operations[i])
            except:
                if operations[i] not in supported_operators:
                    print(f"Syntax Error: operator not supported ({operations[i]})")
                    file.close()
                    return None
                if operations[i] == '+':
                    i += 1
                    total += float(operations[i])
                elif operations[i] == '-':
                    i += 1
                    total -= float(operations[i])
                elif operations[i] == '*':
                    i += 1
                    total *= float(operations[i])
                elif operations[i] == '/':
                    i +=1
                    if float(operations[i])==0:
                        print("Math Error: cannot divide by 0")
                        file.close()
                        return None
                    else:
                        total /= float(operations[i])
        print(total)

calculadora('Challenge21.txt')