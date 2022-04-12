from ast import Num


soma = 0
cont = 0
for c in range(1, 7):
  num = int(input('Digite o {}° valor: '.format(c)))
  if num % 2 == 0:
    soma = soma + num
    cont = cont + 1
print('você informou {} numeros pares e a soma de é: {}'.format(cont , soma))