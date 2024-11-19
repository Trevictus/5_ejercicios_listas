import random
def configurar_vector():
    min = int(input("Valor mínimo de los elementos del vector: "))
    max = int(input("Valor máximo de los elementos del vector: "))
    rango_vector = int(input("Longitud del vector: "))
    
    return min, max, rango_vector

def generar_vector(min: int, max: int, rango_vector: int):
    vector = list()

    for _ in range(rango_vector):
        vector.append(generar_numero_aleatorio(min, max))
    return vector


def generar_numero_aleatorio(min: int, max: int):
    numero_generado = random.randint(min, max)
    return numero_generado

def main():
    min, max, rango_vector = configurar_vector()
    vector = generar_vector(min, max, rango_vector)
    print(vector)

if __name__ == "__main__":
    main() 