def imprime_letra(cadena, letra):
    for i in range(len(cadena)):
        if cadena[i].lower() == letra.lower():
            print(cadena[i], end="")
        else:
            print("x", end="")

def cuenta_caracter_y_espacios (cadena, letra):
    cont = 0
    for i in range(len(cadena)):
        if cadena[i].upper() == letra.upper() or cadena[i] == ' ':
            cont = cont + 1
    return cont
        
        
def main():
    cadena = input("Dame una cadena: ")
    letra = input("Dame una letra: ")
    res = cuenta_caracter_y_espacios(cadena, letra)
    print("El resultado es: ", res)
    #imprime_letra(cadena, letra)

main()