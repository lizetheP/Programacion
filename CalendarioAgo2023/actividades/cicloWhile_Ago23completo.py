def tabla_multiplicar(n):
    cont = 1
    while cont <= 10:
        res = cont * n
        print("%i x %i = %i" % (cont, n, res))
        cont = cont + 1

def cuenta_suma():
    suma = 0
    cont = 0
    while suma <= 1000:
        cantidad = int(input("Dame una cantidad: "))
        suma = suma + cantidad
        cont = cont + 1
    print("La suma es: ", suma)
    print("La cantidad de números fue: ", cont)
            
def comprueba_codigo (clave):
    password = input("Dame tu password: ")
    while clave != password:
        print("Clave incorrecta, intenta de nuevo")
        password = input("Dame tu clave: ")
    print("Clave exitosa")

def valida_codigo (clave):
    password = input("Dame tu password: ")
    while clave != password:
        print("Clave incorrecta, intenta de nuevo")
        password = input("Dame tu clave: ")
    print("Clave exitosa")

def valida_matricula (lista):
    matricula = input("Dame tu matrícula: ")
    while matricula not in lista:
        print("Matrícula inválida, intenta de nuevo")
        matricula = input("Dame tu matrícula: ")
    print("Matrícula válida")
    
def valida_matricula0 (matricula_correcta):
    matricula = input("Dame tu matrícula: ")
    while matricula != matricula_correcta:
        print("Matrícula incorrecta, intenta de nuevo")
        matricula = input("Dame tu matrícula: ")
    print("Matrícula correcta")
    
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
    print()
    print("1. Cuenta y suma")
    print("2. Total a pagar")
    print("3. Total de depósitos")
    print("4. Clientes")
    print("5. Comprueba clave")
    print("6. Valida matrícula")
    print("7. Valida matrícula 2")
    print("8. Salir")
    
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
            n = int(input("Dame el número de clientes: "))
            clientes(n)
        elif opcion == 5:
            clave = input("Dame la clave: ")
            comprueba_codigo(clave)
        elif opcion == 6:
            matricula_correcta = "A01201524"
            valida_matricula(matricula_correcta)
            nombre = input("Dame tu nombre: ")
            carrera = input("Dame tu carrera: ")
            print(matricula_correcta + " " + nombre + " " + carrera)
        elif opcion == 7:
            lista = ["A01300000", "A01201524", "A01200000"]
            valida_matricula(lista)
        elif opcion == 8:
            print("Adiós")
            continua = False
        else:
            print("Error opción inválida")
    
main()