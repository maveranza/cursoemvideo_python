# Exercício Python #007 - Média Aritmética
while True:
    try:
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
        break
    except ValueError:
        print("Digite um valor válido.")

ma = (n1 + n2) / 2
print('A média aritmética entre {} e {} é {}'.format(n1, n2 , ma))