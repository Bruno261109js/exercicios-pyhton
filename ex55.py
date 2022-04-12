maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(p)))
    if p == 1:
        maior = p
        menor = p

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\033[1;92mO maior peso foi de {}kg e o menor de {}kg'.format(maior, menor))