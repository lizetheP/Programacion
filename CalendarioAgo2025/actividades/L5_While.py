def total_depositos(n, mes_curso):
    cont = 1
    cont2 = 0
    acum = 0
    while cont <= n:
        print()
        mes = input("Mes: ")
        importe = int(input("Importe: "))
        if mes.lower() == mes_curso.lower():
            acum = acum + importe
            cont2 = cont2 + 1
        else:
            print("Error en el mes")
        cont = cont + 1
    print()
    print("Total de importes: ", acum)
    print("Total de importes del mes en curso: ", cont2)
            
def main():
    n = int(input("Número de depósitos: "))
    mes = input("Mes en curso: ")
    total_depositos (n, mes)
    
main()
            