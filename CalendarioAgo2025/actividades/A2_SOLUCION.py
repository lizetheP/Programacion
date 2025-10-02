if s > 1000000:
    print("Excelente cliente")
elif s > 100000 and s <= 1000000:
    print("Buen cliente")
elif s > 2000 and s <= 100000:
    print("Cliente promedio")
elif s >= 0 and s <= 2000:
    print("Cliente con saldo insuficiente")
elif s < 0:
    print("Y tu dinero?")