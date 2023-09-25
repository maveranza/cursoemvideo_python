# Exercício Python #008 - Conversor de Medidas
medida = float(input("Uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
print("A medida de {}m corresponde a {:.0f}cm e {:.0f}mm".format(medida, cm, mm))