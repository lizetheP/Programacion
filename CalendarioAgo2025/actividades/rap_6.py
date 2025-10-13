def crea_matriz(reng, col):
    matriz = []
    for i in range(0, reng):
        matriz.append([])
        for j in range(0, col):
            num = int(input("Dame un número: "))
            matriz[i].append(num)
    return matriz

def multiplica_columna(matriz, columna, num):
    for i in range(0, len(matriz)): # renglones
        for j in range(0, len(matriz[i])): # columnas
            if j == columna:
                matriz[i][j] = matriz[i][j]*num

def reemplaza(matriz, num):
    for i in range(0, len(matriz)): # renglones
        for j in range(0, len(matriz[i])): # columnas
            if matriz[i][j] % 2 != 0:
                matriz[i][j] = num
                
def main():
    r = int(input("Dame los renglones: "))
    c = int(input("Dame las columnas: "))
    m = crea_matriz(r, c)
    print(m)
    #col = int(input("Dame la columna: "))
    num = int(input("Dame un número: "))
    reemplaza(m, num)
    #multiplica_columna(m, col, num)
    print(m)
    
main()