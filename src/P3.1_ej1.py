# Ejercicio 3.1.1¶
"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""

def mostrar_asignaturas():
    lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    return f"La lista de asignaturas a cursar son:\n{lista[0]}\n{lista[1]}\n{lista[2]}\n{lista[3]}\n{lista[4]}"





def main():
    print(mostrar_asignaturas())


if __name__ == "__main__":
    main()