# Exercício Python #012 - Calculando Descontos
prod = float(input("Qual é o preço do produto? "))
desc = prod - (prod * 5/100)
print("Com o desconto, o produto que custava R$ {:.2f}, agora está saindo por R$ {:.2f}".format(prod, desc))
