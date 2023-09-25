# Exercício Python #017 - Catetos e Hipotenusa
from math import hypot
co = int(input("Quanto vale o cateto oposto? "))
ca = int(input("Quanto vale o cateto adjacente? "))
hi = hypot(ca, co)
print("A hipotenusa vai medir {:.2f}".format(hi))