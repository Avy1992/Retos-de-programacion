"""
 * Reto #18
 * TRES EN RAYA
 * Fecha publicación enunciado: 02/05/22
 * Fecha publicación resolución: 09/05/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
"""
import re

characters=['o','O','x','X','']

def count_chars(matrix: list[list[str]]):
    char_accepted=True
    count_O=0
    count_X=0
    count_blank=0
    for row in matrix:
        for char in row:
            if char in characters:
                if char.upper()=='X':
                    count_X+=1
                elif char.upper()=='O':
                    count_O+=1
                elif char=='':
                    count_blank+=1
            else:
                char_accepted==False
    return char_accepted,count_O,count_X

def check_row(matrix: list[list[str]]):
    win_X=False
    win_O=False
    for row in matrix:
        if len(re.findall(r"[xX]"))==3:
            win_X=True
        elif len(re.findall(row,r"[oO]"))==3:
            win_O=True
    return win_O,win_X

def tres_en_raya(matrix: list[list[str]]):

    if len(matrix)!=3:
        return None
    for row in matrix:
        if len(row)!=3:
            return None
    char_accepted, countO, countX = count_chars(matrix)
    if not char_accepted :
        return None
    columns = [[matrix[i][j] for i in range(3)]for j in range(3)]
    win_o_row, win_x_row = check_row(matrix)
    win_o_column,win_x_column = check_row(columns)
    diagonals = [matrix[i][i] for i in range(3)]
    diagonals.append([matrix[-i-1][-i-1] for i in range(3)])
    print(diagonals)