# def generar_tablero(filas: int, columnas: int, valor_defecto: int)-> tuple:



def preguntar_dimensiones():
    filas = int(input("Introduce el número de filas de la matriz a generar: "))
    columnas  = int(input("Introduce el número de columnas de la matriz a generar: "))
    valor_defecto = 0

    return filas, columnas, valor_defecto

def crear_tablero(filas: int, columnas: int, valor_defecto: tuple)-> tuple:
    matriz = [[valor_defecto for _ in range(columnas)] for _ in range(filas)]

    return matriz
    
def mostrar_tablero(tablero):
    tablero_completo = ""
    variable = "-" * (len(tablero) * 4) + "-"

    for fila in tablero:
        tablero_completo += f"\n{"| " + " | ".join(map(str, fila)) + " |"}" + f"\n{variable}"

    return tablero_completo



def main():
    filas, columnas, valor_defecto = preguntar_dimensiones()
    matriz = crear_tablero(filas, columnas, valor_defecto)
    print(mostrar_tablero(matriz))
    




if __name__ == "__main__":
    main()

