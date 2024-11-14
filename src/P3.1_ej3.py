# Ejercicio 3.1.3¶
"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""

def mostrar_asignaturas():
    lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    return lista

def preguntar_notas(lista):
    notas = []
    for i in range(len(lista)):
        nota = float(input(f"Introduce las notas de {lista[i]}: "))
        notas.append(nota)
    return notas
    
def mostrar_notas(lista, notas):
    resultado = ""
    for i in range(len(lista)):
        resultado += f"En {lista[i]} he sacado {notas[i]}\n"
    return resultado
    

        


def main():
    lista = mostrar_asignaturas()
    notas = preguntar_notas(lista)
    print(mostrar_notas(lista, notas))


if __name__ == "__main__":
    main()