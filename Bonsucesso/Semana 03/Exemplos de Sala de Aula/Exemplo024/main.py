# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# ● para homens: (72.7 * h) – 58;
# ● para mulheres: (62.1 * h) – 44.7.


altura = float(input("Digite sua altura: "))
sexo = input("Digite o sexo: ")

if sexo == "M":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

print("Peso Ideal: " + str(peso))



