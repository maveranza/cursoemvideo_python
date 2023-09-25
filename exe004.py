# Exercício Python #004 - Dissecando uma Variável
entrada_usuario = input("Digite algo para determinar seu tipo primitivo: ")
print("Qual é o tipo primitivo do valor inserido? {}".format(type(entrada_usuario)))
print("Consiste apenas em espaços em branco? {}".format(entrada_usuario.isspace()))
print("É alfanumérico? {}".format(entrada_usuario.isalnum()))
print("É composto exclusivamente por letras? {}".format(entrada_usuario.isalpha()))
print("Consiste apenas em números? {}".format(entrada_usuario.isnumeric()))
print("Todos os caracteres estão em maiúsculas? {}".format(entrada_usuario.isupper()))
print("Todos os caracteres estão em minúsculas? {}".format(entrada_usuario.islower()))
print("É composto por caracteres imprimíveis? {}".format(entrada_usuario.isprintable()))
print("Segue o padrão de título (capitalização inicial)? {}".format(entrada_usuario.istitle()))
print("É um identificador válido em Python? {}".format(entrada_usuario.isidentifier()))
print("Consiste apenas em dígitos numéricos? {}".format(entrada_usuario.isdigit()))
print("Contém apenas caracteres ASCII? {}".format(entrada_usuario.isascii()))
print("É composto exclusivamente por dígitos decimais? {}".format(entrada_usuario.isdecimal()))
print("É composto por caracteres imprimíveis? {}".format(entrada_usuario.isprintable()))


