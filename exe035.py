# Exercício Python #035 - Analisando Triângulo v1.0
l1 = float(input("Digite o 1º lado: "))
l2 = float(input("Digite o 2º lado: "))
l3 = float(input("Digite o 3º lado: "))

if l1 <= 0 or l2 <= 0 or l3 <= 0:
    print("Os lados do triângulo devem ser maiores que zero!")
elif l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print("Esse triângulo não existe!")
else:
    print("Esse triângulo existe!")
    