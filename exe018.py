# Exercício Python #018 - Seno, Cosseno e Tangente
from math import radians, sin, cos, tan
ângulo = float(input("Digite o número: "))
seno = sin(radians(ângulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(ângulo, seno))
cosseno = cos(radians(ângulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, tangente))