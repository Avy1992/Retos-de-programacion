"""
 * Reto #25
 * PIEDRA, PAPEL, TIJERA
 * Fecha publicación enunciado: 20/06/22
 * Fecha publicación resolución: 27/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

def winner(plays: list):
    player1=0
    player2=0
    possible_plays=['R', 'P', 'S']
    for play in plays:
        if play[0] not in possible_plays and play[1] in possible_plays:
            player2 += 1
        elif play[0] in possible_plays and play[1] not in possible_plays:
            player1 += 1
        elif play[0] in possible_plays and play[1] in possible_plays:
            if play[0] == 'R':
                if play[1] == 'S':
                    player1 += 1
                if play[1] == 'P':
                    player2 += 1
            if play[0] == 'S':
                if play[1] == 'P':
                    player1 += 1
                if play[1] == 'R':
                    player2 += 1
            if play[0] == 'P':
                if play[1] == 'R':
                    player1 += 1
                if play[1] == 'S':
                    player2 += 1
    if player1>player2:
        return "The winner ir Player number 1"
    if player1 == player2:
        return "The result is a tie"
    else:
        return "The winner is Player number 2"

print(winner([("R","S"), ("R","R"), ("P","S"), ('S', 'P')]))