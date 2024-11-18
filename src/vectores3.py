
def producto_especial(vector1: tuple, vector2: tuple)-> tuple:
    vector3 = []

    for i in range(len(vector2)):
        resultado = 0
        for j in range(len(vector2)):
            resultado += vector1[j] * vector2[i]
        vector3.append(resultado)

    return tuple(vector3)





def main():
    vector1 = (1, 2, 3)
    vector2 = (-1, 0, 2)
    resultado = producto_especial(vector1, vector2)
    print(resultado)


   

if __name__ == "__main__":
    main()