def cuenta_suma():
    suma = 0
    cont = 0
    while suma <= 1000:
        cantidad = int(input("Dame una cantidad: "))
        suma = suma + cantidad
        cont = cont + 1
    print("La suma es: ", suma)
    print("La cantidad de números fue: ", cont)
            
def valida_matricula (lista):
    matricula = input("Dame tu matrícula: ")
    while matricula not in lista:
        print("Matrícula inválida, intenta de nuevo")
        matricula = input("Dame tu matrícula: ")
    print("Matrícula válida")
     
def total_pagar(n):
    cont = 1
    acum = 0
    while cont <= n:
        print("\nProducto %i" % cont)
        nombre = input("Producto: ")
        precio = float(input("Precio: "))
        cont = cont + 1
        acum = acum + precio
    return acum

def total_depositos(n, mes_curso):
    cont = 1
    contdep = 0
    acum = 0
    while cont <= n:
        mes = input("Mes: ")
        importe = float(input("Importe: "))
        cont = cont + 1
        if mes.lower() == mes_curso.lower(): 
            acum = acum + importe
            contdep = contdep + 1
        else:
            print("Error en el mes")
    print("Total de importes:", acum)
    print("Total de importes del mes en curso:", contdep)

def menu():
    print()
    print("1. Cuenta y suma")
    print("2. Total a pagar")
    print("3. Total de depósitos")
    print("4. Valida matrícula 2")
    print("5. Salir")
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            cuenta_suma()
        elif opcion == 2:
            n = int(input("Dame el número de productos: "))
            res = total_pagar(n)
            print("El total a pagar es: %.2f" % res) 
        elif opcion == 3:
            n = int(input("Dame el número de depósitos: "))
            mes_curso = input("Dame el mes en curso: ")
            total_depositos(n, mes_curso)
        elif opcion == 4:
            lista = ["A01300000", "A01201524", "A01200000"]
            valida_matricula(lista)
        elif opcion == 5:
            print("Adiós")
            continua = False
        else:
            print("Error opción inválida")
    
main()