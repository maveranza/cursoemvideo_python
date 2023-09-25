# Exercício Python #011 - Pintando Parede
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = altura * largura
print("Sua parede possui a dimensão {}x{} e sua área é de: {}m²".format(largura, altura, area))
tinta = area / 2
print("Para pintar essa parede você vai precisar de {}l de tinta".format(tinta))
