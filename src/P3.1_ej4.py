# Ejercicio 3.1.4¶
"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""

def preguntar_numeros_ganadores():
    ganadores = []
    finalizar = False
    while not finalizar:
        try:    
            entrada = input("Introduce los nºs ganadores o pulsa 'enter' para terminar: ")
            if entrada == "":
                finalizar = True
            else:
                numeros = int(entrada) 
                ganadores.append(numeros)
        except ValueError:
            print("Error introduce numeros enteros solamente.")
            
    return ganadores

def ordenar_numeros(ganadores):
    ganadores_ordenados = sorted(ganadores)
    return f"Los numeros ganadores son:\n{' '.join(map(str, ganadores_ordenados))}"

def main():
    ganadores = preguntar_numeros_ganadores()
    print(ordenar_numeros(ganadores))


if __name__ == "__main__":
    main()