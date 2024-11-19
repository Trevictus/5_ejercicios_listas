import random

def preguntar_dimensiones():
    filas = int(input("Introduce el número de filas de la matriz a generar: "))
    columnas  = int(input("Introduce el número de columnas de la matriz a generar: "))
    min = int(input("Introduce el valor mínimo: "))
    max = int(input("Introduce el valor máximo: "))

    return filas, columnas, min, max

def crear_matriz(filas: int, columnas: int, min: int, max: int)-> tuple:
    matriz = [[random.randint(min, max) for _ in range(columnas)] for _ in range(filas)]
    return matriz
    


def main():
    filas, columnas, min, max = preguntar_dimensiones()
    matriz = crear_matriz(filas, columnas, min, max)
    print(matriz)


if __name__ == "__main__":
    main()

