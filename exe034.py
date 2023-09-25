# Exercício Python #034 - Aumentos múltiplos
salário = float(input("Qual é o salário do funcionário? "))
a1 = salário * 1.10
a2 = salário * 1.15

if salário > 1250:
    print("O novo salário é de R${:.2f}".format(a1))
else:
    print("O novo salário é de R${:.2f}".format(a2))
    