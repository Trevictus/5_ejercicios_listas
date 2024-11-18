#Ejercicio 3.1.11¶
"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar."""



def producto_escalar(vector1: tuple, vector2: tuple)-> int:
    resultado = 0

    for i in range(len(vector2)):
        resultado += vector1[i] * vector2[i]

    return resultado


def mostrar_resultado(vector1, vector2, resultado):
    return f"vector1 = {" - ".join(map(str, vector1))}\nvector2 = {" - ".join(map(str, vector2))}\nproducto escalar {resultado}"


def main():
    vector1 = (1,2,3)
    vector2 = (-1,0,2)

    resultado = producto_escalar(vector1, vector2)
    print(mostrar_resultado(vector1, vector2, resultado))


   

if __name__ == "__main__":
    main()
