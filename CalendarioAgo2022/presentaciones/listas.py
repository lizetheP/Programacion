def crea_lista(tam):
    contador = 1
    lista = []
    while contador <= tam:
        numero = int(input("Dame un número: "))
        lista.append(numero)
        contador = contador + 1
    return lista
    
def main():
    t = int(input("Introduce el tamaño de la lista: "))
    if t > 0:
        lista = crea_lista(t)
        print(lista)
    else:
        print("Imposible")
        
main()