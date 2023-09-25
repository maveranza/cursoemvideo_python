# Exercício Python #031 - Custo da Viagem
from time import sleep

distância = float(input("Qual é a distância da sua viagem? "))
sleep(3)
print("Você está prestes a começar uma viagem de {}km!".format(distância))
print("Calculando a passagem...")
sleep(5)
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(preço))