def tabla_multiplicar(n):
    cont = 1
    while cont <= 10:
        res = cont * n
        print("%i x %i = %i" % (cont, n, res))
        cont = cont + 1

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

def total_depositos(n):
    cont = 1
    contdep = 0
    acum = 0
    while cont <= n:
        mes = input("Mes: ")
        importe = float(input("Importe: "))
        cont = cont + 1
        if mes.lower() == "octubre": 
            acum = acum + importe
            contdep = contdep + 1
        else:
            print("Error en el mes")
    print("Total de importes:", acum)
    print("Total de importes de importes del mes en curso:", contdep)

def clientes(n):
    cmay = 0
    clocal = 0
    cforaneo = 0
    cont = 1
    while cont <= n:
        edad = int(input("Edad: "))
        ciudad = input("Ciudad: ")
        cont = cont + 1
        if edad >= 18: 
            cmay = cmay + 1
        if ciudad.lower() == "querétaro": 
            clocal = clocal + 1
        else:
            cforaneo = cforaneo + 1
    print("Total de mayores de edad:", cmay)
    print("Total de clientes foráneos:", cforaneo)
    print("Total de clientes locales:", clocal)

def menu():
    print("1. Tabla de multiplicar")
    print("2. Total a pagar")
    print("3. Total de depósitos")
    print("4. Clientes")
    
def main():
    menu()
    opcion = int(input("Dame una opción: "))
    if opcion == 1:
        n = int(input("Dame un número entero mayor o igual a uno: "))
        tabla_multiplicar(n)
    elif opcion == 2:
        n = int(input("Dame el número de productos: "))
        res = total_pagar(n)
        print("El total a pagar es: %.2f" % res) 
    elif opcion == 3:
        n = int(input("Dame el número de depósitos: "))
        total_depositos(n)
    elif opcion == 4:
        n = int(input("Dame el número de clientes: "))
        clientes(n)
    else:
        print("Error opción inválida")

main()