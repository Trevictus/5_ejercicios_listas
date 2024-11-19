

"""
A = 1 2 3
    4 5 6


B = -1 1
     0 2
     2 3
"""

# matriz_a = (
#             (1, 2, 3),
#             (4, 5, 6)
#             )

# matriz_b = (
#             (-1, 1),
#             (0, 2),
#             (2, 3)
#             )

# matriz_c = [
#             [0, 0],
#             [0, 0]
#             ]


def preguntar_numero_filas():
    f1 = int(input("Número de filas de la matriz 1: "))
    f2 = int(input("Número de filas de la matriz 2: "))

    return f1, f2

def preguntar_numero_columnas():
    c1 = int(input("Número de columnas de la matriz 1: "))
    c2 = int(input("Número de columnas de la matriz 2: "))

    return c1, c2

def verificar_multiplicacion_matrices(c1: int, f2: int)-> bool:
    if c1 != f2:
        print("No se puede hacer la multiplicación.")
        return False
    return True

def crear_matrices(f1, c1, f2, c2):
    matriz_a = [[0 for _ in range(c1)] for _ in range(f1)]
    matriz_b = [[0 for _ in range(c2)] for _ in range(f2)]
    matriz_c = [[0 for _ in range(c2)] for _ in range(f1)]
    print("Introduce los elementos de la matriz_a: ")
    for i in range(0, f1):
        for j in range(0, c1):
            matriz_a[i][j] = float(input(f"Matriz a[{i},{j}]"))
    print("Introduce los elementos de la matriz_b: ")
    for i in range(0, f2):
        for j in range(0, c2):
            matriz_b[i][j] = float(input(f"Matriz b[{i}, {j}]"))

    return matriz_a, matriz_b, matriz_c


def multiplicacion_matrices(matriz_a, matriz_b, matriz_c, f1, f2, c2):
    # for i in range(len(matriz_a)):
    #     for j in range(len(matriz_b[0])):
    #         for k in range(len(matriz_b)):
    #             matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]
    # print(matriz_c)
    for i in range(f1):
        for j in range(c2):
            for k in range(f2):
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return matriz_c

def main():
    f1, f2 = preguntar_numero_filas()
    c1, c2 = preguntar_numero_columnas()

    if not verificar_multiplicacion_matrices(c1, f2):
        return
    
    matriz_a, matriz_b, matriz_c = crear_matrices(f1, c1, f2, c2)
    matriz_c = multiplicacion_matrices(matriz_a, matriz_b, matriz_c, f1, f2, c2)

    print("Matriz resultante => ", matriz_c)

if __name__ == "__main__":
    main()  