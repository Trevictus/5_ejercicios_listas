
from random import randint


lista = []#5 numeros
estrellas = []#2 numeros

#mostrar_resultado()

def imprimir_numeros() -> list:
    numeros = []
    # for i in range(1,6):
    #     bombo = randint(1,50)
    #     if bombo not in numeros:
    #         numeros.append(bombo)
    #     else:
    #         bombo == set(bombo)
    # return numeros
    cont = 0
    while cont < 6:
        bombo = randint(1,50)
        cont += 1
        numeros.append(bombo)
    return numeros

def imprimir_estrellas():
    estrellas = []
    # for i in range(1,3):
    #     estrella = randint(1,12)
    #     if estrella not in estrellas:
    #         estrellas.append(estrella)
    #     else:
    #         estrella == set(estrellas)
    # return estrellas
    cont = 0
    while cont < 3:
        estrella = randint(1,12)
        cont += 1
        estrellas.append(estrella)
    return estrellas


def imprimir_euromillon(numeros, estrellas):
    
    numeros = " - ".join(map(str, imprimir_numeros()))
    estrellas = " - ".join(map(str, imprimir_estrellas()))

    return f"EUROMILLÓN DE HOY\n-----------------\nNºs->{numeros}\n***->{estrellas}"


numeros = imprimir_numeros()
estrellas = imprimir_estrellas()
print(imprimir_euromillon(numeros, estrellas))
