# Faça um algoritmo em Python que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.


A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A == B:
  C = A + B
else:
  C = A * B

print(C)

