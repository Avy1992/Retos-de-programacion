"""
 * Reto #27
 * VECTORES ORTOGONALES
 * Fecha publicación enunciado: 07/07/22
 * Fecha publicación resolución: 11/07/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def are_orthogonal(vector1: list or tuple, vector2: list or tuple ):
    if len(vector1) != len(vector2):
        print("Los vectores tienen que tener la misma dimension")
        return
    total=0
    for i in range(len(vector1)):
        try:
            int(vector1[i])
            int(vector2[i])
        except:
            print("Los vectores solo pueden contener numeros enteros")
            return
        total += (vector1[i] * vector2[i])
    if total == 0:
        return True
    return False

print(are_orthogonal([1, -2], [4,2]))