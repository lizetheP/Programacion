import math
r = float(input("Dame el radio: "))
h = float(input("Dame la altura: "))
a = 2 * math.pi * r * (h + r)
print("Area: %.2f" % a)
v = math.pi * r**2 * h
print("Volumen: %.2f" % v)

