# Ejercicio 3.1.5¶
"""Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""
def almacenar_lista():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return lista

def mostrar_lista_inversa(lista):
    reves = ", ".join(map(str, lista[::-1]))
    return reves
    





def main():
    lista = almacenar_lista()
    print(mostrar_lista_inversa(lista))


if __name__ == "__main__":
    main()