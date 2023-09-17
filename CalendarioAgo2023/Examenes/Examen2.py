numero = int(input("Escriba un número: "))
if numero % 2 == 0 and numero % 4 != 0:
    print("%i es múltiplo de dos" % numero)
elif numero % 4 == 0:
    print("%i es múltiplo de cuatro y de dos" % numero)
else:
    print("%i no es múltiplo de dos" % numero)