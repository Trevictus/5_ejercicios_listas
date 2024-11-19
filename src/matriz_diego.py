import random


def crear_matriz(filas: int, columnas: int, min: int, max: int)-> tuple:
    matriz = [[random.randint(min, max) for _ in range(columnas)] for _ in range(filas)]
    return matriz

matriz = crear_matriz(3, 2, -10, 10)
print(matriz)
