"""
 * Reto #17
 * LA CARRERA DE OBSTÁCULOS
 * Fecha publicación enunciado: 25/04/22
 * Fecha publicación resolución: 02/05/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
 *        variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""



def carrera(atleta: list, pista: list):
    new_pista=[]
    for i in range(len(atleta)):
        if pista[i]not in ['_','|'] or atleta[i]not in ['run','jump']:
            print('Entrada no valida')
            quit()
        if atleta[i]=='run' and pista[i]=='|':
            new_pista.append('/')
        elif atleta[i]=='jump' and pista[i]=='_':
            new_pista.append('x')
        else:
            new_pista.append(pista[i])
    return new_pista==pista

print(carrera(['run','jump','run','jump','run'],['_','|','_','|','?']))