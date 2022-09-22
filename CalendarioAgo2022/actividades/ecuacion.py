import math
print("Juan Pérez A01928282")
a = float(input("Dame el valor de a: "))
b = float(input("Dame el valor de b: "))
c = float(input("Dame el valor de c: "))
x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
print("La raíz positiva es: %.2f" % x1)
print("La raíz negativa es: %.2f" % x2)


