# Ejercicio 3.1.2¶
"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista."""
def mostrar_asignaturas():
    lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    return f"Yo estudio {lista[0]}\nYo estudio {lista[1]}\nYo estudio {lista[2]}\nYo estudio {lista[3]}\nYo estudio {lista[4]}"





def main():
    print(mostrar_asignaturas())


if __name__ == "__main__":
    main()