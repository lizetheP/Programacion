print("Juan Pérez Álvarez A08888888")

def cuenta_suma():
    acum = 0
    cont = 0
    while acum < 1000:
        valor = int(input("Dame un valor: "))
        acum = acum + valor
        cont = cont + 1
    print("Suma = ", acum)
    print("Cantidad de números =", cont)

def total_depositos(n, mes_curso):
    cont = 1
    cont_importes = 0
    acum = 0
    while cont <= n:
        mes = input("Mes: ")
        importe = int(input("Importe: "))
        if mes.upper() == mes_curso.upper():
            acum = acum + importe
            cont_importes = cont_importes + 1
        else:
            print("Error en el mes")
        cont = cont + 1
    print("Total de importes: ", acum)
    print("Total de importes del mes en curso: ", cont_importes)
    
def valida_matricula(lista):
    matricula = input("Dame tu matrícula: ")
    while matricula not in lista:
        print("Matrícula inválida, intenta de nuevo")
        matricula = input("Dame tu matrícula: ")
    print("Matrícula validada, acceso permitido")
        
def menu():
    print()
    print("1. Cuenta y suma")
    print("2. Total de depósitos")
    print("3. Valida matrícula")
    print("4. Salir")
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            cuenta_suma()
        elif opcion == 2:
            num = int(input("Dame el número de depósitos: "))
            mes = input("Dame el mes en curso: ")
            total_depositos(num, mes)
        elif opcion == 3:
            lista = ["A01300000", "A01201524", "A01200000"]
            valida_matricula(lista)
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()
    
        